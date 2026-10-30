#!/usr/bin/env python3
"""Draw the README taxonomy from its topic sections; paper counts are read, branch labels are editorial."""

import argparse
from collections import Counter
from pathlib import Path
from xml.sax.saxutils import escape

ROOT=Path(__file__).resolve().parents[1]
OUTPUT=ROOT/"assets/medical-ai-papers-taxonomy.svg"
WIDTH=760
TOP=72
BOTTOM=24
LEAF_PITCH=27
CATEGORY_GAP=18
FONT='font-family="sans-serif"'

# icon, box label lines, gradient start, gradient end, hub stroke, leaf fill, leaf text, branch labels
CATEGORIES=[
    ("🔬",["Medical Imaging &","Segmentation"],"#1e3a8a","#3b82f6","#93c5fd","#eff6ff","#1e40af",
     ["Segmentation","Reconstruction & MRI","Synthesis & Diffusion","Domain Generalization","Registration"]),
    ("🧫",["Computational Pathology","& Microscopy"],"#5b21b6","#8b5cf6","#c4b5fd","#f5f3ff","#4c1d95",
     ["Whole-Slide Analysis & MIL","Microscopy","Cell & Nucleus Analysis","Spatial Transcriptomics","Survival Prediction"]),
    ("🤖",["Foundation Models &","Vision-Language"],"#7f1d1d","#f43f5e","#fda4af","#fff1f2","#7f1d1d",
     ["Multimodal Vision-Language","Medical LLMs","Report Generation","SAM & Foundation Adaptation"]),
    ("📋",["Clinical NLP, EHR &","Healthcare"],"#92400e","#f59e0b","#fcd34d","#fffbeb","#78350f",
     ["Medical LLMs & Question Answering","Risk & Outcome Prediction","Retrieval & Knowledge",
      "Diagnosis & Treatment","Mental Health","Information Extraction"]),
    ("🧠",["Neuroimaging, EEG &","Brain AI"],"#065f46","#10b981","#6ee7b7","#ecfdf5","#064e3b",
     ["EEG","fMRI & Neural Decoding","Brain MRI & Tumors","Neurodegeneration"]),
    ("🫀",["Physiological Signals &","Medical Time Series"],"#111827","#4b5563","#9ca3af","#f9fafb","#1f2937",
     ["ECG","Sleep","PPG & Wearables","Physiological Signal Models"]),
    ("🏥",["Surgical AI"],"#155e75","#06b6d4","#67e8f9","#ecfeff","#164e63",
     ["Endoscopy","Surgical Video & Workflow","Instruments & Robotics","3D & Depth Estimation"]),
]


def topic_counts(readme):
    counts=Counter()
    topic=None
    for line in readme.split("## Proceedings indexing\n",1)[0].splitlines():
        if line.startswith("#### "):
            topic=line[5:].split(" ",1)[0]
        elif line.startswith("- **[") and topic:
            counts[topic]+=1
    return counts


def text(x,y,value,size,weight,fill):
    return (f'<text x="{x}" y="{y}" text-anchor="middle" dominant-baseline="middle" {FONT} '
            f'font-size="{size}" font-weight="{weight}" fill="{fill}">{escape(value)}</text>')


def render(counts):
    unknown=set(counts)-{category[0] for category in CATEGORIES}
    if unknown:
        raise ValueError(f"README topics missing from taxonomy: {sorted(unknown)}")
    defs=['<linearGradient id="bg-g" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#eef4ff"/>'
          '<stop offset="100%" stop-color="#f8fafc"/></linearGradient>',
          '<linearGradient id="root-g" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#0f172a"/>'
          '<stop offset="100%" stop-color="#1e3a8a"/></linearGradient>']
    body=[]
    junctions=[]
    y=TOP
    for index,(icon,label,start,end,hub,fill,ink,leaves) in enumerate(CATEGORIES):
        defs.append(f'<linearGradient id="cat-{index}" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="{start}"/>'
                    f'<stop offset="100%" stop-color="{end}"/></linearGradient>')
        first=y+12
        last=first+LEAF_PITCH*(len(leaves)-1)
        center=(first+last)//2
        height=26+16*len(label)
        top=center-height//2
        junctions.append((center,end))
        body.append(f'<line x1="228" y1="{center}" x2="240" y2="{center}" stroke="{end}" stroke-width="2"/>')
        body.append(f'<rect x="243" y="{top+3}" width="210" height="{height}" rx="8" fill="#000" opacity="0.08"/>')
        body.append(f'<rect x="240" y="{top}" width="210" height="{height}" rx="8" fill="url(#cat-{index})"/>')
        for offset,line in enumerate(label):
            body.append(text(345,top+15+16*offset,line,12,700,"#ffffff"))
        body.append(text(345,top+15+16*len(label),f"{counts[icon]:,} papers",11,500,"#ffffff"))
        body.append(f'<line x1="450" y1="{center}" x2="460" y2="{center}" stroke="{end}" stroke-width="1.5"/>')
        body.append(f'<line x1="460" y1="{first}" x2="460" y2="{last}" stroke="{hub}" stroke-width="1.5"/>')
        for position,leaf in enumerate(leaves):
            leaf_y=first+LEAF_PITCH*position
            body.append(f'<line x1="460" y1="{leaf_y}" x2="470" y2="{leaf_y}" stroke="{hub}" stroke-width="1"/>')
            body.append(f'<rect x="470" y="{leaf_y-12}" width="266" height="24" rx="12" fill="{fill}" stroke="{hub}" stroke-width="1.5"/>')
            body.append(text(603,leaf_y,leaf,11,600,ink))
        y=last+12+CATEGORY_GAP
    height=y-CATEGORY_GAP+BOTTOM
    spine_top,spine_bottom=junctions[0][0],junctions[-1][0]
    root=(spine_top+spine_bottom)//2
    total=sum(counts.values())
    lines=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {height}" width="{WIDTH}" height="{height}" '
           'role="img" aria-label="Visual taxonomy of medical AI papers">',
           "<defs>",*defs,"</defs>",
           f'<rect width="{WIDTH}" height="{height}" fill="url(#bg-g)" rx="12" stroke="#dde6f0" stroke-width="1.5"/>',
           text(380,30,"Medical AI Papers — Visual Taxonomy",16,700,"#0f172a"),
           f'<line x1="24" y1="47" x2="736" y2="47" stroke="#cbd5e1" stroke-width="1"/>',
           f'<rect x="27" y="{root-25}" width="190" height="56" rx="10" fill="#000" opacity="0.10"/>',
           f'<rect x="24" y="{root-28}" width="190" height="56" rx="10" fill="url(#root-g)"/>',
           text(119,root-9,"Medical AI Papers",13,700,"#ffffff"),
           text(119,root+10,f"{total:,} papers, 2023–2025",11,500,"#ffffff"),
           f'<line x1="214" y1="{root}" x2="228" y2="{root}" stroke="#94a3b8" stroke-width="2"/>',
           f'<line x1="228" y1="{spine_top}" x2="228" y2="{spine_bottom}" stroke="#94a3b8" stroke-width="2"/>',
           *[f'<circle cx="228" cy="{center}" r="5" fill="{color}" stroke="#ffffff" stroke-width="1.5"/>' for center,color in junctions],
           *body,"</svg>",""]
    return "\n".join(lines)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readme",type=Path,default=ROOT/"README.md")
    parser.add_argument("--output",type=Path,default=OUTPUT)
    args=parser.parse_args()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(render(topic_counts(args.readme.read_text())))


if __name__=="__main__":
    main()
