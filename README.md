# AIDING Academic Style

**面向中文论文、科研项目书、学术报告与学术润色的表达风格技能。**

从AIDING团队中文学术语料中提炼解释展开、对象承接、条件分析和有依据的判断，帮助模型在不同研究主题中保持连贯、正式而自然的行文方式。支持起草、重写、续写、精简和轻度润色。

它是一组可复用的写作指令与参考材料，无须模型微调，也不需要运行服务器或配置额外API密钥。

## 它怎样改变文字

围绕同一研究对象逐步说明：对象有什么特性，为什么需要某项处理，处理得到什么，下一步如何使用所得结果。保留技术术语与事实边界，不依靠堆叠“针对、为此、从而”制造风格。

以下为构造的学术进展示例，并非实际研究结果：

> 目前已完成均匀采样与边界加密采样两组计算，后者在边界附近得到的误差较小。不过，两组计算采用的样本总量不同，现有结果尚不能区分误差改善来自样本数量增加，还是边界样本分布的调整。下一步将在固定样本总量的条件下，比较不同边界样本比例的计算结果，以明确样本分布对边界预测误差的影响。

更多内容：[12组学术试写](skills/aiding-academic-style/references/academic-examples.md) · [6组句段拆解](skills/aiding-academic-style/references/paragraph-anatomy.md) · [完整行文方式](skills/aiding-academic-style/references/style-fingerprint.md)

## 安装到 Codex

### 方式一：让 Codex 安装

向 Codex 发送：

```text
请使用 $skill-installer，从下面的 GitHub 地址安装 aiding-academic-style：
https://github.com/mathliuyang/aiding-academic-style/tree/main/skills/aiding-academic-style
```

安装后在下一次对话中调用；若技能未出现，重启 Codex。GitHub 仓库安装与本地技能发现方式见 [OpenAI 官方技能文档](https://learn.chatgpt.com/docs/build-skills)。

### 方式二：下载并复制

从 [Releases](https://github.com/mathliuyang/aiding-academic-style/releases) 下载技能 ZIP，解压后将完整的 `aiding-academic-style` 文件夹放入个人技能目录。按照当前官方文档，可使用：

- Windows：`%USERPROFILE%/.agents/skills/aiding-academic-style/`
- macOS / Linux：`~/.agents/skills/aiding-academic-style/`
- 仅当前项目：`<项目根目录>/.agents/skills/aiding-academic-style/`

目录下应直接存在 `SKILL.md`、`agents/` 和 `references/`。若你的客户端或内置安装器使用 `$CODEX_HOME/skills`，沿用其实际安装目录即可；不要在多个技能目录重复安装同名副本。

ZIP 包同时包含使用说明与MIT许可。请保留许可文件。已经安装同名技能时，先备份个人修改，再更新。

## 使用

```text
用 AIDING 风格润色下面这段论文。保留数值、公式、引用与结论力度，只做轻度润色。
```

```text
使用 $aiding-academic-style，按 AIDING 风格重写这段项目研究内容。
可以调整句序，让问题、研究动作和预期认识衔接起来，不新增研究任务。
```

```text
按 AIDING 风格写一段组会进展报告，区分已完成工作、当前观察和下一步计划。
```

```text
把下面三个算例说明精简成一段，共同设置只写一次，保留各自差异。
```

论文、项目书和报告自动按上下文适配。需要校准时，可要求给出同事实的两种解释密度，再指出哪一句更接近自己的习惯。技能不会自动改写研究事实或持久保存每位使用者的个人偏好。

## 仓库内容

```text
skills/aiding-academic-style/
  SKILL.md                  技能入口与工作方式
  agents/openai.yaml        Codex 界面元数据
  references/
    style-fingerprint.md    通用学术行文方式
    papers.md               论文各章节适配
    proposals.md            科研项目书适配
    academic-reports.md     学术报告与进展
    academic-examples.md    12组构造示例
    paragraph-anatomy.md    6组构造例拆解
    calibration.md         使用者交互校准
    sources.md              来源与公开范围
    evaluation.md          效果检查与维护
```

## 来源与适用边界

这是对AIDING团队及刘东共同署名中文语料的表达倾向进行归纳，不能将每一句归因为某位作者个人执笔，也不代表作者个人认证或机构官方发布。英文任务可参考论证组织，但本项目未建立团队英文措辞模型。

公开版保留提炼规则和原创构造例；原始论文与项目PDF、原文摘录、内部审读记录、个人对话和本机路径不随仓库分发。构造例中的数字和研究结论不能转作使用者的真实成果。详情见 [来源说明](skills/aiding-academic-style/references/sources.md)。

## 维护与反馈

欢迎通过 Issue 提供可公开分享的最小改写示例，注明用途、改写幅度以及希望保留的表达。请勿上传未获授权的论文全文、项目材料、个人信息或凭据。

维护者可运行：

```bash
python scripts/validate.py
```

检查范围是发布文件、技能结构和内部链接；通过检查不等同于科研事实核验或作者风格盲测。技能本身使用时不需要 Python。

## License

本仓库原创技能指令、说明、构造示例与辅助代码以 [MIT License](LICENSE) 发布。许可不覆盖未随仓库分发的原始论文、项目材料或其他第三方内容；相关名称不表示官方背书。
