# Medical AI 会议论文研究：2023–2025

本研究使用本仓库收录的 1,430 篇论文及完整会议目录索引，区分三个问题：已发表论文中 medical 文章的占比、投稿后的录用情况，以及研究主题的变化。脚本、逐篇标签、CSV 和图表均保存在仓库。

## 1. 已收录 medical 论文占会议论文的多少？

| 发表年份 | 已收录 medical 论文 | 同范围可比研究论文 | 已收录占比 |
|---|---:|---:|---:|
| 2023 | 282 | 15,799 | 1.78% |
| 2024 | 443 | 20,315 | 2.18% |
| 2025 | 705 | 26,607 | 2.65% |

这是**索引语料中已收录 medical 论文的占比下界**，不能当成所有 medical 论文的完整占比。仍有待审候选，收录完整度也可能随年份不同。逐年合计还受到会议规模、NAACL 2023 未举办及 ICCV/ECCV 交替举办的影响。

报告同时提供会议逐年分表、track 分表，以及固定会议家族等权重的敏感性分析。AAAI 的博士/学生摘要、faculty/senior presentations、journal track、demo、勘误及合办 IAAI/EAAI 不混入研究论文分母；NeurIPS/KDD 的 research、benchmark 等范围则按明确的 track 保留。

详见[会议占比研究](../reports/analysis/medical-share.md)和[完整 CSV](../reports/analysis/conference_year_shares.csv)。

## 2. Medical 的录用率比其他领域如何？

完整录用论文目录无法回答这个问题，因为缺少被拒稿件和领域投稿分母。当前可完成的比较限定为 **ICLR 2023–2025 的历史公开投稿快照**，不外推至所有会议。

我们对录用和拒稿的标题使用同一套 medical 关键词规则，不使用“只有录用文章才有的人工标签”标记录用组。另一组准确名称是“未匹配该 medical 标题规则的其他标题”，其中仍可能包含漏检的 medical 研究。

| 年份 | Medical 关键词组：录用 / 录用加拒稿 | 条件录用率 | 其他标题组条件录用率 |
|---|---:|---:|---:|
| 2023 | 12 / 33 | 36.36% | 40.84% |
| 2024 | 23 / 72 | 31.94% | 39.76% |
| 2025 | 46 / 157 | 29.30% | 43.24% |

分母仅包含获得明确 accept/reject 决定的投稿，**不含撤稿和 desk reject**。因此它是条件录用率，不能直接与会议官方 accepted/submitted 总录用率相比。CSV 另有包含撤稿等状态的 observed-pool 比例，以及更宽关键词定义的敏感性分析。

在这个快照和规则下，medical 关键词组的条件录用比例较低；但这**不能证明审稿对 medical 存在偏好或歧视**。样本量、领域构成、撤稿行为、标签漏检和快照选择都可能影响结果。2023/2024 medical 组尤其小，报告提供 Wilson 区间，不把这些观察结果写成因果结论。

数据来自 [Paper Copilot 固定版本的 OpenReview 历史快照](https://github.com/papercopilot/paperlists/tree/9fcfd1234879a8e5630b5116dde411ec143dd763)，不是本次直接获取的官方全量实时数据。本环境的 OpenReview notes 接口返回浏览器验证页，脚本对此明确报错。快照录用标题与官方索引的精确匹配率分别约为 99.94%、100% 和 99.81%，差异保留供核查。

另有 2024/2025 作者自报研究领域的[分领域统计](../reports/analysis/acceptance_by_area.csv)。这些领域名称跨年变化，2023 缺失，因而不强行拼接成统一的三年领域排行榜。详见[录用情况研究与官方基线](../reports/analysis/acceptance-rates.md)。

## 3. 这些年在研究什么？

所有年份统一使用标题，避免摘要覆盖率不同制造虚假的主题增长。研究领域与研究方法分开标记，并允许一篇论文匹配多个标签。

| 方法标签 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|
| Vision-language / multimodal | 24（8.5%） | 51（11.5%） | 116（16.5%） |
| Large language models | 7（2.5%） | 41（9.3%） | 68（9.6%） |
| Foundation models / SAM | 8（2.8%） | 33（7.4%） | 49（7.0%） |
| Diffusion models | 9（3.2%） | 23（5.2%） | 35（5.0%） |
| Segmentation | 47（16.7%） | 54（12.2%） | 97（13.8%） |

可以观察到，多模态与视觉语言标题标签持续增加；LLM 标签主要在 2023→2024 间上升，2025 占比变化较小。Foundation/SAM 和 diffusion 的论文数量增加，但 2024→2025 的占比没有继续上升。分割论文从 47 篇增加到 97 篇，不能因为相对占比下降就说研究数量萎缩。

关键词分析按每篇标题的 document frequency 计数，同时输出每年标准化比例、unigram/bigram 及明确的最低出现次数。它是可检查的词频分析，不声称恢复论文全部研究内容。完整领域、方法、年度关键词和变化排名见[主题研究](../reports/analysis/topics.md)。

## 复现

```sh
python -m pip install -r requirements-analysis.txt
python scripts/index_papers.py --abstracts candidates
python scripts/fetch_submissions.py --source snapshot
python scripts/analyze_research.py
python scripts/build_site.py
```

首次下载后，索引与投稿抓取可用 `--offline` 复用本地缓存。研究脚本不发网络请求，输入与配置哈希、固定快照版本及数据边界均有记录。详见[英文方法说明](research-methodology.md)。
