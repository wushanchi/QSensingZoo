# 02-Application / 技术应用

本目录收录量子传感的工作原理、系统设计、工程实现方案等技术应用相关内容。

## 分类说明

- **工作原理** - 量子传感器的物理机制和传感原理
- **系统设计** - 传感器系统的架构设计、信号处理方案
- **工程实现** - 硬件实现、算法优化、实验方案

## 文件命名规范

```
[年份]-[作者/机构]-[标题].pdf
```

## 资料索引

- [Compact Cold Atom Interferometer Gyroscope (IEEE ICASSP 2025)](https://ieeexplore.ieee.org/document/11300795/) - 高精度旋转测量对惯性导航和地球物理至关重要；冷原子干涉仪陀螺仪(CAIG)无需机械旋转元件即可实现高灵敏度角速度检测；论文提出紧凑型设计方案，分析灵敏度与系统参数关系，为量子陀螺仪实用化提供工程参考

- [Performance Evaluation of a Compact Cold Atom Interferometer Gyroscope](https://ieeexplore.ieee.org/document/11300795/) - 冷原子干涉陀螺仪(CAIG)性能评估研究，分析系统噪声预算、 Allan方差、长期稳定性；是量子陀螺仪从实验室向实用惯性导航系统转化的重要技术基础
### 芯片化与微型化 / Chip-Scale & Miniaturization

- [QuantumVillage/UncutGem V2 - 全球首个全栈开源NV色心磁力计,DEF CON 33 2025发布 (2025)](https://github.com/QuantumVillage/UncutGem) - 全球首个全栈开源量子传感平台,V2版本于2025年 DEF CON 33发布;硬件(PCB/钻石支架)、固件(Arduino IDE)、science文档完整开源;采用COTS器件,微波源用ADF4350/1,ESP32主控,整机构建成本约£115;设计原则:平台化、COTS最大化、软件定义传感、简化装配;被称为量子技术的"Apple II时刻",让任何人能在家里安全操作量子传感设备

- [Laser-written micro-channel atomic magnetometer (arXiv:2404.14345, 2024)](https://arxiv.org/abs/2404.14345) - 利用飞秒激光刻蚀+化学蚀刻在熔融 silica 中制作亚毫米沟道,埋深<1mm,内含Rb蒸汽和0.75 amg N2缓冲气体,传感体积2.25 mm3,零场共振方案实现~1 pT/√Hz@10Hz灵敏度,可与光子结构和微流控通道3D集成;为芯片级碱金属原子磁力计的低成本微型化提供新路径

### 核心器件 / Core Devices

- [attocube attoNVM - 低温NV色心扫描成像磁强计，商业量产 (2026)](https://new.qq.com/rain/a/20260122A024JB00) - 德国attocube研发，2K至300K温度区间、纳米级分辨率杂散磁场成像；3 µT/√Hz灵敏度，无需微波传输线预处理；首台样机已在科研机构完成部署；商业化量产

- [Solid-State Microwave Magnetometer with Picotesla-Level Sensitivity (2023)](https://journals.aps.org/prapplied/abstract/10.1103/PhysRevApplied.19.054093) - 基于NV色心集合的微波磁力计实现3.4pT/√Hz灵敏度,为芯片级磁场检测提供新方案
- [macQsimal EU Project - Quantum Sensing & Metrology (2024)](https://www.macqsimal.eu/) - 欧盟FET Flagship项目,整合14家机构研发MEMS原子气室量子传感器,覆盖磁场、惯性、加速度等多维度传感;项目凝聚欧洲顶级量子研究机构,推动量子传感从实验室走向产业应用
- [All-Fiber Vector Magnetometer Based on Nitrogen-Vacancy Center (Nano 2023)](https://doi.org/10.3390/nano13050949) - 全光纤NV色心矢量磁力计,用光纤替代所有空间光学元件,实现0.73 nT/√Hz灵敏度,便携灵活可远距/内窥探测
- [Quantum Force Sensing by Digital Twinning of Atomic Bose-Einstein Condensates (Communications Physics 2024)](https://www.nature.com/articles/s42005-024-01662-1) - 原子Bose-Einstein凝聚体数字孪生量子力传感,机器学习信号处理,灵敏度达1.7×10-25 N/√Hz,较常规协议提升一个数量级
- [PROMISE - European Quantum Magnetic Imaging System Prototype (2025)](https://www.sohu.com/a/863260901_121798711) - 欧洲磁成像量子传感器预产业化项目,基于金刚石NV色心研发宽场动态高速量子磁力仪,无需真空/低温/磁屏蔽;参与机构包括Tecnalia、TNO、Fondazione Bruno Kessler、INRIM、SMEDiatope;目标应用:半导体高速高分辨测量、材料工程成像
- [Improved Inertial Navigation With Cold Atom Interferometry (Gyroscopy and Navigation, 2022)](https://link.springer.com/article/10.1134/S207510872104009X) - 冷原子干涉仪惯性导航系统误差特性分析,扩展卡尔曼滤波器框架在线估计误差源,校正传统IMU系统误差,显著提升 strapdown 计算精度;适用于地球轨道卫星等高端应用场景

### 系统设计与实现

- [Quantum Magnetometers for Infrastructure Inspection and Monitoring (arXiv:2605.04136, 2026)](https://arxiv.org/abs/2605.04136) - 利用NV色心磁力计/光泵磁力计进行基础设施检测与监测，可穿透涂层/绝缘层/混凝土无需耦合剂；系统分析提拉高度/低频漂移/背景噪声等现场性能限制因素，为钢梁疲劳/腐蚀/电池异常电流等提供非接触式磁诊断方案

- [Low-frequency vector electrometry with Rydberg dipolar chain (Frontiers of Optoelectronics 2026)](https://www.sciencedaily.com/releases/2026/04/260416071956.htm) - 新加坡南洋理工大学利用里德堡原子链集体响应测量低频电场，提出三种互补测量技术获取电场强度与方向信息，突破传统蒸汽室EIT多原子Doppler展宽限制，实现微米级空间分辨率与可溯源校准，为紧凑型可编程量子电场传感器开辟新途径
- [Microscale Fiber-Integrated Vector Magnetometer with On-Tip Field Biasing (arXiv:2404.14089, 2024)](https://arxiv.org/abs/2404.14089) - 微米级光纤集成矢量磁力计，尖端集成微型线圈产生局部偏置磁场，片上微型化方案显著减少传统笨重的3D Helmholtz线圈配置；便携灵活可远距/内窥探测
- [Pulsed vector atomic magnetometer using an alternating fast-rotating field (Nature Communications 2025)](https://www.nature.com/articles/s41467-025-56668-2) - 利用快速旋转磁场实现脉冲矢量原子磁力计,同时测量总磁场及其相对旋转平面的两个极角;梯度计模式下总场梯度灵敏度达35 fT/√Hz (十亿分之0.7),50μT地磁场中角分辨率达6 nrad/√Hz;提出峰值改变调制技术消除动态航向误差等系统效应;矢量灵敏度接近标量灵敏度,为高精度矢量磁场测量提供新方案

### 学术研究 / Research

- [Utilising NV based quantum sensing for velocimetry at the nanoscale (Scientific Reports 2020)](https://link.springer.com/article/10.1038/s41598-020-61095-y) - 利用NV色心量子传感实现纳米级流速测量,通过扩散噪声引起的磁场变化检测流体漂移速度
- [Entanglement-Assisted Multiparameter Estimation with Solid-State Quantum Sensor - MIT/东京大学/港中大 (PRX Quantum 2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_15469e0c1b599852) - 基于NV色心实现量子多参数同步估计,利用电子-核自旋纠缠在单次测量序列中同步估计微波驱动场幅值、失谐量与相位
- [High-resolution magnetic resonance spectroscopy using a solid-state spin sensor (Nature 2018)](https://www.nature.com/articles/nature25781) - 基于NV色心实现高分辨率磁共振波谱,检测单蛋白产生的磁场信号;最佳谱分辨率约100 Hz,可解析核自旋拉摩尔频率百万分之一的关键谱标识,为纳米级化学分析提供新工具

### NV色心灵敏度突破 / Sensitivity Records

- [Magnetic sensitivity enhancement via polarimetric excitation and detection of an ensemble of NV centers (Scientific Reports 2024)](https://www.nature.com/articles/s41598-024-60199-z) - 偏振激发与检测增强NV色心集合灵敏度,系统性研究偏振光学方案对磁灵敏度的提升机制
- [全光学核量子传感 - all-optical nuclear quantum sensing (npj Quantum Information 2023)](https://www.nature.com/articles/s41534-023-00724-6) - 纯光学方案实现NV色心核自旋量子传感,无需微波/射频驱动,突破量子传感器小型化、低功耗、非侵入性瓶颈

### 传感技术突破 / Sensing Breakthroughs

- [Bristol University - 量产光子芯片实现量子极限传感 (Nature Photonics 2025)](https://www.techbriefs.com/component/content/article/52474-quantum-sensing-to-engineer-photonic-sensors) - 英国布里斯托尔大学团队在商业代工厂量产光子芯片微环谐振器,首次在量子极限运行;可增强温室气体监测和癌症检测灵敏度;为量子传感产业化开辟光电子集成新路径
- [Quantum magnetometry of transient signals with 1.1 ns time resolution (arXiv:2411.05542)](https://arxiv.org/abs/2411.05542) - 基于单NV色心室温磁力计,实现1.1纳秒时间分辨率与450 MHz瞬时带宽,突破量子磁传感器的动态响应极限

### 量子多参数估计 / Multiparameter Estimation

- [Entanglement-Assisted Multiparameter Estimation with Solid-State Quantum Sensor - MIT/东京大学/港中大 (PRX Quantum 2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_15469e0c1b599852) - 基于NV色心实现量子多参数同步估计,利用电子-核自旋纠缠在单次测量序列中同步估计微波驱动场幅值、失谐量与相位
- [All-Fiber Vector Magnetometer Based on Nitrogen-Vacancy Center (Nano 2023)](https://doi.org/10.3390/nano13050949) - 全光纤NV色心矢量磁力计,用光纤替代所有空间光学元件,实现0.73 nT/√Hz灵敏度,便携灵活可远距/内窥探测
- [SBQuantum量子钻石磁力计CEO专访 (2026)](https://new.qq.com/rain/a/20260114A05PSZ00) - 加拿大SBQuantum CEO访谈:室温工作、矢量磁场测量、无漂移特性;公司成立于2017年,参与多伦多Creative Destruction Lab孵化;量子钻石磁力计可在公共安全/矿业/航天/国防领域提供准确及时的数据

### 生物医学传感 / Biomedical Sensing

- [Q-BIOMED - 英国量子生物医学传感研究Hub (2026)](https://www.qbiomed.org/) - 英国国家量子技术计划支持的量子生物医学传感研究中心,聚焦量子传感技术在早期疾病诊断与治疗中的应用,覆盖神经退行性疾病、心血管疾病、癌症早筛等方向;汇集帝国理工学院、伦敦大学学院等顶尖研究团队
- [QDTI - Quantum Powered Biomarker Detection (2026)](https://qdti.com/) - 利用量子传感技术实现超灵敏生物标志物检测的创新公司,样本量仅需≤5μL,检测限<1 pg/mL,分析灵敏度达亚皮克级,1小时内完成检测;量子传感技术为体外诊断与药物研发提供全新工具

---

### 量子传感与AI融合 / Quantum Sensing + AI

- [Q-CTRL量子计算材料发现速度提升3000倍 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_86369fc767b43452) - 2026年5月宣布利用IBM量子平台在材料科学问题上实现3000倍加速,首次展示实用量子优势;性能管理软件将仿真时间从100多小时缩短至仅两分钟;量子传感与量子计算底层技术融合的里程碑式应用
- [机器学习+量子钻石磁力计实时追踪磁性目标 (arXiv:2502.14683, 2025)](https://arxiv.org/abs/2502.14683) - 利用机器学习(无需物理模型)结合量子钻石磁力计实时追踪磁性目标位置,演示地下基础设施测绘、地面运输监测;为量子传感+AI融合应用提供新范式

- [Q-CTRL量子算法交通优化性能提升20倍 (2026)](https://www.163.com/dy/article/HAS3OU7L0538K1OZ.html) - Q-CTRL与澳大利亚CSIRO团队利用Fire Opal软件将交通优化量子算法性能提高20倍以上;展示量子传感/量子计算底层技术在交通物流优化领域的实用价值

- [SandboxAQ AQNav - 全球首款商用量子+AI导航系统 (2026)](https://www.sandboxaq.com/press/sandboxaq-announces-aqnav---worlds-first-commercial-real-time-navigation-system-powered-by-ai-and-quantum-to-address-gps-jamming) - 2026年5月2日发布,整合AI算法、量子传感与地球地壳磁场实现GPS拒止环境导航,覆盖空中/陆地/海上全场景;已在美国空军多型飞机上完成飞行测试;抗干扰、全天候、地形无关;估值超50亿美元;代表量子传感在导航领域首个大规模商用里程碑

- [量子传感国防应用路线图:NSA三大支柱,2029年25亿美元市场 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_89669beb1a1ac452) - 量子传感与量子计算、量子通信并列构成NSA量子技术三大支柱;量子惯性导航、量子磁力计、量子陀螺仪是国防应用三大方向;量子传感器市场预测2029年达25亿美元,2033年达32亿美元

### 分布式量子传感网络 / Distributed Quantum Sensor Networks

- [Distributed Network of Optically Pumped Magnetometers for Space Weather Monitoring (Scientific Reports 2024)](https://link.springer.com/10.1038/s41598-024-79841-x) - 分布式光泵磁力计(OPM)网络用于空间天气监测,太阳能供电、模块化设计,支持离网独立运行;量子磁传感器结合高灵敏度与固有校准特性,可弥补传统地基磁力计网络覆盖盲区;展示量子传感在地球物理与太空基础设施监测中的实用价值

- [城际分布式量子传感网络 - 轴子暗物质搜索新范式 (Nature 2026)](https://www.nature.com/articles/s41586-025-10034-w) - 全球城际分布式量子传感器网络,利用超极化惰性气体核自旋实现10-6 rad灵敏度,在轴子拓扑缺陷暗物质搜索领域取得里程碑式新约束;是量子传感网络在大物理搜索中的标志性应用

- [中科大城际量子传感网络 - 合肥-杭州320公里五城分布式测量Nature 2026 (Nature 2026)](https://www.nature.com/articles/s41586-025-10034-w) - 中科大等团队构建国际首个基于核自旋的城际量子传感网络,5台核自旋量子传感器跨320公里,利用卫星同步实现分布式量子传感;核自旋量子放大技术将信号放大100倍,旋转灵敏度约10⁻⁶ rad;首次实验突破轴子拓扑缺陷暗物质天体物理观测极限,误报率降低约三个数量级,能量分辨率较GNOME提升约4个数量级;是量子传感在大物理搜索领域的标志性应用

### 量子传感国防应用 / Defense Applications

- [量子传感在国防军事领域应用路线图 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_89669beb1a1ac452) - 量子传感与量子计算、量子通信并列构成美国国家安全局(NSA)量子技术三大支柱;量子传感器市场预测2029年达25亿美元,2033年达32亿美元;量子惯性导航、量子磁力计、量子陀螺仪是国防应用三大方向
- [IonQ入选MDA 1510亿美元SHIELD计划 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_690699ed88536652) - 2026年2月入围美国导弹防御局SHIELD合同,标志着量子传感正式进入美国核心武器系统长期采购目录
- [Q-CTRL获DARPA 2440万美元RoQS合同 (2025)](https://new.qq.com/rain/a/20250828A07QF600) - 美国DARPA"稳健量子传感器"计划合同,将量子传感应用于高性能军用车辆可靠导航

### 高时间分辨率传感 / High Time Resolution Sensing

- [Quantum magnetometry of transient signals with 1.1 ns time resolution (arXiv:2411.05542)](https://arxiv.org/abs/2411.05542) - 基于单NV色心室温磁力计,实现1.1纳秒时间分辨率与450 MHz瞬时带宽,突破量子磁传感器的动态响应极限
- [Wideband electric field quantum sensing via motional Raman transitions (Nature Physics, 2025)](https://www.nature.com/articles/s41567-024-02753-0) - 基于囚禁离子运动Raman跃迁实现宽带射频电场传感,频率范围扩大800倍,超越标准量子极限3.4(2.0)dB;可用于暗物质搜索与高频量子比特控制

### 机器学习与量子传感融合 / ML + Quantum Sensing

- [Machine Learning Assisted Tracking of Magnetic Objects using Quantum Diamond Magnetometry (arXiv:2502.14683, 2025)](https://arxiv.org/abs/2502.14683) - 利用机器学习(无需物理模型)结合量子钻石磁力计实时追踪磁性目标位置,演示地下基础设施测绘、地面运输监测;为量子传感+AI融合应用提供新范式

- [Q-CTRL量子算法交通优化性能提升20倍 (2026)](https://www.163.com/dy/article/HAS3OU7L0538K1OZ.html) - Q-CTRL与澳大利亚CSIRO团队引入评估框架判断哪些交通优化问题适合量子算法,利用Fire Opal软件将交通优化量子算法性能提高20倍以上;展示量子传感/量子计算底层技术在交通物流优化领域的实用价值

### 量子传感新兴应用 / Emerging Applications

- [QuiX Quantum突破光子误差阈值 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_67369cfa2c255852) - 2026年4月荷兰QuiX Quantum成功将光子量子计算机物理误差抑制到容错计算阈值以下,光子路径正式进入"阈值以下"新纪元;为量子传感与量子计算融合提供更可靠的光子学硬件基础,推动规模化容错量子系统走向实用

- [Monarch Quantum + Oratomic 战略合作:光子系统×中性原子架构 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_95769f1e58162352) - 2026年4月达成战略合作,整合光子系统与中性原子架构,目标本十年末交付数万个物理量子比特、编码数千个错误更正逻辑量子比特的容错量子计算机;代表量子传感底层硬件的原子系综技术与集成光子技术加速融合

### 量子传感新兴应用 / Emerging Applications

- [Monarch Quantum + Oratomic 战略合作:光子系统×中性原子架构 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_95769f1e58162352) - 2026年4月达成战略合作,整合光子系统与中性原子架构,目标本十年末交付数万个物理量子比特、编码数千个错误更正逻辑量子比特的容错量子计算机;代表量子传感底层硬件的原子系综技术与集成光子技术加速融合

- [Equal1与Q-CTRL战略合作 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_17269d78bd535352) - 全球硅基量子计算领导者Equal1与Q-CTRL合作,将Q-CTRL自主校准基础设施软件集成到Equal1硅量子计算机,推动机架式量子计算机在企业数据中心大规模部署

### 量子光学钟首次部署无人潜艇 / Quantum Optical Clock Underwater Deployment

- [全球首次!量子光学钟成功部署无人潜艇,导航不再依赖GPS (2025)](https://so.html5.qq.com/page/real/search_news?docid=70000021_527690345dc09652) - 2025年10月28日,英国皇家海军超大型无人水下航行器(XLUUV)"XV Excalibur"成功搭载Infleqtion公司研发的Tiqker量子光学原子钟并完成测试,标志着高精度量子传感器首次在水下作战平台上投入实战部署;将实验室级精确授时能力带入水下作战环境,对全球定位、导航和授时(PNT)技术体系产生深远影响;量子导航与授时技术从实验室走向深海实战应用的关键里程碑

### 量子导航与惯性传感 / Quantum Navigation & Inertial Sensing

- [SandboxAQ AQNav - 全球首款商用量子+AI导航系统,应对GPS干扰 (2026)](https://www.sandboxaq.com/press/sandboxaq-announces-aqnav---worlds-first-commercial-real-time-navigation-system-powered-by-ai-and-quantum-to-address-gps-jamming) - 2026年5月2日SandboxAQ发布AQNav,整合AI算法、量子传感与地球地壳磁场实现GPS拒止环境导航,覆盖空中/陆地/海上全场景;已在美国空军多型飞机上完成飞行测试,从单发动机到大型军用运输机均验证有效;抗干扰、全天候、地形无关;代表量子传感在导航领域首个大规模商用里程碑
- [Delft Vydar - GPS-free无人机导航获美国 funding (2026)](https://www.bits-chips.nl/) - 代尔夫特理工大学衍生公司Vydar于2026年5月获美国资金支持,开发无GPS无人机导航技术;结合量子传感与AI实现复杂电磁环境下的可靠自主导航;代表量子传感在无人系统定位领域加速商业化
- [量子导航技术在英国铁路取得重大突破 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_53669c4a73c75752) - 2026年3月量子惯性导航系统(RQINS)在全球范围内首次完成铁路实车测试,搭载于英国GTR运营列车在伦敦至韦林花园市线路运行;项目由MoniRail牵头,联合帝国理工学院/萨塞克斯大学/QinetiQ等战略联盟推进,获英国创新署与DSIT支持;量子传感为GPS拒止环境提供更低成本、更可靠、更抗干扰的定位方案
- [A Short Introduction to Basic Principles of Quantum Navigation Based-on Rb Cold Atom Interferometry (arXiv:2405.14910, 2024)](https://arxiv.org/abs/2405.14910) - 基于铷冷原子干涉仪的量子导航入门综述,阐述如何利用原子能级对外部变化的固有敏感性实现无卫星自校准导航系统;适用于惯性导航传感器与量子陀螺仪基础研究
- [Improved Inertial Navigation With Cold Atom Interferometry (Gyroscopy and Navigation, 2022)](https://link.springer.com/article/10.1134/S207510872104009X) - 冷原子干涉仪惯性导航系统误差特性分析,扩展卡尔曼滤波器框架在线估计误差源,校正传统IMU系统误差,显著提升 strapdown 计算精度;适用于地球轨道卫星等高端应用场景
- [Sandia Labs Atom Interferometry - GPS-free Navigation Sensor (2025)](https://www.sandia.gov/quantum/atom-interferometry/) - 美国桑迪亚国家实验室研发紧凑型原子干涉仪传感器头,采用光栅磁光阱(GMOT)技术实现冷原子囚禁,目标实现无卫星导航;量子惯性传感与重力辅助导航结合,减少GPS依赖

### 量子陀螺仪重大突破 / Quantum Gyroscope Breakthroughs

- [MIT/本田/陆军DEVCOM — 腔增强固态核自旋陀螺仪灵敏度提升3个数量级 (PRL 2026-05-09)](https://new.qq.com/rain/a/20250512A083QW00) - MIT、美国本田研究所、陆军DEVCOM陆军研究实验室、马萨诸塞大学波士顿分校联合发表，基于NV系综构建nNV-cQED系统，首次实现电磁感应透明、无反转激射、振荡行为；评估为惯性传感器时旋转灵敏度较此前固态自旋演示提升3个数量级；NV电子自旋可同时用作comagnetometer，四个结晶轴NV可实现矢量分辨率；是固态核自旋量子陀螺仪的重要里程碑

### 生物医学传感 / Biomedical Sensing

- [Biomagnetik Park - 量子心磁图(MCG)+AI心血管诊断 (Charité Berlin 2026)](https://www.biomagnetik.com/) - 德国初创公司基于最灵敏量子传感器(金刚石NV色心)开发无创心磁图,结合AI实现心血管疾病精准诊断;Charité Berlin 2021-2024临床研究证明,基于Park-Brachmann评分,Vector MCG排除心肌炎特异性达95.0%(传统方法难以企及);量子传感在心脏病早期诊断与无创筛查领域展现变革性潜力

### 量子传感新兴应用 / Emerging Applications

- [Nature Sensors 2026年正式创刊 - 全球传感共同体新平台 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_39069cca2fd62052) - Nature系列全新期刊将于2026年1月正式上线;2026年4月创刊论坛(延世大学/成均馆大学/汉阳大学),推动量子传感与全球传感研究网络深度融合

- [热光源聚束光子LIDAR - 远距离无探测激光隐蔽传感 (Nature Communications 2025)](https://www.nature.com/articles/s41467-025-67830-1) - 利用热光源光子聚束效应替代传统调制光源进行测距,通过二阶相干函数测量距离,实现完全无调制光源的隐蔽LIDAR;电信波段高亮光子源,探测距离超出散粒噪声极限;为量子传感在生物医学成像与空间探测中的隐蔽探测提供新范式

### 高时间分辨率传感 / High Time Resolution Sensing

- [Low-frequency vector electrometry with Rydberg dipolar chain (Frontiers of Optoelectronics 2026)](https://www.sciencedaily.com/releases/2026/04/260416071956.htm) - 新加坡南洋理工大学团队利用里德堡原子链集体响应测量低频电场,提出三种互补测量技术(传播动力学/Ramsey谱/频率域传输谱)获取电场强度与方向信息;突破传统蒸汽室EIT光谱术多原子Doppler展宽限制,实现微米级空间分辨率与可溯源校准,为紧凑型可编程量子电场传感器开辟新途径

- [宽带射频电场量子传感 - 频率范围扩大800倍 (Nature Physics 2025)](https://www.nature.com/articles/s41567-024-02753-0) - 基于囚禁离子运动Raman跃迁实现宽带射频电场传感,超越标准量子极限3.4(2.0)dB,可用于暗物质搜索与高频量子比特控制

### 新型原子矢量磁力计 / Novel Vector Atomic Magnetometry

- [Pulsed vector atomic magnetometer using an alternating fast-rotating field (Nature Communications 2025)](https://www.nature.com/articles/s41467-025-56668-2) - 利用快速旋转磁场实现脉冲矢量原子磁力计,同时测量总磁场及其相对旋转平面的两个极角;梯度计模式下总场梯度灵敏度达35 fT/√Hz (十亿分之0.7),50μT地磁场中角分辨率达6 nrad/√Hz;提出峰值改变调制技术消除动态航向误差等系统效应;矢量灵敏度接近标量灵敏度,为高精度矢量磁场测量提供新方案
- [低频里德堡原子链矢量电场计 - 微米级空间分辨率 (南洋理工大学, Frontiers in Optoelectronics 2026)](https://www.sciencedaily.com/releases/2026/04/260416071956.htm) - 利用里德堡原子链集体响应测量低频电场,提出三种互补测量技术(传播动力学/Ramsey谱/频率域传输谱)获取电场强度与方向信息,突破传统蒸汽室EIT多原子Doppler展宽限制,实现微米级空间分辨率与可溯源校准,为紧凑型可编程量子电场传感器开辟新途径

### 量子传感工程实现 / Engineering Implementation

- [Light-sheet confocal quantum diamond microscope (LC-QDM) - efficient scanning confocal readout (arXiv:2503.00252, 2025)](https://arxiv.org/abs/2503.00252) - 提出光片共聚焦量子钻石显微镜(LC-QDM)，结合光片照明与激光扫描共聚焦方法实现高效宽场3D量子传感；消除对薄NV层金刚石芯片的依赖，可在有限激光功率下实现高分辨率高速3D测量；为NV色心量子显微镜系统设计提供新架构


- [清华大学丁世谦团队148nm超窄线宽VUV激光光源 — 补齐核光钟最后拼图 (2026-05-08)](https://k.sina.com.cn/article_5953190046_162d6789e067033d8a.html) - 清华大学物理系团队利用镉蒸汽四波混频实现148nm连续波VUV激光器，线宽<100Hz、功率>100nW，光谱纯度达国际领先水平；补齐钍-229核光钟研制的最后关键环节，标志中国在量子精密测量最前沿领域取得重大原创性突破；该成果发表在《Optics Express》期刊

### 量子传感工程实现 / Engineering Implementation

- [硅基光电子原子干涉仪 - 量子指南针里程碑 (Science Advances, LatitudeDa 2026)](https://www.latitudeda.com/document/753) - 首次使用硅基光电子微芯片组件执行原子干涉仪量子传感技术,是开发"量子指南针"迈出的重要一步;传统原子干涉仪系统占据一个小房间的空间,硅基光电子集成使其微型化成为可能,为芯片级量子导航奠定基础

- [Bristol University - 量产光子芯片实现量子极限传感 (Nature Photonics 2025)](https://www.techbriefs.com/component/content/article/52474-quantum-sensing-to-engineer-photonic-sensors) - 英国布里斯托尔大学团队在商业代工厂量产光子芯片微环谐振器,首次在量子极限运行;可增强温室气体监测和癌症检测灵敏度;为量子传感产业化开辟光电子集成新路径

- [中国科大构建城际量子传感网络 - 核自旋量子精密测量突破 (Nature 2026)](https://www.nature.com/articles/s41586-025-10034-w) - 中科大等团队构建国际首个基于核自旋的城际量子传感网络,分布于合肥-杭州5台核自旋量子传感器,跨度320公里,利用卫星同步实现分布式量子传感;首次在实验上突破轴子暗物质天体物理观测极限;误报率降低约三个数量级,能量分辨率较基于碱金属传感器的GNOME提升约4个量级;团队结合核自旋量子放大技术,将信号放大至少100倍,旋转灵敏度约10-6 rad

- [NV色心ASIC芯片实现低功耗微型化 (2025)](https://www.sohu.com/a/864294113_121798711) - 德国斯图加特大学+NVision团队,采用ASIC芯片集成微波电子(QPLL芯片+四通道功率发射器),有源面积仅π×180×180μm2,直流/交流磁场检测限分别达32nT/√Hz和300pT/√Hz,频率调谐范围22%,实现NV磁力计的芯片级低功耗低成本方案
- [极端压力量子传感器 - Nature Communications 2025 (超过3万倍大气压稳定工作)](https://so.html5.qq.com/page/real/search_news?docid=70000021_34768cb600555252) - 华盛顿大学团队利用中子辐射氮化硼产生的带电空位对实现量子传感,首个在超过大气压3万倍极端高压环境中稳定运行的量子传感器,可用于探索物质在极端状态下的量子效应

- [全光纤NV色心矢量磁力计 (Nano 2023)](https://doi.org/10.3390/nano13050949) - 全光纤NV色心矢量磁力计,用光纤替代所有空间光学元件,实现0.73 nT/√Hz灵敏度,便携灵活可远距/内窥探测

### 量子传感产业分析 / Industry Analysis

- [量子传感:工业感知的下一次跨越 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_08569a8149706452) - 深度长文解析量子传感产业发展:全球市场规模2025年18.8亿美元、2035年将达50.7亿美元(年均复合增长率10.42%);阐述量子叠加态/纠缠态/相干性三大物理机制驱动的传感器家族;量子传感正在跨越实验室与工业应用的"死亡之谷",是量子技术商业化最快速的分支

### 其他量子传感公司 / Other Companies

- [QuantX Labs - 澳大利亚量子传感与精密计时 (2026)](https://quantxlabs.com/) - 澳大利亚阿德莱德大学衍生企业,专注量子传感与精密计时技术,量子传感方向涵盖地下资产追踪、空间威胁探测、水下威胁探测、重力与磁场地球物理勘探;量子计时产品用于GNSS降级/拒止环境下的弹性备选PNT sovereign太空计时网络;与澳大利亚国防与太空项目深度合作;代表大洋洲量子传感产业的战略布局

### 学术会议与产业峰会 / Conferences & Summits

- [Optica Quantum 2.0 Conference and Exhibition (2026-06-15~18, 格拉斯哥)](https://www.optica.org/events/topical_meetings/quantum) - Optica主办,量子2.0前沿会议,覆盖量子计算/通信/器件/传感与计量;会议主席包括Stony Brook/ICFO/IBM Research Zurich/FAU Erlangen-Nürnberg/University of Oregon等机构代表;量子传感与计量是核心议题之一;Quantum.Tech World 2026 (2026-06-25~26, 波士顿)同期召开
- [Quantum Singapore 2026论坛 - 量子汇聚:从硬件突破到工业应用 (2026)](https://new.qq.com/rain/a/20260207A067DT00) - 2026年2月4日新加坡滨海湾金沙会展中心开幕,ICV TA&K/FinQ Tech/Informa Markets联合主办,IEEE Photonics Society学术支持;主题聚焦量子传感从硬件突破到工业应用的产业化路径;反映东南亚在全球量子产业布局中的战略地位提升

### 分布式量子传感 / Distributed Quantum Sensing

- [Constraints on axion dark matter by distributed intercity quantum sensors (Nature 2026)](https://www.nature.com/articles/s41586-025-10034-w) - 利用五城分布式惰性气体核自旋实验室构成量子传感器网络,对轴子暗物质进行超灵敏探测,相关性分析放大信号并进行最优噪声滤波,旋转灵敏度约10-6 rad;超越天体物理观测限制,为超越标准模型物理搜索提供新路径

### 量子传感芯片化 / Chip-Scale Quantum Sensing

- [Sandia Labs - Guided Atom Interferometer专利获批 (US12392611B1, 2025)](https://www.sandia.gov/quantum/quantum-sensing/) - Sandia量子传感项目聚焦微型化量子传感器与原子钟,2025年8月获批"大动态范围高灵敏度渐逝场模式引导原子干涉仪测量协议"专利(US12392611B1);核心技术:悬空波导膜结构/针尖结构光原子陷阱集成平台(US11914188B1);关键能力覆盖:量子赋能电场传感/成像、超灵敏重力场及梯度测量、Sandia专利非侵入式功能脑成像系统、微型光原子钟(集成单光子探测器与波导光传输);代表美国国家实验室量子传感芯片化最新进展

### 生物医学传感 / Biomedical Sensing

- [量子传感microRNA检测 - NV色心早期癌症诊断 (Nature Communications Chemistry 2024)](https://www.nature.com/articles/s42004-024-01182-7) - 利用NV色心测量microRNA与钻石表面相互作用引起的Mn2+顺磁counter ion聚集,通过自旋弛豫对比度变化实现无标记microRNA检测;可克服溶液去屏蔽效应限制,为下一代量子传感癌症早筛提供新路径

- [Q-BIOMED - 英国量子生物医学传感研究Hub (2026)](https://www.qbiomed.org/) - 英国国家量子技术计划支持的量子生物医学传感研究中心,聚焦量子传感技术在早期疾病诊断与治疗中的应用,覆盖神经退行性疾病、心血管疾病、癌症早筛等方向;汇集帝国理工学院、伦敦大学学院等顶尖研究团队

- [QDTI - Quantum Powered Biomarker Detection (2026)](https://www.qdti.com/) - 利用量子传感技术实现超灵敏生物标志物检测的创新公司,样本量仅需≤5μL,检测限<1 pg/mL,分析灵敏度达亚皮克级,1小时内完成检测;量子传感技术为体外诊断与药物研发提供全新工具

- [Spin-enhanced nanodiamond biosensing for ultrasensitive diagnostics (Nature 2020)](https://link.springer.com/article/10.1038/s41586-020-2917-1) - 利用金刚石NV色心量子自旋特性实现超灵敏生物诊断,纳米金刚石生物传感可探测单个蛋白质分子,为早期疾病诊断提供全新工具

---

*最后更新: 2026-05-10 (本次新增: 中科院长春光机所量子陀螺专用VCSEL芯片国产化突破/清华大学148nm核光钟激光光源)*

### 学术研究 / Research

- [Chemically resolved NMR spectroscopy by longitudinal magnetization detection with diamond magnetometer (arXiv:2503.02140, 2025)](https://arxiv.org/abs/2503.02140) - 利用NV色心实现化学分辨核磁共振波谱,在0.32T磁场下达到~350 ppb分数光谱分辨率,可在~1nL检测体积内解析乙醇化学位移结构,为纳米级化学分析提供无感应磁力计新方案

### 量子传感与医疗健康 / Medical Health

- [Siemens Sensus Quantum - 量子传感器实现胎儿脑缺氧毫秒级预警 (2025)](https://www.toutiao.com/w/1827883145188356/) - 西门子Sensus Quantum系统捕捉脑血氧量子涨落,缺氧事件检测灵敏度99.3%,使紧急剖宫产决策时间缩短至3.2分钟;量子传感器在产科急危重症精准监测中的临床突破

- [心磁图检查提高冠心病诊断能力 (海淀医院, 2024)](https://k.sina.com.cn/article_1749990115_684ebae302001jck0.html?from=health) - 国内首款无液氦心磁图仪在海淀医院试点启用,创新应用量子精密磁场测量技术,适用于各年龄段冠心病无创诊断,可提早发现心肌缺血,降低急性心梗风险;患者提前预约即可免费检测

- [量子传感脑成像从实验室走向临床 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_08569a8149706452) - 基于量子磁力计的脑成像技术正在从实验室走向临床,无需传统SQUID所需的笨重液氦超导屏蔽设备即可在室温下探测神经元放电磁信号;量子传感正跨越临床应用"死亡之谷"

- [全球量子传感市场预测:2025年18.8亿美元/2035年50.7亿美元 (2026)](https://www.sohu.com/a/1001444609_122259177) - 量子传感产业分析:量子叠加态/纠缠态/相干性三大机制驱动;市场增长动能由早期少数领域向全物理量覆盖转变;心脑疾病诊断是量子传感商用最成熟方向之一

### 量子传感导航应用 / Navigation Applications

- [硅基光电子原子干涉仪 - 量子指南针里程碑 (Science Advances, 2026)](https://www.latitudeda.com/document/753) - 首次使用硅基光电子微芯片组件执行原子干涉仪量子传感技术,是开发"量子指南针"迈出的重要一步,目标实现无GPS精准导航;硅基光电子集成技术使传统占据一个房间的原子干涉仪系统实现芯片级微型化

- [量子导航技术在英国铁路取得重大突破 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_53669c4a73c75752) - 2026年3月量子导航系统搭载于英国GTR运营列车,在伦敦至韦林花园市线路进行实地测试,采集真实运营数据用于评估量子定位技术在铁路网实际环境中的表现;量子传感为GPS拒止环境提供高精度定位方案

- [Sandia Labs Atom Interferometry - GPS-free Navigation Sensor (2025)](https://www.sandia.gov/quantum/atom-interferometry/) - 美国桑迪亚国家实验室研发紧凑型原子干涉仪传感器头,采用光栅磁光阱(GMOT)技术实现冷原子囚禁,目标实现无卫星导航;量子惯性传感与重力辅助导航结合,减少GPS依赖

- [Chip-scale integrated optical gyroscope based on multi-mode co-detection (Photonics Research 2025)](https://read.cnki.net/web/Journal/Article/GZXJ202502008.html) - 浙江大学/上海交大/密歇根大学联合提出芯片级集成光学陀螺仪多模协同探测技术,突破传统陀螺仪微型化瓶颈;代表量子传感与集成光子技术融合的工程化突破

### 量子传感工程实现 / Engineering Implementation

- [硅基光电子原子干涉仪 - 量子指南针里程碑 (Science Advances, LatitudeDa 2026)](https://www.latitudeda.com/document/753) - 首次使用硅基光电子微芯片组件执行原子干涉仪量子传感技术,是开发"量子指南针"迈出的重要一步;传统原子干涉仪系统占据一个小房间的空间,硅基光电子集成使其微型化成为可能,为芯片级量子导航奠定基础

- [Bristol University - 量产光子芯片实现量子极限传感 (Nature Photonics 2025)](https://www.techbriefs.com/component/content/article/52474-quantum-sensing-to-engineer-photonic-sensors) - 英国布里斯托尔大学团队在商业代工厂量产光子芯片微环谐振器,首次在量子极限运行;可增强温室气体监测和癌症检测灵敏度;为量子传感产业化开辟光电子集成新路径

- [中国科大构建城际量子传感网络 - 核自旋量子精密测量突破 (Nature 2026)](https://www.nature.com/articles/s41586-025-10034-w) - 中科大等团队构建国际首个基于核自旋的城际量子传感网络,分布于合肥-杭州5台核自旋量子传感器,跨度320公里,利用卫星同步实现分布式量子传感;首次在实验上突破轴子暗物质天体物理观测极限;误报率降低约三个数量级,能量分辨率较基于碱金属传感器的GNOME提升约4个量级;团队结合核自旋量子放大技术,将信号放大至少100倍,旋转灵敏度约10-6 rad

- [NV色心ASIC芯片实现低功耗微型化 (2025)](https://www.sohu.com/a/864294113_121798711) - 德国斯图加特大学+NVision团队,采用ASIC芯片集成微波电子(QPLL芯片+四通道功率发射器),有源面积仅π×180×180μm2,直流/交流磁场检测限分别达32nT/√Hz和300pT/√Hz,频率调谐范围22%,实现NV磁力计的芯片级低功耗低成本方案
- [极端压力量子传感器 - Nature Communications 2025 (超过3万倍大气压稳定工作)](https://so.html5.qq.com/page/real/search_news?docid=70000021_34768cb600555252) - 华盛顿大学团队利用中子辐射氮化硼产生的带电空位对实现量子传感,首个在超过大气压3万倍极端高压环境中稳定运行的量子传感器,可用于探索物质在极端状态下的量子效应

- [全光纤NV色心矢量磁力计 (Nano 2023)](https://doi.org/10.3390/nano13050949) - 全光纤NV色心矢量磁力计,用光纤替代所有空间光学元件,实现0.73 nT/√Hz灵敏度,便携灵活可远距/内窥探测

### 量子传感产业分析 / Industry Analysis

- [量子传感:工业感知的下一次跨越 (2026)](https://so.html5.qq.com/page/real/search_news?docid=70000021_08569a8149706452) - 深度长文解析量子传感产业发展:全球市场规模2025年18.8亿美元、2035年将达50.7亿美元(年均复合增长率10.42%);阐述量子叠加态/纠缠态/相干性三大物理机制驱动的传感器家族;量子传感正在跨越实验室与工业应用的"死亡之谷",是量子技术商业化最快速的分支

### 其他量子传感公司 / Other Companies

- [QuantX Labs - 澳大利亚量子传感与精密计时 (2026)](https://quantxlabs.com/) - 澳大利亚阿德莱德大学衍生企业,专注量子传感与精密计时技术,量子传感方向涵盖地下资产追踪、空间威胁探测、水下威胁探测、重力与磁场地球物理勘探;量子计时产品用于GNSS降级/拒止环境下的弹性备选PNT sovereign太空计时网络;与澳大利亚国防与太空项目深度合作;代表大洋洲量子传感产业的战略布局

### 学术会议与产业峰会 / Conferences & Summits

- [Optica Quantum 2.0 Conference and Exhibition (2026-06-15~18, 格拉斯哥)](https://www.optica.org/events/topical_meetings/quantum) - Optica主办,量子2.0前沿会议,覆盖量子计算/通信/器件/传感与计量;会议主席包括Stony Brook/ICFO/IBM Research Zurich/FAU Erlangen-Nürnberg/University of Oregon等机构代表;量子传感与计量是核心议题之一;Quantum.Tech World 2026 (2026-06-25~26, 波士顿)同期召开
- [Quantum Singapore 2026论坛 - 量子汇聚:从硬件突破到工业应用 (2026)](https://new.qq.com/rain/a/20260207A067DT00) - 2026年2月4日新加坡滨海湾金沙会展中心开幕,ICV TA&K/FinQ Tech/Informa Markets联合主办,IEEE Photonics Society学术支持;主题聚焦量子传感从硬件突破到工业应用的产业化路径;反映东南亚在全球量子产业布局中的战略地位提升

### 分布式量子传感 / Distributed Quantum Sensing

- [Constraints on axion dark matter by distributed intercity quantum sensors (Nature 2026)](https://www.nature.com/articles/s41586-025-10034-w) - 利用五城分布式惰性气体核自旋实验室构成量子传感器网络,对轴子暗物质进行超灵敏探测,相关性分析放大信号并进行最优噪声滤波,旋转灵敏度约10-6 rad;超越天体物理观测限制,为超越标准模型物理搜索提供新路径

### 量子传感芯片化 / Chip-Scale Quantum Sensing

- [Sandia Labs - Guided Atom Interferometer专利获批 (US12392611B1, 2025)](https://www.sandia.gov/quantum/quantum-sensing/) - Sandia量子传感项目聚焦微型化量子传感器与原子钟,2025年8月获批"大动态范围高灵敏度渐逝场模式引导原子干涉仪测量协议"专利(US12392611B1);核心技术:悬空波导膜结构/针尖结构光原子陷阱集成平台(US11914188B1);关键能力覆盖:量子赋能电场传感/成像、超灵敏重力场及梯度测量、Sandia专利非侵入式功能脑成像系统、微型光原子钟(集成单光子探测器与波导光传输);代表美国国家实验室量子传感芯片化最新进展

### 生物医学传感 / Biomedical Sensing

- [量子传感microRNA检测 - NV色心早期癌症诊断 (Nature Communications Chemistry 2024)](https://www.nature.com/articles/s42004-024-01182-7) - 利用NV色心测量microRNA与钻石表面相互作用引起的Mn2+顺磁counter ion聚集,通过自旋弛豫对比度变化实现无标记microRNA检测;可克服溶液去屏蔽效应限制,为下一代量子传感癌症早筛提供新路径

- [Q-BIOMED - 英国量子生物医学传感研究Hub (2026)](https://www.qbiomed.org/) - 英国国家量子技术计划支持的量子生物医学传感研究中心,聚焦量子传感技术在早期疾病诊断与治疗中的应用,覆盖神经退行性疾病、心血管疾病、癌症早筛等方向;汇集帝国理工学院、伦敦大学学院等顶尖研究团队

- [QDTI - Quantum Powered Biomarker Detection (2026)](https://qdti.com/) - 利用量子传感技术实现超灵敏生物标志物检测的创新公司,样本量仅需≤5μL,检测限<1 pg/mL,分析灵敏度达亚皮克级,1小时内完成检测;量子传感技术为体外诊断与药物研发提供全新工具

- [Spin-enhanced nanodiamond biosensing for ultrasensitive diagnostics (Nature 2020)](https://link.springer.com/article/10.1038/s41586-020-2917-1) - 利用金刚石NV色心量子自旋特性实现超灵敏生物诊断,纳米金刚石生物传感可探测单个蛋白质分子,为早期疾病诊断提供全新工具

---

*最后更新: 2026-05-12 (本次新增: 腔增强固态核自旋陀螺仪灵敏度提升3个数量级PRL 2026-05-09/去重量子导航惯性传感冗余条目)*
