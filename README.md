# QSensingZoo 🧪
量子传感技术学习库 - 理论、应用与产业

> Tutorial of quantum sensing technology, including theory, application and production.

## 📁 目录结构

| 目录 | 内容 |
|------|------|
| [01-Theory](./01-Theory/) | 理论基础:经典论文、学术资料、基础科普 |
| [02-Application](./02-Application/) | 技术应用:工作原理、系统设计、工程实现 |
| [03-Products](./03-Products/) | 产业与产品:公司介绍、商用产品、核心技术参数 |

## 🔬 关于量子传感

量子传感是利用量子效应(如纠缠、叠加、相干)实现高灵敏度测量的技术。典型应用包括:
- NV色心磁力计
- 原子钟与惯性导航
- 量子陀螺仪
- 超导量子干涉仪(SQUID)

## 📚 学习资源

本仓库持续更新,欢迎 Star ⭐ 和 Fork！



### 🆕 新增条目(2026-05-30早-11:15 - 本次更新)

#### arXiv:2605.30301 - Lindbladian模拟样本复杂度改进:WML算法从O(d²)到O(d)维度依赖(Siheon Park等,2026-05-28)
- [arXiv:2605.30301](https://arxiv.org/abs/2605.30301) | 31页; 量子物理/量子信息
- **技术方案**:基于波矩阵Lindblad化(WML)算法建立样本复杂度界限;对维度d和维数d的跳跃算子L,推导显式非渐近样本复杂度:n_d^*(t,ε) ≤ ((2d+3)/8)‖L‖_∞² (t²/ε),优于此前最优O(d²t²/ε)
- **核心发现**:维度开销可完全避免当‖L‖_∞²=O(1/d);最坏情况下WML需要Ω(dt²/ε)样本;典型vs对抗样本复杂度存在尖锐二分
- **量子传感关联**:开放量子系统(open quantum system)是NV色心、金刚石传感器、电子自旋器件的核心;Lindbladian模拟的样本复杂度改进对量子传感系统的退相干建模与控制具有直接意义

#### arXiv:2605.30224 - Bright Squeezed Vacuum光实现宏观量子态超快生成:从Dicke态到猫态的相干操控(Imai等,2026-05-28)
- [arXiv:2605.30224](https://arxiv.org/abs/2605.30224) | 21页,5图; quant-ph/cond-mat.mes-hall/physics.optics
- **技术方案**:bright squeezed vacuum光结合单次正交测量,在弱耦合区即可实现宏观量子态的超快制备;通过高斯滤波作用选择性地将物质制备到零本征值Dicke态;counter-rotating terms驱动从Dicke态到猫态的量子态转换
- **核心发现**:光-物质纠缠原本使物质态保持经典混合;基于正交的预示(heralding)机制使物质态塌缩到量子叠加;更亮的squeezed vacuum光可加速Dicke态制备
- **量子传感关联**:量子传感中常用的多原子/多自旋集合(如原子蒸汽室、NV ensembles)若实现Dicke态或猫态将显著提升灵敏度;该工作为量子传感中的非经典态工程提供新路径

#### arXiv:2605.29883 - 非球形粒子旋转激发动力Casimir光子:单颗粒自由空间发射的严格上限(Impens等,2026-05-28)
- [arXiv:2605.29883](https://arxiv.org/abs/2605.29883) | 8页,3图; quant-ph
- **技术方案**:研究非球形中性粒子在自由空间自旋时与量子真空电磁场的相互作用;当旋转轴垂直于对称轴时,散射场产生频率边带,引发动力Casimir光子对发射
- **核心发现**:在最大尖端速度结构约束下,接近球形几何时发射率最大;靠近极化激元共振时进一步增强;即使是最优参数下单颗粒自由空间旋转Casimir发射仍极微弱
- **量子传感关联**:动力Casimir效应是量子真空涨落探测的一种方式;该研究确立了量子传感背景下Casimir效应可探测性的严格量化上限,对纳米机械传感、量子真空涨落计量的实际应用具有参考价值

#### Quantinuum - 拟IPO募资10.5亿美元、估值127亿美元:离子阱量子处理进入商用精度最高阶段(2026-05-26)
- 来源:so.html5.qq.com; Quantinuum为霍尼韦尔国际支持,2026-05-26向SEC提交IPO文件
- **技术指标**:最新离子阱量子处理器Helios基于QCCD架构,98个钡离子量子比特,单比特门保真度99.9975%,双比特门99.921%,量子态探测与制备保真度99.952%
- **量子传感关联**:Quantinuum离子阱平台高精度量子比特同时用于量子传感模拟(引力传感器、相干性检验);高保真离子阱系统是实现量子传感极端精度的重要硬件基础

#### Quantum Motion - 1.6亿美元C轮融资,硅基CMOS量子计算新里程碑(2026-05-13)
- 来源:so.html5.qq.com; 英国量子计算初创公司Quantum Motion,DCVC和Kembara领投
- **技术亮点**:硅基量子比特技术路线,利用标准CMOS工艺兼容平台;已为首个客户英国国家量子计算中心(NQCC)建造量子计算机,处理器仅数毫米,体积约三个服务器机架
- **量子传感关联**:硅自旋量子比特具有长相干时间优势,是未来集成化量子传感芯片的候选技术;标准CMOS兼容意味着可与经典硅基传感读出电路单片集成,是量子传感走向大规模商用的关键技术路线之一

---
*本次更新(追加): 量子传感最新论文 arXiv quant-ph 2026-05-28~29 / Quantinuum IPO / Quantum Motion融资(2026-05-30早-11:15)*


---

### 🆕 新增条目(2026-05-30午-11:44 - 本次更新)

#### 布里斯托尔大学 - 可大规模制造的 photonic chip 量子极限传感:温室气体检测/癌症早筛(2025-02)
- [Quantum sensing to engineer photonic sensors - Tech Briefs / University of Bristol](https://www.techbriefs.com/component/content/article/52474-quantum-sensing-to-engineer-photonic-sensors) | 研究团队:Joel Tasker等,QET Labs
- **技术突破**:在商业代工厂大规模制造的微环谐振器光子系统,在量子极限下运行;首次实现质量可量产的光子传感器达到量子噪声极限
- **应用场景**:温室气体监测、癌症早筛;为量子传感从实验室走向工业规模部署提供新路径
- **量子传感关联**:光子芯片传感器具有高灵敏度、低功耗、可片上集成优势;是量子光学传感走向消费电子和医疗设备的关键技术

#### Northwestern/Stanford - 全球首个商业 foundry 电子-光子混合量子芯片:量子通信/传感/处理一体化(2025-07)
- [First electronic-photonic quantum chip manufactured in commercial foundry - Northwestern Now](https://news.northwestern.edu/stories/2025/07/first-electronic-photonic-quantum-chip-manufactured-in-commercial-foundry/) | 首席研究员:Professor Ajay Nair Kumar团队
- **技术突破**:首次在商业半导体 foundry 将量子光源、控制电子单片集成于硅芯片;填补了"量子光学器件需要特种工艺、无法在标准商业 foundry 制造"的行业空白
- **量子光源+控制电子**:单片集成量子光源与经典控制电子,代表光量子通信、量子传感和量子处理硬件的重要突破
- **量子传感关联**:光子量子传感系统的片上集成是降低成本、提高稳定性的核心路径;该成果证明标准CMOS foundry可生产量子光子器件

#### 2026量子科技展/量子通信与量子信息技术博览会 - 西部(成都,7月15-17日) / 上海(11月5-7日)(2026-03)
- [2026量子科技展(腾讯, 2026-03-25)](https://so.html5.qq.com/page/real/search_news?docid=70000021_67869c34b5802652)
- **成都展会**:2026年7月15-17日,成都世纪城新国际会展中心
- **上海展会**:2026年11月5-7日



### 🆕 新增条目(2026-05-21下午-13:14 - 本次更新)

#### arXiv:2605.21457 - 相干量子推理的指数级样本复杂度优势:量子纯度放大(QPA)仅需O(1/ε)份拷贝(2026-05-20)
- [arXiv:2605.21457](https://arxiv.org/abs/2605.21457) | 作者:Zhaoyi Li等; 5+21页,3+0图
- **技术方案**:标准量子推理将量子数据转换为经典输出;本研究探索相干量子推理设置--输出保持量子态,保留相干性;涵盖量子纯度放大(QPA)、混合态近似纯化或克隆、密度矩阵指数化等任务
- **核心发现**:对于d维输入的主特征态目标,QPA相干处理仅需O(1/ε)份拷贝即达到误差ε,而任何非相干(测量中介)协议需要Ω(d/ε)份--指数级加速;该分离为"相干量子推理"理论奠定基础
- **量子传感关联**:量子传感系统采集的量子数据(如NV色心荧光、自旋态)直接进行相干量子处理可避免经典化的信息损失;相干量子推理的指数加速将直接赋能下一代量子传感器的数据处理架构设计

#### arXiv:2605.21346 - 量子机器学习在30-40个嘈杂量子比特规模下即展现明显优势:数据获取成为瓶颈而非经典计算(2026-05-19)
- [arXiv:2605.21346](https://arxiv.org/abs/2605.21346) | 作者:19页; 量子物理+机器学习
- **技术方案**:在具有量子数据的学习问题上,比较相干量子处理与固定测量方案后跟经典处理的性能;对已知具有渐近优势的特定任务,在存在噪声的量子数据下进行模拟和分析
- **核心发现**:在仅30-40个嘈杂量子比特规模下,相干量子数据处理即展现出明显量子优势;数据获取成为瓶颈而非经典计算;用测量优先策略匹配嘈杂相干协议仍需要数月甚至数年的测量时间
- **量子传感关联**:量子传感系统(如量子成像、量子磁场测量)产生的量子数据若直接进行相干量子处理而非经典化,可突破经典数据处理瓶颈;量子传感+量子机器学习融合是重要方向

---
*本次更新(追加): 量子传感最新论文 arXiv quant-ph 2026-05-21(2026-05-21下午-13:14)*



### 🆕 新增条目(2026-05-21中午-12:44 - 本次更新)

#### arXiv quant-ph 2026-05-21 最新论文:57篇量子物理新论文,量子传感相关工作摘要(2026-05-21)
- [arXiv quant-ph New Submissions (2026-05-21)](https://arxiv.org/list/quant-ph/recent) | 57篇新提交论文
- **量子传感相关论文重点关注**:
  - **arXiv:2605.21457** - An Exponential Sample-Complexity Advantage for Coherent Quantum Inference (Zhaoyi Li等, 2026-05-20);相干量子推理相较于非相干(测量中介)协议,在样本复杂度上实现指数级加速;量子纯度放大(QPA)仅需O(1/ε)份拷贝,而任何非相干协议需要Ω(d/ε)份;为量子传感数据处理中的相干保持提供理论依据
  - **arXiv:2605.21346** - Evidence of Quantum Machine Learning Advantage with Tens of Noisy Qubits (2026-05-19);在仅30-40个嘈杂量子比特规模下,相干量子数据处理即展现出明显量子优势;数据获取成为瓶颈而非经典计算;为量子传感+量子机器学习的实用化提供关键证据
  - **arXiv:2605.21380** - Modeling and Resource Optimization for Quantum Oracles (2026-05-19);量子oracle的分层递归综合评估(HRSE)模型,自适应时空权衡(ASDT)算法;与W-cycle方法相比平均电路深度降低53.99%;量子传感系统可建模为oracle进行资源优化
  - **arXiv:2605.21293** - Quantum Nonlocality and Device-Independent Randomness are Robust to Noisy Signaling Channels (Lewis Wooltorton等, 2026-05-20);量子非定域性在有噪信令通道下仍然鲁棒;即使发送近乎完美的输入副本时仍可认证设备无关随机性;为量子传感网络的信息安全提供新保障
  - **arXiv:2605.21140** - Optimization of Secret Key Rate for BB84 under Collective Rotation Noise (2026-05-19);BB84协议在集合旋转噪声下的安全密钥率优化;识别出Eve获取信息最小而SKR降解相对较小的非零噪声区间;为量子传感安全通信提供实用参考
  - **arXiv:2605.20930** - Symmetry-Protected Fast Relaxation and the Strong Quantum Mpemba Effect (2026-05-19);对称性保护的快弛豫机制与强量子Mpemba效应;SU(2)对称点附近高度对称初态展现出与系统尺寸无关的指数弛豫;为量子传感器退相干控制提供新思路
  - **arXiv:2605.21447** - Combining non-parametric quantum states and MERA tensor networks for ground-state optimization (2026-05-20);结合量子退火制备的非参数量子态与经典等距张量网络;改进基态近似精度而不增加量子电路深度;为量子传感器读出数据的变分优化提供新框架
  - **arXiv:2605.21274** - Semidefinite Programming for Optimal Quantum Cloning (2026-05-19);量子克隆优化的半定规划计算框架;为BB84协议在去极化噪声下的克隆攻击提供定量安全分析;量子克隆上限直接影响量子传感信息的泄露风险评估
- **量子传感关联**:今日57篇论文中量子传感相关工作集中在量子机器学习、量子oracle优化、量子安全通信三个方向;量子传感系统与量子计算共享量子数据处理框架,相干量子推理的指数加速将直接赋能下一代量子传感器设计

---
*本次更新(追加): 量子传感最新论文 arXiv quant-ph 2026-05-21(2026-05-21中午-12:44)*


### 🆕 新增条目(2026-05-21早-08:14 - 本次更新)

#### arXiv:2605.19125 - 超导陷阱中纳米磁体的旋转量子隧穿:rest-gas退相干保护+实验可行参数区(2026-05-18)
- [arXiv:2605.19125](https://arxiv.org/abs/2605.19125) | 作者:Francis Headley等; 26页,8图
- **技术方案**:研究纳米磁体在超导陷阱中的旋转自由度量子动力学;纳米磁体建模为磁化强度钉扎在易轴上的磁偶极子;超导磁陷阱产生阻碍自由旋转的势垒,但纳米磁体可通过隧穿穿越
- **核心发现**:rest-gas散射是低温下最重要的退相干机制;接近旋转轴完美旋转对称的粒子形状可保护旋转隧穿免受退相干影响;识别出旋转隧穿可观测的实验可行参数区域
- **量子传感关联**:旋转量子隧穿是新型量子传感机制;超导陷阱+纳米磁体的组合可用于高灵敏度磁场传感器;该工作为固态量子传感器的相干性控制提供重要指导

#### arXiv:2605.19117 - 量子魔态揭示CP相位:自旋0衰变中纠缠不可见的CP相位的量子魔法检测(2026-05-18)
- [arXiv:2605.19117](https://arxiv.org/abs/2605.19117) | 作者:Nicolas Viaux等; 物理+高能物理
- **技术方案**:标准量子信息度量(并发度、负性、纠缠熵、CHSH边界、量子Fisher信息)在自旋0→far{f}衰变中对所有CP角都是纠缠态;但固定在自旋分析物理Pauli框架中的稳定器量子魔法可以检测这些CP相位
- **核心突破**:稳定器Rényi熵在CP确定相和Clifford相消失,在最大非Clifford混合态达到峰值;线性振幅比四分量方案效率高14.3倍,在HL-LHC对H→τ⁺τ⁻达到发现级灵敏度
- **量子传感关联**:量子Fisher信息是量子传感参数估计的核心度量;该工作将量子魔法理论引入高能物理实验,为量子计量的新范式提供参考

#### arXiv:2605.19205 - 非Clifford双量子比特门量子认证协议:实用可扩展的误差边界+Pauli twirling扩展(2026-05-19)
- [arXiv:2605.19205](https://arxiv.org/abs/2605.19205) | 作者:Andrew Jackson等
- **技术方案**:为包含非Clifford双量子比特门(fSim、XY门族)的量子电路开发认证协议;提供实用可扩展的协议,上界无错误和有错误量子计算概率分布间的总变差距离
- **核心成果**:建立协议对小扰动的鲁棒性;将Pauli twirling扩展至非Pauli单量子比特基;为量子传感器的读出电路认证提供实用工具
- **量子传感关联**:双量子比特门保真度直接影响纠缠辅助量子传感器性能;量子认证是保证量子传感系统可靠性的关键技术

#### Princeton量子计划 - NV色心量子传感:二维材料磁学成像+量子系统实验,de Leon团队(2026-04)
- [Princeton Quantum Initiative](https://quantum.princeton.edu/research/quantum-systems-experiment/quantum-sensing-and-metrology) | Princeton大学
- **研究方向**:利用NV传感器探测钻石表面的二维自旋bath;研究量子材料中的磁性现象;开发新型量子传感协议
- **核心平台**:Princeton量子计划由de Leon团队主导,是NV色心量子传感的全球领先研究中心之一
- **量子传感关联**:Princeton在NV色心量子传感领域持续产出高质量成果;二维材料+NV色心的组合是当前最活跃的量子传感研究方向之一

#### SBQuantum量子钻石磁力计CEO专访:室温NV色心+无漂移读数+立方星搭载2026年3月发射(2026-01)
- [SBQuantum CEO专访(腾讯新闻)](https://so.html5.qq.com/page/real/search_news?docid=70000021_679696777d198552) | 量子传感初创公司
- **技术原理**:使用含数十亿氮-空位(NV)色心的人造钻石;NV色心产生具有量子自旋特性的自由电子,可精确测量磁场;室温下工作,提供磁场矢量信息,具备无漂移读数特性
- **商业化进展**:开发可直接插入立方体卫星的传感器,计划2026年3月发射升空;产品定位于GNSS拒止环境导航
- **量子传感关联**:SBQuantum代表量子传感创业公司的新兴力量;室温NV色心是量子磁力计商业化的重要方向

---
*本次更新(追加): 量子传感最新论文/技术应用/商用产品更新(2026-05-21早-08:14)*

### 🆕 新增条目(2026-05-21早-07:44 - 本次更新)

#### Q-BIOMED - 英国国家量子技术计划首个生物医学量子传感研究中心:16亿英镑网络,早期癌症/阿尔茨海默病诊断(2026)
- [Q-BIOMED官网](https://www.qbiomed.org/) | [UK Quantum Biomedical Sensing Research Hub](https://www.qbiomed.org/)
- **研究范围**:超灵敏血液检测(癌症早筛)、MRI扫描时间缩短、便携低成本仪器(基层医疗可及性)
- **技术平台**:量子磁力计(OPM/NV色心)、量子成像、量子生物传感混合系统
- **产业目标**:实现癌症早诊早治;减轻NHS等待压力;改善患者预后
- **量子传感关联**:Q-BIOMED是全球首个国家级量子生物医学传感研究中心;量子传感+医疗健康是最具商业化潜力的应用方向之一

#### SRI International - 超灵敏量子传感技术:原子量子态精密探测,医疗成像/国防安全/工业检测(2026持续)
- [SRI量子传感主页](https://www.sri.com/atsd/quantum/sri-is-developing-breakthrough-quantum-technologies-for-ultrasensitive-sensing/) | SRI International
- **技术方向**:利用原子与电场的量子态相互作用,开发测量任何引入原子系统行为变化的传感器;原子量子态对环境变化极度敏感,可探测极微弱信号
- **应用场景**:医疗成像(癫痫脑磁图MEG、肿瘤检测)、国防安全(地下目标探测)、工业检测(精密制造测量)
- **量子传感关联**:SRI是量子传感商业化的重要推手;其量子传感技术已进入产业化准备阶段

#### University of Bristol量子工程中心 - 光量子传感器:纠缠增强相位测量超越标准量子极限,量子工程博士培养(2026)
- [Bristol量子传感研究主页](https://www.bristol.ac.uk/quantum-engineering/research/sensing/) | Quantum Engineering Centre for Doctoral Training
- **核心技术**:利用量子纠缠实现光学相位测量,精度超越标准量子极限;已演示四光子纠缠干涉可见度超过阈值
- **应用方向**:距离测量、位置测量、位移测量、加速度测量、光程长度测量
- **量子传感关联**:Bristol是量子传感工程化的全球领先中心;量子纠缠增强光学相位测量是量子传感精度提升的重要方向

#### Quantum Coast Capital:专注量子传感早期投资,推动量子传感从实验室走向市场的产业化加速(2026-05)
- [Quantum Coast Capital](https://quantumcoastcapital.com/) | 专注于量子传感早期投资的风投机构
- **投资方向**:量子计算、量子传感、量子安全通信;量子传感是重点投资领域之一
- **团队背景**:科学顾问+资本市场+风投建设+企业运营的综合团队;执行内部科学尽职调查
- **战略定位**:不仅是投资者,更是战略合作伙伴;在量子传感商业化、监管和长期规模扩展方面积极支持创始团队
- **量子传感关联**:量子传感创业公司获资本市场持续支持;量子传感从实验室到市场的产业化加速

#### Nature Portfolio首个传感技术专业期刊Nature Sensors正式创刊:量子传感获得专业顶刊平台,2026年发行(2026)
- [Nature Sensors期刊主页](https://www.nature.com/natsensors/) | Nature Portfolio
- **创刊背景**:量子传感、机器学习传感、柔性传感等新型传感技术快速发展,需要一个专门的顶刊平台促进学术交流
- **收录范围**:量子传感、物理传感、化学传感、生物传感、柔性可穿戴传感等;涵盖传感原理、器件、系统与应用
- **量子传感关联**:Nature Sensors是量子传感领域首个专业顶刊,为量子传感研究提供高影响力发表平台,将加速量子传感从基础研究向技术应用转化

---
*本次更新(追加): 量子传感最新论文/技术应用/商用产品更新(2026-05-21早-07:44)*

### 🆕 新增条目(2026-05-21早-07:14 - 本次更新)

#### arXiv:2605.18876 - 统计量子相位估计(SQPE):扩展至负Pauli权重+变化点检测,适用于早期容错量子计算机(2026-05-15)
- [arXiv:2605.18876](https://arxiv.org/abs/2605.18876) | 作者:Brandon Allen等; 9页,4图
- **技术方案**:统计量子相位估计(SQPE)框架改进,适用于早期容错量子计算机;通过傅里叶近似估计哈密顿量谱密度累积分布函数(CDF),识别第一跳变点确定基态能量(GSE)
- **核心改进**:推广随机编译程序至负Pauli权重;采用变化点检测方法确定GSE,不依赖试凑态与真实基态重叠估计;利用傅里叶级数对称性减少2倍采样量
- **量子传感关联**:量子相位估计是量子传感参数估计的理论基础;该工作为早期容错量子传感器的电路设计提供实用指导

#### arXiv:2605.18912 - 量子Viterbi算法:隐藏量子马尔可夫模型(HQMM)的量子解码,连续流形优化超越经典对角策略(2026-05-17)
- [arXiv:2605.18912](https://arxiv.org/abs/2605.18912) | 作者:Abdessatar Souissi; 量子物理+数学物理+概率
- **技术方案**:量子Viterbi解码算法用于隐藏量子马尔可夫模型,在纯量子效应连续流形上进行优化,而非有限离散状态空间,利用相干叠加作为隐藏记忆
- **核心突破**:严格证明量子优势——相干隐藏轨迹可获得严格超过任何对角(对易)效应经典策略的解码分数,即使两者共享相同观测统计
- **量子传感关联**:量子Viterbi解码是量子传感序列决策的新算法原语;可直接应用于量子记忆、量子通信和NISQ设备上的量子机器学习

#### arXiv:2605.18914 - 超导量子比特非平稳退相干:记忆多分数布朗运动+时变量子布朗运动扩展,T1~5.00×10⁶ns(2026-05-18)
- [arXiv:2605.18914](https://arxiv.org/abs/2605.18914) | 作者:Mahboob Ul Haq; 21页,9图
- **技术方案**:基于记忆多分数布朗运动(mmFBM)的统一随机漂移模型(SdM),经典部分采用时变Hurst指数H(t)和自适应记忆核K(t,s);量子扩展采用时变Caldeira-Leggett环境
- **核心发现**:(1)弛豫和噪声振幅独立作用于能量衰减;(2)时变H(t)比任何固定指数更准确匹配实验1/f谱;(3)自适应核动力学保持相关性;(4)模拟预测与理论一致(T1~5.00×10⁶ns,T2~4.18×10⁵ns)
- **量子传感关联**:超导量子比特是量子传感器读出的核心平台;非平稳退相干模型对设计抗噪声量子传感架构有重要指导意义

#### arXiv:2605.19019 - 量子混沌半经典周期轨道理论:Gutzwiller迹公式从路径积分推导,连接量子能级与经典周期轨道(2026-05-18)
- [arXiv:2605.19019](https://arxiv.org/abs/2605.19019) | 作者:Sebastian Müller; 30页,11图; 量子混沌体积章节
- **技术方案**:从费曼路径积分推导Gutzwiller迹公式,建立经典周期轨道与量子能级间的半经典近似;解释随机矩阵理论描述的量子能级分布普适特征
- **量子传感关联**:量子混沌理论为高性能量子传感器的噪声特性分析提供理论基础;量子传感系统的能级统计与传感器性能直接相关

#### arXiv:2605.19114 - 动力学冻结诱导相互作用工程:驱动-only控制范式实现固定频率量子架构高速双量子比特门(2026-05-18)
- [arXiv:2605.19114](https://arxiv.org/abs/2605.19114) | 作者:Songbo Xie; 5页,4图
- **技术方案**:通过动态冻结辅助子系统重塑剩余自由度的有效哈密顿量;三量子比特架构中驱动调制器M被冻结于dressed本征态时,其投影重整化Q1的局部哈密顿量
- **核心成果**:实现iSWAP门,结合原生耦合门速与驱动only操作简单性;为固定频率量子架构提供快速、驱动控制的纠缠门途径
- **量子传感关联**:双量子比特门的高保真实现直接影响量子传感器纠缠辅助读出性能;量子控制技术是量子传感实用化的关键基础设施

#### Quantum.Tech World 2026会议启动:量子+AI+HPC融合,从突破到部署(2026-05)
- [Quantum.Tech World 2026](https://www.quantumtechcongress.com/) | 全球量子技术综合会议
- **主题**:`Quantum, AI & HPC: Redefining What's Possible`;突破已发生且正在被部署;从国家安全到医疗健康
- **核心议题**:量子传感与量子计算的工程化挑战;量子AI融合;量子技术商业化路径
- **量子传感关联**:量子传感是大会核心板块之一;跨学科融合推动量子传感从实验室向实际应用转化

---
*本次更新(追加): 量子传感最新论文/技术应用/商用产品更新(2026-05-21早-07:14)*

### 🆕 新增条目(2026-05-21凌晨-05:44 - 本次更新)

#### Qnami - 全球量子传感领先企业,NV色心扫描显微镜+ProteusQ双产品线商业化(2026-05)
- [Qnami官网](https://qnami.ch/) | [ProteusQ产品页](https://qnami.ch/proteusq/) | [ProteusQ-LT产品页](https://qnami.ch/proteusq/)
- **ProteusQ-LT**:低温扫描NV显微镜专用,原子尺度捕获表面磁场,用于量子材料表征;工作温度2K至300K;灵敏度3µT/√Hz(1.8K低温条件);空间分辨率亚纳米级
- **ProteusQ**:常温量子波技术平台,面向纳米技术、生命科学和地球科学应用
- **实测案例**:斯图加特大学Wrachtrup团队用attoNVM在1.8K低温下以<50nm分辨率清晰分辨NbSe₂单个磁通涡旋(PRL);波士顿学院Zhou团队对CrPS₄反铁磁畴实现原子级成像(Nature Materials)
- **市场扩张**:2026年5月宣布东亚市场扩张,Quantum Design Japan和Quantum Design Korea正式成为区域代理
- **量子传感关联**:Qnami是全球量子传感商业化最成功的企业之一;金刚石NV色心是当前最成熟的固态量子传感平台

#### Quantum Innovation Summit Dubai 2026:9月28-30日迪拜,量子传感从硬件突破到工业采纳(2026-09)
- [Quantum Innovation Summit Dubai 2026](https://quantuminnovationsummit.com/) | 主办方:Quantum for Good Curator,战略合作伙伴:阿联酋政府
- **主题**:"Quantum & Emerging Frontiers - Advancing Global Innovation & Technological Leadership"
- **核心议题**:量子传感商业化路径、量子AI融合、量子与先进计算协同、量子传感从实验室到工业采纳的转型
- **量子传感关联**:中东地区加大量子科技投资;迪拜量子峰会聚焦量子技术从展示向规模化交付的转型

#### IDTechEx量子传感市场报告2024-2044:17类技术覆盖,原子钟/量子磁力计/量子重力仪/量子陀螺仪/量子图像传感器(2024-07)
- [Quantum Sensors Market 2024-2044(IDTechEx)](https://www.idtechex.com/en/research-report/quantum-sensors-market-2024-2044/951) | 报告覆盖17类量子传感技术
- **技术覆盖**:原子钟、量子陀螺仪、量子磁场传感器( NV/OPM/SQUID)、量子重力仪、量子图像传感器
- **应用领域**:电动汽车(EV)、GPS拒止导航、工业检测、国防安全、脑成像等
- **核心技术路线**:NV色心磁力计、原子干涉重力仪、冷原子Rb/Rb蒸汽室、光泵磁力计、超导量子干涉仪(SQUID)
- **SWaP-C挑战**:尺寸、重量、功耗、成本是商业化最大瓶颈;晶圆级VCSEL、微纳加工蒸汽电池是破局关键
- **量子传感关联**:IDTechEx是量子传感市场最权威的分析机构之一;报告系统梳理全球量子传感技术格局与商业化路径

---
*本次更新(追加): 量子传感最新论文/技术应用/商用产品更新(2026-05-21早-06:14)*

---

### 🆕 新增条目(2026-05-21早-06:14 - 本次更新)

#### Nature Portfolio首个传感技术专业期刊Nature Sensors正式创刊:量子传感获得专业顶刊平台,2026年发行(2026)
- [Nature Sensors期刊主页](https://www.nature.com/natsensors/) | Nature Portfolio
- **创刊背景**:量子传感、机器学习传感、柔性传感等新型传感技术快速发展,需要一个专门的顶刊平台促进学术交流
- **收录范围**:量子传感、物理传感、化学传感、生物传感、柔性可穿戴传感等;涵盖传感原理、器件、系统与应用
- **量子传感关联**:Nature Sensors是量子传感领域首个专业顶刊,为量子传感研究提供高影响力发表平台,将加速量子传感从基础研究向技术应用转化

#### SRI International - 超灵敏量子传感技术:原子量子态精密探测,量子传感从实验室走向商业化(2026持续)
- [SRI量子传感研究主页](https://www.sri.com/atsd/quantum/sri-is-developing-breakthrough-quantum-technologies-for-ultrasensitive-sensing/) | SRI International
- **技术方向**:利用原子与电场的量子态相互作用,开发测量任何引入原子系统行为变化的传感器;原子量子态对环境变化极度敏感,可探测极微弱信号
- **应用场景**:医疗成像(癫痫脑磁图、肿瘤检测)、国防安全(地下目标探测)、工业检测(精密制造测量)
- **量子传感关联**:SRI是量子传感商业化的重要推手;其量子传感技术已进入产业化准备阶段

#### University of Bristol量子工程中心 - 光量子传感器:纠缠增强相位测量超越标准量子极限,量子工程博士培养(2026)
- [Bristol量子传感研究主页](https://www.bristol.ac.uk/quantum-engineering/research/sensing/) | Quantum Engineering Centre for Doctoral Training
- **核心技术**:利用量子纠缠实现光学相位测量,精度超越标准量子极限;已演示四光子纠缠干涉可见度超过阈值
- **应用方向**:距离测量、位置测量、位移测量、加速度测量、光程长度测量
- **量子传感关联**:Bristol是量子传感工程化的全球领先中心;量子纠缠增强光学相位测量是量子传感精度提升的重要方向

#### Quantum Innovation Summit Dubai 2026 - 2026年9月28-30日迪拜,主题"量子与新兴前沿,推进全球创新与技术领导力"(2026-05)
- [Quantum Innovation Summit Dubai 2026](https://quantuminnovationsummit.com/) | Quantum for Good Curator主办,阿联酋政府战略合作
- **核心议题**:量子传感商业化路径、量子AI融合、量子与先进计算协同、量子传感从实验室到工业采纳的转型
- **量子传感关联**:中东地区加大量子科技投资;迪拜量子峰会是2026年下半年最具影响力的量子传感活动之一

#### 量子传感市场预测:2025年18.8亿美元→2035年50.7亿美元(CAGR 10.42%),三大支柱磁场/重力/时频形成(2026)
- [ICV TA&K量子传感产业分析](https://so.html5.qq.com/page/real/search_news?docid=70000021_08569a8149706452) | 市场数据
- **三大支柱**:时频测量(13.3亿美元)、磁场测量(13.1亿美元)、重力测量(12.3亿美元);电场、惯性方向加速演进
- **驱动因素**:半导体工艺降低SWaP-C;国防和医疗领域早期落地;量子传感器从实验室走向嵌入式系统
- **量子传感关联**:量子传感从早期少数领域支撑向全物理量覆盖转变;商业化路径日益清晰

#### IQIS 2026 - 量子传感与量子信息国际会议,年度量子传感学术盛会(2026)
- [IQIS 2026](https://quantuminnovationsummit.com/) | 量子传感与量子信息国际会议
- **量子传感关联**:IQIS是量子传感领域最具影响力的国际学术会议之一;会议发布量子传感最新研究进展

---
*本次更新(追加): 量子传感最新论文/技术应用/商用产品更新(2026-05-21凌晨-02:44)*

---

### 🆕 新增条目(2026-05-21凌晨-05:44 - 本次更新)

#### MIT Technology Review 2025 - NIST×RTX Rydberg原子量子雷达:玻璃气室铯原子室温探测反射射频波,可成像地下隐蔽目标(2025-08)
- [MIT Technology Review (2025-08-11)](https://www.technologyreview.com/2025/08/11/1121314/this-quantum-radar-could-image-buried-objects/) | 研究团队:NIST + RTX(原Raytheon)防务承包商
- **技术原理**:使用玻璃气室中悬浮的铯(Caesium)原子云在室温下探测反射的射频波;激光将原子驱动到高度敏感的Rydberg状态(膨胀至细菌大小约10,000倍);当射频信号反弹回来时,原子云发射可检测的光信号,光颜色随射频相互作用而改变
- **创新点**:传统雷达需发射强射频信号才能探测回波,容易被探测和干扰;量子雷达利用原子量子态放大微弱返回信号,可探测隐蔽目标;单个紧凑玻璃气室(约1厘米)可覆盖多个频段,无需改变物理设置
- **测试结果**:在泡沫尖刺隔音室中成功定位铜板、管道、钢棒等目标,精度达4.7厘米(5米距离);arXiv论文(2506.20862)已发表
- **量子传感关联**:量子雷达本质是量子传感技术的军事延伸;Rydberg原子射频传感与NV色心磁力计共享量子相干增强原理;室温原子传感无需低温制冷,是商用量子雷达的重要方向

#### Cerca Magnetics完成380万英镑A轮融资:可穿戴量子脑成像扫描仪规模化,向临床医疗市场拓展(2026-04)
- [Cerca Magnetics官网](https://www.cercamagnetics.com/) | [Quantum Insider (2026-04-21)](https://thequantuminsider.com/2026/04/21/cerca-magnetics-secures-38m-series-a-funding-scale-quantum-brain-scanner/) | 领投:Guinness Ventures;投后估值3000万英镑
- **技术**:可穿戴式脑成像扫描仪,采用量子光泵磁力仪(OPM)替代传统固定式MEG设备;允许受试者自然活动,首次实现婴幼儿脑功能成像
- **市场进展**:已向12个国家神经科学研究机构交付19套系统;过去三年年销售额增长率持续保持100%以上;临床注册审批同步推进英国与美国
- **应用场景**:癫痫、多发性硬化、痴呆等神经系统疾病研究;英国国防部280万英镑项目(爆炸冲击对军人脑部影响评估)
- **量子传感关联**:OPM是量子磁力计商业化最活跃方向之一;常温运行+可穿戴是其相对于SQUID的核心竞争优势

#### MarketsandMarkets量子传感器市场:2034年前规模显著增长,原子钟/磁传感器/PAR量子传感器/重力仪(2024-12)
- [MarketsandMarkets Quantum Sensors Market](https://www.marketsandmarkets.com/Market-Reports/quantum-sensors-market-61825400.html) | 报告覆盖原子钟、量子磁传感器、PAR量子传感器、量子重力仪与加速度计
- **市场驱动**:量子传感器在精度上显著优于传统传感器;半导体工艺进步降低SWaP-C(尺寸/重量/功耗/成本)是商业化关键
- **应用领域**:国防安全(量子雷达/量子导航)、医疗健康(脑成像/癌症检测)、工业检测(精密制造/石油勘探)、汽车(EV电池检测/自动驾驶)
- **量子传感关联**:MarketsandMarkets是量子传感市场最权威的分析机构之一;报告系统梳理全球量子传感技术格局与商业化路径

#### Princeton Quantum Initiative - NV色心量子传感:二维材料磁学成像与量子系统实验(2026-04)
- [Princeton量子传感研究主页](https://quantum.princeton.edu/research/quantum-systems-experiment/quantum-sensing-and-metrology) | de Leon研究组
- **研究方向**:NV传感器探测金刚石表面二维自旋bath;探索量子传感在材料表征中的应用
- **技术平台**:NV色心扫描磁学显微镜;金刚石NV色心是当前最成熟的固态量子传感平台
- **量子传感关联**:Princeton在美国量子传感研究领域处于领先地位;该工作为量子传感在凝聚态物理和材料科学中的应用提供示范

#### Quantum Singapore 2026论坛:2026年2月4日新加坡滨海湾金沙会展中心开幕,聚焦量子从硬件突破到工业应用(2026-02)
- [Quantum Singapore 2026报道(腾讯, 2026-02-07)](https://new.qq.com/rain/a/20260207A067DT00) | 主办方:ICV TA&K、FinQ Tech Inc.、Informa Markets;学术支持:IEEE Photonics Society新加坡分会
- **论坛主题**:"Quantum Convergence: From Hardware Breakthrough to Industrial Applications"
- **核心议程**:量子计算在不同维度的前沿突破;量子传感商业化路径;量子通信与量子计算协同;量子技术从理论到产业化的工程挑战
- **量子传感关联**:东南亚是量子传感产业的新兴市场;Quantum Singapore是亚太地区最具影响力的量子技术论坛之一

---

---


### 🆕 新增条目(2026-05-21凌晨-02:44 - 本次更新)

#### Quantum Sensing Research Frontiers 2026 - 多维度最新研究进展汇总

**NV色心与金刚石量子传感**
- **SBQuantum(2026)**:基于氮空位(NV)色心的量子磁力计开发商,利用NV中心实现地下/水下/隐蔽环境磁场探测;通过精确测量地球磁场局部变化支持导航与资源勘探
- **arXiv(2024-08)**:Princeton大学实现大规模 multiplexed NV传感 - 使用低噪声相机同时读取多个NV中心,实现多节点协方差磁力计,显著提升 throughput
- **Nature Communications(2022)**:扫描梯度计实现单自旋量子磁力计,利用NV色心对纳米级磁结构进行量子成像,展示在二维磁系统和拓扑磁结构中的应用

**原子磁力计与光泵磁力计(OPM)**
- **Zurich Instruments**:光泵磁力仪(OPM/原子磁力计)是探测极弱磁场最灵敏的工具之一;Larmor磁力计可测量与地球磁场相当量级的磁场
- **Scientific Reports(2024)**:移动磁屏蔽条件下光泵磁力计心磁图的可行性研究;OPM替代SQUID实现室温可穿戴MEG
- **PKU Quantum Optical Magnetometry(2026-05)**:北京大学量子光学磁力仪研究组,量子精密测量的重要分支,在生物磁场检测等领域应用

**量子陀螺仪与惯性传感**
- **IDTechEx Quantum Sensors 2024-2044**:量子陀螺仪是量子传感市场重要细分领域;预计2044年量子传感器市场达71亿美元,量子陀螺仪贡献显著份额
- **Sandia National Labs**:美国国家实验室量子惯性传感研究,原子干涉仪技术处于领先地位

**量子重力仪与加速度计**
- **MarketsandMarkets**:量子重力仪与加速度计是量子传感器市场重要组成;地下资源勘探、惯性导航、国防安全为核心应用场景
- **Quantum Singapore 2026**:量子传感商业化论坛涉及量子重力仪在石油勘探和精密制造中的应用进展

**量子传感市场与产业**
- **IDTechEx报告(2023-07)**:量子传感器市场2024-2044年预测,覆盖17类量子传感技术,包括原子钟、量子陀螺仪、量子磁场传感器、量子重力仪等;市场将达71亿美元
- **App Developer Magazine(2025-04)**:量子传感器市场到2045年增长至20亿美元;半导体工艺降低SWaP-C(尺寸/重量/功率/成本)是商业化关键
- **ResearchAndMarkets(2025)**:量子技术市场报告2025-2035,量子传感是重要细分市场,整体量子市场将达994亿美元
- **Quantum Coast Capital**:专注量子传感早期投资的VC机构,推动量子传感从实验室走向市场

**商用产品与临床应用**
- **Cerca Magnetics**:量子OPM脑成像扫描仪,已完成380万英镑A轮融资,向12个国家神经科学研究机构交付19套系统,年销售增长100%+
- **Q-CTRL**:量子传感+量子计算基础设施软件公司,入选TIME 100;实现全球首个GPS-free导航量子优势;量子传感惯性导航是其核心产品之一
- **Bosch Quantum Sensing**:Bosch量子传感技术布局,量子磁力计产品开发
- **Sandia原子干涉仪**:美国国家实验室量子传感硬件平台,支持国防和商业应用

**量子传感学术与技术**
- **arXiv(2026-05)**:多参数函数估计与通用哈密顿量量子传感终极精度极限 - 量子传感理论前沿
- **Nature(2025-12)**:分布式城际量子传感器约束轴子暗物质 - 量子传感网络在基础物理探索中首次超越天文观测
- **Nature Sensors(2026)**:Nature Portfolio首个传感技术专业期刊创刊,量子传感获得专业顶刊平台
- **arXiv(2026-05)**:NV色心自旋-128mg悬浮谐振器耦合研究 - 纳米力学与量子传感融合

**2026年度量子传感会议与活动**
- **Quantum Innovation Summit Dubai 2026(2026-09)**:9月28-30日迪拜,聚焦量子传感从硬件突破到工业采纳
- **Quantum Singapore 2026(2026-02)**:新加坡滨海湾金沙会展中心,量子技术亚太论坛
- **IOPhys Quantum Science 2026**:量子传感科学大会
- **IQIS 2026**:量子传感与量子信息国际会议
- **AIRSA 2026(2026-04)**:AI与遥感传感应用国际会议,量子传感与AI融合

#### 量子传感技术路线图更新

| 技术方向 | 成熟度 | 核心突破 | 主要玩家 |
|---------|--------|---------|---------|
| NV色心磁力计 | 商业化早期 | 超高空间分辨率(~nm)、室温工作 | Princeton, SBQuantum, Qnami |
| OPM/原子磁力计 | 商业化中期 | 室温高灵敏度、可穿戴MEG | Cerca Magnetics,Fieldline, QuSpin |
| 量子陀螺仪 | 研发阶段 | 军事级精度、GPS拒止导航 | Honeywell,SAAB,Sandia |
| 量子重力仪 | 商业化早期 | 地下资源勘探、惯性导航 | Muquans,Atomionics |
| 量子原子钟 | 成熟商用 | 最高精度时间频率标准 | Microsemi,Symmetricom |
| SQIF太赫兹传感 | 研发阶段 | 高灵敏度太赫兹探测 | NIST,MIT |

---
*本次更新(追加): 量子传感最新论文/布里斯托量子光子芯片/Quantum Sensing Zoo资料搜集(2026-05-21凌晨-01:14)*

---

### 🆕 新增条目(2026-05-21凌晨-01:14 - 本次更新)

#### University of Bristol - 质子级光量子传感器:环谐振器实现量子极限探测,晶圆级量产(2025-02)
- [Quantum Sensing to Engineer Photonic Sensors(TechBriefs, 2025-02)](https://www.techbriefs.com/component/content/article/52474-quantum-sensing-to-engineer-photonic-sensors) | QET Labs, Bristol
- **技术**:利用微环谐振器(microring resonator)实现质量可manufacture的光子传感器在量子极限运行;微环谐振器形状像跑道,光在环中循环并与样品最大化相互作用
- **突破**:无需复杂的纠缠或压缩态即可实现量子极限精度测量;用与智能手机芯片相同工艺的晶圆级CMOS工艺制造
- **应用**:吸收率/折射率变化传感可识别温室气体、癌症检测;芯片级量子光子传感器是量子传感商业化的重要方向
- **量子传感关联**:光子芯片量子传感器是量子传感走向大规模商用的重要路径;量子工程与技术实验室(QET Labs)实现mass manufacturable的量子极限光子传感器

#### Quantum Innovation Summit Dubai 2026:9月28-30日迪拜,量子传感从硬件突破到工业采纳(2026-09)
- [Quantum Innovation Summit Dubai 2026](https://quantuminnovationsummit.com/) | 主办方:Quantum for Good Curator,战略合作伙伴:阿联酋政府
- **主题**:"Quantum & Emerging Frontiers - Advancing Global Innovation & Technological Leadership"
- **核心议题**:量子传感商业化路径、量子AI融合、量子与先进计算协同、量子传感从实验室到工业采纳的转型
- **量子传感关联**:中东地区加大量子科技投资;迪拜量子峰会聚焦量子技术从展示向规模化交付的转型

#### MarketsandMarkets量子传感器市场:2034年前规模显著增长,原子钟/磁传感器/PAR量子传感器/重力仪(2024-12)
- [MarketsandMarkets Quantum Sensors Market](https://www.marketsandmarkets.com/Market-Reports/quantum-sensors-market-61825400.html) | 报告覆盖原子钟、量子磁传感器、PAR量子传感器、量子重力仪与加速度计
- **市场驱动**:量子传感器在精度上显著优于传统传感器;半导体工艺进步降低SWaP-C(尺寸/重量/功耗/成本)是商业化关键
- **应用领域**:国防安全(量子雷达/量子导航)、医疗健康(脑成像/癌症检测)、工业检测(精密制造/石油勘探)、汽车(EV电池检测/自动驾驶)
- **量子传感关联**:MarketsandMarkets是量子传感市场最权威的分析机构之一;报告系统梳理全球量子传感技术格局与商业化路径

#### Quantum Coast Capital:投资量子传感早期创业公司,量子传感从实验室走向市场的产业化加速(2026-05)
- [Quantum Coast Capital](https://quantumcoastcapital.com/) | 专注于量子传感早期投资的风投机构
- **投资方向**:量子计算、量子传感、量子安全通信;量子传感是重点投资领域之一
- **团队背景**:科学顾问+资本市场+风投建设+企业运营的综合团队;执行内部科学尽职调查
- **战略定位**:不仅是投资者,更是战略合作伙伴;在量子传感商业化、监管和长期规模扩展方面积极支持创始团队
- **量子传感关联**:量子传感创业公司获资本市场持续支持;量子传感从实验室到市场的产业化加速

#### Quantum Singapore 2026论坛:2026年2月4日新加坡滨海湾金沙会展中心开幕,聚焦量子从硬件突破到工业应用(2026-02)
- [Quantum Singapore 2026报道(腾讯, 2026-02-07)](https://new.qq.com/rain/a/20260207A067DT00) | 主办方:ICV TA&K、FinQ Tech Inc.、Informa Markets;学术支持:IEEE Photonics Society新加坡分会
- **论坛主题**:"Quantum Convergence: From Hardware Breakthrough to Industrial Applications"
- **核心议程**:量子计算在不同维度的前沿突破;量子传感商业化路径;量子通信与量子计算协同;量子技术从理论到产业化的工程挑战
- **主持人**:FinQ Tech Inc.总裁、英国石油公司(BP)量子计算专家Shangjie Guo
- **量子传感关联**:东南亚是量子传感产业的新兴市场;Quantum Singapore是亚太地区最具影响力的量子技术论坛之一

#### Nature Communications Physics 2026 - NV色心量子传感Fe₃GeTe₂居里临界点热激活磁化翻转:室温近邻效应与量子磁学成像(2026-03)
- [Communications Physics (2026-03-02)](https://www.nature.com/articles/s42005-023-01472-x) | DOI: 10.1038/s42005-023-01472-x
- **技术方案**:将Fe₃GeTe₂多层薄膜转移至金刚石(100)表面并封装于两层hBN之间;532nm激光垂直激发,微波通过金线施加;利用NV色心扫描磁学显微镜对二维材料磁结构进行量子成像
- **核心发现**:揭示Fe₃GeTe₂中临近临界点的热激活逃离双稳态磁态行为;Fe₃GeTe₂是研究范德华磁性和拓扑磁结构的理想平台
- **量子传感关联**:NV色心是实现二维材料纳米尺度磁性表征的唯一无损、非接触式工具;量子成像可捕捉居里临界点附近磁化动力学细节

---
*本次更新(追加): Cerca Magnetics量子脑扫描仪380万英镑A轮/Q-CTRL TIME 100/Sandia原子干涉仪/Princeton NV传感/arXiv NV自旋-128mg悬浮谐振器/Equal1-Q-CTRL量子计算合作(2026-05-21凌晨-00:44)*

---

### 🆕 新增条目(2026-05-21凌晨-00:44 - 本次更新)

#### Cerca Magnetics完成380万英镑A轮融资:量子脑成像设备规模化,临床医疗市场拓展(2026-04)
- [Cerca Magnetics官网](https://www.cercamagnetics.com/) | [Quantum Insider (2026-04-21)](https://thequantuminsider.com/2026/04/21/cerca-magnetics-secures-38m-series-a-funding-scale-quantum-brain-scanner/) | 领投:Guinness Ventures
- **技术**:可穿戴式脑成像扫描仪,采用量子光泵磁力仪(OPM)替代传统固定式MEG设备;允许受试者自然活动,首次实现婴幼儿脑功能成像
- **应用**:癫痫、多发性硬化、痴呆等神经系统疾病研究;英国国防部280万英镑项目(爆炸冲击对军人脑部影响评估)
- **市场**:已向12个国家神经科学研究机构交付19套系统;过去三年年销售额增长率持续保持100%以上;临床注册审批同步推进英国与美国
- **量子传感关联**:OPM是量子磁力计商业化最活跃方向之一;常温运行+可穿戴是其相对于SQUID的核心竞争优势;儿童脑成像是差异化临床应用场景

#### Q-CTRL入选TIME 100行业领袖2026:全球唯一实现GPS-free导航真实量子优势的量子基础设施软件公司(2026-05)
- [Q-CTRL官网](https://q-ctrl.com/) | [TIME 100 List 2026](https://time.com/) | McKinsey量子市场估值2万亿美元
- **量子优势**:First and only in the world to deliver quantum advantage in GPS-free navigation;量子基础设施软件填补量子与经典世界之间的鸿沟
- **核心产品**:量子传感+量子计算双垂直领域;AI驱动的量子控制基础设施软件
- **市场定位**:量子传感和量子计算基础设施建设者;桥接量子硬件与实际应用需求
- **量子传感关联**:Q-CTRL是量子传感软件基础设施领域的全球领导者;GPS-free导航量子优势是其量子传感能力的直接验证

#### Equal1与Q-CTRL战略合作:自主校准技术集成至硅量子计算机,推动企业数据中心量子计算大规模部署(2026-04-08)
- [Equal1官网](https://equal1.com/) | [Q-CTRL官网](https://q-ctrl.com/) | 战略合作公告
- **技术方案**:Q-CTRL自主校准基础设施软件与Equal1硅量子计算机集成;使机架式量子系统能在无需专家干预情况下实现并保持峰值性能
- **目标**:推动机架式量子计算机在企业数据中心的规模化部署
- **量子传感关联**:量子计算与量子传感技术共享控制与校准基础设施;量子计算规模化经验可直接迁移至量子传感系统部署

#### Q-CTRL在IBM量子平台实现3000倍加速:材料科学领域首次展示实用量子优势(2026-05-06)
- [Q-CTRL公告(搜狐, 2026-05-07)](https://so.html5.qq.com/page/real/search_news?docid=70000021_86369fc767b43452) | 全球量子基础设施软件领导者
- **技术突破**:在具有商业相关性的材料科学问题上,实现相较于性能优化行业标准经典软件3000倍加速;在IBM量子平台上完成
- **里程碑**:首次实现实用量子优势;量子基础设施软件将量子计算实用化
- **量子传感关联**:量子传感与量子计算共享量子控制技术;Q-CTRL在量子计算领域的突破验证了其量子控制平台的技术领先性

#### Sandia国家实验室 - 原子干涉仪量子惯性传感器:无需GPS实现高精度导航,移动化是最大挑战(2025-10)
- [Sandia量子传感](https://www.sandia.gov/quantum/atom-interferometry/) | [Sandia量子传感主页](https://www.sandia.gov/quantum/quantum-sensing/)
- **技术方案**:原子干涉仪量子传感器用于惯性测量;结合重力辅助导航减少对GPS依赖;关键挑战是传感器的微型化与坚固化
- **核心能力**:紧凑坚固的原子干涉仪传感器头(grating magneto-optical trap, GMOT);极端微型化需要开发新型传感器子系统技术和架构
- **应用场景**:GPS拒止环境下的高性能量子惯性传感;恶劣条件下运行的传感器平台
- **量子传感关联**:原子干涉仪是量子传感精密测量的核心方向;Sandia代表美国国家实验室在量子传感领域的最高水平

#### Princeton量子 Initiative - NV色心量子传感:二维材料磁学成像与量子系统实验(2026-04)
- [Princeton量子传感研究主页](https://quantum.princeton.edu/research/quantum-systems-experiment/quantum-sensing-and-metrology)
- **研究方向**:NV传感器探测金刚石表面二维自旋系统bath;量子传感用于材料科学和基础物理研究
- **核心平台**:金刚石NV色心是实现纳米尺度磁性表征的核心工具;Princeton在NV量子传感实验平台处于全球领先地位
- **量子传感关联**:NV色心是当前最成熟的固态量子传感平台;Princeton的研究推动NV色心在量子材料表征中的应用边界

#### arXiv:2605.17750 - NV色心系综自旋力驱动128mg悬浮谐振器:量子-宏观力耦合里程碑,自旋-质量混合系统进入高质量regime(2026-05-19)
- [arXiv:2605.17750](https://arxiv.org/abs/2605.17750) | 22页,4图
- **技术**:在金刚石中利用NV缺陷系综的自旋力驱动128mg抗磁性悬浮振荡器的可控质心运动;通过周期性光初始化NV自旋态诱导振荡器相干运动,实现超过100nm的运动幅度
- **核心突破**:首次实验观测到原子尺度以上自旋力对宏观质量的作用;是实现自旋-质量混合系统量子工程的关键里程碑
- **量子传感关联**:NV色心自旋与机械振荡器的耦合为新型量子传感器(如量子加速度计、量子重力仪)提供混合系统路径;悬浮机械振子可用于探索量子与引力界面

---

#### Qnami - 全球量子传感领先企业,东亚市场扩张,NV色心扫描显微镜+ProteusQ双产品线商业化(2026-05)
- [Qnami官网](https://qnami.ch/) | [ProteusQ产品页](https://qnami.ch/proteusq/) | [ProteusQ-LT产品页](https://qnami.ch/proteusq/)
- **ProteusQ-LT**:低温扫描NV显微镜专用,原子尺度捕获表面磁场,用于量子材料表征;工作温度2K至300K;灵敏度3µT/√Hz(1.8K低温条件);空间分辨率亚纳米级
- **ProteusQ**:常温量子波技术平台,面向纳米技术、生命科学和地球科学应用
- **实测案例**:斯图加特大学Wrachtrup团队用attoNVM在1.8K低温下以<50nm分辨率清晰分辨NbSe₂单个磁通涡旋(PRL);波士顿学院Zhou团队对CrPS₄反铁磁畴实现原子级成像(Nature Materials)
- **市场扩张**:2026年5月宣布东亚市场扩张,Quantum Design Japan和Quantum Design Korea正式成为区域代理
- **量子传感关联**:Qnami是全球量子传感商业化最成功的企业之一;金刚石NV色心是当前最成熟的固态量子传感平台

#### Quantum Innovation Summit Dubai 2026:9月28-30日迪拜,量子传感从硬件突破到工业采纳(2026-09)
- [Quantum Innovation Summit Dubai 2026](https://quantuminnovationsummit.com/) | 主办方:Quantum for Good Curator,战略合作伙伴:阿联酋政府
- **主题**:"Quantum & Emerging Frontiers - Advancing Global Innovation & Technological Leadership"
- **核心议题**:量子传感商业化路径、量子AI融合、量子与先进计算协同、量子传感从实验室到工业采纳的转型
- **量子传感关联**:中东地区加大量子科技投资;迪拜量子峰会聚焦量子技术从展示向规模化交付的转型

#### IDTechEx量子传感市场报告2024-2044:17类技术覆盖,原子钟/量子磁力计/量子重力仪/量子陀螺仪/量子图像传感器(2024-07)
- [Quantum Sensors Market 2024-2044(IDTechEx)](https://www.idtechex.com/en/research-report/quantum-sensors-market-2024-2044/951) | 报告覆盖17类量子传感技术
- **技术覆盖**:原子钟、量子陀螺仪、量子磁场传感器( NV/OPM/SQUID)、量子重力仪、量子图像传感器
- **应用领域**:电动汽车(EV)、GPS拒止导航、工业检测、国防安全、脑成像等
- **核心技术路线**:NV色心磁力计、原子干涉重力仪、冷原子Rb/Rb蒸汽室、光泵磁力计、超导量子干涉仪(SQUID)
- **SWaP-C挑战**:尺寸、重量、功耗、成本是商业化最大瓶颈;晶圆级VCSEL、微纳加工蒸汽电池是破局关键
- **量子传感关联**:IDTechEx是量子传感市场最权威的分析机构之一;报告系统梳理全球量子传感技术格局与商业化路径

---
*本次更新(追加): Cisco量子传感研究/Quantum Singapore 2026/量子传感市场$2B-$99B/UN国际量子科技年/IOP Commercialising Quantum Global 2025(2026-05-21凌晨-00:14)*

---

### 🆕 新增条目(2026-05-21凌晨-00:14 - 本次更新)

#### Cisco Research - 量子传感最新研究论文:GKP态量子传感+量子安全研究(2025-12/2026-02)
- [Cisco Research Quantum Publications](https://research.cisco.com/) | 研究机构:Cisco Research
- **arXiv(2025-12)**: Optimized GKP State for Bosonic Channel Sensing - Thinh Le, Jianqing Liu, Jiapeng Zhao, Eneet Kaur;GKP(Gottesman-Kitaev-Preskill)压缩态优化用于量子传感,量子编码纠错与传感的融合
- **ACM(2026-02)**: Secure optical communication enabled by wavelength-division-multiplexed quantum alarm - Amir Minoofar, Jiapeng Zhao, Michael Kilzer, Eneet Kaur, Ramana Rao Kompella, Reza Nejabati;量子报警(quantum alarm)结合波分复用实现安全光通信
- **IEEE Quantum(2025-09)**: Quantum-Resistant Security: PQC Readiness and Research Challenges (Invited) - Ashish Kundu, Ramana Kompella;后量子密码(PQC)准备度与量子安全研究挑战
- **量子传感关联**:Cisco布局量子传感与量子安全的融合;量子传感技术可支撑量子通信安全;GKP态结合量子纠错是量子传感实用化的重要方向

#### Quantum Singapore 2026论坛:2026年2月4日新加坡滨海湾金沙会展中心开幕,聚焦量子从硬件突破到工业应用(2026-02)
- [Quantum Singapore 2026报道(腾讯, 2026-02-07)](https://new.qq.com/rain/a/20260207A067DT00) | 主办方:ICV TA&K、FinQ Tech Inc.、Informa Markets;学术支持:IEEE Photonics Society新加坡分会
- **论坛主题**:"Quantum Convergence: From Hardware Breakthrough to Industrial Applications"
- **核心议程**:量子计算在不同维度的前沿突破;量子传感商业化路径;量子通信与量子计算协同;量子技术从理论到产业化的工程挑战
- **主持人**:FinQ Tech Inc.总裁、英国石油公司(BP)量子计算专家Shangjie Guo
- **量子传感关联**:东南亚是量子传感产业的新兴市场;Quantum Singapore是亚太地区最具影响力的量子技术论坛之一

#### 量子传感市场规模:2025年约18.8亿美元→2045年增至20亿美元以上,复合增长率约12-15%(2025-04)
- [Quantum sensor market to grow to 2B by 2045(App Developer Magazine, 2025-04-02)](https://appdevelopermagazine.com/quantum-sensor-market-to-grow-to-2b-by-2045/) | 引用数据
- **市场驱动**:量子传感器在精度上显著优于传统传感器;半导体工艺进步降低SWaP-C(尺寸/重量/功耗/成本)是商业化关键
- **应用领域**:国防安全(量子雷达/量子导航)、医疗健康(脑成像/癌症检测)、工业检测(精密制造/石油勘探)、汽车(EV电池检测/自动驾驶)
- **量子传感关联**:量子传感市场规模相对量子计算更小但增长稳定;2025年是联合国"国际量子科学与技术年",量子传感从展示进入规模化交付阶段

#### 量子技术市场2025-2035:339亿美元→993亿美元(CAGR 11.3%),量子传感与成像是四大板块之一(2025-08)
- [ResearchAndMarkets:Quantum Technology Market 2025-2035](https://www.researchandmarkets.com/reports/5317365/quantum-technology-market-by-computing) | 416页,2025年8月发布
- **市场预测**:2025年339亿美元→2035年993亿美元(CAGR 11.3%);量子传感与成像是四大板块之一(另三:量子计算、量子通信、量子建模与仿真)
- **驱动因素**:半导体工艺进步降低SWaP-C;国防和医疗领域早期落地;量子传感器从实验室走向嵌入式系统
- **区域格局**:北美主导,亚太快速增长;亚太地区制造业升级推动量子传感工业应用
- **量子传感关联**:ResearchAndMarkets报告验证量子传感市场高速增长;国防和医疗是量子传感率先落地场景

#### IOP Physics - Commercialising Quantum Global 2025:4th Annual Conference,庆祝联合国"国际量子科学与技术年",量子传感商用化从承诺到落地(2025-05)
- [IOP Commercialising Quantum Global 2025](https://www.iop.org/events/4th-annual-commercialising-quantum-global-2025) | Institute of Physics主办
- **会议主题**:量子技术从展示向实用转型的真实案例;量子传感、量子计算、量子通信的商用化路径
- **核心议题**:量子传感商业应用与投资回报;量子技术落地准备度评估;量子传感在国防和工业检测中的应用
- **亮点**:UN宣布2025年为"国际量子科学与技术年",量子传感获全球政策支持;论坛强调量子传感已从"承诺"进入"交付"阶段
- **量子传感关联**:IOP是英国物理学会,量子传感商用化会议代表欧洲最高规格;量子传感投资从早期探索进入理性布局阶段

#### 联合国宣布2025年为"国际量子科学与技术年":全球量子科技从理论走向产业化(2024-06)
- [联合国量子科学与技术年(quantumcomputer.ac.cn, 2024-06-17)](https://quantumcomputer.ac.cn/Knowledge/detail/70a8dd38f650480facb909c705f60ea1/586594a45b4a4c4aad86dc6c1def947a.html)
- **国际背景**:联合国大会宣布2025年为国际量子科学与技术年(IYQ-2025);全球量子科技从理论探索迈向产业化落地
- **中国响应**:量子科技被列为未来产业首位;量子传感在磁传感、重力领域形成集群优势;中国量子传感市场规模快速增长
- **量子传感关联**:国际量子年的宣布标志着量子传感从学术研究进入国家战略层面;全球协调加速量子传感标准化和产业化

---
*本次更新(追加): Nature子刊量子传感论文/Imperial量子导航/Princeton NV量子成像/MIT量子雷达/量子传感产业最新arXiv(2026-05-20晚-22:45)*

---

### 🆕 新增条目(2026-05-20晚-22:45 - 本次更新)

#### Nature Communications Physics 2026 - NV色心量子传感Fe₃GeTe₂居里临界点热激活磁化翻转:室温近邻效应与量子磁学成像(2026-03)
- [Communications Physics (2026-03-02)](https://www.nature.com/articles/s42005-023-01472-x) | DOI: 10.1038/s42005-023-01472-x
- **技术方案**:将Fe₃GeTe₂多层薄膜转移至金刚石(100)表面并封装于两层hBN之间;532nm激光垂直激发,微波通过金线施加;利用NV色心扫描磁学显微镜对二维材料磁结构进行量子成像
- **核心发现**:揭示Fe₃GeTe₂中临近临界点的热激活逃离双稳态磁态行为;Fe₃GeTe₂是研究范德华磁性和拓扑磁结构的理想平台
- **量子传感关联**:NV色心是实现二维材料纳米尺度磁性表征的唯一无损、非接触式工具;量子成像可捕捉居里临界点附近磁化动力学细节

#### Nature 2025 - 分布式城际量子传感器约束轴子暗物质:全球光学磁力计网络探测拓扑缺陷暗物质(2025)
- [Nature论文:s41586-025-10034-w](https://www.nature.com/articles/s41586-025-10034-w) | DOI: 10.1038/s41586-025-10034-w
- **技术方案**:利用分布式光学磁力计(OPM)城际网络探测轴子类暗物质拓扑缺陷(Topological Defect Dark Matter, TDM);当地球穿越暗物质墙时,轴子与核自旋传感器发生极微弱相互作用产生瞬时信号
- **研究意义**:探索占比宇宙26.8%的暗物质;轴子是暗物质热门候选者之一;拓扑缺陷暗物质是轴子场的重要表现形式
- **量子传感关联**:分布式量子传感网络是量子传感技术的重要发展方向;光学磁力计(OPM)无需低温即可工作,是构建城际量子传感网络的理想平台

#### Imperial College London × 皇家海军 - 量子导航系统海试成功:量子惯性传感器可在GPS拒止环境下提供高精度定位(2026-05)
- [Imperial量子导航海试(2026)](https://www.imperial.ac.uk/news/245114/quantum-sensor-future-navigation-system-tested/) | [Imperial量子传感Q&A(2026-05-08)](https://www.imperial.ac.uk/news/246634/qa-how-will-quantum-science-transform)
- **技术突破**:英国皇家空军飞机量子导航测试成功后,延伸至皇家海军舰船;量子惯性传感器可在GPS拒止环境下提供高精度定位
- **已实用化三大领域**:1超精密时钟(原子钟);2超灵敏重力仪(地下勘探);3超灵敏磁力计(脑成像+自主导航)
- **QuEST中心**:量子工程、科学与技术中心正式启动,三大主题:量子材料、量子互联网、量子计算应用
- **量子传感关联**:量子惯性导航是量子传感最明确的军用需求之一;英国在量子导航领域处于全球领先地位

#### MIT Technology Review 2025 - NIST×RTX量子雷达:原子云室温探测反射射频波,可成像隐蔽目标(2025-08)
- [MIT Technology Review (2025-08-11)](https://www.technologyreview.com/2025/08/11/1121314/this-quantum-radar-could-image-buried-objects/) | 研究团队:NIST + RTX(原Raytheon)
- **技术原理**:使用玻璃气室中悬浮的铯(Caesium)原子云在室温下探测反射的射频波;激光将原子驱动到高度敏感的量子态,当射频信号反弹回来时,原子云发射可检测的光信号
- **创新点**:传统雷达需发射强射频信号才能探测回波,容易被探测和干扰;量子雷达利用原子量子态放大微弱返回信号,可探测隐蔽目标
- **当前状态**:仍为原型阶段,体积较大(光学表+组件);展示了量子传感在国防安全领域的巨大潜力
- **量子传感关联**:量子雷达是量子传感在国防领域的前沿应用;室温原子传感无需低温制冷,是商用量子雷达的重要方向

#### arXiv:2605.17750 - NV色心系综自旋力驱动128mg悬浮谐振器:量子-宏观力耦合里程碑,自旋-质量混合系统进入高质量regime(2026-05-19)
- [arXiv:2605.17750](https://arxiv.org/abs/2605.17750) | 作者:22页,4图
- **技术**:在金刚石中利用NV缺陷系综的自旋力驱动128mg抗磁性悬浮振荡器的可控质心运动;通过周期性光初始化NV自旋态诱导振荡器相干运动,实现超过100nm的运动幅度
- **核心突破**:首次实验观测到原子尺度以上自旋力对宏观质量的作用;是实现自旋-质量混合系统量子工程的关键里程碑
- **量子传感关联**:NV色心自旋与机械振荡器的耦合为新型量子传感器(如量子加速度计、量子重力仪)提供了混合系统路径;悬浮机械振子可用于探索量子与引力界面

#### arXiv:2605.16559 - 非厄米超导量子系统中复Berry相位的测量与控制:实部+虚部同时测量,非厄米量子控制的几何方法(2026-05-19)
- [arXiv:2605.16559](https://arxiv.org/abs/2605.16559) | 作者:10页,8图
- **技术**:利用具有工程耗散的超导transmon电路实验测量复Berry相位的实部和虚部;展示虚部对耗散的路径依赖效应及其在非厄米量子控制中的应用
- **核心突破**:首次在完全量子系统中同时测量复Berry相位的实部和虚部;建立复Berry相位的实部与虚部之间的明确几何区分
- **量子传感关联**:Berry相位在几何量子计算和量子传感中具有重要作用;非厄米量子系统为鲁棒量子传感和量子计量提供新途径

#### Physical Review Letters 2025 - 量子纠缠增强原子钟:计时稳定性突破标准量子极限,精度提升至全新水平(2025-12)
- [量子纠缠让原子钟更精确(搜狐, 2026-03-10)](https://so.html5.qq.com/page/real/search_news?docid=70000021_62569afdfb189352) | 发表于Physical Review Letters
- **技术原理**:利用量子纠缠态使原子钟的计时稳定性超越标准量子极限;量子纠缠提供比独立原子更高的测量精度
- **核心突破**:原子钟是量子传感最成熟的应用;量子纠缠增强进一步提升时间测量的精度上限
- **量子传感关联**:量子纠缠是量子传感中提升信噪比的核心资源;该工作将量子纠缠直接应用于时频测量这一最成熟的量子传感方向

#### arXiv:2605.04136 - 多参数量子传感终极极限:通用哈密顿量参数函数估计,commuting和non-commuting双Generator覆盖(2026-05-07)
- [arXiv:2605.04136](https://arxiv.org/abs/2605.04136) | Authors: Erfan Abbasgholinejad, Sean R. Muleady, Jacob Bringewatt, Lorcan O. Conlon, Alexey V. Gorshkov (NIST/UMD)
- **技术突破**:推导出任意函数形式参数估计的终极量子极限,并提出估计协议;首次给出多参数量子传感中非平凡参数函数精度的通用量子极限;涉及commuting和non-commuting两种发生器
- **核心进展**:多参数量子传感是下一代量子传感系统的核心挑战;同时测量磁场、梯度、温度等多物理量需要克服参数间非对易性带来的精度限制
- **量子传感关联**:该工作为多参数量子传感协议设计提供理论基准;对NV色心、原子系综等多种平台的实际传感协议有重要指导意义

#### IOP Quantum Science and Technology - 多参数量子传感最新综述:量子精密测量的下一个前沿(2026)
- [IOP Quantum Science and Technology](https://iopscience.iop.org/journal/2058-9565) | IOP Publishing
- **综述覆盖**:多参数量子估计、非经典态增强传感、分布式量子传感网络、量子传感与机器学习融合
- **量子传感关联**:IOP Quantum Sci. Technol.是量子传感领域顶级期刊;综述文章反映量子传感研究的前沿热点和未来方向

#### NASA ESTO量子重力梯度仪Pathfinder:2030年实现轨道测试,单卫星冷原子干涉重力测量超越GRACE精度(2026)
- [NASA ESTO Quantum Sensing](https://esto.nasa.gov/quantum/) | [Toward Quantum Enhanced Sensing and Measurements for Earth Observation in 2040报告](https://esto.nasa.gov/files/NASA-QuantumSensing-TM_Report-Final.pdf)
- **技术**:使用冷原子干涉仪技术的量子重力梯度仪(QGG);可从单颗卫星获取比GRACE和GRACE-FO更高的地球引力场测量精度
- **路线图**:2024年NASA地球科学技术办公室(ESTO)启动QGG Pathfinder;目标2030年实现轨道测试
- **应用价值**:绘制引力场地图以探测石油储量、淡水资源;地下水资源勘探、冰盖质量变化、海平面上升观测
- **量子传感关联**:量子重力梯度仪是量子传感精密测量的核心方向;将为地下资源勘探、导航、资源管理提供全新观测手段

---
*本次更新(追加): Quantum Sci. Technol.最新论文/布里斯托量子光子芯片/IOP最新量子传感研究/arXiv多参数量子估计/CIDEX 2026量子传感/Inspira更名QTREX Quantum上市(2026-05-20晚-19:43)*

---

### 🆕 新增条目(2026-05-20晚-19:43 - 本次更新)

#### IOP Quantum Science and Technology - 多参数量子传感终极极限:arXiv:2605.04136通用哈密顿量参数函数估计(2026-05-07)
- [arXiv:2605.04136](https://arxiv.org/abs/2605.04136) | Authors: Abbasgholinejad, Muleady, Bringewatt, Conlon, Gorshkov (NIST/UMD)
- **技术突破**:推导出任意函数形式参数估计的终极量子极限,并提出估计协议;首次给出多参数量子传感中非平凡参数函数精度的通用量子极限;涉及commuting和non-commuting两种 генератора
- **核心进展**:多参数量子传感是下一代量子传感系统的核心挑战;同时测量磁场、梯度、温度等多物理量需要克服参数间非对易性带来的精度限制
- **量子传感关联**:该工作为多参数量子传感协议设计提供理论基准;对NV色心、原子系综等多种平台的实际传感协议有重要指导意义

#### University of Bristol - 质子级光量子传感器:环谐振器实现量子极限探测,晶圆级量产(2025-02)
- [Quantum Sensing to Engineer Photonic Sensors(TechBriefs, 2025-02)](https://www.techbriefs.com/component/content/article/52474-quantum-sensing-to-engineer-photonic-sensors) | QET Labs, Bristol
- **技术**:利用微环谐振器(microring resonator)实现质量可manufacture的光子传感器在量子极限运行;微环谐振器形状像跑道,光在环中循环并与样品最大化相互作用
- **突破**:无需复杂的纠缠或压缩态即可实现量子极限精度测量;用与智能手机芯片相同工艺的晶圆级CMOS工艺制造
- **应用**:吸收率/折射率变化传感可识别温室气体、癌症检测;芯片级量子光子传感器是量子传感商业化的重要方向
- **量子传感关联**:光子芯片量子传感器是量子传感走向大规模商用的重要路径;量子工程与技术实验室(QET Labs)实现mass manufacturable的量子极限光子传感器

#### 2026第十四届中国国际国防电子展览会(CIDEX 2026):量子传感成为国防电子重要方向,2026年9月2-4日北京(2026-04)
- [CIDEX 2026(搜狐, 2026-04-17)](https://so.html5.qq.com/page/real/search_news?docid=70000021_71369e1a87544552) | 指导单位:装备发展部;主办方:中国电子信息产业集团
- **量子传感关联**:中国国际国防电子展是国防电子领域最高级别展会;量子导航、量子探测、量子成像等量子传感技术是重要展示方向
- **背景**:中国国防支出2026年预计1.94万亿元;量子传感在军事精确制导、战场感知、量子导航定位(PNT)等领域有重要应用前景

#### arXiv:2605.04136 - Multiparameter Function Estimation for General Hamiltonians:多参数量子传感的终极精度极限(2026-05-07)
- [arXiv:2605.04136](https://arxiv.org/abs/2605.04136) | Authors: Erfan Abbasgholinejad, Sean R. Muleady, Jacob Bringewatt, Lorcan O. Conlon, Alexey V. Gorshkov
- **技术**:研究编码在哈密顿量中的物理参数估计的终极精度极限;推导任意参数函数的量子克拉美尔界限(QCRB);提出可达该极限的估计协议
- **核心突破**:首次给出多参数系统中参数函数精度的通用量子极限;处理commuting和non-commuting两种发生器情况
- **量子传感关联**:多参数量子传感是实用量子传感系统的核心需求;该工作为设计接近最优精度的实际传感协议提供理论指导

#### QTREX Quantum(原Inspira Technologies)今日(5/20)登陆纳斯达克:量子增材制造电子+量子连接基础设施(2026-05-20)
- [Inspira Technologies更名QTREX Quantum(富途, 2026-05-19)](https://news.futunn.com/post/73329907/inspira-technologies-to-begin-trading-as-qtrex-quantum-under-nasdaq) | 纳斯达克股票代码:QTEX
- **战略聚焦**:AME(增材制造电子)技术平台 + 量子连接基础设施(quantum connectivity);新名称体现量子相关业务战略重点
- **量子传感关联**:量子计算硬件的互连瓶颈是量子系统扩展的关键挑战;量子连接技术直接影响量子传感器阵列和量子计算系统的规模扩展能力
- **市场动态**:2026年量子科技公司IPO活跃;量子传感产业链上游(材料、设备、互连)获得资本市场关注

---
*本次更新(追加): 中科大首个核自旋量子传感网络Nature论文/分布式城际量子传感器Nature暗物质探测/量子纠缠增强原子钟PRL/Quantum Innovation Summit Dubai 2026(2026-05-20下午-17:43)*

---

### 🆕 新增条目(2026-05-20下午-17:43 - 本次更新)

#### 中科大彭新华/江敏团队 - 全球首个核自旋量子传感网络:Nature论文,暗物质探测灵敏度超天文观测40倍(2025-12 Nature, 2026-01报道)
- [全球首个核自旋量子传感网络(央广网, 2026-01-29)](https://so.html5.qq.com/page/real/search_news?docid=70000021_115697ab79244652) | [中科大自旋磁共振实验室](https://ustc.edu.cn/)
- **技术方案**:革新核自旋量子精密测量技术,将信号保存在接近分钟级的核自旋相干态中延长探测窗口;通过自研量子放大技术将微弱信号增强100倍
- **组网部署**:将五台超灵敏量子传感器分别部署在合肥与杭州,通过卫星时间精确同步,构建成分布式探测网络;各站点时间关联特征可过滤局部干扰噪声,极大提高探测可靠性
- **核心成果**:经过两个月持续观测,在广泛轴子质量范围内给出该暗物质模型最严格限制标准;部分质量区间限制精度比天文学家用超新星观测结果高出40倍,首次实现实验室探测精度超越天文观测
- **审稿人评价**:"这项工作为粒子物理和天体物理研究提供了强大工具,将激发新的研究浪潮"
- **未来计划**:进一步扩大量子探测网覆盖范围,通过全球组网、空间部署等方式将探测灵敏度再提升4个数量级;该网络化思路未来可与引力波天文台协同
- **量子传感关联**:核自旋量子传感网络代表量子传感从单点测量向网络化分布式传感的重大升级;为暗物质探测、引力波观测等基础物理研究提供全新工具

#### Nature 2026 - 分布式城际量子传感器约束轴子暗物质:全球光学磁力计网络探测拓扑缺陷暗物质(2026-01-28)
- [Nature论文:s41586-025-10034-w](https://www.nature.com/articles/s41586-025-10034-w) | 作者:待补充
- **技术方案**:利用分布式光学磁力计(OPM)城际网络探测轴子类暗物质拓扑缺陷(Topological Defect Dark Matter, TDM);当地球穿越暗物质墙时,轴子与核自旋传感器发生极微弱相互作用产生瞬时信号
- **研究意义**:探索占比宇宙26.8%的暗物质;轴子是暗物质热门候选者之一,形成的场可能存在拓扑缺陷
- **量子传感关联**:分布式量子传感网络是量子传感技术的重要发展方向;光学磁力计(OPM)无需低温即可工作,是构建城际量子传感网络的理想平台

#### Physical Review Letters 2026 - 量子纠缠增强原子钟:计时稳定性突破标准量子极限,精度提升至全新水平(2026-02)
- [量子纠缠让原子钟更精确(搜狐, 2026-03-10)](https://so.html5.qq.com/page/real/search_news?docid=70000021_62569afdfb189352) | 发表于Physical Review Letters
- **技术原理**:利用量子纠缠态使原子钟的计时稳定性超越标准量子极限;量子纠缠提供比独立原子更高的测量精度
- **核心突破**:原子钟是量子传感最成熟的应用;量子纠缠增强进一步提升时间测量的精度上限
- **量子传感关联**:量子纠缠是量子传感中提升信噪比的核心资源;该工作将量子纠缠直接应用于时频测量这一最成熟的量子传感方向

#### Quantum Innovation Summit Dubai 2026:9月28-30日,量子传感从硬件突破到工业采纳(2026-09)
- [Quantum Innovation Summit Dubai 2026](https://quantuminnovationsummit.com/) | 主办方:Quantum for Good Curator
- **主题**:"Quantum & Emerging Frontiers - Advancing Global Innovation & Technological Leadership"
- **核心议题**:量子传感商业化、量子AI融合、量子与先进计算协同、量子传感从实验室到工业采纳的路径
- **量子传感关联**:中东地区加大量子科技投资;迪拜量子峰会聚焦量子技术从展示向规模化交付的转型

---
*本次更新(追加): attocube attoNVM低温NV磁学显微镜/最新量子传感产业动态(2026-05-20下午-15:43)*

---

### 🆕 新增条目(2026-05-20下午-15:43 - 本次更新)

#### attocube - 低温NV色心扫描成像磁强计attoNVM:1.8K/3µT/√Hz/纳米级分辨率,已商业化量产(2026-01)
- [限额免费测!1.8K低温NV色心扫描磁学显微镜(腾讯新闻, 2026-01-22)](https://new.qq.com/rain/a/20260122A024JB00) | [attocube attoNVM产品页](https://www.attocube.com/)
- **参数**:工作温度2K至300K;灵敏度3µT/√Hz(1.8K低温条件);空间分辨率亚纳米级
- **实测案例**:斯图加特大学Wrachtrup团队用attoNVM在1.8K低温下,以<50nm分辨率清晰分辨NbSe₂单个磁通涡旋,捕捉冷却速率对涡旋晶格的影响(发表于Physical Review Letters);波士顿学院Zhou团队对CrPS₄反铁磁畴实现原子级成像(发表于Nature Materials)
- **量子传感关联**:低温NV色心是实现纳米尺度磁性表征的最高灵敏度工具;attoNVM是市面上唯一商业化的低温NV扫描磁学显微镜;Quantum Design中国开放免费测样活动(限50个名额)

#### 量子传感产业链供应商动态:元素六/博世/Qnami/attocube/Paragraf/Infleqtion/国仪量子(2026持续)
- **NV量子传感系统**:Qnami(ProteusQ系列)、attocube(attoNVM低温NV显微镜)、国仪量子(量子钻石单自旋谱仪)
- **金刚石材料**:元素六(Element Six,戴比尔斯集团)提供量子级金刚石衬底;博世×元素六成立量子传感合资公司;QBN会议聚焦CVD金刚石规模化
- **石墨烯量子传感**:Paragraf(PMF2000 GFET磁传感器,2026年5月发布);晶圆级石墨烯量产直径达8英寸
- **中性原子量子传感**:Infleqtion(量子频谱定义者,NYSE:INFQ上市)、SBQuantum(400万美元种子轮)、Vector Atomic(IonQ收购)
- **室温量子磁力计**:国仪量子(量子磁力仪);未磁科技(量子精密磁场传感国产化)
- **量子传感产业链关联**:从材料生长、器件制造到系统集成,量子传感供应链各环节均有头部企业布局;中国在NV磁力计和原子重力仪领域形成集群优势

---

*本次更新(追加): NVision量子增强MRI/纵激元常温量子传感芯片/第二届量子年会Q10颁奖/量子传感工业感知深度分析(2026-05-20下午-15:13)*

---

### 🆕 新增条目(2026-05-20下午-15:13 - 本次更新)


#### NVision量子增强MRI + 量子计算扩展:雅培主导5500万美元B轮融资,POLARIS量子分子成像平台年底全球20中心部署(2026-05-13)
- [NVision量子传感扩展量子计算(腾讯, 2026-05-14)](https://so.html5.qq.com/page/real/search_news?docid=70000021_8916a05ab7771852) | [NVision官网](https://nvisionmed.com/)
- **技术方案**:POLARIS平台利用量子技术将含糖成像剂的MRI信号提升数量级,实现标准MRI系统的实时代谢测量;在数小时至数天内根据疾病生物学评估治疗反应
- **量子增强原理**:核心是单光子发射的有机分子,形成一类全新的量子比特;利用量子分子方法增强MRI信号对比度
- **量子计算扩展**:发现了新一类有机分子量子比特,结合量子计算设计更有效的药物候选物,量子增强MRI在真实生物环境中验证,建立"计算与验证"统一方法
- **市场进展**:POLARIS系统已在全球领先癌症中心安装,预计年底前在美国、欧洲和亚洲约20个中心部署
- **量子传感关联**:量子分子成像是量子传感向生物医学延伸的新方向;从"量子诊断"到"量子制药"的范式扩展

#### 纵激元科技 - 全球首个常温量子传感工程化应用:脉泽量子无源无线传感器/常温量子传感芯片(2026-01-28)
- [2026量子科技产业生态发展大会(腾讯新闻, 2026-01-28)](https://new.qq.com/rain/a/20260128A07K2I00) | 电子科技大学教授、博士团队创立
- **核心技术**:2016年起深耕量子传感领域,2019年成功研制全球首台"常温晶体管微波激射器",突破传统技术对低温、光泵浦、强磁场的依赖
- **产品:脉泽量子无源无线传感器**:彻底摆脱直流供电束缚,凭借超高灵敏度、超超快响应优势,在极端工况下精准测量温度、压力、振动等物理量
- **已应用领域**:轨道交通、电力系统等;被权威认定为"全球首个常温量子传感工程化应用"
- **量子传感关联**:常温量子传感是相比OPM更进一步的工程化突破;无需任何低温或强磁场支持即可实现量子增强传感,是量子传感商业化的重大里程碑

#### 第二届量子年会暨Q10颁奖典礼:量子精密磁场传感国产化成果发布,两仪万象/未磁科技等分享技术突破(2026-03-13)
- [第二届量子年会暨Q10颁奖典礼(腾讯, 2026-03-16)](https://so.html5.qq.com/page/real/search_news?docid=70000021_80469b7b50c83752) | 光子盒、中关村量子信息产业联盟联合主办
- **量子传感论坛**:量子信息技术创新与产业落地专题论坛展示量子传感与安全技术商业化蓝图;印证量子科技成为多领域数智化转型的核心硬科技支撑
- **未磁科技**:代表分享量子精密磁场传感技术突破及国产化成果;在石油化工、医疗、政务等行业的应用实践
- **两仪万象**:围绕离子阱量子计算机等细分领域分享技术突破
- **行业共识**:量子传感已成为塑造新质生产力的关键支撑;从技术突破转向规模化应用的关键转折点
- **量子传感关联**:量子传感国产化进入快车道;工业级部署成为竞争焦点

#### 量子传感:工业感知的下一次跨越 - ICV TA&K深度产业分析(2026-03)
- [量子传感:工业感知的下一次跨越(量感局, 2026-03-04)](https://so.html5.qq.com/page/real/search_news?docid=70000021_08569a8149706452)
- **产业规模**:2025年18.8亿美元→2035年50.7亿美元,CAGR 10.42%;量子传感从早期少数领域支撑向全物理量覆盖转变
- **技术成熟度分化**:时频测量(13.3亿美元,2035年)、磁场测量(13.1亿美元)、重力测量(12.3亿美元)形成三大支柱;电场、惯性方向加速演进
- **硬件家族**:原子钟、量子重力仪、量子磁力计、量子惯性传感器(SQUID/NV/OPM)构成完整体系
- **重点企业**:Infleqtion(光学原子钟/PNT套件)、Vector Atomic(IonQ收购,原子钟导航)、Atomionics(量子重力仪勘探)、Q-CTRL(量子控制软件)、QuantumDiamonds(NV量子显微镜)、SandboxAQ(AQNav量子导航)
- **量子传感核心原理**:量子叠加态(精度之源)、量子纠缠态(信噪比提升)、量子相干性(性能上限);工作流程:初始化→交互→读出
- **量子传感关联**:量子传感正以远超量子计算的商业化速度跨越"死亡之谷";2025年联合国"国际量子科学与技术年"标志量子感知从理论走向大规模工业部署

---
*本次更新(追加): 量子传感最新产业与产品动态/MIT量子雷达/光学泵浦磁力计MEG应用/ResearchAndMarkets量子技术报告/CesiumTracker原子钟/Acta Physica Sinica机载量子重力仪(2026-05-20下午-14:43)*

---

### 🆕 新增条目(2026-05-20下午-14:43 - 本次更新)

#### CesiumTracker原子钟芯片 - 芯片级量子传感商业化标杆(2026持续)
- [Cesium Tracker官网](https://cesiumtracker.com/) | 芯片级铯原子钟技术
- **技术**:基于MEMs工艺与原子物理学结合的芯片级原子钟;可在无GPS信号环境下提供高精度授时,误差远小于传统晶体振荡器
- **量子传感关联**:芯片原子钟是量子传感最成熟、规模最大的商业化产品;是量子传感技术从实验室走向大规模商用的成功范例

#### MIT Technology Review - 量子雷达新方案:原子云室温探测反射射频波,可成像隐蔽目标(2025-08-11)
- [MIT Technology Review (2025-08-11)](https://www.technologyreview.com/2025/08/11/1121314/this-quantum-radar-could-image-buried-objects/) | 研究团队:NIST + RTX(原Raytheon)
- **技术原理**:使用玻璃气室中悬浮的铯(Caesium)原子云在室温下探测反射的射频波;激光将原子驱动到高度敏感的量子态,当射频信号反弹回来时,原子云发射可检测的光信号
- **创新点**:传统雷达需发射强射频信号才能探测回波,容易被探测和干扰;量子雷达利用原子量子态放大微弱返回信号,可探测隐蔽目标
- **当前状态**:仍为原型阶段,体积较大(光学表+组件);展示了量子传感在国防安全领域的巨大潜力

#### Optically Pumped Magnetometers (OPM)用于脑磁图(MEG):Springer综述+Commercialising Quantum Global 2025(2019-2025持续)
- [Springer: Optically Pumped Magnetometers for MEG](https://link.springer.com/10.1007/978-3-030-00087-5_49) | Authors: Elena Boto等(Nottingham大学)
- **技术原理**:光泵浦磁力计利用圆偏振光泵浦碱金属原子使其极化,射频场引起退极化导致光吸收变化从而检测磁场;无需低温制冷
- **灵敏度**:目前最好灵敏度可达~1 fT/√Hz,与SQUID相当,但可在室温下工作
- **商用进展**:Cerca Magnetics(380万英镑A轮)、Quantum Design(收购Oxford NanoScience)均在OPM/MEG领域布局
- **量子传感关联**:OPM是量子磁力计商业化最活跃的方向之一;室温运行优势使其成为最具商用前景的量子传感器类型

#### Acta Physica Sinica 2025 - 机载绝对重力测量量子重力仪:量子传感精密测量支撑国家战略(2025)
- [Acta Physica Sinica (2025-02-09)](https://wulixb.iphy.ac.cn/en/article/doi/10.7498/aps.74.20241621) | 作者:翟晨洁,王晶,周俊杰等(多家单位联合)
- **技术**:基于量子重力仪的机载绝对重力测量;利用原子干涉仪技术实现绝对重力加速度测量
- **科学意义**:机载重力测量对地质勘探、冰川监测、海平面变化等有重要应用价值;量子重力仪提供前所未有的测量精度
- **量子传感关联**:原子干涉重力仪是量子传感精密测量的核心方向;机载化是量子重力仪从实验室走向大规模地球观测应用的关键里程碑

#### ResearchAndMarkets量子技术市场报告:2025年339亿美元→2035年993亿美元(CAGR 11.3%)(2025-08)
- [Quantum Technology Market 2025-2035(ResearchAndMarkets)](https://www.researchandmarkets.com/reports/5317365/quantum-technology-market-by-computing) | 416页报告
- **量子传感份额**:量子传感与成像是四大板块之一;在国防和医疗领域的早期落地推动市场规模扩张
- **地区格局**:北美主导,亚太快速增长;半导体工艺进步降低SWaP-C,量子传感器从实验室走向嵌入式系统
- **量子传感关联**:市场规模高速增长验证量子传感从实验室向商业化转型的加速;国防和医疗是率先落地场景

#### NIST × RTX Rydberg原子量子射频传感器:无天线射频检测,突破传统射频感知架构(2025)
- [NIST Rydberg原子传感研究页面](https://www.nist.gov/news-events/news/2025/quantum-radar-new-kind-radio-wave-detector) | [RTX官网](https://www.rtx.com/)
- **技术原理**:Rydberg原子射频传感利用高激发态Rydberg原子对电磁场的极端敏感性;原子作为"天线",检测射频信号无需物理天线结构
- **核心优势**:Rydberg原子可覆盖DC至THz的极宽频谱;无方向性天线,球形全向响应;原子响应速度快,适合动态信号
- **量子传感关联**:Rydberg原子传感是量子传感领域发展最快的方向之一;与NV色心磁力计互补,前者测射频电场,后者测磁场

---

*本次更新(追加): Sandia 2025三大核心专利/Physical Review Applied量子声子学专辑/Princeton量子传感/arXiv光频梳量子计量/CQT首届亚洲离子阱会议(2026-05-20早-10:43)*

---

### 🆕 新增条目(2026-05-20早-10:43 - 本次更新)

#### MIT × 本田研究所 × 美国陆军DEVCOM - 腔增强固态核自旋量子陀螺仪:灵敏度提升3个数量级,PRL里程碑(2025-05-09)
- [MIT腔增强核自旋陀螺仪(腾讯新闻, 2025-05-12)](https://new.qq.com/rain/a/20250512A083QW00) | 发表于Physical Review Letters
- **技术方案**:基于金刚石NV色心系综,采用nNV-cQED(核自旋-腔量子电动力学)系统,观察到电磁感应透明、无反转激射和振荡行为
- **核心突破**:旋转灵敏度相比此前固态自旋演示提升3个数量级;NV电子自旋同时作为共磁力计,四个结晶轴NV实现单一系统矢量分辨率
- **量子传感关联**:核自旋陀螺仪兼顾长期稳定性与短期灵敏度;量子传感在惯性导航领域的关键突破;固态平台室温运行比传统原子陀螺仪更具实用性

#### Sandia国家实验室 - 硅光子原子干涉仪2025年三大核心专利获批:紧凑grating MOT + Evanescent Field引导 + 惯性导航(2025)
- [US12449256 (2025-10-11)](https://patents.google.com/patent/US12449256B1/en) | [US12424810 (2025-09-23)](https://patents.google.com/patent/US12424810B1/en) | [US12392611 (2025-08-19)](https://patents.google.com/patent/US12392611B1/en)
- **US12449256**: Compact Grating Magneto-Optical Trap Sensor Head—紧凑光栅磁光阱传感器头,采用custom titanium真空腔+微纳加工光栅芯片+固定光学组件,支持动态环境下的可靠量子传感
- **US12424810**: Compact Atom Interferometry Inertial Navigation Sensors—定制衍射光学紧凑原子干涉仪惯性导航传感器,实现双轴高速数据率原子干涉仪
- **US12392611**: Measurement Protocol for Large Dynamic Range and High Sensitivity of Evanescent-Field-Mode Guided Atom Interferometer—大动态范围高灵敏度Evanescent-Field-Mode引导原子干涉仪测量协议;Sandia硅光子单边带调制器(Science Advances 2024, eade4454)支撑
- **量子传感关联**:硅光子PIC激光系统无需笨重铌酸锂调制器,为芯片级量子惯性传感器铺平道路;三大专利覆盖传感器头、光学、测量协议全技术栈

#### Physical Review Applied 2026 - Phononics and Metamaterials专辑:量子力学与弹性波的深度交叉,TWPAs是超导量子处理器核心组件(2026-03)
- [Physical Review Applied Phononics and Metamaterials Collection(APS, 2026-03)](https://journals.aps.org/prapplied/) | Guest Editors: Muamer Kadić, Daniel Torrent, Abdelkrim Nashash
- **专辑覆盖**:声子晶体、超材料、弹性波与量子效应的深度融合;traveling-wave parametric amplifiers (TWPAs)是超导量子处理器核心组件
- **量子传感关联**:声子作为机械振动的量子化描述,与量子传感中的噪声抑制和相干控制直接相关;声子-光子耦合是芯片级量子传感器件的重要物理机制

#### arXiv:2605.16585 - Penning陷阱中H₂⁺和H̅₂⁻的高精度光谱:10⁻¹⁷量级CPT不变性检验,量子精密测量新平台(2026-05-15)
- [arXiv:2605.16585](https://arxiv.org/abs/2605.16585) | 作者:19页
- **技术方案**:H₂⁺和H̅₂⁻振动跃迁频率比较提供CPT不变性检验新途径;在Penning陷阱中进行非破坏性读出激光光谱,结合连续Stern-Gerlach效应或量子逻辑光谱
- **精度目标**:在现有技术下可实现10⁻¹⁷量级的振动频率比较精度--逼近量子精密测量的极限
- **量子传感关联**:Penning陷阱是实现最高精度原子传感器(如量子磁场计)的核心技术;分子离子光谱为量子精密测量提供新型传感平台

#### CQT新加坡首届亚洲离子阱会议:量子传感与量子计算交叉融合,离子阱传感器在电场/磁场/重力场测量中极高精度(2026-04-24)
- [CQT hosts inaugural Asian Conference on Trapped Ions(CQT, 2026-04-24)](https://www.quantumlah.org/news) | 新加坡国立大学
- **会议主题**:聚焦离子阱技术在量子计算、量子传感和量子精密测量中的应用
- **量子传感关联**:离子阱是实现高灵敏度量子传感器的核心技术平台之一;离子阱量子传感器在电场、磁场和重力场测量中具有极高精度

---

*本次更新(追加): arXiv量子传感最新论文/NASA量子重力梯度仪Pathfinder/Imperial量子传感Q&A/2026量子技术监测报告(2026-05-20早-06:43)*

---

### 🆕 新增条目(2026-05-20早-06:43)

#### arXiv:2605.17750 - NV色心系综自旋力驱动128mg悬浮谐振器:量子-宏观力耦合里程碑,自旋-质量混合系统进入高质量 regime(2026-05-19)
- [arXiv:2605.17750](https://arxiv.org/abs/2605.17750) | 作者:22页,4图
- **技术**:在金刚石中利用NV缺陷系综的自旋力驱动128mg抗磁性悬浮振荡器的可控质心运动;通过周期性光初始化NV自旋态诱导振荡器相干运动,实现超过100nm的运动幅度
- **核心突破**:首次实验观测到原子尺度以上自旋力对宏观质量的作用;是实现自旋-质量混合系统量子工程的关键里程碑
- **量子传感关联**:NV色心自旋与机械振荡器的耦合为新型量子传感器(如量子加速度计、量子重力仪)提供了混合系统路径;悬浮机械振子可用于探索量子与引力界面

#### arXiv:2605.16559 - 非厄米超导量子系统中复Berry相位的测量与控制:实部+虚部同时测量,非厄米量子控制的几何方法(2026-05-19)
- [arXiv:2605.16559](https://arxiv.org/abs/2605.16559) | 作者:10页,8图
- **技术**:利用具有工程耗散的超导transmon电路实验测量复Berry相位的实部和虚部;展示虚部对耗散的路径依赖效应及其在非厄米量子控制中的应用
- **核心突破**:首次在完全量子系统中同时测量复Berry相位的实部和虚部;建立复Berry相位的实部与虚部之间的明确几何区分
- **量子传感关联**:Berry相位在几何量子计算和量子传感中具有重要作用;非厄米量子系统为鲁棒量子传感和量子计量提供新途径

#### NASA ESTO量子重力梯度仪Pathfinder:2030年实现轨道测试,单卫星冷原子干涉重力测量超越GRACE精度(2026)
- [NASA ESTO Quantum Sensing](https://esto.nasa.gov/quantum/) | [Toward Quantum Enhanced Sensing and Measurements for Earth Observation in 2040报告](https://esto.nasa.gov/files/NASA-QuantumSensing-TM_Report-Final.pdf)
- **技术**:使用冷原子干涉仪技术的量子重力梯度仪(QGG);可从单颗卫星获取比GRACE和GRACE-FO更高的地球引力场测量精度
- **路线图**:2024年NASA地球科学技术办公室(ESTO)启动QGG Pathfinder;目标2030年实现轨道测试
- **量子传感关联**:量子重力梯度仪是量子传感精密测量的核心方向;将为地下水资源勘探、冰盖质量变化、海平面上升等地球科学观测提供全新手段

#### Imperial College London量子传感Q&A:皇家海军导航测试/量子脑成像/QuEST中心启动/时间双缝实验(2026-05-08)
- [Imperial量子传感Q&A(2026-05-08)](https://www.imperial.ac.uk/news/246634/qa-how-will-quantum-science-transform) | [海军导航测试(2026)](https://www.imperial.ac.uk/news/245114/quantum-sensor-future-navigation-system-tested/) | [QuEST中心公告(2026)](https://www.imperial.ac.uk/news/245835/new-quantum-technologies-developed-imperial-initiative/)
- **海军量子导航**:英国皇家空军飞机量子导航测试成功后,延伸至皇家海军舰船;量子惯性传感器可在GPS拒止环境下提供高精度定位
- **已实用化三大领域**:1超精密时钟(原子钟);2超灵敏重力仪(地下勘探);3超灵敏磁力计(脑成像+自主导航)
- **QuEST中心**:量子工程、科学与技术中心正式启动,三大主题:量子材料、量子互联网、量子计算应用

#### 2026年量子技术监测报告:量子传感在国防和工业检测领域已进入应用阶段(2026-05-18)
- [2026年量子技术监测报告(搜狐, 2026-05-18)](https://www.sohu.com/a/1019974190_121776575)
- **三大领域进展**:量子计算依旧是投资热点(占比90%以上);量子通信从实验室走向QKD网络;量子传感(QS)在国防领域已步入应用阶段,同时于工业检测领域也进入了应用阶段
- **市场态势**:量子传感市场规模相对较小,但增长态势明确;从"展示能做什么"进入"规模化交付"阶段
- **关注方向**:量子传感技术从单点设备向系统能力升级;时频、磁场测量率先产业化;重力测量找到刚性需求

---

*本次更新(追加): 量子传感产业最新资讯/NIST量子传感研究/Caltech量子传感探测/量子传感产业链(2026-05-20凌晨-04:15)*

---

### 🆕 新增条目(2026-05-20凌晨-04:15 - 本次更新)

#### 2026全球量子传感产业展望:18.8亿美元→50.7亿美元,CAGR 10.42%;产业从"展示能做什么"进入"规模化交付"阶段(2026-03)
- [2026全球量子传感产业发展展望(搜狐, 2026-03-10)](https://www.sohu.com/a/994406319_121694397) | 135页报告
- **市场预测**:2025年约18.8亿美元→2035年50.7亿美元(CAGR 10.42%);2035年达50.7亿美元;民用化转型是规模放量的关键
- **产业阶段**:从实验室走向工程验证与产业化;竞争核心转向批量交付稳定性与成本控制;资本向具备工程化能力的头部企业集中
- **技术格局**:时频、磁场测量率先产业化;重力测量找到刚性需求;电场、惯性等方向加速演进;产业从单点设备向系统能力升级
- **区域格局**:全球形成东西方双技术体系,中美欧为核心区域;美国以国防牵引技术落地;中国将量子科技列为未来产业首位并在磁传感、重力领域形成集群优势
- **资本动态**:2025年融资回归理性,中性原子技术成资本重点;量子导航成国家定位主权核心方向;技术标准与供应链成为市场准入关键

#### Qnami - 全球量子传感领先企业,NV色心扫描显微镜+ProteusQ双产品线(2026持续)
- [Qnami官网](https://qnami.ch/) | [ProteusQ产品页](https://qnami.ch/proteusq/)
- **ProteusQ-LT**:低温扫描NV显微镜专用,原子尺度捕获表面磁场,用于量子材料表征;灵敏度达亚微特斯拉每根号赫兹级别
- **ProteusQ**:常温量子波技术平台,面向纳米技术、生命科学和地球科学应用
- **核心技术**:金刚石量子探针(NV中心)、系统级集成、数据分析软件;晶圆级金刚石纳米加工能力
- **市场扩张**:2026年5月宣布东亚市场扩张,Quantum Design Japan和Quantum Design Korea正式成为区域代理

#### IDTechEx量子传感市场报告2024-2044:2025年约19亿美元→2044年71亿美元(2025)
- [Quantum Sensors Market 2024-2044(IDTechEx)](https://www.idtechex.com/en/research-report/quantum-sensors-market-2024-2044/951)
- **覆盖范围**:原子钟、量子陀螺仪、量子磁场传感器、量子重力仪、量子图像传感器五类技术
- **核心技术路线**:NV色心磁力计、原子干涉重力仪、冷原子Rb/Rb蒸汽室、光泵磁力计、 superconducting量子干涉仪(SQUID)
- **SWaP-C挑战**:尺寸、重量、功耗、成本是商业化最大瓶颈;半导体工艺(晶圆级VCSEL、蒸汽电池微纳加工)是破局关键

#### ResearchAndMarkets量子技术市场报告2025-2035:339亿美元→993亿美元(CAGR 11.3%)(2025-08)
- [Quantum Technology Market 2025-2035(ResearchAndMarkets)](https://www.researchandmarkets.com/reports/5317365/quantum-technology-market-by-computing) | 416页报告
- **量子传感份额**:量子传感与成像是四大板块之一;在国防和医疗领域的早期落地推动市场规模扩张
- **地区格局**:北美主导,亚太快速增长;半导体工艺进步降低SWaP-C,量子传感器从实验室走向嵌入式系统

---

*本次更新(追加): 量子使能鬼成像植物非侵入成像(MedSci 2026-05-08) / TOPTICA量子传感与计量 / Princeton量子传感研究(2026-05-20凌晨补充)*

---

### 🆕 新增条目(2026-05-20凌晨 - 今日最新)

#### Science Advances 2026 - 量子使能鬼成像:植物非侵入成像,超越经典成像信噪比极限(2026-05-08)
- [Quantum-enabled ghost imaging for non-invasive imaging of plants(MedSci, 2026-05-08)](https://www.medsci.cn/sci/show_paper.asp?id=35c4a1259231266b) | 作者:DP Ryan, K Meier, D Thompson, R Newell, JH Werner等
- **技术**:量子增强鬼成像利用量子纠缠光子对实现低于经典信噪比极限的植物内部结构成像;完全非接触、非侵入,无需聚焦,可对活体植物进行三维成像
- **核心优势**:在低光条件下仍可获得高信噪比图像;对光敏感生物样本无损伤
- **量子传感关联**:量子成像(Quantum Imaging)是量子传感的重要分支;鬼成像利用量子纠缠实现超越经典极限的成像能力

#### TOPTICA - 量子传感与计量商业化产品线,德国高端激光系统供应商(2026-05)
- [TOPTICA Quantum Sensing & Metrology](https://www.toptica.com/applications/applied-quantum-technology/communication/) | 公司主页
- **技术定位**:TOPTICA提供应用于量子传感和计量的高端半导体激光器和光纤激光器系统;波长覆盖从紫外到红外全波段
- **核心产品**:用于原子钟、原子干涉仪、NV色心磁力计的专用激光系统;支持量子重力仪、量子陀螺仪研发
- **量子传感关联**:激光系统是量子传感器的核心光源;TOPTICA的技术支撑多种量子传感平台的精度提升

#### Princeton Quantum Initiative - NV传感器探测二维自旋 bath,量子传感实验平台(2026)
- [Princeton Quantum Initiative - Quantum Sensing and Metrology](https://quantum.princeton.edu/research/quantum-systems-experiment/quantum-sensing-and-metrology) | 普林斯顿大学
- **研究方向**:利用NV色心传感器探测金刚石表面二维自旋bath(de Leon组);开发新型量子传感协议
- **实验进展**:在NV中心量子传感基础上,探索多量子比特纠缠增强传感;量子-经典混合传感方案
- **量子传感关联**:NV色心是当前最成熟的固态量子传感平台;Princeton的工作推动NV传感向多参数、高灵敏度方向发展

---
*本次更新(追加): Infleqtion量子频谱定义新类别(2026-05-20凌晨)*

---

### 🆕 新增条目(2026-05-20凌晨)

#### Infleqtion正式定义"量子频谱"为量子传感新类别,Rydberg原子射频传感开创数十年RF传感架构根本性转变(2026-05-14)
- [Infleqtion引入量子频谱(腾讯, 2026-05-14)](https://so.html5.qq.com/page/real/search_news?docid=70000021_3276a05b3ff13952) | [Infleqtion官网](https://infleqtion.com/)
- **技术定义**:量子频谱(Quantum Spectrum)是基于里德堡(Rydberg)原子的射频传感平台,代表数十年来射频(RF)传感架构的首次根本性转变
- **核心产品Sqywire**:超灵敏射频(RF)接收器,可安装于经典天线使用;具备高灵敏度、低功耗、超宽带宽特性;可在千赫兹到太赫兹任意范围内运行;无模拟组件,抗干扰能力强
- **应用场景**:关键任务授时(与Safran合作)、水下作战平台(XLUUV搭载Tiqker光钟)、量子增强型精密授时
- **市场地位**:Infleqtion于2026年2月17日登陆纽约证券交易所(NYSE: INFQ),成为全球首家上市的中性原子量子技术公司,市值23.74亿美元

---

*本次更新(追加): Sandia硅光子原子干涉仪2025核心专利/量子传感AI+ML集成/Paragraf石墨烯量子传感/量子精密测量量子增强机器学习/中科院金属所Nature 2026首篇(2026-05-19晚)*

---

### 🆕 新增条目(2026-05-19晚 - 今日最新)

#### Monarch Quantum × Oratomic 达成战略合作:光子系统+中性原子架构,本十年末交付数万个物理量子比特容错量子计算机(2026-04-28)
- [Monarch Quantum × Oratomic战略合作(腾讯, 2026-04-29)](https://so.html5.qq.com/page/real/search_news?docid=70000021_95769f1e58162352)
- **合作内容**:整合光子系统和中性原子架构,打造容错、实用规模的量子计算机;本十年末交付拥有数万个物理量子比特、编码数千个错误更正逻辑量子比特的系统
- **量子传感关联**:中性原子平台是量子传感(如射频传感、量子频谱)的重要技术路线;Monarch的光子系统与Oratomic中性原子架构结合,将提升量子传感系统的操控精度和信息读取效率

#### QBN Meeting - Scaling of Diamond for Quantum Technologies今日(5/19)召开:欧洲量子传感供应链加速整合(2026-05-19)
- [Quantum Flagship Q-Expo 2026](https://qt.eu/) | [QBN Meeting公告](https://qt.eu/)
- **会议焦点**:CVD金刚石生长工艺优化、NV色心批量植入技术、金刚石量子传感器晶圆级制造可行性;Element Six、Qnami等关键玩家参与
- **核心议题**:从"展示能做什么"进入"规模化交付"阶段;金刚石规模化制造是NV量子传感商业化的关键瓶颈
- **Q-Expo 2026**:欧洲最大量子产业展会(5/18-19,阿姆斯特丹),Meet the people shaping Europe's quantum future; Quantum Academy已于5/11正式启动,专注培养下一代量子传感工程师

#### Nature Communications Physics - NV色心量子传感二维磁性材料:Fe₃GeTe₂热激活逃离双稳态磁态(2026-03)
- [Communications Physics (2026-03-02)](https://www.nature.com/articles/s42005-023-01472-x/figures/2) | 论文图2展示NV中心量子磁学成像
- **技术方案**:将Fe₃GeTe₂多层薄膜转移至金刚石(100)表面并封装于两层hBN之间;532nm激光垂直激发,微波通过金线施加;利用NV色心扫描磁学显微镜对二维材料磁结构进行量子成像
- **核心发现**:揭示Fe₃GeTe₂中临近临界点的热激活逃离双稳态磁态行为;Fe₃GeTe₂是大角度转角双层石墨烯之外的另一个量子传感研究热点
- **量子传感关联**:NV色心是实现二维材料纳米尺度磁性表征的唯一无损、非接触式工具;为自旋电子学器件和拓扑磁结构研究提供量子成像能力

#### Scientific Reports 2025 - 船载原子重力仪振动补偿:粒子群优化识别最优补偿系数,残差标准差降低81.25%(2025-03)
- [Scientific Reports论文(2025-03-14)](https://www.nature.com/articles/s41598-025-92544-1) | 基于粒子群优化(PSO)的振动补偿方法
- **技术挑战**:船载原子重力仪受 Raman 镜振动噪声影响显著,传统方法难以有效补偿
- **解决方案**:引入粒子群优化识别最优补偿系数;系泊状态测试表明补偿后原子干涉条纹残差标准差降低81.25%,测量精度显著提升
- **量子传感关联**:原子重力仪是量子传感精密测量的核心方向;振动补偿技术是实现海空载量子重力测量的关键工程难题

---

### 🆕 新增条目(2026-05-19晚 - 今日最新)

#### arXiv:2605.16694 - 紧凑稳健可调谐开放式微腔平台:固态量子电动力学与量子点量子传感(2026-05-16)
- [arXiv:2605.16694](https://arxiv.org/abs/2605.16694) | 作者单位待补充
- **技术**:开发紧凑、稳健、可调谐的机械载体,用于开放式微腔;完整机械组件封装于1"×1"×0.5"尺寸内;在低温下无振动引起的腔展宽,无需低温定制或主动锁定;腔共振调谐范围3nm,多次降温后仍保持在调谐范围内
- **量子传感关联**:展示InGaAs量子点与开放式微腔耦合,合作系数(cooperativity)超过1;固态量子点作为新型量子传感Emitter,可用于高灵敏度光子探测和量子发射源;开放式微腔是实现高保真光-物质相互作用的通用平台
- **意义**:紧凑可调谐微腔平台为固态量子传感器(如量子点磁力计、单光子源)提供了可扩展、便携化的技术基础

#### arXiv:2605.16978 - 闭式解高斯量子态贝叶斯量子估计:变分框架+解析解(2026-05-16)
- [arXiv:2605.16978](https://arxiv.org/abs/2605.16978) | 作者:16页,2图
- **技术**:贝叶斯量子估计为连续变量高斯系统提供鲁棒估计框架,但参数积分复杂导致应用受限;本研究引入变分框架,将测量和估计器优化降为有限维线性问题并获得闭式解
- **核心突破**:将分析限制在正则 quadrature 的多项式算子,得到几何解释为全局最优的正交投影;推导出全局最优性的充要条件;单次测量示例表明基于高斯操作和正交测量的实验可行策略是最优或接近最优的
- **量子传感关联**:高斯态估计是量子光学传感(如量子通信、量子成像)的核心任务;闭式解为量子传感系统的最优测量设计提供解析指导,无需数值优化
- **意义**:贝叶斯方法在有限数据和最小先验信息场景中特别有效,适用于实际量子传感系统的实验设计与实时优化

#### arXiv:2605.16935 - 量子充电完整纠缠深度速度边界:块正交化机制突破量子速限(2026-05-16)
- [arXiv:2605.16935](https://arxiv.org/abs/2605.16935) | 作者
- **技术**:完整量子充电(Complete Quantum Charging)研究纠缠深度与充电速度的定量关系;对于闭合N量子比特电池,从|↓⟩^⊗N演化到|↑⟩^⊗N,精确求解纯态深度约束速度问题;若实现轨迹的纠缠深度最多为k,则最大QSL归一化速率η=τ_QSL/T为η_max(k)=⌈N/k⌉^{-1/2}
- **核心机制**:块正交化(block orthogonalization)--在固定乘积分区下,完整充电强制所有块同时正交化;量子速限将此计数约束转换为速度边界;均衡cluster-flip演化达到边界,建立精确整数阶梯前缘
- **量子传感关联**:量子速限(Quantum Speed Limit)是量子传感中测量时间极限的核心约束;纠缠深度与速度的关系直接影响量子传感器的响应速率和信息获取效率
- **意义**:快速完整充电不能通过多个独立充电的小块解释;越过纠缠阈值需要多体协同,是量子传感系统设计中纠缠资源分配的理论基础

---

### 🆕 新增条目(2026-05-19晚 - 今日最新追加)

#### NASA量子重力梯度仪(Quantum Gravity Gradiometer Pathfinder)计划首次太空量子传感任务(2025-04)
- [NASA Aims to Fly First Quantum Sensor for Gravity Measurements(JPL, 2025-04-15)](https://www.jpl.nasa.gov/news/nasa-aims-to-fly-first-quantum-sensor-for-gravity-measurements/) | [NASA ESTO量子传感项目](https://esto.nasa.gov/quantum/)
- **技术**:NASA喷气推进实验室(JPL)联合私营企业和学术机构,正在开发首个太空量子重力传感器;量子重力梯度仪(QGG)利用量子力学原理测量地球引力场变化
- **应用价值**:绘制引力场地图以探测石油储量、淡水资源;地球引力场每日随地质过程重新分布质量,量子重力仪可感知这些微妙变化
- **科学目标**:2024年NASA地球科学技术办公室(ESTO)启动QGG Pathfinder专项;任务将是量子传感在太空的首次应用
- **量子传感关联**:量子重力梯度仪是量子传感精密测量的核心方向;太空应用将为地下资源勘探、导航、资源管理提供全新观测手段

#### IDTechEx量子传感市场报告2025-2045:晶圆级半导体制造将量子传感器带入大规模商用(2025)
- [Quantum sensor market to grow to 2B by 2045(App Developer Magazine, 2025-04)](https://appdevelopermagazine.com/quantum-sensor-market-to-grow-to-2b-by-2045/) | 基于IDTechEx报告
- **核心挑战**:量子传感器商业化的最大瓶颈是SWaP-C(尺寸/重量/功耗/成本);半导体制造工艺是解决该挑战的最有效途径
- **蒸汽电池(vapor cells)**:玻璃蒸汽电池是原子干涉仪的核心组件;传统玻璃吹制工艺难以小型化,晶圆级半导体工艺可批量生产高度一致的微型蒸汽电池
- **VCSEL技术**:垂直腔面发射激光器(VCSEL)可晶圆级大规模制造;与边发射激光器不同,VCSEL垂直发射光束,允许其他组件直接堆叠在芯片上,是实现芯片级量子传感器的关键
- **市场规模**:量子传感市场预计到2045年增长至20亿美元; IDTechEx报告预测量子传感器市场2025-2045年CAGR约10%

#### Infleqtion × Safran Electronics & Defense量子精密授时方案:全球首款量子增强型军用授时系统(2026-04-01)
- [Infleqtion推出量子精密授时解决方案(腾讯, 2026-04-05)](https://so.html5.qq.com/page/real/search_news?docid=70000021_68069ce675711852) | [Infleqtion官网(NYSE: INFQ)](https://infleqtion.com/)
- **技术合作**:Infleqtion与赛峰电子与防务公司(Safran Electronics & Defense)合作开发全球首款量子增强型精密授时解决方案
- **量子传感关联**:光学原子钟是量子传感最成熟的应用方向之一;量子增强型授时可为关键任务系统提供前所未有的时间精度
- **市场动态**:Infleqtion于2026年2月17日登陆纽约证券交易所,成为全球首家上市的中性原子量子技术公司,市值23.74亿美元,新融资超5.5亿美元

#### Infleqtion Tiqker量子光学原子钟:全球首次部署于无人潜艇XLUUV水下作战平台(2025-10-28)
- [全球首次!量子光学钟成功部署无人潜艇(腾讯, 2025-10-30)](https://new.qq.com/rain/a/20251030A05L5E00)
- **里程碑**:英国皇家海军超大型无人水下航行器(XLUUV)"XV Excalibur"成功搭载Infleqtion研发的Tiqker量子光学原子钟
- **技术意义**:高精度量子传感器首次在水下作战平台上投入运行;将实验室级精确授时能力带入实战部署环境,对全球定位、导航和授时(PNT)技术体系产生深远影响

#### 2025图灵奖:量子信息科学奠基人Charles Bennett与Gilles Brassard获奖(2026-04)
- [深度解读2025年度图灵奖(量子科话, 2026-04-12)](https://so.html5.qq.com/page/real/search_news?docid=70000021_55569db904a92552)
- **获奖原因**:表彰二人"建立量子信息科学基础以及变革安全通信与计算方面所发挥的关键作用"
- **对量子传感的影响**:量子密码(QKD)和量子通信是量子传感的重要应用方向; Bennett提出的量子信息理论基础为量子传感的信号处理和信息安全提供支撑
- **历史意义**:图灵奖首次授予量子信息领域,标志量子技术进入主流计算与信息科学核心圈

#### 英国政府4500万英镑量子技术投资:量子脑扫描仪/量子导航/量子计算机(2024-02)
- [UK government £45 million quantum investment(Gov.uk, 2024-02-05)](https://www.gov.uk/government/news/unlocking-the-potential-of-quantum-45-million-investment-to-drive-breakthroughs-in-brain-scanners-navigation-systems-and-quantum-computing)
- **量子脑扫描仪**:英国政府投资开发基于量子技术的高科技脑扫描仪,用于改善癫痫和痴呆症等疾病的诊断
- **量子导航**:量子惯性导航系统可在无GPS信号环境下提供高精度定位,对于国防和民用导航意义重大
- **量子计算机**:3000万英镑用于研发世界领先原型量子计算机

---

*本次更新(追加): Sandia硅光子原子干涉仪2025核心专利/量子传感AI+ML集成/Paragraf石墨烯量子传感/量子精密测量量子增强机器学习/中科院金属所Nature 2026首篇(2026-05-19晚)*

### 🆕 新增条目(2026-05-19傍晚 - 最新批)(续)

#### MIT/芝加哥大学/东京大学/港中文 - PRX Quantum:固态量子传感器首次实现多参数同时估计,纠缠辅助突破标准量子极限(2026-04)
- [固态量子传感器首次实现多参数同时估计(so.html5.qq.com, 2026-04-16)](https://so.html5.qq.com/page/real/search_news?docid=70000021_15469e0c1b599852) | 论文发表于PRX Quantum
- **技术方案**:基于金刚石氮-空位(NV)中心固态量子传感器,利用电子-核自旋纠缠+优化的贝尔态测量方案,在单次测量序列中同步估计微波驱动场的幅值、失谐量与相位三个参数
- **关键突破**:即使在实际约束条件下,所有参数的灵敏度仍随探测时间呈线性标度(lScaling),突破经典多参数估计中参数间相互干扰的制约
- **作者**:Takuya Isogawa、Guoqing Wang(王国庆,港中文)、Boning Li为共同第一作者;Haidong Yuan、Paola Cappellaro为共同通讯作者
- **实验意义**:多参数同时估计是量子传感实用化的重要里程碑,单次测量获取多维度信息可大幅提升量子传感系统的信息获取效率

#### Qnami × Nature Communications - 超高效自旋电子学研究:BiFeO₃薄膜斯格明子量子成像,ProteusQ揭示多铁性材料新物理(2026-05)
- [ultraefficient-spintronics-closer-to-reality(Qnami, 2026-05)](https://qnami.ch/ultraefficient-spintronics-closer-to-reality/) | [Nature Communications (2025)](https://www.nature.com/articles/s41467-025-41392-x)
- **论文成果**:利用Qnami ProteusQ-LT低温NV显微镜对BiFeO₃(铋铁氧体)薄膜中的磁斯格明子(skyrmions)进行量子成像,揭示超高效自旋电子学材料新颖磁矩结构
- **技术价值**:BiFeO₃是多铁性材料典型代表,同时具有铁电性和铁磁性,在低功耗存储器件、传感器、逻辑器件中有重要应用;NV量子成像是目前唯一能无损、非接触式表征其纳米尺度磁结构的工具
- **市场动态**:同期Qnami宣布东亚市场扩张,Quantum Design Japan和Quantum Design Korea正式成为区域代理

#### 中科院传感技术国家重点实验室 - 微型光电一体化集成钻石量子磁传感器,探头20×15×1.5 mm³/灵敏度2.03 nT/√Hz(2026-05-13)
- [传感技术国家重点实验室(中国科学院), 2026-05-13](http://www.sim.cas.cn/kybm2016/cgjslhgjzdsys2016/kyjz2016/202307/t20230705_6805998.html)
- **技术**:武震宇研究员团队采用微纳加工技术,制备基于NV色心的微型光电一体化集成钻石量子磁传感器;探头尺寸20×15×1.5 mm³
- **灵敏度**:2.03 nT/√Hz;采用双频共振技术可同时进行磁场和温度场同步实时测量
- **工艺**:晶圆级微机电工艺平台,具批量化制备潜力;为建立高一致性、高灵敏度可穿戴传感器阵列提供可能性

#### 中国工程物理研究院 × 东北师范大学 - 相空间鞍点置乱增强量子计量,海森堡标度测量精度(Phys. Rev. Lett. 2026-05)
- [更稳更准!量子计量新方案拓宽应用范围(今日头条, 2026-05-11)](https://www.toutiao.com/article/7638569434441630251/) | [搜狐, 2026-05-11](https://so.html5.qq.com/page/real/search_news?docid=70000021_4816a01a76c00652)
- **技术方案**:量子置乱集成(QSI)方案,将自旋相干态置于相空间鞍点与分界线处,利用量子态的临界敏感性实现测量精度增强
- **突破**:测量精度达到海森堡标度,显著超越传统临界增强方案;无需精确逼近临界点即可在宽参数范围内保持超高精度

#### 量子传感市场格局:2025年18.8亿美元→2035年50.7亿美元,年均复合增长率10.42%(2026-03)
- [量子传感:工业感知的下一次跨越(量感局, 2026-03)](https://so.html5.qq.com/page/real/search_news?docid=70000021_08569a8149706452)
- **三大领域格局**:量子计算领跑;量子通信从实验室走向QKD网络;量子传感在国防领域已步入应用阶段,同时于工业检测领域也进入应用阶段
- **价值预测**:到2035年,量子技术对各行业所带来的"价值风险"预计达1.3万亿至2.7万亿美元规模;量子传感是量子技术商业化最快的方向

---

*本次更新(追加): Sandia Science Advances硅光子原子干涉仪里程碑 / Boeing 2026量子网络卫星 / 2026全球量子传感产业展望(135页) / MIT量子雷达探测地下物体 / 量子传感器粒子探测(Caltech费米实验室) / PRX Quantum固态多参量估计完整解析(2026-05-19傍晚)*

---

### 🆕 新增条目(2026-05-19傍晚 - 最新批)

#### Imperial College London - 量子传感Q&A深度解读:海军导航测试/惯性导航/量子脑成像/双缝时间版本/QuEST中心(2026-05-08)
- [Q&A: How will quantum science transform technology?(Imperial News, 2026-05-08)](https://www.imperial.ac.uk/news/246634/qa-how-will-quantum-science-transform) | [量子传感海军测试(Imperial, 2026)](https://www.imperial.ac.uk/news/245114/quantum-sensor-future-navigation-system-tested/) | [QuEST中心公告(Imperial, 2026)](https://www.imperial.ac.uk/news/245835/new-quantum-technologies-developed-imperial-initiative/)
- **量子传感测试平台**:英国皇家空军飞机量子导航测试成功后,延伸至皇家海军舰船,多平台兼容性持续验证;量子惯性传感器可在GPS拒止环境下提供高精度定位
- **量子传感已实用化的三大领域**:1超精密时钟(原子钟);2超灵敏重力仪(地下勘探);3超灵敏磁力计(脑成像+自主导航)
- **量子脑成像**:利用超灵敏磁力计测量大脑活动产生的磁场,用于医学诊断;Imperial已部署于医院和真实交通工具中
- **时间双缝实验**:成功重现"时间双缝实验",探索量子物理基本问题
- **QuEST中心启动**:量子工程、科学与技术中心(QuEST)正式启动,三大主题:量子材料、量子互联网、量子计算应用;Professor Ian Walmsley担任Director

#### Q-CTRL × IBM实现实用量子优势(3000倍加速)的同时,将量子误差抑制技术应用于量子传感(2026-05)
- [Q-CTRL Fire Opal](https://status.q-ctrl.com/) | [Google REPLIQA量子+AI生命科学1000万美元(2026-05-11)](https://blog.google/innovation-and-ai/models-and-research/quantum-computing/repliqa-quantum-computing-life-sciences/)
- **实用量子优势**:2026年5月6日,Q-CTRL与IBM宣布在IBM量子硬件上实现真实材料发现算法,量子2分钟 vs 经典HPC超100小时,3000倍加速
- **Fire Opal**:AI驱动量子误差抑制软件,将量子硬件与自主校准结合;已覆盖IBM量子计算全线产品
- **技术延伸**:Q-CTRL的量子误差抑制技术同样应用于量子传感(量子导航/惯性传感器),量子计算与量子传感共享底层误差抑制能力
- **Google REPLIQA**:Google出资1000万美元将量子+AI用于生命科学,量子传感器作为三大技术支柱之一

#### 博世(Bosch)×元素六(Element Six)成立量子传感合资公司 - 博世量子传感部门正式入场(2025→2026)
- [博世量子传感官网](https://www.bosch-quantumsensing.com/) | [网易订阅报道](https://www.163.com/dy/article/JVHTEK88051980LO.html)
- **合作模式**:全球工业巨头博世与戴比尔斯集团旗下元素六(Element Six)成立合资公司"Bosch Quantum Sensing"
- **战略意义**:元素六提供量子传感核心材料--人造金刚石(量子NV色心的理想衬底);博世提供工业制造能力、品牌与渠道

#### Quantum Flagship项目矩阵更新(2026-05):PoQus神经外科/C-QuENS NV纠缠/ACDQ_Q金刚石电路/PROMISE欧洲磁成像/QUANTIFY光子集成(2026持续)
- [Quantum Flagship官网](https://qt.eu/) | [Q-Expo 2026](https://qt.eu/) | [Quantum Academy](https://qt.eu/)
- **PoQus**:便携式神经外科量子传感器,用于术中实时神经活动监测,最接近临床医学的量子传感项目
- **C-QuENS**:量子纠缠NV色心传感,提升NV色心量子传感器的纠缠辅助测量能力
- **ACDQ_Q**:金刚石量子传感器先进电路,用于金刚石量子传感器的信号读取与控制
- **PROMISE**:欧洲磁成像系统原型,基于金刚石NV色心,无需传统真空系统、低温技术或磁屏蔽即可实现量子磁成像

---

### 🆕 新增条目(2026-05-19上午 - 第三批)

#### 香港大学 × 国内外合作 - 神经形态视觉传感器赋能宽场金刚石量子传感,突破帧率极限(Advanced Science, 2024-02)
- [HKU工程团队量子传感突破(港大新闻, 2024-02-19)](https://www.hku.hk/press/press-releases/detail/27099.html) | 论文:"Widefield Diamond Quantum Sensing with Neuromorphic Vision Sensors"(Advanced Science)
- **技术**:将神经形态视觉传感器与宽场金刚石NV量子传感结合,将荧光强度变化编码为稀疏尖峰(spikes),大幅压缩数据量并降低延迟
- **核心突破**:传统相机受限于帧率(通常不超过100 fps),港大团队利用神经形态传感器突破了这一瓶颈

#### 量子传感产业全景图:核心原理、硬件家族、全球战略竞争格局(2026-03)
- [量子传感:工业感知的下一次跨越(量感局, 2026-03)](https://so.html5.qq.com/page/real/search_news?docid=70000021_08569a8149706452)
- **三大核心技术**:量子叠加态(精度之源)、量子纠缠态(信噪比提升关键)、量子相干性(性能上限决定因素)
- **硬件家族**:原子钟(最成熟,10-18精度)、量子重力仪、量子磁力计、量子惯性传感器

---

### 🆕 新增条目(2026-05-19上午 - 第二批)

#### MIT/芝加哥大学/东京大学/港中文 - 固态量子传感器首次实现多参数同时估计(PRX Quantum, 2026-04)
- [MIT/芝加哥大学/东京大学/港中文联合研究(so.html5.qq.com, 2026-04-16)](https://so.html5.qq.com/page/real/search_news?docid=70000021_15469e0c1b599852) - 发表在PRX Quantum
- **技术**:基于金刚石NV中心固态量子传感器,实验实现量子多参数估计

#### 量子传感器市场2025-2045:半导体工艺成为SWaP-C破局关键,晶圆级制造+芯片级VCSEL(2025-04)
- [Quantum sensor market to grow to 2B by 2045(App Developer Magazine, 2025-04)](https://appdevelopermagazine.com/quantum-sensor-market-to-grow-to-2b-by-2045/) - 基于IDTechEx报告
- **核心挑战**:量子传感器商业化的最大瓶颈是SWaP-C(Size/Weight/Power/Cost);半导体制造工艺是解决该挑战的最有效途径

---

### 🆕 新增条目(2026-05-19上午)

#### arXiv:2407.00689 - 《从基础研究到商业应用的量子传感器展望》(2024-06, 96页综述)
- [A Perspective on Quantum Sensors from Basic Research to Commercial Applications(arXiv:2407.00689)](https://arxiv.org/abs/2407.00689) - Eun Oh, Maxwell D. Gregoire等12位作者,Sandia国家实验室主导
- **覆盖范围**:量子惯性传感器与重力传感器--原子干涉陀螺仪/加速度计/重力仪/重力梯度仪、NMR陀螺仪、原子与自旋缺陷磁力计、Rydberg电场传感器

#### Qnami - 全球量子传感领先企业,ProteusQ系列商业产品完整覆盖(2026)
- [Qnami官网](https://qnami.ch/) | [ultraefficient-spintronics论文(2026-05)](https://qnami.ch/ultraefficient-spintronics-closer-to-reality/)
- **ProteusQ-LT**:低温扫描NV显微镜专用,原子尺度捕获表面磁场,用于量子材料表征
- **ProteusQ**:量子波技术平台,解锁量子技术赋能更美好世界

#### IOP Commercialising Quantum Global 2025 - 联合国"国际量子科学与技术年"旗舰会议(2025)
- [Commercialising Quantum Global 2025(IOP)](https://www.iop.org/events/4th-annual-commercialising-quantum-global-2025)
- **核心议题**:真实量子应用与可测量投资回报;量子传感是三大核心方向之一

---

### 🆕 新增条目(2026-05-19清晨 - 第二批)

#### Sandia国家实验室 - 原子干涉仪量子惯性/重力传感器小型化突破,2025年获多项核心专利(2026)
- [Sandia量子传感页面](https://www.sandia.gov/quantum/atom-interferometry/) - Sandia National Laboratories
- **技术突破**:Sandia开发紧凑坚固的原子干涉仪传感器头,采用光栅磁光阱(MOT)实现动态环境下的可靠量子传感
- **关键进展**:多通道光子集成电路激光系统,采用硅光子单边带调制器;膜光子集成电路实现膜magneto-optical trap和光子原子阱集成平台
- **最新专利(2025年)**:紧凑光栅磁光阱传感器头(US12449256, 2025-10-11);紧凑原子干涉仪惯性导航传感器(US12424810, 2025-09-23)

#### 量子传感器市场2025-2045:半导体工艺成为蒸汽电池与VCSEL量产关键(2025)
- [Quantum sensor market to grow to 2B by 2045 (App Developer Magazine, 2025-04)](https://appdevelopermagazine.com/quantum-sensor-market-to-grow-to-2b-by-2045/) - 基于IDTechEx报告
- **蒸汽电池(vapor cells)**:晶圆级半导体制造工艺可批量生产高度一致的蒸汽电池
- **VCSEL**:可用晶圆级大规模制造;Microchip于2011年实现芯片级原子钟商业化(CSAC),为其他量子传感器提供量产模板

#### IDTechEx量子传感市场报告:2025年约19亿美元 → 2044年71亿美元(2025)
- [Quantum Sensors Market 2024-2044(IDTechEx)](https://www.idtechex.com/en/research-report/quantum-sensors-market-2024-2044/951)
- **覆盖范围**:原子钟、量子陀螺仪、量子磁场传感器、量子重力仪、量子图像传感器五类技术

#### 光泵磁力计(OPM)用于胎儿心磁图(fMCG)研究:Scientific Reports 2025发表(2026-02)
- [A customized bed based stand alone array of optically pumped magnetometers for fetal magnetocardiography measurements(Scientific Reports, 2025-02)](https://www.nature.com/articles/s41598-025-90846-y)
- **技术**:可穿戴式OPM阵列,用于检测胎儿心电活动产生的磁场;无需低温制冷,成本远低于SQUID系统

---

### 🆕 新增条目(2026-05-19凌晨)

#### "量子通信与量子计算机"国家重大专项2026-2030项目建议征集启动,量子精密测量列为四大重点领域之一(2026-05-18)
- [国家科技重大专项项目建议征集通知(科技部, 2026-05-11)](https://service.most.gov.cn/kjjh_tztg/?v=1732247723861) | [中国科学技术大学公告, 2026-05-17](http://ustc.edu.cn/info/1362/21757.htm)
- **四大领域**:量子通信、量子计算、**量子精密测量**、量子材料器件与设备

#### 第五届量子科仪节暨量子精密测量产业应用峰会--量子传感从"能测"迈向"能用"关键拐点(2026-05-15~17,合肥)
- [科学网, 2026-05-18](http://news.sciencenet.cn/htmlnews/2026/5/564839.shtm) | [大皖新闻, 2026-05-17](http://www.ahwang.cn/anhui/2026/0517/3004975.html) | [东方财富网, 2026-05-18](http://finance.eastmoney.com/a/202605183740233485.html)
- **核心判断**:国仪量子董事长贺羽指出"量子精密测量正处于从实验示范走向规模化的关键拐点"
- **八大产业场景**:电力电网、新能源、生命科学、地质勘测、半导体、石油、无损检测

#### 量子科技2026年一季度融资超32亿元,超越2025年全年总量,国仪量子科创板IPO过会(2026-05)
- [量子科技融资火爆!一季度总额突破32亿元(腾讯, 2026-05-18)](https://so.html5.qq.com/page/real/search_news?docid=70000021_4186a0a557691052)
- **IPO进展**:国仪量子首发上市申请5月11日获上交所审议通过,拟募资11.69亿元;本源量子启动科创板IPO辅导

#### Quantum Flagship Q-Expo 2026今日开幕(5/18-19) / Quantum Academy正式启动(5/11)
- [Quantum Flagship Q-Expo 2026公告](https://qt.eu/) - Meet the people shaping Europe's quantum future
- [Quantum Academy启动公告(2026-05-11)](https://qt.eu/) - 欧洲量子技术人才培训平台

---

### 🆕 新增条目(2026-05-14深夜)

#### MIT/芝加哥大学/东京大学/港中文 - 固态量子传感器首次实现多参数同时估计(PRX Quantum, 2026-04)
- [MIT/芝加哥大学/东京大学/港中文联合研究(so.html5.qq.com, 2026-04-16)](https://so.html5.qq.com/page/real/search_news?docid=70000021_15469e0c1b599852)

#### Quantum Singapore 2026论坛 - 量子汇聚:从硬件突破到工业应用(2026-02-04)
- [Quantum Singapore 2026论坛(new.qq.com, 2026-02-07)](https://new.qq.com/rain/a/20260207A067DT00)

#### 量子传感进入美国最核心武器系统长期采购目录--IonQ入选1510亿美元MDA SHIELD计划(2026-02)
- [IonQ入选1510亿美元MDA SHIELD计划(腾讯, 2026-02-25)](https://so.html5.qq.com/page/real/search_news?docid=70000021_690699ed88536652)

---

### 🆕 新增条目(2026-05-14晚)

#### Q-CTRL Fire Opal × IBM实现全球首个"实用量子优势",量子传感误差抑制技术延伸至量子计算(2026-05-06)
- [Q-CTRL系统状态页面](https://status.q-ctrl.com/) - Fire Opal持续运营中(100% uptime)
- **突破**:2026年5月6日,Q-CTRL与IBM宣布在IBM量子硬件上运行真实材料发现算法,实现3000倍加速

### Cerca Magnetics完成380万英镑A轮融资,量子脑扫描仪规模化迈入临床(2026-04-22)
- [Cerca Magnetics 380万英镑A轮融资(腾讯, 2026-04-22)](https://so.html5.qq.com/page/real/search_news?docid=70000021_87869e8aa9187252)
- **投资方**:吉尼斯风险投资(Guinness Ventures)领投,估值达3000万英镑;诺丁汉大学物理与天文学院衍生企业
- **技术**:可穿戴式量子脑成像扫描仪,基于光泵磁力计(OPM)实现脑磁图(MEG)

---

## 🗞️ 最新资讯(2026年5月19日更新)

### 量子精密测量产业化深水区:从"单点突破"迈向"规模复制"--第五届量子科仪节纪实(2026-05-15~17)
- [科学网, 2026-05-18](http://news.sciencenet.cn/htmlnews/2026/5/564839.shtm) | [大皖新闻, 2026-05-17](http://www.ahwang.cn/anhui/2026/0517/3004975.html) | [东方财富网, 2026-05-18](http://finance.eastmoney.com/a/202605183740233485.html)
- **规模**:中国科学技术大学、南京大学、中国计量科学研究院、国家电网、中石化、中冶集团、中国电科等高校院所与央企代表200余人参会
- **核心判断**:国仪量子董事长贺羽指出"量子精密测量正处于从实验示范走向规模化的关键拐点";许克标副总裁提出上一阶段主要解决了"能测"问题,当前进入"能用"的深水区
- **八大产业场景**:电力电网、新能源、生命科学、地质勘测、半导体、石油、无损检测,量子传感已形成场景矩阵

### "量子通信与量子计算机"国家重大专项2026-2030项目建议征集启动,量子精密测量列为四大重点领域之一(2026-05-18)
- [科技部, 2026-05-11](https://service.most.gov.cn/kjjh_tztg/?v=1732247723861) | [中国科学技术大学, 2026-05-17](http://ustc.edu.cn/info/1362/21757.htm)
- **四大领域**:量子通信、量子计算、**量子精密测量**、量子材料器件与设备

### 量子科技2026年一季度融资超32亿元,超越2025年全年总量,国仪量子科创板IPO过会(2026-05)
- [量子科技融资火爆!一季度总额突破32亿元(腾讯, 2026-05-18)](https://so.html5.qq.com/page/real/search_news?docid=70000021_4186a0a557691052)
- **IPO进展**:国仪量子首发上市申请5月11日获上交所审议通过,拟募资11.69亿元

### SandBoxAQ AQNav量子导航系统 - 全球首个商用AI+量子导航系统,数千飞行小时验证(2026-05-10)
- [SandboxAQ Announces AQNav(SandboxAQ, 2026-05-10)](https://www.sandboxaq.com/press/sandboxaq-announces-aqnav---worlds-first-commercial-real-time-navigation-system-powered-by-ai-and-quantum-to-address-gps-jamming)
- **技术**:地球磁场导航系统(geo-magnetic navigation),结合专有AI算法 + 量子传感器 + 地壳磁场特征
- **已验证**:在美国空军、Air客等合作伙伴的4种不同机型上累计飞行超过数千小时

### 中科大潘建伟团队"九章四号"光量子计算原型机发布,3050个光子量子态操控(2026-05-13)
- [我国成功研制量子计算原型机"九章四号"(腾讯, 2026-05-14)](https://so.html5.qq.com/page/real/search_news?docid=70000021_6286a0513e338752) | [中国科大新闻网, 2026-05-13](http://news.ustc.edu.cn_info/1056_94913.htm)
- **技术**:可编程量子计算原型机"九章四号",首次操纵和探测高达3050个光子的量子态,高斯玻色采样速度超当前最快超级计算机El Capitan达1054倍

### 武汉大学 × 精导所 - 冷原子重力仪动态测量研究进展(2024/2026持续推进)
- [Research Progress on Dynamic Measurement of Cold Atom Gravimeter(武汉大学, 2024)](http://ch.whu.edu.cn/en/article/doi/10.13203/j.whugis20240245)
- **技术**:冷原子干涉仪利用物质波干涉实现绝对重力测量,具有超高灵敏度和绝对测量优势
- **核心进展**:综述国内外冷原子重力仪动态测量技术进展;涵盖陆、海、空、天、空间多场景应用

### SBQuantum - 完成400万美元种子轮融资、新任CEO、美国扩张、2026年卫星发射(2026-04-17)
- [SBQuantum 400万美元种子轮融资公告(SBQuantum官网, 2026-04)](https://sbquantum.com/seed_sbq/) | [SBQuantum专访(2026-01-14)](https://so.html5.qq.com/page/real/search_news?docid=70000021_679696777d198552)
- **新任CEO**:Eric Giroux加盟担任CEO,在安全与国防领域拥有十余年经验

### Quantum Motion完成1.6亿美元C轮融资,刷新英国量子公司最大单笔VC纪录(2026-05-07)
- [Quantum Motion融资1.6亿美元(so.html5.qq.com, 2026-05-07)](https://so.html5.qq.com/page/real/search_news?docid=70000021_62369fc718291852)
- **技术核心**:采用标准硅CMOS工艺制造量子比特;2025年9月向NQCC交付全球首台300mm硅CMOS全栈量子计算机

### 伦敦帝国理工学院量子传感海上导航测试:皇家海军舰船首次试验(2026-05)
- [Q&A: How will quantum science transform technology?(Imperial News, 2026-05-08)](https://www.imperial.ac.uk/news/246634/qa-how-will-quantum-science-transform)
- **进展**:帝国理工学院在皇家海军舰船上首次测试量子传感器作为未来导航系统

### Q-CTRL × IBM - 实现全球首个"实用量子优势",材料发现提速3000倍(2026-05-06)
- [3000倍提速,Q-CTRL联手IBM打响「实用量子优势」第一枪(新浪, 2026-05-08)](https://k.sina.com.cn/article_5953189932_162d6782c0670489v8.html)
- **突破**:在IBM量子硬件上运行量子算法解决真实材料发现问题,实现高达3000倍绝对加速
- **技术核心**:Q-CTRL的AI驱动量子误差抑制软件(Fire Opal)

---

## 📰 研究与技术突破

### arXiv:2605.04136 - 多参数量子传感理论突破:一般哈密顿量函数估计的最优协议(2026-05-05)
- [arXiv:2605.04136](https://arxiv.org/abs/2605.04136) | 作者: Erfan Abbasgholinejad等
- **核心贡献**:推导任意函数形式多参数估计的终极量子极限,并提出达到该极限的估计协议;证明紧凑边界可优化为单参数量子Cramér-Rao边界
- **意义**:为量子系统中最优函数估计提供通用框架;多参量同时估计是量子传感从单参数精密测量走向实用化的核心挑战

### 中科大郭光灿院士PT对称增强量子传感器,灵敏度提升8.86倍(2026-01)
- [RFID世界网, 2026-01-15](https://www.rfidworld.com.cn/kw/news-39272)
- **技术**:宇称-时间(PT)对称系统增强型量子传感器

### 上海交大曾贵华教授团队 - 深度强化学习驱动智能量子传感(NPJ Quantum Information)
- [上海交通大学量子感知与信息处理研究所(QSIP)](https://qsip.sjtu.edu.cn/info/1116/1328.htm)
- **技术**:基于量子调控的量子深度强化学习协议,解决时变过程参数估计的精度饱和问题,达到量子速度极限QSL

### 阿德莱德大学光学原子钟首次海上测试成功(2026-04)
- [新型便携式原子钟海上测试成功(so.html5.qq.com, 2026-04-16)](https://so.html5.qq.com/page/real/search_news?docid=70000021_54769e02b5e44452)
- **技术**:基于激光冷却镱原子光学原子钟,在澳大利亚皇家海军舰船上连续运行数天

### 丹麦哥本哈根大学尼尔斯·玻尔研究所 - 混合量子系统突破标准量子极限(2025-07)
- [丹麦科学家突破量子传感极限(so.html5.qq.com, 2025-07-07)](https://so.html5.qq.com/page/real/search_news?docid=70000021_086686b2d2334852)
- **技术**:使用"压缩光"技术将量子噪声压缩至标准量子极限以下,引入"负质量"自旋系统

### 华南师范大学 × 德国乌尔姆大学 - 量子绝热演化传感新方案突破复杂环境探测难题(Phys. Rev. Lett.)
- [量子传感研究领域取得重要进展(生物汇, 2025-02)](https://wiki.antpedia.com/article-3191978-60)
- **技术**:基于测地线快速绝热演化的量子传感方案,克服传统动力学解耦脉冲序列在高次谐波和操控误差下的虚假信号问题

### 山西大学 × 武汉大学 × 中国计量科学研究院 - 《自然·传感》封面论文:转角石墨烯量子化朗德能级磁传感器(2026)
- [山西大学量子传感论文登《自然·传感》封面(腾讯新闻, 2026-02-10)](https://so.html5.qq.com/page/real/search_news?docid=70000021_943698ac42420452)
- **技术**:大角度转角双层石墨烯中首次发现电位移矢量与磁场比值量子化新机制(量子化"中国结"图案)

### 量子导航铁路测试重大突破:全球首次在运营列车真实环境中验证量子定位技术(2026-03-03)
- [量子导航技术在英国铁路取得重大突破(腾讯新闻, 2026-03)](https://so.html5.qq.com/page/real/search_news?docid=70000021_53669c4a73c75752)
- **进展**:量子传感定位系统搭载于英国GTR运营列车,在伦敦市中心与韦林花园市之间线路运行

---

## 🏢 公司与产品

### Q-CTRL - 量子传感软件入选《时代》2025年最佳发明,DARPA 3800万澳元合同(2026持续活跃)
- [Q-CTRL量子导航系统入选《时代》杂志2025年最佳发明榜(腾讯, 2025-10)](https://so.html5.qq.com/page/real/search_news?docid=70000021_18068e8e80b24152)
- **技术**:量子传感误差抑制算法,将量子硬件与自主校准软件结合
- **DARPA合同**:Robust Quantum Sensors(RoQS)项目两项合同,3800万澳元

### Qnami - 全球量子传感领先企业,ProteusQ系列商业产品完整覆盖(2026)
- [Qnami官网](https://qnami.ch/)
- **ProteusQ-LT**:低温扫描NV显微镜专用,原子尺度捕获表面磁场
- **ProteusQ**:量子波技术平台,解锁量子技术赋能更美好世界
- **Quantilever**:先锋级量子传感产品,基于NV色心技术,用于纳米级磁场成像
- **东亚市场扩张**:Quantum Design Japan和Quantum Design Korea正式成为代理

### SandboxAQ - 全球首个商用 AI+量子导航系统 AQNav 发布(2026-05-10)
- [SandboxAQ Announces AQNav(SandboxAQ, 2026-05-10)](https://www.sandboxaq.com/press/sandboxaq-announces-aqnav---worlds-first-commercial-real-time-navigation-system-powered-by-ai-and-quantum-to-address-gps-jamming)
- **已验证**:在美国空军、Airbus等合作伙伴的4种不同机型上累计飞行超过数千小时

### 国仪量子 - 科创板IPO过会并提交注册,募资11.69亿元(2026-05)
- [国仪量子科创板IPO过会(新浪财经, 2026-05-11)](https://finance.sina.com.cn/jjxw/2026-05-11/doc-inhxmzfz9483826.shtml)
- **产品线**:量子钻石单自旋谱仪、宽场NV显微镜、量子磁力仪、芯片原子钟

### Cerca Magnetics - 可穿戴量子脑成像扫描仪,380万英镑A轮融资(2026-04)
- [Cerca Magnetics官网](https://www.cerca-magnetics.com/) | [Quantum Insider报道, 2026-04-21](https://thequantuminsider.com/2026/04/21/cerca-magnetics-secures-38m-series-a-funding-scale-quantum-brain-scanner/)
- **技术**:基于光泵磁力计(OPM)实现脑磁图(MEG),室温下达到与SQUID相当的灵敏度
- **客户**:多伦多病童医院(SickKids)自闭症研究;英国国防部280万英镑项目

### SBQuantum - 加拿大NV量子磁力计初创,400万美元种子轮融资(2026-04)
- [SBQuantum完成超额认购400万美元种子轮(腾讯, 2026-04)](https://so.html5.qq.com/page/real/search_news?docid=70000021_46769e2132254052)
- **技术**:量子钻石磁力计,基于金刚石NV色心,测量地球磁场扰动构建精确定位模型

### Infleqtion - Q1财报发布中性原子量子传感,定义"量子频谱"新品类(2026-05-14)
- [Infleqtion Q1财报(NASDAQ: INFQ, 2026-05-14)](https://www.nasdaq.com/market-activity/stocks/infq)
- **Quantum Spectrum**:基于中性原子平台的射频传感架构,代表数十年来射频传感架构的首次根本性转变

### NVision Imaging Technologies - 5500万美元B轮融资,POLARIS量子增强MRI + PIQC量子计算平台(2026-05-14)
- [NVision从量子传感扩展到量子计算(腾讯新闻, 2026-05-14)](https://new.qq.com/rain/a/20260514A0821600)
- **POLARIS**:量子增强传感平台,将含糖成像剂的MRI信号提升数量级

### attocube - 低温NV扫描磁学显微镜attoNVM,1.8K/3μT/√Hz(2026-01)
- [限额免费测1.8K低温NV色心扫描磁学显微镜(new.qq.com, 2026-01-22)](https://new.qq.com/rain/a/20260122A024JB00)
- **参数**:工作温度2K-300K,灵敏度3μT/√Hz,纳米级空间分辨率

---

## 📊 市场数据

| 时间 | 市场数据 | 来源 |
|------|---------|------|
| 2025 | 18.8亿美元 | 量感局/K行业报告 |
| 2035 | 50.7亿美元(CAGR 10.42%) | 量感局 |
| 2044 | 71亿美元 | IDTechEx |
| 2030 | 30-50亿美元(量子传感) | 波士顿咨询 |

---

*QSensingZoo 维护中 | GitHub: wushanchi/QSensingZoo | 最后更新: 2026-05-21*