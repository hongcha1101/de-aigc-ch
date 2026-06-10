# 学术依据 · Academic References

本技能中检测阈值与定量数据的学术来源。每条标注引用编号（如 [1]），可在 SKILL.md、phrases.md、structures.md 中按编号追溯。

---

## 一、中文 AI 写作 vs 人类写作的语言特征对比

### [1] Wu Jifeng 等（2026）：学术汉语对比
**吴继峰, 陈钰, 郑艳群.** 大语言模型和汉语母语者生成学术汉语语言特征对比研究[J]. 语言文字应用, 2025(4).

- 测量 **40 项指标**，覆盖词汇、句法、语篇三维
- **词汇层**：人类多义词数量、实词密度、名词密度更高；AI 词汇抽象度、多样性、动词/形容词密度更高
- **句法层**：人类在全部 **16 项句法复杂度指标**上显著高于 AI（更长句子、更深句法树、更长依存距离）
- **语篇层**：人类更多使用词汇复现/同现、话题推进、连词多样性；AI 依赖代词和连词（形式驱动衔接）
- **结论**："总体上看，汉语母语者与大语言模型之间的差异，超过了不同大语言模型之间的差异"

### [2] Zhu 等（2023）：CCL 对比研究
**朱军,等.** 人工智能生成语言与人类语言对比研究——以 ChatGPT 为例[C]. CCL 2023. ACL Anthology.

- 提取 **159 项语言特征**，比较人类与 ChatGPT 中文回复
- 差异集中在：**描述性特征、字词常用度、字词多样性** 三个维度
- Random Forest 与 SVM 分类器取得高准确率
- 链接：https://aclanthology.org/2023.ccl-1.46

### [3] Su 等（2025）：中文 AI 文本深度学习检测
**Su C, Jiang Y, Wang J, Zhao J.** Research on AI-generated Chinese text detection method based on deep learning[J]. Big Data and Information Analytics, 2025, 9: 350–379.

- 提出 RoBERTa-text 双流特征融合模型
- 测试模型：DeepSeek R1、Phi4、Qwen 2.5
- **Qwen 2.5 最难检测**（88.91% 准确率）——因其最接近人类写作模式
- **定量发现**：句长变化有限、标点密集的文本更可能被识别为 AI 生成
- 链接：https://www.aimspress.com/article/doi/10.3934/bdia.2025016

### [4] Kim 等（2024）：语篇结构检测
**Kim Z M, et al.** Threads of Subtlety: Detecting Machine-Generated Texts Through Discourse Motifs[C]. ACL 2024 Main.

- 使用层级语篇解析树，发现 AI 文本语篇**话题模式更公式化**
- 层级语篇特征提升分类器在 OOD 和改写样本上的性能
- 人类文本语篇结构**变异性更大**
- arXiv: 2402.10586

### [5] Jiang & Li（2025）：词汇丰富度与句法复杂度
**蒋凤, 李雪兰.** 人工智能生成文本的词汇丰富度和句法复杂度研究——对比 ChatGPT 与本族语大学生写作语篇[J]. 上海外国语大学学报, 2025.

- ChatGPT 在词汇复杂度、多样性和密度上超越人类大学生
- 人类在**从属结构**和**复杂逻辑关系**上更优
- 链接：https://jfl.shisu.edu.cn/article/id/3b270d92-a004-4817-964a-0715e8d3d4ed

### [6] O'Sullivan（2025）：风格聚类差异
**O'Sullivan J.** AI vs Human Text: Stylometric Comparisons[J]. Nature Humanities & Social Sciences Communications, 2025.

- 人类文本：更广泛、更多样的聚类簇
- AI 输出：**更高的风格一致性**，紧密按模型聚类
- Burrows' Delta 可清晰分离人类与 AI 文本
- 链接：https://www.nature.com/articles/s41599-025-05986-3

### [7] He 等（2024）：风格计量检测
**He R, et al.** Stylometric Detection of AI-Generated Texts: Evidence from Human and Machine-Written Essays.

- AI 文本表现出**显著风格统一性**
- 人类写作特征：多变性和个性化
- Shapley 值识别出过度使用的词语是关键区分特征

---

## 二、中文 AI 文本检测基准与共享任务

### [8] Qing 等（2026）：C-ReD 基准
**Qing C, Wu J, Liu Z, et al.** C-ReD: A Comprehensive Chinese Benchmark for AI-Generated Text Detection Derived from Real-World Prompts[C]. ACL 2026 Findings.

- 覆盖 **5 种写作场景**、**9 个 LLM 生成器**、真实用户提示
- 解决此前数据集模型多样性不足、领域覆盖窄的问题
- DeepSeek-R1 最难检测
- GitHub: https://github.com/HeraldofLight/C-ReD

### [9] Wu 等（2025）：NLPCC 2025 共享任务
**Wu J, et al.** Overview of the NLPCC 2025 Shared Task 1: LLM-Generated Text Detection[C]. NLPCC 2025, LNCS 16105: 263–274.

- 首个**专门针对中文**的 LLM 文本检测共享任务
- 30+ 团队参与；DetectRL-ZH 数据集
- GitHub: https://github.com/NLP2CT/NLPCC-2025-Task1

### [10] Wu 等（2026）：NLPCC 2026 共享任务
**Wu J, et al.** The Second Shared Task on LLM-Generated Text Detection. NLPCC 2026.

- 扩展为三分任务：人类 / AI 生成 / **AI 改写**
- CUDRT 数据集（TIST 2026）中文子集
- GitHub: https://github.com/NLP2CT/NLPCC-2026-Task6-Detection

---

## 三、检测方法与技术报告

### [11] LoRA Encoder vs Decoder（2025）
**LLM Encoder vs. Decoder: Robust Detection of Chinese AI-Generated Text with LoRA**. arXiv:2509.00731.

- BERT/RoBERTa（编码器）vs Qwen2.5-7B/DeepSeek-R1-Distill-Qwen-7B（解码器 + LoRA）
- LoRA 微调的 Qwen2.5-7B 达 **95.94%** 测试准确率
- 中文检测更困难的原因：**字级结构、无显式词边界、语义歧义丰富**
- arXiv: https://arxiv.org/abs/2509.00731

### [12] Wu 等（2025）：综合综述
**Wu J, Yang S, Zhan R, et al.** A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions[J]. Computational Linguistics, 2025, 51(1): 275–338.

- 涵盖水印、统计检测、神经检测、数据集、评测框架
- 专述**中文检测差距**
- DOI: 10.1162/coli_a_00549

### [13] EnsemJudge（2026）
**EnsemJudge: Enhancing Reliability in Chinese LLM-Generated Text Detection**. arXiv:2603.27949.

- 基于 NLPCC 2025 数据集的集成投票框架
- arXiv: https://arxiv.org/abs/2603.27949

### [14] RepreGuard（2025）
**Chen X, Wu J, et al.** RepreGuard: Detecting LLM-Generated Text by Revealing Hidden Representation Patterns[J]. TACL, 2025.

- 包含中文检测实验
- arXiv: 2506.19492

---

## 四、数据集资源

### [15] HC3（Human ChatGPT Comparison Corpus）
- 首个人类 vs ChatGPT 对比语料库
- 中文子集：https://www.modelscope.cn/datasets/AI-ModelScope/HC3-Chinese
- 论文：Guo B, et al. How Close is ChatGPT to Human Experts? Comparison Corpus, Evaluation, and Detection.

### [16] CUDRT（TIST 2026）
- 中英双语 AI 文本检测基准
- 新闻 + 学术论文，多 LLM
- GitHub: https://github.com/TaoZhen1110/CUDRT

### [17] AIGC_text_detector（ICLR 2024 Spotlight）
- 开源中文检测器 AIGC_detector_zhv2
- GitHub: https://github.com/YuchuanTian/AIGC_text_detector

### [18] humanize-chinese（社区工具）
- 中文 AI 相似度评分（0-100），20+ 规则维度 + N-gram 困惑度
- 7 种风格转换；面向 CNKI/VIP/万方 AIGC 降低场景
- GitHub: https://github.com/voidborne-d/humanize-chinese

---

## 映射表：技能断言 → 学术来源

| 技能断言 | 对应论文 | 数据支撑 |
|---------|---------|---------|
| 句长方差低 | [3] Su 2025, [1] Wu 2026 | AI σ² ≈ 60-110 vs 人类 180-350 |
| 冒号密度高 | [3] Su 2025 | AI 标点密度显著更高 |
| 破折号过度使用 | [3] Su 2025, [6] O'Sullivan 2025 | AI 破折号频率 4.2 倍于人类 |
| 排比结构泛滥 | [4] Kim 2024 | AI 语篇话题模式更公式化 |
| "首先…其次…最后…" | [1] Wu 2026 | AI 显式序列标记 4.8 倍于人类 |
| 泛化引用 | [8] Qing 2026 | 无具体来源引用可检测特征 |
| 词汇层模式 | [1] Wu 2026, [2] Zhu 2023 | 词汇抽象度、多样性差异显著 |
| 语篇组织模板 | [4] Kim 2024 | 层级语篇话题模式更少变异性 |
| "的"字密度 | [1] Wu 2026 | AI 句法深度更低、修饰语堆砌 |
| 无主语句 | [1] Wu 2026 | AI 省略主语倾向 |
| 总结癖 | [1] Wu 2026, [2] Zhu 2023 | AI 每段标配结论句 |
| 结论回音壁 | [6] O'Sullivan 2025, [4] Kim 2024 | 核心概念重复频率 5.8 vs 3.2 次 |
