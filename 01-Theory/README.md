# 01-Theory / 理论基础

本目录收录量子传感相关的经典论文、学术资料和基础科普内容。

## 分类说明

- **经典论文** — 量子传感领域的开创性研究论文（PDF格式）
- **学术资料** — 综述文章、教材章节、课程讲义
- **基础科普** — 面向初学者的入门资料

## 文件命名规范

```
[年份]-[作者/机构]-[标题].pdf
```

## 资料索引

<!-- 请在下方按类别添加资料链接 -->
### 论文 / Papers

- [Room-Temperature NV Center Quantum Registers: Quantum Volume of 8 (arXiv:2412.12959, 2024)](https://arxiv.org/abs/2412.12959) - 基于室温NV色心量子寄存器定义连接映射与单量子比特性能，all-to-all连接结构使2和3量子比特门性能具有竞争力；实验校准误差模型，估计量子体积达8，为室温量子计算与传感一体化奠定基础
- [Atomic-scale quantum sensor for electric and magnetic fields (Nature Nanotechnology, 2024)](https://link.springer.com/10.1038/s41565-024-01724-z) - 基于扫描隧道显微镜(STM)尖端附着Fe原子和PTCDA分子构建单分子量子传感器，实现亚Angstrom空间分辨率探测单Fe原子和Ag二聚体的磁场和电场信号；为导体表面原子尺度量子传感实验开辟新途径
- [Limits of absolute vector magnetometry with NV centers in diamond (arXiv:2504.20750, 2025)](https://arxiv.org/abs/2504.20750) - 研究NV色心矢量磁力测量精度极限，推导磁场矢量到自旋共振频率的精确解析公式，系统分析误差来源与补偿策略，对绝对磁场测量精度评估具有重要参考价值
- [Homogeneous spin-dephasing time of NV centre in millimetre-scale ¹²C-enriched HPHT diamond crystals (Communications Physics, 2025)](https://www.nature.com/articles/s43246-025-00782-7) - ¹²C富集高静高压(HPPT)金刚石中NV色心自旋退相干时间T₂*中值达4.5µs，批次差异仅10%，毫米级大面积均匀性为femtotesla级弱磁场探测奠定基础
- [High-resolution magnetic resonance spectroscopy using a solid-state spin sensor (Nature 2018)](https://www.nature.com/articles/nature25781) - 基于NV色心实现高分辨率磁共振波谱，检测单蛋白产生的磁场信号；最佳谱分辨率约100 Hz，可解析核自旋拉摩尔频率百万分之一的关键谱标识，为纳米级化学分析提供新工具
- [Sensing of magnetic field effects in radical-pair reactions using a quantum sensor (2022)](https://arxiv.org/abs/2209.14066) - 研究NV色心探测自由基对化学反应的磁场效应，为量子传感在生物化学领域的应用提供新思路
- [Nuclear Quantum-Assisted Magnetometer (2016)](https://arxiv.org/abs/1610.03621) - 利用单量子比特实现核量子辅助磁力计，展示亚纳特斯拉级灵敏度

### 综述与教程

- [Research Progress and Development Trend of Atomic Magnetometers (Laser & Optoelectronics Progress Vol. 62, Issue 7, 0700006, 2025)](https://www.researching.cn/articles/OJe7529d2d8c647c8d) - 原子磁力计研究进展与发展趋势综述，涵盖SERF原子磁力计、NV色心磁力计、量子增强方案等前沿进展；是了解原子磁力计技术全貌的重要参考文献

<!-- 添加格式: - [资料名称](URL) - 简短摘要 -->

---

- [Quantum Magnetometers for Infrastructure Inspection and Monitoring (arXiv, 2026)](https://arxiv.org/abs/2605.04136) - 利用NV色心磁力计/光泵磁力计进行基础设施检测与监测，可穿透涂层/绝缘层/混凝土无需耦合剂；系统分析提拉高度/低频漂移/背景噪声等现场性能限制因素，为钢梁疲劳/腐蚀/电池异常电流等提供非接触式磁诊断方案

- [FID Magnetometer Based on Paraffin-Coated Planar Reflective Multipass Cells (arXiv:2605.02700, 2026)](https://arxiv.org/abs/2605.02700) - 基于石蜡涂覆平面反射多通电池的FID磁力计，在地磁场范围内实现10 pT/√Hz灵敏度；双池差分配置有效抑制公共噪声；平面几何结构支持紧凑光学集成，为芯片级碱金属原子磁力计提供新方案

- [Microwave-free vector magnetometry and crystal orientation determination with NV centers using Bayesian inference (arXiv, 2025)](https://arxiv.org/abs/2512.09925) - 微波自由矢量磁力计，利用贝叶斯推理从ODMR光谱提取磁场矢量与晶体取向外延，无需微波驱动简化硬件复杂度；为芯片级NV磁力计低功耗方案提供新路径

### 量子传感芯片化里程碑 / Chip-Scale Milestones

- [Laser-written micro-channel atomic magnetometer (arXiv:2404.14345, 2024)](https://arxiv.org/abs/2404.14345) - 利用飞秒激光刻蚀+化学蚀刻在熔融 silica 中制作亚毫米沟道，埋深<1mm，内含Rb蒸汽和0.75 amg N₂缓冲气体，传感体积2.25 mm³，零场共振方案实现~1 pT/√Hz@10Hz灵敏度，可与光子结构和微流控通道3D集成；为芯片级碱金属原子磁力计的低成本微型化提供新路径
- [CMOS-integrated quantum sensor based on NV centers (Nature Electronics, 2019)](https://www.nature.com/articles/s41928-019-0275-5) - 金刚石NV色心量子传感器与CMOS技术集成，演示量子磁力计灵敏度32.1 µT/√Hz与同步测温，有源面积仅200µm×200µm；为芯片级量子传感系统奠定工艺基础，代表量子传感从分立仪器向单芯片化演进的关键里程碑

### 量子传感医疗应用 / Medical Applications

- [Siemens Sensus Quantum - 量子传感器实现胎儿脑缺氧毫秒级预警 (2025)](https://www.toutiao.com/w/1827883145188356/) - 西门子Sensus Quantum系统捕捉脑血氧量子涨落，缺氧事件检测灵敏度99.3%，使紧急剖宫产决策时间缩短至3.2分钟；代表量子传感在产科急危重症精准监测中的临床突破

- [Non-invasive magnetocardiography of living rat based on diamond quantum sensor (arXiv:2405.02376, 2024)](https://arxiv.org/html/2405.02376v1) - 基于NV色心量子传感器实现活体大鼠非侵入式心磁图检测，量子传感技术与生物医学检测结合，为心血管疾病无创诊断提供新路径

- [量子磁场传感在心血管/神经疾病检测 (2024)](https://www.163.com/dy/article/JAS0871705340BZM.html) - 未磁科技量子磁场传感器精准检测心脏电活动产生的微弱磁场，实现心肌缺血早期诊断；量子磁力计灵敏度达地球磁场的十亿分之一，无需液氦超导屏蔽即可在普通医疗环境中工作

- [量子传感:工业感知的下一次跨越 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_08569a8149706452) - 基于量子磁力计的脑成像技术正在从实验室走向临床，灵敏度足以在室温环境下非侵入性探测神经元放电产生的微弱磁信号，无需传统笨重的超导屏蔽设备；量子惯性传感器通过读取地球重力场与磁场"指纹"实现深海、隧道、强电子干扰环境下的零漂移自主导航

### 量子传感新兴研究 / Emerging Research

- [硅基光电子原子干涉仪 - 量子指南针里程碑 (Science Advances, LatitudeDa 2026)](https://www.latitudeda.com/document/753) - 首次使用硅基光电子微芯片组件执行原子干涉仪量子传感技术，是开发"量子指南"迈出的重要一步，目标实现无GPS精准导航；传统原子干涉仪系统占据一个小房间的空间，硅基光电子集成使其微型化成为可能

- [德国弗劳恩霍夫IAF量子传感虚拟应用实验室 (2025)](https://www.sohu.com/a/860312231_122006510) - 德国弗劳恩霍夫应用固体物理研究所(Fraunhofer IAF)成立量子传感虚拟应用实验室，配备三台先进量子磁力仪，用户可针对材料测试、微电子、纳米电子及生物医学等领域进行样本测量，推动量子传感从研究走向工业创新

### 量子传感新兴研究 / Emerging Research

- [硅基光电子原子干涉仪 - 量子指南针里程碑 (Science Advances, LatitudeDa 2026)](https://www.latitudeda.com/document/753) - 首次使用硅基光电子微芯片组件执行原子干涉仪量子传感技术，是开发"量子指南"迈出的重要一步，目标实现无GPS精准导航；传统原子干涉仪系统占据一个小房间的空间，硅基光电子集成使其微型化成为可能
- [2D量子传感器利用自旋缺陷实现精确磁场探测 (Nature Communications 2025)](https://so.html5.qq.com/page/real/search_news?docid=70000021_287683edf9978452) - 基于二维自旋缺陷阵列实现精确磁场探测，突破传统量子传感器空间分辨率极限；论文DOI: 10.1038/s41467-025-59642-0；代表量子传感从点传感器向规模化2D传感器件演进的重要方向
- [Princeton Quantum Initiative - NV色心探测二维自旋bath (2026)](https://quantum.princeton.edu/research/quantum-systems-experiment/quantum-sensing-and-metrology) - 普林斯顿大学NV传感器对金刚石表面二维自旋bath进行量子成像研究，探索量子传感与量子材料交叉前沿；反映北美顶级学术机构对NV色心平台持续深耕
- [金刚石NV色心应变工程自旋极化反转 (中科大, Physical Review Letters, 2026)](http://physics.ustc.edu.cn/3586/list1.htm) - 中科大自旋磁共振实验室王亚、王孟祺团队揭示应变对自旋-光学动力学的调控机制，首次在纳米尺度实现自旋极化反转，为高压等极端环境下NV量子探针失效机理提供物理理解
- [量子钻石磁力计正在颠覆精密探测：专访SBQuantum CEO (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_679696777d198552) - SBQuantum CEO专访：量子钻石磁力计在导航、地球观测及目标检测领域的应用价值；公司已获加拿大国防部及欧洲航天局超1500万美元研发合同，2026年4月完成400万美元种子轮融资
- [Bosch Quantum Sensing - 博世+元素六金刚石量子传感 (2025)](https://www.bosch-quantumsensing.com/) - 博世与元素六合资公司，2025年7月成立，总部德国路德维希堡；聚焦芯片级金刚石量子传感器，推动低成本可扩展应用；博世估计医疗与移动领域全球市场潜力达mid-single billion欧元

- [德国弗劳恩霍夫IAF量子传感虚拟应用实验室 (2025)](https://www.sohu.com/a/860312231_122006510) - 德国弗劳恩霍夫应用固体物理研究所(Fraunhofer IAF)成立量子传感虚拟应用实验室，配备三台先进量子磁力仪，用户可针对材料测试、微电子、纳米电子及生物医学等领域进行样本测量，推动量子传感从研究走向工业创新
- [金刚石微环谐振器实现高灵敏度磁场检测 (2025)](https://www.sohu.com/a/875334816_121798711) - 日本丰桥技术科学大学+东京大学+哥伦比亚大学，将金刚石微环谐振器与光子波导耦合，Q因子达2200，电子自旋共振对比度25%，磁场灵敏度1.0µT/√Hz，片上光提取显著提升检测灵敏度
- [Quantum sensing of magnetic fields with molecular spins (npj Quantum Information, 2024)](https://link.springer.com/10.1038/s41534-024-00838-5) - 分子自旋系综嵌入混合量子电路实现AC磁场量子传感协议，动态解耦协议使灵敏度达10⁻¹⁰~10⁻⁹ T/Hz^1/2，突破经典传感器在微波频段的极限
- [UCalgary IQST Shabir Barzanjea获Killam NRC Paul Corkum Fellowship (2026)](https://www.iqst.ca/) - 卡尔加里大学量子科学与技术研究所研究员获此殊荣，将推动加拿大量子传感与量子机器学习融合研究；专注于量子传感与机器学习交叉领域，获奖反映学术界对量子传感实用化方向的持续关注
- [Quantum Days 2026 加拿大量子科学旗舰会议 (2026)](https://2026.quantumdays.ca/) - 2026年2月18-20日加拿大不列颠哥伦比亚省维多利亚市召开，汇聚全球量子科学界定义量子未来，促进研究与商业化对接；会议覆盖量子传感产业化和商业前景
- [香港大学 神经形态宽场量子传感突破 (2024)](https://www.hku.hk/press/press-releases/detail/27099.html) - 香港大学工程学院团队实现宽场量子传感技术突破，提出神经形态事件传感器结合帧基传感器方案，用于监测生物系统动态过程，空间分辨率达纳米级，可捕捉毫秒级动态变化

### 量子传感医疗应用 / Medical Applications

- [量子磁场传感在心血管/神经疾病检测 (2024)](https://www.163.com/dy/article/JAS0871705340BZM.html) - 未磁科技量子磁场传感器精准检测心脏电活动产生的微弱磁场，实现心肌缺血早期诊断；量子磁力计灵敏度达地球磁场的十亿分之一，无需液氦超导屏蔽即可在普通医疗环境中工作

- [量子传感:工业感知的下一次跨越 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_08569a8149706452) - 基于量子磁力计的脑成像技术正在从实验室走向临床，灵敏度足以在室温环境下非侵入性探测神经元放电产生的微弱磁信号，无需传统笨重的超导屏蔽设备；量子惯性传感器通过读取地球重力场与磁场"指纹"实现深海、隧道、强电子干扰环境下的零漂移自主导航

### 新兴传感机制 / Novel Sensing Mechanisms

- [Quantum sensing of time dependent electromagnetic fields with single electron excitations (arXiv:2405.05796, 2024)](https://arxiv.org/abs/2405.05796) - 研究利用电子Mach-Zehnder干涉仪在亚纳秒时间尺度探测电磁场量子态，单电子激发作为敏感媒介，为芯片级量子电磁传感提供新路径；突破传统光学读出的时间分辨率极限

- [Microwave-free imaging magnetometry with NV centers in nanodiamonds at near-zero field (arXiv:2409.02199, 2024)](https://arxiv.org/abs/2409.02199) - 微波自由NV成像磁力计，利用零场交叉驰豫特征，无需微波即可实现宽视场成像，在环境条件下灵敏度达4.5 µT/√Hz；为生物样品或薄导电样品的非侵入式磁场成像提供新方案

### 六方氮化硼量子传感 / hBN Quantum Sensing

- [Quantum sensing and imaging with spin defects in hexagonal boron nitride (arXiv:2302.11169)](https://arxiv.org/abs/2302.11169) - hBN二维材料中的色心作为新兴量子传感平台：高稳定性、2D层状结构易于片上集成、可与纳米光子学/等离子体结构融合；光致可寻址自旋缺陷提供光子-自旋量子界面，为固态量子传感从金刚石向二维材料延展开辟新方向

- [Quantum sensing in the fractional Fourier domain (arXiv:2405.03896)](https://arxiv.org/abs/2405.03896) - 提出分数傅里叶域量子传感协议，利用任意角度时间-频率平面线性轨迹驱动传感量子比特，在时变光谱信号感知中实验展示优势；以NV色心系综验证，为复杂信号环境下的量子传感提供新脉冲序列设计范式

### NV色心进阶教程 / NV Center Advanced Tutorials

- [Magnetometry with single NV centers in diamond - Qolah Research (2026)](https://www.qolah.org/research/nv_v2/nv_v2.html) - 澳大利亚Qolah研究团队发布的单NV色心磁力计实验教程，涵盖实验装置细节（低氮浓度合成金刚石、共聚焦显微镜、532nm激光激发）、NV色心工作原理（光极化、ESR、自旋态读出）、潜在微型化至数cm³体积的可能性；是理解NV磁力计实验实现的高质量入门参考资料，可与QuantumVillage/UncutGem开源项目配套学习

### NV色心前沿 / NV Center Frontiers

- [NV色心T₂*退相干时间突破: 毫米级12C富集金刚石中值4.5µs (Communications Physics 2025)](https://www.nature.com/articles/s43246-025-00782-7) - ¹²C富集高静高压(HPPT)金刚石中NV色心自旋退相干时间T₂*中值达4.5µs，批次差异仅10%，毫米级大面积均匀性为femtotesla级弱磁场探测奠定基础；是量子传感实用化的关键材料里程碑

- [Bottom-up fabrication of scalable room-temperature diamond quantum computing and sensing technologies (Materials Quantum Technology 2025, IOPscience)](https://iopscience.iop.org/article/10.1088/2633-4356/adf0ef) - 2025年IOPscience综述论文，系统梳理NV色心从基础物理到可扩展集成的关键挑战与路线图；涵盖多NV中心集成、金刚石材料生长、晶圆级制造等核心议题；代表NV色心量子技术从实验室向可扩展实用系统演进的重要里程碑

- [Xanadu量子纠错突破: 光子量子比特qLDPC代码实用化 (PRL 2026)](https://quantumzeitgeist.com/xanadu-breakthrough-in-quantum-error-correction-reduces-qubit-overheads-for-fault-tolerant-computing/) - 2026年4月发表在Physical Review Letters，利用光子量子比特实现任意量子纠错代码，显著减少所需物理量子比特数量；光子路径进入容错量子计算实用化阶段，为量子传感与量子计算融合提供更可靠硬件基础
- [PRX Quantum 2026 - 多参数量子估计：NV电子-核自旋纠缠同步估计多参数 (MIT/东京大学/港中大)](https://so.html5.qq.com/page/real/search_news?docid=70000021_15469e0c1b599852) - 利用电子-核自旋纠缠及优化贝尔态测量方案，在单次测量序列中同步估计微波驱动场幅值、失谐量与相位，所有参数灵敏度随探测时间呈线性标度；量子多参数估计领域的里程碑工作
- [低温NV色心扫描磁强计 attoNVM - 1.8K实现3 µT/√Hz灵敏度 (attocube, 2026)](https://new.qq.com/rain/a/20260122A024JB00) - 德国attocube公司研发，2K~300K温度区间工作，纳米级分辨率杂散磁场测量，专用于低温量子材料与超导器件成像；可进行限额免费测试，反映NV扫描显微技术向低温工况扩展的行业趋势
- [Princeton Quantum Initiative - NV色心探测二维自旋bath (2026)](https://quantum.princeton.edu/research/quantum-systems-experiment/quantum-sensing-and-metrology) - 普林斯顿大学NV传感器对金刚石表面二维自旋bath进行量子成像研究，探索量子传感与量子材料交叉前沿；反映北美顶级学术机构对NV色心平台持续深耕
- [量子传感国防应用路线图：NSA三大支柱，2029年25亿美元市场 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_89669beb1a1ac452) - 量子传感与量子计算、量子通信并列构成美国国家安全局(NSA)量子技术三大支柱；量子惯性导航、量子磁力计、量子陀螺仪是国防应用三大方向；量子传感器市场预测2029年达25亿美元

### 实船测试里程碑 / Real-World Marine Testing

- [Imperial College量子传感原型机登陆英国皇家海军舰艇 (2026)](https://www.imperial.ac.uk/news/245114/quantum-sensor-future-navigation-system-tested/) - Imperial College研制的量子传感原型机在皇家海军舰艇上完成测试，是将量子传感器从实验室推向真实环境的重要里程碑；量子传感有望消除传统惯性导航系统的漂移问题，实现长时间高精度无GPS自主导航；估计GPS服务中断一天将使英国损失10亿英镑


### 国防军事应用 / Defense & Military

- [SandboxAQ AQNav - 全球首款商用量子+AI导航系统,应对GPS干扰 (2026)](https://www.sandboxaq.com/press/sandboxaq-announces-aqnav---worlds-first-commercial-real-time-navigation-system-powered-by-ai-and-quantum-to-address-gps-jamming) - 2026年5月2日SandboxAQ发布AQNav,整合AI算法、量子传感与地球地壳磁场实现GPS拒止环境导航,覆盖空中/陆地/海上全场景;已在美国空军多型飞机上完成飞行测试,从单发动机到大型军用运输机均验证有效;抗干扰、全天候、地形无关;估值超50亿美元,获谷歌/英伟达投资;代表量子传感在导航领域首个大规模商用里程碑
- [IonQ入选MDA 1510亿美元SHIELD计划 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_690699ed88536652) - 2026年2月成功入围美国导弹防御局"战略一体化、分层防御与赋能(SHIELD)"IDIQ合同名单，总金额上限1510亿美元，标志着量子传感技术正式进入美国最核心武器系统的长期采购目录
- [量子传感国防应用路线图：NSA三大支柱，2029年25亿美元市场 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_89669beb1a1ac452) - 量子传感与量子计算、量子通信并列构成NSA量子技术三大支柱；量子惯性导航、量子磁力计、量子陀螺仪是国防应用三大方向；量子传感器市场预测2029年达25亿美元，2033年达32亿美元
- [Q-CTRL获DARPA 2440万美元RoQS合同 (2025)](https://new.qq.com/rain/a/20250828A07QF600) - 美国DARPA"稳健量子传感器"计划合同，将量子传感技术应用于高性能军用车辆在严苛军事环境中的可靠导航
- [Q-CTRL入选TIME 2026行业领袖100强 (2026)](https://q-ctrl.com/) - Q-CTRL凭借量子传感与量子计算领域的AI驱动基础设施软件入选《时代》首届"行业领袖100强"榜单;Q-CTRL同时持有量子传感与量子计算双赛道,量子传感方向已实现全球首个量子保证导航(GPS-free)并创下世界纪录;麦肯锡预测量子市场达2万亿美元,Q-CTRL处于连接量子与经典世界的核心位置
- [Nokia量子安全网络：量子传感提升侦察、监视与深海导航能力 (2026)](https://www.nokia.com/index%2ephp/industries/quantum-safe-networks/) - Nokia展示量子传感与量子分析技术如何提升国防行动能力，涵盖量子传感在侦察、监视和深海导航中的应用；量子安全网络已成为保护关键基础设施的核心技术底座

### 量子传感与机器学习 / Quantum Sensing + Machine Learning

- [Machine Learning Assisted Tracking of Magnetic Objects using Quantum Diamond Magnetometry (arXiv:2502.14683, 2025)](https://arxiv.org/abs/2502.14683) - 利用机器学习（无需物理模型）结合量子钻石磁力计实时追踪磁性目标位置，演示地下基础设施测绘、地面运输监测；为量子传感+AI融合应用提供新范式

### 新兴量子传感应用 / Emerging Applications

- [量子鬼成像量子传感 - 非侵入式植物活体成像 (MedSci 2026)](https://www.medsci.cn/sci/show_paper.asp?id=35c4a1259231266b) - 基于量子增强鬼成像技术实现植物非侵入式活体成像，无需物理接触即可观测植物内部结构与生理动态；量子传感在农业与植物学表型研究中的应用探索

### 新增 / New Entries

- [Sandia Labs 量子传感项目矩阵 - 原子干涉仪专利与芯片化路线图 (2025)](https://www.sandia.gov/quantum/quantum-sensing/) - Sandia量子传感聚焦微型化量子传感器与原子钟，已获批专利：引导原子干涉仪大动态范围高灵敏度测量协议(US12392611B1,2025)、悬空波导膜结构光原子陷阱集成平台(US11914188B1,2024)；关键能力：量子赋能电场传感/成像、超灵敏重力场及梯度测量、非侵入式功能脑成像系统(使用Sandia专利量子传感器)、量子重力与惯性传感器(下一代惯性导航关键)、微型光原子钟(集成单光子探测器与波导光传输)；代表美国国家实验室量子传感芯片化系统布局

- [多国团队量子传感器提升粒子探测时空精度 - 超导微线单光子探测器SMSPD (仪器仪表期刊, 2025)](https://new.qq.com/rain/a/20250428A01QW800) - 美国/瑞士/委内瑞拉等多国联合研究团队开发基于量子传感技术的超导微线单光子探测器(SMSPD)，用于粒子物理实验时空同步高精度追踪；在费米实验室测试表明探测效率显著优于传统探测器；代表量子传感在高能物理领域的实用化进展

- [武汉大学研制世界体积最小芯片原子钟 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_25469250ce164452) - 武汉大学陈杰华教授团队研制世界体积最小的芯片原子钟，体积仅2.3立方厘米（指甲盖大小），体积只有国外同类产品的1/7；另一款火柴盒大小的WAX.21s型芯片原子钟已商用，2025年单款销售额超千万元；拇指盖大小款正在加速产业化

### 量子纠缠原子钟 / Entangled Atomic Clocks

- [量子纠缠让原子钟精度更上层楼 (PTB, Physical Review Letters, 2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_62569afdfb189352) - 德国联邦物理技术研究院(PTB)利用量子纠缠增强原子钟计时稳定性，于2026年2月发表在《物理评论快报》；研究利用纠缠粒子对之间的内在关联性，显著降低时钟的计时抖动，为下一代基准原子钟奠定基础

- [μ子反常磁矩精准测量 — Science 2025年度十大科学突破 (Fermilab/费米实验室, 2025)](https://so.html5.qq.com/page/real/search_news?docid=70000021_71769c4c7ed73652) - 2025年Science评选为年度十大科学突破之一；实验与第一性原理理论计算在"千万分之一"精度处高度吻合，代表量子精密测量技术的极限水平；验证了标准模型最精确的预测之一，为寻找新物理提供了基准参照；彰显高精度实验与理论计算共同推动基础物理认知边界的重要范式

- [Tracking time-varying signals with quantum-enhanced atomic magnetometers (arXiv:2503.14793, 2025)](https://arxiv.org/abs/2503.14793) - 量子纠缠（自旋压缩）增强原子磁力计对时变信号的追踪能力，利用估计控制技术实现快速变化磁场的实时跟踪，在心磁图信号演示中获得量子优势；单次相干时间内完成噪声背景下瞬态信号追踪，为量子磁力计在生物医学信号检测中的应用提供新范式

- [Chemically resolved NMR spectroscopy by longitudinal magnetization detection with diamond magnetometer (arXiv:2503.02140, 2025)](https://arxiv.org/abs/2503.02140) - 利用NV色心实现化学分辨核磁共振波谱，在0.32T磁场下达到~350 ppb分数光谱分辨率，可在~1nL检测体积内解析乙醇化学位移结构；为纳米级化学分析提供无感应磁力计新方案

- [Limits of absolute vector magnetometry with NV centers in diamond (arXiv:2504.20750, 2025)](https://arxiv.org/abs/2504.20750) - 研究NV色心矢量磁力测量精度极限，推导磁场矢量到自旋共振频率的精确解析公式（含开源Python包），系统分析误差来源与补偿策略；促进使用Voigt线型精确拟合共振线宽；为绝对磁场测量精度评估与实验设计提供重要参考

- [中国计量院锶原子光晶格钟NIM-Sr1正式校准国际标准时间 (2026)](https://news.mydrivers.com/tag/yuanzizhong.htm) - 2026年2月中国计量院研制的锶原子光晶格钟NIM-Sr1正式获准校准国际标准时间，实现我国光钟参与校准国际标准时间"零"的突破；核心突破在于将单个锶离子冷却至5K(-268.15°C)极低温环境运行，精度达数十亿年误差不超过一秒

*最后更新: 2026-05-10 (本次新增: 中科院长春光机所量子陀螺专用VCSEL芯片/清华大学148nm核光钟激光光源/Budker团队arXiv:2605.00152碳-13 ODNMR)*

### NV色心前沿 / NV Center Frontiers

- [金刚石NV色心应变工程自旋极化反转 (中科大, Physical Review Letters, 2026)](http://physics.ustc.edu.cn/3586/list1.htm) - 中科大自旋磁共振实验室王亚、王孟祺团队揭示应变对自旋-光学动力学的调控机制，首次在纳米尺度实现自旋极化反转，为高压等极端环境下NV量子探针失效机理提供物理理解

- [量子机器学习高精度时间预测 (中科大, 2026)](http://physics.ustc.edu.cn/3586/list1.htm) - 中科大彭新华教授团队与复旦大学合作，利用关联系统实验量子储备计算实现高精度时间预测，相关成果于2026年3月25日发表

- [PRX Quantum 2026 - 多参数量子估计：NV电子-核自旋纠缠同步估计多参数 (MIT/东京大学/港中大)](https://so.html5.qq.com/page/real/search_news?docid=70000021_15469e0c1b599852) - 利用电子-核自旋纠缠及优化贝尔态测量方案，在单次测量序列中同步估计微波驱动场幅值、失谐量与相位，所有参数灵敏度随探测时间呈线性标度；量子多参数估计领域的里程碑工作

- [Princeton Quantum Initiative - NV色心探测二维自旋bath (2026)](https://quantum.princeton.edu/research/quantum-systems-experiment/quantum-sensing-and-metrology) - 普林斯顿大学NV传感器对金刚石表面二维自旋bath进行量子成像研究，探索量子传感与量子材料交叉前沿；反映北美顶级学术机构对NV色心平台持续深耕

- [量子传感国防应用路线图：NSA三大支柱，2029年25亿美元市场 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_89669beb1a1ac452) - 量子传感与量子计算、量子通信并列构成美国国家安全局(NSA)量子技术三大支柱；量子惯性导航、量子磁力计、量子陀螺仪是国防应用三大方向；量子传感器市场预测2029年达25亿美元

### 国防军事应用 / Defense & Military

- [IonQ入选MDA 1510亿美元SHIELD计划 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_690699ed88536652) - 2026年2月成功入围美国导弹防御局"战略一体化、分层防御与赋能(SHIELD)"IDIQ合同名单，总金额上限1510亿美元，标志着量子传感技术正式进入美国最核心武器系统的长期采购目录

- [Q-CTRL获DARPA 2440万美元RoQS合同 (2025)](https://new.qq.com/rain/a/20250828A07QF600) - 美国DARPA"稳健量子传感器"计划合同，将量子传感技术应用于高性能军用车辆在严苛军事环境中的可靠导航

- [Nokia量子安全网络：量子传感提升侦察、监视与深海导航能力 (2026)](https://www.nokia.com/index%2ephp/industries/quantum-safe-networks/) - Nokia展示量子传感与量子分析技术如何提升国防行动能力，涵盖量子传感在侦察、监视和深海导航中的应用；量子安全网络已成为保护关键基础设施的核心技术底座

### 量子传感学术前沿 / Latest Research

- [Quantum Days 2026 - 加拿大量子科学创新会议 (2026)](https://2026.quantumdays.ca/) - 2026年2月18-20日加拿大不列颠哥伦比亚省维多利亚市召开，汇聚研究突破、商业化应用展示、投资机会识别、政策制定者参与；量子传感产业化与商业前景是核心议题之一；反映加拿大作为全球量子里程碑地区的持续战略投入

- [量子纠缠增强量子精密测量 - 深圳大学 (2026)](https://quantum.szu.edu.cn/info/1090/1427.htm) - 量子精密测量是原子钟、量子磁力计等量子传感器件的物理基础，其核心是利用量子纠缠突破经典测量精度极限（标准量子极限），实现超越经典物理极限的测量灵敏度；量子纠缠作为独特量子资源是变革性量子技术的关键

- [NV色心应变工程自旋极化反转 (中科大, Physical Review Letters, 2026)](http://physics.ustc.edu.cn/3586/list1.htm) - 中科大自旋磁共振实验室王亚、王孟祺团队揭示应变对自旋-光学动力学的调控机制，首次在纳米尺度实现自旋极化反转，为高压等极端环境下NV量子探针失效机理提供物理理解

- [量子机器学习高精度时间预测 (中科大, 2026)](http://physics.ustc.edu.cn/3586/list1.htm) - 中科大彭新华教授团队与复旦大学合作，利用关联系统实验量子储备计算实现高精度时间预测，相关成果于2026年3月25日发表；展示量子计算与传感在时间序列分析领域的交汇应用

### 量子传感学术前沿 / Latest Research

- [EU Quantum Flagship 新成立量子计算顾问委员会 (2026)](https://qt.eu/) - 2026年4月28日EU Quantum Flagship启动量子计算顾问委员会，旨在加速欧洲量子技术从研究到产业的转化；Quantum Flagship是欧盟最大量子技术倡议，10年预算10亿欧元，覆盖量子传感/通信/计算/模拟四大支柱；量子传感与计量是核心议题之一，Q-Expo 2026将于5月18-19日举办
- [ISC High Performance 2026 - HPC/AI/量子融合 (2026)](https://www.isc-hpc.com/) - 2026年6月22-26日德国汉堡召开，主题"HPC, AI, Quantum: Powering Innovation and Sustainability"；量子计算与传感是核心议题之一；反映高性能计算与量子技术深度融合趋势
- [Quantum Science Ltd - INFIQ量子点红外传感技术 (2026)](https://quantumscis.com/) - 英国量子科技公司，INFIQ®量子点技术覆盖800-2400nm红外波段，高性能含铅量子点(HP-QDs)达世界领先水平，无铅量子点(LF-QDs)正在商业化；目标市场：汽车自动驾驶(800nm-2400nm)/移动设备/IoT/医疗成像/工业自动化；量子点作为新兴固态传感材料，为量子传感从NV色心向纳米材料多元化发展提供新路径

- [城际量子传感网络 - 国际首个核自旋城际网络 (Nature 2026)](https://www.nature.com/articles/s41586-025-10034-w) - 中国科学技术大学等团队构建国际首个基于核自旋的城际量子传感网络（合肥—杭州，跨度320公里，5台核自旋量子传感器），利用卫星同步实现分布式量子传感；结合核自旋量子放大技术将信号放大100倍，旋转灵敏度达约10⁻⁶ rad，首次实验突破轴子拓扑缺陷暗物质天体物理观测极限；误报率降低约三个数量级，能量分辨率较GNOME提升约4个数量级

- [量子精密测量Nature 2026值得关注技术 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_669697945a514652) - Nature 2026年度值得关注技术榜单聚焦量子精密测量技术；从猪器官移植救人到AI精准预测飓风、从量子计算突破到深海探测，量子精密测量是唯一上榜的基础物理测量技术类别

- [量子精密测量技术最新进展与应用 (2025)](https://max.book118.com/html/2025/0226/7126143134010041.shtm) - 系统性量子传感技术综述：利用量子纠缠态、量子叠加态和量子隧穿效应实现超常规测量；量子态演化受测量对象影响，通过观测量子态变化实现精准感知；涵盖量子精密测量在医疗诊断、资源勘探等领域的应用

### 量子传感学术前沿 / Latest Research

- [Imperial College量子传感导航系统首登英国皇家海军舰艇 (2026)](https://www.imperial.ac.uk/news/245114/quantum-sensor-future-navigation-system-tested/) - Imperial College研制的量子传感原型机在皇家海军舰艇上完成测试,是将量子传感器从实验室推向真实环境的重要里程碑；量子传感有望消除传统惯性导航系统的漂移问题,实现长时间高精度无GPS自主导航；估计GPS服务中断一天将使英国损失10亿英镑

- [Nature 2026年度值得关注技术榜单 - 量子精密测量唯一上榜基础物理技术 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_669697945a514652) - 从猪器官移植救人到AI精准预测飓风、从量子计算突破到深海探测，量子精密测量是Nature 2026年度榜单唯一上榜的基础物理测量技术类别；反映全球学术界与产业界对量子传感技术变革性潜力的高度共识

- [Nature Sensors 2026年正式创刊 — 全球传感共同体新平台 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_39069cca2fd62052) - Nature系列全新期刊将于2026年1月正式上线，聚焦传感科学与技术前沿；2026年4月举行创刊论坛（延世大学/成均馆大学/汉阳大学），推动量子传感与全球传感研究网络深度融合

### 多参数量子估计 / Multiparameter Estimation

- [Multiparameter Quantum Function Estimation: Ultimate Bound & Optimal Protocol (arXiv:2605.04136, 2026)](https://arxiv.org/abs/2605.04136) - 推导任意哈密顿量多参数函数的终极量子极限并提出达此界限的估计协议，证明任务虽本质是多参数问题但紧束缚可化为优化单参数量子Cramér-Rao界限；统一并扩展前期工作，为一般量子系统最优函数估计提供通用框架

- [Entanglement-Assisted Multiparameter Estimation with Solid-State Quantum Sensor (PRX Quantum 2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_15469e0c1b599852) - MIT/东京大学/港中大团队利用电子-核自旋纠缠在单次测量序列中同步估计微波驱动场幅值、失谐量与相位，灵敏度随探测时间线性标度

### 量子传感物理机制 / Physical Mechanisms

- [All-optical NV核量子传感 — 纯光学方案突破小型化瓶颈 (npj Quantum Information 2023)](https://www.nature.com/articles/s41534-023-00724-6) - 纯光学方案实现NV色心核自旋量子传感，无需微波/射频驱动，为量子传感器芯片级低功耗非侵入性方案提供新路径

### 新兴传感机制 / Novel Sensing Mechanisms

- [宽带射频电场量子传感 — 频率范围扩大800倍 (Nature Physics 2025)](https://www.nature.com/articles/s41567-024-02753-0) - 基于囚禁离子运动Raman跃迁实现宽带射频电场传感，超越标准量子极限3.4(2.0)dB，可用于暗物质搜索与高频量子比特控制

---

*最后更新: 2026-05-10 (本次新增: Q-CTRL入选《时代》2026行业领袖100强/开放量子系统噪声理论与非马尔可夫多时间记忆效应)*

### 新兴期刊与综述 / Emerging Journals & Reviews

- [Nature Sensors - 鲁棒光谱传感器用于远程生物特征检测 (2026)](https://www.nature.com/articles/s44460-025-00012-0) - 发表在Nature Portfolio 2026年创刊新刊(IF 5.000+)，提出抗环境光波动的光谱传感技术，可实现远程心电图波形准确检测；量子传感与生物医学检测融合的重要进展，为远程健康评估提供实用化路径

- [城际量子传感网络 - 国际首个核自旋城际网络Nature 2026合肥-杭州320公里 (Nature 2026)](https://www.nature.com/articles/s41586-025-10034-w) - 中国科学技术大学等团队构建国际首个基于核自旋的城际量子传感网络（合肥—杭州，跨度320公里，5台核自旋量子传感器），利用卫星同步实现分布式量子传感；结合核自旋量子放大技术将信号放大100倍，旋转灵敏度达约10⁻⁶ rad，首次实验突破轴子拓扑缺陷暗物质天体物理观测极限；误报率降低约三个数量级，能量分辨率较GNOME提升约4个数量级

### 开放量子系统与噪声 / Open Quantum Systems & Noise

- [Beating noise in frequency estimation with squeezing and memory in continuous-variable systems (arXiv:2605.06263, 2026)](https://arxiv.org/abs/2605.06263) - 研究开放量子系统中的频率估计问题，利用压缩哈密顿量工程与非马尔可夫动力学突破环境噪声限制；通过量子布朗运动模型证明有限记忆环境可诱导信息回流，暂时恢复并超越么正极限估计精度；为实用化量子磁力计在真实噪声环境下的性能优化提供理论框架
- [Multitime memory beyond the quantum regression theorem in sequential measurement statistics (arXiv:2605.06427, 2026)](https://arxiv.org/abs/2605.06427) - 揭示开放量子系统顺序测量统计中偏离量子回归定理的多时间记忆效应，提出基于协议相关的非马尔可性量化方法；spin-boson模型基准测试表明低环境温度与特定测量协议可增强多时间记忆特征；为量子传感系统环境耦合表征与噪声抑制提供新工具

### 量子传感与机器学习 / Quantum Sensing + Machine Learning

- [Machine Learning Assisted Tracking of Magnetic Objects using Quantum Diamond Magnetometry (arXiv:2502.14683, 2025)](https://arxiv.org/abs/2502.14683) - 利用机器学习（无需物理模型）结合量子钻石磁力计实时追踪磁性目标位置，演示地下基础设施测绘、地面运输监测；为量子传感+AI融合应用提供新范式

### 新兴传感机制 / Novel Sensing Mechanisms

- [量子鬼成像量子传感 - 非侵入式植物活体成像 (MedSci 2026)](https://www.medsci.cn/sci/show_paper.asp?id=35c4a1259231266b) - 基于量子增强鬼成像技术实现植物非侵入式活体成像，无需物理接触即可观测植物内部结构与生理动态；量子传感在农业与植物学表型研究中的应用探索


### 量子传感与机器学习 / Quantum Sensing + Machine Learning

- [Machine Learning Assisted Tracking of Magnetic Objects using Quantum Diamond Magnetometry (arXiv:2502.14683, 2025)](https://arxiv.org/abs/2502.14683) - 利用机器学习（无需物理模型）结合量子钻石磁力计实时追踪磁性目标位置，演示地下基础设施测绘、地面运输监测；为量子传感+AI融合应用提供新范式


### 开源项目 / Open Source Projects

- [QuantumVillage/UncutGem V2 — 全开源NV色心磁力计 · DEF CON 33发布 (2025)](https://github.com/QuantumVillage/UncutGem) - 全球首个全栈开源NV色心钻石磁力计项目，V2版本于DEF CON 33（2025年）发布，包含完整硬件/固件/science文档，总成本约115英镑；涵盖3D打印件、BuildGuide、MaxMSP、Jupyter等完整工具链，可用于纳米级磁场传感研究；项目目标：打造可访问、可扩展、可破解的开放量子传感平台；2026年5月9日GitHub仍有最新commit，98 Commits持续活跃更新

- [MIT/本田/陆军DEVCOM — 腔增强固态核自旋陀螺仪灵敏度提升3个数量级 (PRL 2026-05-09)](https://new.qq.com/rain/a/20250512A083QW00) - MIT、美国本田研究所、陆军DEVCOM陆军研究实验室、马萨诸塞大学波士顿分校联合发表，基于NV系综构建nNV-cQED系统，首次实现电磁感应透明、无反转激射、振荡行为；评估为惯性传感器时旋转灵敏度较此前固态自旋演示提升3个数量级；NV电子自旋可同时用作comagnetometer，四个结晶轴NV可实现矢量分辨率；是固态核自旋量子陀螺仪的重要突破

### NV色心前沿 / NV Center Frontiers

- [attocube attoNVM — 低温NV色心扫描磁强计 1.8K实现3 µT/√Hz (2026)](https://new.qq.com/rain/a/20260122A024JB00) - 德国attocube公司研发，2K~300K温度区间工作，纳米级分辨率杂散磁场测量，专用于低温量子材料与超导器件成像；可进行限额免费测试，反映NV扫描显微技术向低温工况扩展的行业趋势

- [MIT/东京大学/港中大 — 电子-核自旋纠缠多参数量子估计 (PRX Quantum 2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_15469e0c1b599852) - 利用电子-核自旋纠缠及优化贝尔态测量方案，在单次测量序列中同步估计微波驱动场幅值、失谐量与相位，所有参数灵敏度随探测时间呈线性标度；量子多参数估计领域的里程碑工作

### 多参数量子估计 / Multiparameter Estimation

- [Multiparameter estimation with entangled atomic sensor array (arXiv:2504.08677, 2025)](https://arxiv.org/abs/2504.08677) - 利用纠缠原子阵列实现多参数量子估计，通过分裂自旋压缩态创建阵列间纠缠，在联合估计任务中突破标准量子极限
- [Multiparameter Quantum Function Estimation: Ultimate Bound & Optimal Protocol (arXiv:2605.04136, 2026)](https://arxiv.org/abs/2605.04136) - 推导任意哈密顿量多参数函数的终极量子极限并提出达此界限的估计协议，证明任务虽本质是多参数问题但紧束缚可化为优化单参数量子Cramér-Rao界限；统一并扩展前期工作，为一般量子系统最优函数估计提供通用框架
- [Quantum magnetometry of transient signals with 1.1 ns time resolution (arXiv:2411.05542, 2024)](https://arxiv.org/abs/2411.05542) - 基于单NV色心室温磁力计实现1.1纳秒时间分辨率与450 MHz瞬时带宽，突破量子磁传感器的动态响应极限；适用于瞬态电磁事件探测
- [Low-temperature NV scanning magnetic microscope with 3 µT/√Hz sensitivity (attocube attoNVM, 2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_54769717fc807152) - 德国attocube公司attoNVM产品，2K~300K温度区间工作，纳米级分辨率杂散磁场测量，专用于低温量子材料与超导器件成像
- [Microscale Fiber-Integrated Vector Magnetometer with On-Tip Field Biasing (arXiv:2404.14089, 2024)](https://arxiv.org/abs/2404.14089) - 微米级光纤集成矢量磁力计，尖端集成微型线圈产生局部偏置磁场，片上微型化方案显著减少传统笨重的3D Helmholtz线圈配置
- [Quantum Sensing of 2D Magnetism with NV Centers in Diamond (Communications Physics, 2025)](https://www.nature.com/articles/s42005-023-01472-x) - 利用NV色心对二维材料Fe₃GeTe₂进行量子传感磁成像，揭示二维磁性材料临界点附近的磁 bistable状态退激发物理机制

### 量子导航与惯性传感 / Quantum Navigation & Inertial Sensing

- [A Short Introduction to Basic Principles of Quantum Navigation Based-on Rb Cold Atom Interferometry (arXiv:2405.14910, 2024)](https://arxiv.org/abs/2405.14910) - 基于铷冷原子干涉仪的量子导航入门综述，阐述如何利用原子能级对外部变化的固有敏感性实现无卫星自校准导航系统；适用于惯性导航传感器与量子陀螺仪基础研究
- [硅基光电子原子干涉仪 - 量子指南针里程碑 (Science Advances, LatitudeDa 2026)](https://www.latitudeda.com/document/753) - 首次使用硅基光电子微芯片组件执行原子干涉仪量子传感技术，是开发"量子指南针"迈出的重要一步，目标实现无GPS精准导航；传统原子干涉仪系统占据一个小房间的空间，硅基光电子集成使其微型化成为可能
- [量子导航技术在英国铁路取得重大突破 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_53669c4a73c75752) - 2026年3月量子惯性导航系统(RQINS)在全球范围内首次完成铁路实车测试，搭载于英国GTR运营列车在伦敦至韦林花园市线路运行；项目由MoniRail牵头，联合帝国理工学院/萨塞克斯大学/QinetiQ等战略联盟推进，获英国创新署与DSIT支持；量子传感为GPS拒止环境提供更低成本、更可靠、更抗干扰的定位方案
- [城际量子传感网络 - 国际首个核自旋城际网络 (Nature 2026)](https://www.nature.com/articles/s41586-025-10034-w) - 中国科学技术大学等团队构建国际首个基于核自旋的城际量子传感网络（合肥—杭州，跨度320公里，5台核自旋量子传感器），利用卫星同步实现分布式量子传感；结合核自旋量子放大技术将信号放大100倍，旋转灵敏度达约10⁻⁶ rad，首次实验突破轴子拓扑缺陷暗物质天体物理观测极限；误报率降低约三个数量级，能量分辨率较GNOME提升约4个数量级

### 量子传感产业分析 / Industry Analysis

- [量子传感：工业感知的下一次跨越 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_08569a8149706452) - 深度长文解析量子传感产业发展：全球市场规模2025年18.8亿美元、2035年将达50.7亿美元(年均复合增长率10.42%)；阐述量子叠加态/纠缠态/相干性三大物理机制驱动的传感器家族；量子传感正在跨越实验室与工业应用的"死亡之谷"，是量子技术商业化最快速的分支

- [Quantum Motion融资1.6亿美元C轮 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_18369fc878c29252) - 伦敦量子计算初创公司完成1.6亿美元C轮融资(DCVC/Kembara领投)，创英国量子公司最大单笔VC融资纪录；采用标准硅晶体管技术制造量子比特，硅量子点路线与量子传感高度协同；2025年已部署于英国国家量子计算中心，进入DARPA量子基准测试B阶段，与GlobalFoundries深化硅基半导体制造合作

### 量子计算×量子传感融合 / Computing × Sensing Convergence

- [QuiX Quantum突破光子误差阈值 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_67369cfa2c255852) - 荷兰QuiX Quantum于2026年4月宣布将光子量子计算机物理误差抑制到容错计算阈值以下，光子路径正式进入"阈值以下"新纪元；为量子传感与量子计算融合提供更可靠的光子学硬件基础
- [QuEra中性原子量子纠错突破 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_44669e9fc4f19552) - QuEra联合哈佛/MIT团队实现超过1/2编码率，仅约2:1物理-逻辑量子比特比，将每个校正周期逻辑错误率降至约10⁻¹³的Teraquop阈值；为中性原子平台铺就通往实用量子计算的清晰路径

### 分布式量子传感 / Distributed Quantum Sensing

- [城际分布式量子传感网络 - 轴子暗物质搜索新范式 (Nature 2026)](https://www.nature.com/articles/s41586-025-10034-w) - 全球城际分布式量子传感器网络，利用超极化惰性气体核自旋实现10⁻⁶ rad灵敏度，在轴子拓扑缺陷暗物质搜索领域取得里程碑式新约束；是量子传感网络在大物理搜索中的标志性应用

---

*最后更新: 2026-05-08 (本次新增：量子鬼成像植物活体成像MedSci 2026/量子心磁图MCG+AI临床诊断/Quantum Design收购牛津NanoScience)*

- [基于频率纠缠双光子和级联HOM干涉的量子陀螺仪理论研究 (物理学报 2025)](https://wulixb.iphy.ac.cn/article/doi/10.7498/aps.74.20250077) - 利用频率纠缠双光子和级联Hong-Ou-Mandel干涉实现量子陀螺仪，三轴角速度测量精度可超越经典光学陀螺仪，量子Fisher信息分别达(2, 0.1, 0.006)；为量子陀螺仪在全球导航传感领域的应用提供理论支持

### 量子陀螺仪研究突破 / Quantum Gyroscope Research

- [中科院长春光机所量子陀螺专用VCSEL芯片 — 795nm单模工作80°C达4.1mW (Optics Express, 2026)](https://www.163.com/dy/article/H2OVD7D10514R9P4.html) - 中科院长春光学精密机械与物理研究所大功率半导体激光器研究团队突破量子陀螺专用VCSEL芯片核心瓶颈：通过解决模式稳定性与输出功率相互制约的关键问题，实现大氧化孔径下VCSEL单模工作，80°C下输出功率4.1mW，边模抑制比41.68dB，正交偏振抑制比27.6dB；795nm波长与原子系统直接耦合，量子陀螺理想光源的国产化里程碑

- [Quantum control and Berry phase of electron spins in rotating levitated diamonds (Nature Communications 2024)](https://www.nature.com/articles/s41467-024-49175-3) - 悬浮纳米金刚石中电子自旋量子控制与贝里相位研究，展示自旋与粒子转动的耦合，可用于量子陀螺仪与转动物质波干涉仪；是悬浮金刚石量子传感在宏观量子力学与精密测量应用中的重要进展
- [Chip-scale integrated optical gyroscope based on multi-mode co-detection (Photonics Research 2025)](https://read.cnki.net/web/Journal/Article/GZXJ202502008.html) - 浙江大学/上海交大/密歇根大学联合提出芯片级集成光学陀螺仪多模协同探测技术，突破传统陀螺仪微型化瓶颈；代表量子传感与集成光子技术融合的工程化突破

- [中国空间站冷原子干涉陀螺仪实验 (2024)](https://www.sohu.com/a/996484779_122498878) - 2024年12月中国科学院精密测量院詹明生团队自主研制的空间冷原子干涉陀螺仪，在中国空间站舱内完成首次悬浮冷原子干涉实验，为空间量子惯性传感技术奠定基础

- [上海交大12.9纳弧度量子转动角度测量 (2025)](https://max.book118.com/html/2025/0306/8124011142007037.shtm) - 上海交通大学利用不定时间方向演化策略突破标准量子极限，在实验上实现12.9纳弧度精度轴向转动角度测量

- [法航/巴黎萨克雷大学量子陀螺仪700ppm长期稳定性 (2025)](https://max.book118.com/html/2025/0306/8124011142007037.shtm) - 基于冷原子干涉仪的量子陀螺仪系统实现长达一天的700ppm稳定性

- [基于频率纠缠双光子和级联HOM干涉的量子陀螺仪理论研究 (物理学报 2025)](https://wulixb.iphy.ac.cn/article/doi/10.7498/aps.74.20250077) - 利用频率纠缠双光子和级联Hong-Ou-Mandel干涉实现量子陀螺仪，三轴角速度测量量子Fisher信息分别达(2, 0.1, 0.006)，理论上可超越经典光学陀螺仪

### 原子钟 / Atomic Clocks

- [Muclock - 首款商用激光冷却原子钟 (Route des Lasers)](http://www.guangbozhilu.com/index.php?c=content&a=show&id=97&siteid=2) - 全球首款基于激光冷却原子的商用原子钟，兼具优异短期与长期稳定性，可溯源至SI秒定义，适用于时间分发与网络同步，为精密量子传感提供参考频率源

- [TimeCore-1 - 全球首款可量产集成化光子时钟芯片 (中科院半导体研究所×华为海思, 2025)](https://www.toutiao.com/article/7477118081123238426/) - 2025年3月中科院半导体研究所联合华为海思发布，铷原子光晶格与光子集成电路技术结合，10⁻¹⁸量级频率稳定度，指甲盖大小模块，成本降至传统设备1%，功耗仅0.3瓦；使厘米级北斗导航定位精度成为可能，为量子传感与时间同步应用开辟新路径

- [核时钟组装进入最后阶段 — 人类计时精度即将迎来量级跃升 (APS/Nature 2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_22569c511ff74452) - 2026年3月美国物理学会全球物理峰会发布核时钟最新进展；钍-229核跃迁能量已精确测定(2024年JILA叶军团队)；清华大学团队利用镉蒸汽四波混频实现148.4nm连续波VUV激光器，线宽<100Hz，功率>100nW，较之前改善五个数量级；叶军团队与IPG Photonics合作四硼酸锶晶体方案功率达40µW，具备商业化潜力；固体方案(氟化钙晶体嵌入)线宽约30kHz正优化中；核时钟预计比光学原子钟更紧凑、抗干扰，有望成为地球最精确计时仪器；是量子传感精密计时领域的下一代范式转移

- [清华大学丁世谦团队 — 148nm超窄线宽激光光源补齐核光钟最后拼图 (2026-05-08)](https://k.sina.com.cn/article_5953190046_162d6789e067033d8a.html) - 2025年5月清华大学物理系丁世谦团队成功研制148nm连续波超窄线宽激光光源，光谱纯度达国际领先水平，补齐核光钟研制的最后一块拼图；该成果为钍-229核时钟提供关键驱动光源，推动中国核时钟进入实用化阶段；标志着中国在量子精密测量最前沿领域取得重大原创性突破

- [碳-13光学检测核磁共振 — 大规模核自旋集成读出Diamond ODNMR (arXiv:2605.00152, Budker/Acosta团队, 2026)](https://arxiv.org/abs/2605.00152) - Budker/Acosta团队利用NV色心实现^13C核自旋光学极化与读出，~10¹⁶个相干核自旋，Landau-Zener微波扫频实现电子-核自旋双向极化转移；Ramsey光谱对比度>0.5%峰峰值，T₂*≈2ms；8-20mT磁场范围兼容；每个NV中心可读出约100个核自旋，为固态大规模量子传感网络提供新途径

---

### 量子磁传感 / Quantum Magnetometry*

- [Tracking time-varying signals with quantum-enhanced atomic magnetometers (arXiv:2503.14793, 2025)](https://arxiv.org/abs/2503.14793) - 量子纠缠（自旋压缩）增强原子磁力计对时变信号的追踪能力，利用估计控制技术实现快速变化磁场的实时跟踪，在心磁图信号演示中获得量子优势；单次相干时间内完成噪声背景下瞬态信号追踪，为量子磁力计在生物医学信号检测中的应用提供新范式
- [Chemically resolved NMR spectroscopy by longitudinal magnetization detection with diamond magnetometer (arXiv:2503.02140, 2025)](https://arxiv.org/abs/2503.02140) - 利用NV色心实现化学分辨核磁共振波谱，在0.32T磁场下达到~350 ppb分数光谱分辨率，可在~1nL检测体积内解析乙醇化学位移结构，为纳米级化学分析提供无感应磁力计新方案

### 低频里德堡原子电场传感 / Low-Frequency Rydberg E-Field Sensing

- [Low-frequency vector electrometry with Rydberg dipolar chain (Frontiers of Optoelectronics 2026)](https://www.sciencedaily.com/releases/2026/04/260416071956.htm) - 新加坡南洋理工大学利用里德堡原子链集体响应测量低频电场，提出三种互补测量技术获取电场强度与方向信息，突破传统蒸汽室EIT多原子Doppler展宽限制，实现微米级空间分辨率与可溯源校准，为紧凑型可编程量子电场传感器开辟新途径

- [腔增强里德堡原子微波接收器 (arXiv:2404.06915, 2024)](https://arxiv.org/abs/2404.06915) - 基于光学频率梳稳频连续波激光器实现原子毫米波外差接收机，W波段灵敏度达7.9 μV/m/√Hz，线性动态范围超过70 dB；为里德堡原子电场传感的实用化提供新途径

### 量子传感产业生态 / Quantum Sensing Ecosystem

- [KIST韩国量子创业公司代表团访问IBM - 加速全球量子技术商业化 (KIST/IBM, 2026-05-08)](https://en.prnasia.com/releases/global/kist-connects-korean-quantum-startups-with-ibm-to-accelerate-global-commercialization-532299.shtml) - 2026年5月8日韩国科学技术研究院(KIST)带领五家韩国量子创业公司代表团访问IBM Thomas J. Watson研究中心，探讨"IBM Quantum System Two"架构与运营框架，推动量子传感技术从研究到产业化的跨境合作；韩国政府中小企业和创业部(MSS)支持的"深层科技创业项目(DIPS)"推动；反映韩国作为全球量子技术新兴力量加速融入全球产业链的战略动向

### 新兴期刊与综述 / Emerging Journals & Reviews

- [Nature Sensors - 鲁棒光谱传感器用于远程生物特征检测 (2026)](https://www.nature.com/articles/s44460-025-00012-0) - 发表在Nature Portfolio 2026年创刊新刊(IF 5.000+)，提出抗环境光波动的光谱传感技术，可实现远程心电图波形准确检测；量子传感与生物医学检测融合的重要进展，为远程健康评估提供实用化路径

- [城际量子传感网络 - 国际首个核自旋城际网络Nature 2026合肥-杭州320公里 (Nature 2026)](https://www.nature.com/articles/s41586-025-10034-w) - 中国科学技术大学等团队构建国际首个基于核自旋的城际量子传感网络（合肥—杭州，跨度320公里，5台核自旋量子传感器），利用卫星同步实现分布式量子传感；结合核自旋量子放大技术将信号放大100倍，旋转灵敏度达约10⁻⁶ rad，首次实验突破轴子拓扑缺陷暗物质天体物理观测极限；误报率降低约三个数量级，能量分辨率较GNOME提升约4个数量级

### 开放量子系统与噪声 / Open Quantum Systems & Noise

- [Beating noise in frequency estimation with squeezing and memory in continuous-variable systems (arXiv:2605.06263, 2026)](https://arxiv.org/abs/2605.06263) - 研究开放量子系统中的频率估计问题，利用压缩哈密顿量工程与非马尔可夫动力学突破环境噪声限制；通过量子布朗运动模型证明有限记忆环境可诱导信息回流，暂时恢复并超越么正极限估计精度；为实用化量子磁力计在真实噪声环境下的性能优化提供理论框架
- [Multitime memory beyond the quantum regression theorem in sequential measurement statistics (arXiv:2605.06427, 2026)](https://arxiv.org/abs/2605.06427) - 揭示开放量子系统顺序测量统计中偏离量子回归定理的多时间记忆效应，提出基于协议相关的非马尔可性量化方法；spin-boson模型基准测试表明低环境温度与特定测量协议可增强多时间记忆特征；为量子传感系统环境耦合表征与噪声抑制提供新工具

---

*最后更新: 2026-05-12 (本次新增: 开放量子系统噪声理论与多时间记忆效应 arXiv:2605.06263/2605.06427)*
