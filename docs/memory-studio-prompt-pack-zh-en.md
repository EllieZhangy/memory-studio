# Memory Studio｜4套照片海报提示词包

**中英双语 · 可复制 Prompt · 适合小红书收藏与 GitHub 分享**

一张照片，可以变成手工拼贴杂志、照片插画明信片、回忆贴纸卡或极简编辑海报。本资源复用 Memory Studio 已有的4套英文视觉模板，并补充中文对照、使用步骤和可选调整语句。

## 先分清：Prompt 模板与 Agent Skill

| 类型 | 本资源提供什么 | 怎么使用 |
| --- | --- | --- |
| 普通 Prompt 模板 | 以下4段完整英文提示词及中文说明 | 在支持上传参考照片并生成/编辑图像的工具中，上传照片后粘贴使用；无需安装仓库 |
| Agent Skill | 本资源不是可安装的 Agent Skill | Agent Skill 通常需要目标代理工具支持的技能目录、说明文件（如 SKILL.md）、安装方式及可能的脚本依赖；不能仅凭目录叫 skills 就称为可安装技能 |
| Memory Studio 应用 | 仓库中的照片到海报工作流程 | 使用应用需要本地部署及图像 API；截至本次检查未提供开放的多人在线生成服务 |

英文 Prompt 保留仓库原文，末尾新增两句通用说明：竖版3:4构图、默认不生成文字。中文是对应的阅读与使用版本。可选参数是本资源补充的自然语言修改指令，不是应用新增的设置项，也不是模型 API 参数。

## 3步开始

1. 选择支持参考图输入的图像工具，上传一张主体清晰的照片。
2. 复制一套完整英文 Prompt。工具有画幅选项时，另设为 **3:4竖版**。
3. 初次使用默认版本；需要变化时，从对应参数表中选择1–2句加到 Prompt 后。涉及比例或数量时，替换原规则，避免互相冲突。

想使用中文也可复制“中文 Prompt 对照”，再加上：“使用3:4竖版构图，把关键内容放在画面内，四周留出安全边距。不要生成可见文字。”

**结果边界：**不同模型、版本与随机生成会产生不同布局、画风和文字效果；本包没有逐模型实测，也不保证与示例一致。提示词只能请求3:4构图，不能保证精确像素；应用的1080 × 1440导出由后续裁切和缩放完成。摄影区域会由模型重绘，并非逐像素贴回原图，人物面貌和细节可能变化；需要严格保留原照片时，可生成版式后用 Canva/PPT 替换摄影区域。发布前检查人物、物件数量、文字及裁切。

## 仓库已有示例

![Memory Studio 仓库已有旅行回忆贴纸卡海报](https://raw.githubusercontent.com/EllieZhangy/memory-studio/39bc72760d741d3588ffc1713fc53713731fb359/outputs/my-favorite-travel-buddy-card-3x4.png)

来源：[查看已有 PNG](https://github.com/EllieZhangy/memory-studio/blob/39bc72760d741d3588ffc1713fc53713731fb359/outputs/my-favorite-travel-buddy-card-3x4.png)。README 将其标注为旅行回忆贴纸卡。仓库另有 app/static/example.png，两者 blob SHA 相同，是同一张图片。本次没有调用付费图像 API，也没有新增四风格对比实测图。其余三套的效果说明来自模板设计方向，不代表新增生成结果。

## 01｜Collage Zine · 手工拼贴杂志

**效果说明：**把一张照片整理成带有纸张层次的旅行杂志页，保留照片主体，再加入同场景插画、局部裁切与纸片。

**适合的输入照片：**旅行街景、咖啡馆、野餐、海边；画面有主体，也有可提取的小细节。

### 完整英文 Prompt｜复制此段

```text
Create a refined collected-scenes editorial zine poster. Keep a recognizable photographic panel from the supplied photo and surround it with simplified illustrated details from the same scene, layered paper fragments and small related scene crops. Quiet handmade collage, airy asymmetric grid, cream paper, muted source-photo colors, subtle paper grain, no glossy or 3D effects. Do not invent destinations or dates.

Use a portrait 3:4 composition. Keep essential content inside the frame with safe margins.
Do not generate any visible text.
```

### 中文 Prompt 对照

制作一张精致的场景收集式编辑杂志海报。保留上传照片中可辨认的摄影区域，在周围加入同一场景的简化插画细节、叠放纸片和相关场景的小幅裁切。采用安静的手工拼贴感、疏朗的不对称网格、奶油色纸张、原照片中的低饱和配色与轻微纸纹。不要光泽或3D效果，不要虚构目的地或日期。 使用3:4竖版构图，把关键内容放在画面内，四周留出安全边距。不要生成可见文字。

### 中文使用指引

上传照片后粘贴英文 Prompt。让照片成为视觉中心；想要更清爽，可减少纸片和局部裁切。 默认关闭生成文字；想加标题，可参照下方通用调整方式。摄影区域的“保留”是视觉指令，不保证像素或身份特征完全不变。

### 可调整的风格参数

| 参数 | 可复制的英文调整句 | 用法 |
| --- | --- | --- |
| 拼贴密度 / Density | Use only 3 layered paper fragments and 2 small scene crops. | 减少元素，让主体更突出 |
| 纸纹 / Texture | Use very subtle paper grain. | 减弱纸张颗粒 |
| 配色 / Palette | Use muted sage green and warm cream, guided by the source photo. | 适合原图含绿植、自然环境时 |

原模板 ID：`scenes-gathered-zine-v1-3`。

## 02｜Illustrated Postcard · 照片 × 插画明信片

**效果说明：**上半张保留摄影感，下半张将同一场景转成扁平手绘插画，像一张可收藏的明信片。

**适合的输入照片：**单一场景、主体清晰的旅行照、建筑照、人物与宠物合照；避免密集人群。

### 完整英文 Prompt｜复制此段

```text
Create a refined scrapbook postcard: photographic source scene in the top half, a simplified flat handmade illustration of that same scene in the lower half, off-white paper, muted colors from the original, generous margins and restrained editorial typography. Preserve identities and scene context in the photographic panel. No 3D, glossy rendering, or invented places and dates.

Use a portrait 3:4 composition. Keep essential content inside the frame with safe margins.
Do not generate any visible text.
```

### 中文 Prompt 对照

制作一张精致的剪贴簿明信片：上半部为原始照片场景，下半部为同一场景的简化扁平手工插画。使用米白纸张、原图中的低饱和颜色、宽裕边距和克制的编辑字体排版。摄影区域保留人物身份特征和场景语境。不要3D或光泽渲染，不要虚构地点和日期。 使用3:4竖版构图，把关键内容放在画面内，四周留出安全边距。不要生成可见文字。

### 中文使用指引

上传照片后粘贴英文 Prompt。先使用默认上下各半的布局；如果需要改比例，明确用新比例替换默认布局。 默认关闭生成文字；想加标题，可参照下方通用调整方式。摄影区域的“保留”是视觉指令，不保证像素或身份特征完全不变。

### 可调整的风格参数

| 参数 | 可复制的英文调整句 | 用法 |
| --- | --- | --- |
| 区域比例 / Split | Replace the half-and-half layout: use the top 60% for the photographic scene and the bottom 40% for the illustration. | 强调照片 |
| 插画细节 / Detail | Use broad flat color shapes and minimal linework in the lower illustration. | 让插画更简洁 |
| 边距 / Margin | Use wide postcard margins. | 增加明信片感 |

原模板 ID：`photo-to-zine-postcard`。

## 03｜Memory Sticker Card · 旅行回忆贴纸卡

**效果说明：**上方是摄影区域，下方左边是场景插画、右边是独立白边纸贴纸，像一页旅行收藏卡。

**适合的输入照片：**人物与一只狗的合照最贴合原模板特例；也可用含5–7个清晰可见物件的旅行或生活照片。

### 完整英文 Prompt｜复制此段

```text
Create a calm nostalgic travel-memory scrapbook sticker card on cream paper. Keep the recognizable source photograph in the top half. In the lower half place a soft flat simplified handmade illustration of the same scene on the left and separate die-cut paper stickers with soft white borders on the right. If the photo features a person and a dog, use exactly two stickers: the person and the dog. Otherwise choose 5–7 iconic motifs visible in the photo. Muted source-photo colors, generous negative space, clean cute refined zine layout, matte flat illustration, not 3D, not glossy, not hyper-detailed. Do not invent places or dates.

Use a portrait 3:4 composition. Keep essential content inside the frame with safe margins.
Do not generate any visible text.
```

### 中文 Prompt 对照

在奶油色纸张上制作一张安静、怀旧的旅行回忆剪贴簿贴纸卡。上半部保留可辨认的原照片。下半部左侧放置同场景的柔和、扁平、简化手工插画，右侧放置带柔和白边的独立模切纸贴纸。如果照片包含一个人和一只狗，恰好使用两张贴纸：人物和狗。否则，从照片中选择5–7个有代表性的可见元素。使用原图中的低饱和配色、充足留白和干净可爱且精致的杂志布局。采用哑光扁平插画，不要3D、光泽或过度细节，不要虚构地点或日期。 使用3:4竖版构图，把关键内容放在画面内，四周留出安全边距。不要生成可见文字。

### 中文使用指引

上传照片后粘贴英文 Prompt。先核对照片里是否真的有足够贴纸元素。人和狗的照片保留“两张贴纸”规则；其他照片若不足5个清晰物件，替换默认数量，避免凭空添加。 默认关闭生成文字；想加标题，可参照下方通用调整方式。摄影区域的“保留”是视觉指令，不保证像素或身份特征完全不变。

### 可调整的风格参数

| 参数 | 可复制的英文调整句 | 用法 |
| --- | --- | --- |
| 贴纸数量 / Count | For a photo without a person-and-dog pair, replace the 5–7 motif rule with exactly 3 separate stickers based only on visible objects. | 仅在非人狗组合照片中替换数量规则 |
| 贴纸边框 / Border | Use thin soft white borders around each sticker. | 细白边更轻盈 |
| 元素间距 / Spacing | Keep each sticker separate with generous spacing; avoid overlapping stickers. | 让贴纸更易辨认 |

原模板 ID：`travel-memory-sticker-card`。

## 04｜Minimal Editorial Poster · 极简编辑海报

**效果说明：**一张主照片、大片留白、少量扁平插画点缀，适合干净安静的生活记录。

**适合的输入照片：**主体明确、背景简洁的建筑、海景、人物、静物；避免多主体拥挤画面。

### 完整英文 Prompt｜复制此段

```text
Create a minimalist editorial zine poster with one dominant recognizable photographic scene, generous off-white negative space, a restrained source-photo palette, an elegant asymmetric grid and small understated flat illustrated accents. Clean artistic print layout, sparse tasteful typography, no busy collage, no 3D or glossy elements, no invented dates or destinations.

Use a portrait 3:4 composition. Keep essential content inside the frame with safe margins.
Do not generate any visible text.
```

### 中文 Prompt 对照

制作一张极简编辑杂志海报，以一个占主导地位且可辨认的摄影场景为核心，使用大量米白留白、克制的原图配色、优雅的不对称网格和少量低调的扁平插画点缀。采用干净的艺术印刷排版与稀疏有品位的字体。不要繁忙拼贴、3D或光泽元素，不要虚构日期或目的地。 使用3:4竖版构图，把关键内容放在画面内，四周留出安全边距。不要生成可见文字。

### 中文使用指引

上传照片后粘贴英文 Prompt。用主照片和留白建立层次；若画面变得拥挤，减少插画点缀并关闭生成文字。 默认关闭生成文字；想加标题，可参照下方通用调整方式。摄影区域的“保留”是视觉指令，不保证像素或身份特征完全不变。

### 可调整的风格参数

| 参数 | 可复制的英文调整句 | 用法 |
| --- | --- | --- |
| 留白 / Whitespace | Reserve approximately 40% of the poster for off-white negative space. | 更安静、适合后期加标题 |
| 点缀数量 / Accents | Use at most 2 small flat illustrated accents. | 减少装饰 |
| 照片位置 / Placement | Place the dominant photographic panel slightly above center on an asymmetric grid. | 调整视觉重心 |

原模板 ID：`gc-minimal-zine-poster-v0-3`。

## 通用调整：标题、配色与纠偏

| 需求 | 修改方式 / English instruction |
| --- | --- |
| 添加指定标题 | 删除末尾“Do not generate any visible text.”，替换为：Add only the exact title "[YOUR TITLE]" in small restrained editorial typography. Do not add any other text. 将占位符换成自己的标题；不填时保留无文字版本 |
| 完全不生成字 | 保留：Do not generate any visible text. 标题可后期手动排版 |
| 指定颜色 | 将原模板的 source-photo colors/palette 配色描述替换为：Use a restrained palette of [COLOR 1], [COLOR 2], and warm off-white. 选择与原图协调的颜色 |
| 主体被改太多 | 加入：Keep the main subject recognizable; do not change clothing, add people, or add objects absent from the reference photo. 这是纠偏请求，仍需检查结果 |
| 出现3D或亮面 | 加入：Use matte paper and flat illustration only; remove glossy surfaces and volumetric 3D rendering. |
| 装饰太多 | 加入：Simplify the layout and increase negative space. |

一次改1–2项更便于判断效果。参考图中的日期、地点或文字可能被误读；这些模板默认不虚构地点和日期，需要出现真实信息时请自行核对后提供。上传个人照片前确认所用工具的数据处理政策及照片使用授权。

## 小红书引用方式

可用一句话概括玩法：“上传一张照片，选一种海报风格，再用可复制提示词把日常整理成一张回忆卡。”

建议图文顺序：已有成品示例 → 四风格效果速览 → 上传与复制步骤 → 可调参数 → 完整提示词资源入口。引用示例时标注“Memory Studio 仓库已有示例”；未生成的其他风格用文字描述，不标作实测对比。分享时称“4套照片海报 Prompt 模板”，避免称“下载即用的 Agent Skill”。

## 来源与版本

- 整理日期：2026-10-14。
- [Memory Studio 仓库](https://github.com/EllieZhangy/memory-studio)。
- [英文原始模板 styles.json](https://github.com/EllieZhangy/memory-studio/blob/39bc72760d741d3588ffc1713fc53713731fb359/skills/styles.json)，blob SHA：a088cbab612afbdb0f2caf606f1708b88c260dee。
- [README：应用流程、部署与限制](https://github.com/EllieZhangy/memory-studio/blob/39bc72760d741d3588ffc1713fc53713731fb359/README.md)。
- 基于提交 `39bc72760d741d3588ffc1713fc53713731fb359`；不修改原模板或应用功能。

English note: This is a bilingual, copy-and-paste prompt pack adapted from Memory Studio's existing style templates. It is not an installable Agent Skill. Use a reference-image-capable image tool; results vary across models. The linked poster is an existing repository example, not a new test of all four prompts.
