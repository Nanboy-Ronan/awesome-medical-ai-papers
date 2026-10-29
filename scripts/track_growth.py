#!/usr/bin/env python3
"""Record GitHub star growth; optional owner traffic stays local and uncommitted."""

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess

ROOT=Path(__file__).resolve().parents[1]


def get(path):
    result=subprocess.run(["gh","api",path],capture_output=True,text=True)
    if result.returncode:
        status=re.search(r"HTTP (\d+)",result.stderr)
        return {"available":False,"error":"HTTP "+status[1] if status else "GitHub API unavailable"}
    return {"available":True,"data":json.loads(result.stdout)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--traffic",action="store_true",help="Also retrieve owner-only aggregate traffic; requires existing administration-read access")
    parser.add_argument("--output-dir",type=Path,default=ROOT/"reports/private-growth")
    args=parser.parse_args()
    config=json.loads((ROOT/"config/site.json").read_text())
    repo=config["repository"].removeprefix("https://github.com/")
    current=get("repos/"+repo)
    if not current["available"]:
        raise SystemExit(current["error"])
    obj=current["data"]
    timestamp=datetime.now(timezone.utc)
    metrics={"captured_utc":timestamp.isoformat(),"repository":repo,
             "stars":obj["stargazers_count"],"forks":obj["forks_count"],
             "interpretation":"Net stars are the outcome. Traffic is diagnostic; these aggregates do not identify visitor-to-star conversion or causal SEO impact."}
    baseline_path=ROOT/"reports/discovery-baseline.json"
    if baseline_path.exists():
        baseline=json.loads(baseline_path.read_text())
        metrics.update(baseline_captured_utc=baseline["captured_utc"],
                       net_star_change_since_baseline=metrics["stars"]-baseline["stargazers_count"])
    if args.traffic:
        for name,endpoint in (("views_last_14_days","views"),("clones_last_14_days","clones"),("top_referrers_last_14_days","popular/referrers")):
            metrics[name]=get("repos/"+repo+"/traffic/"+endpoint)
    args.output_dir.mkdir(parents=True,exist_ok=True)
    text=json.dumps(metrics,ensure_ascii=False,indent=2)+"\n"
    (args.output_dir/(timestamp.strftime("%Y%m%dT%H%M%S%fZ")+".json")).write_text(text)
    (args.output_dir/"latest.json").write_text(text)
    print(json.dumps({"stars":metrics["stars"],"net_star_change_since_baseline":metrics.get("net_star_change_since_baseline"),
                      "traffic_available":{k:v["available"] for k,v in metrics.items() if k.endswith("14_days")},
                      "saved_to":str(args.output_dir/"latest.json")},indent=2))


if __name__=="__main__":
    main()
