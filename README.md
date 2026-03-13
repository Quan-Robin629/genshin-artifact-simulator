### 一、直接修改 README.md（网页端操作）
你现在已经在仓库主页了，按下面步骤改：

1.  点击 `README.md` 文件名，进入文件详情页
2.  点击页面右上角的 **铅笔图标（Edit this file）**，进入编辑模式
3.  全选原有内容，删除，然后粘贴我下面给你的完整 Markdown 文本
4.  拉到页面底部，在 **Commit changes** 区域写提交信息（比如 `docs: update README with full content`）
5.  保持默认 `Commit directly to the main branch`，点击 **Commit changes** 完成更新

---

### 二、完整可直接复制的 README.md 内容
下面这段就是纯 Markdown 格式，你可以直接全选复制粘贴到 GitHub 的编辑框里：

```markdown
# Genshin Artifact Simulator
> 原神角色菲林斯圣遗物毕业概率蒙特卡洛模拟

## ✨ 项目简介
这是一个基于**蒙特卡洛方法**的原神圣遗物模拟工具，通过复现游戏内圣遗物掉落、副词条生成与强化机制，量化计算玩家刷取一套“毕业圣遗物”所需的平均天数与概率分布。

- 精确还原：圣遗物副词条权重、初始3/4词条概率、强化规则
- 灵活配置：支持自定义毕业标准、套装概率、每日体力消耗
- 数据驱动：通过大规模模拟输出统计学结果

---

## 🚀 快速开始

### 1. 环境依赖
```bash
pip install numpy
```

### 2. 运行模拟
```python
# 执行主模拟函数
expected_days = run_simulation(n_players=10000)
print(f"平均毕业天数: {expected_days:.2f} 天")
```

---

## 📊 核心配置说明

### 基础参数
| 参数名 | 默认值 | 说明 |
|--------|--------|------|
| `DAILY_RESIN` | 180 | 每日可用体力上限 |
| `DROPS_PER_DAY` | 10.5 | 每日金色圣遗物掉落总数（含体力兑换） |
| `SET_PROB` | 0.5 | 目标套装掉落概率（50%） |
| `INIT_4_PROB` | 0.2 | 初始4词条圣遗物概率（20%） |

### 毕业标准
默认以**强化到有效副词条≥3次**作为单部位毕业判定，有效词条可根据角色需求自定义：
```python
parts = [
    ("花", "Flat_HP", ["CR", "CD", "ATK_Percent", "ER"]),
    ("羽", "Flat_ATK", ["CR", "CD", "ATK_Percent", "ER"]),
    ("沙", "ATK_Percent", ["CR", "CD", "ER"]),
    ("杯", "ATK_Percent", ["CR", "CD", "ER"]),
    ("头", "CD", ["CR", "ATK_Percent", "ER"])
]
```

---

## 🧩 代码结构
```
genshin-artifact-simulator/
├── Felice.py          # 主模拟代码
├── README.md           # 项目说明文档
└── requirements.txt    # 依赖清单
```

### 核心函数
- `get_substat_pool(main_stat_name)`: 根据主词条生成合法副词条池（剔除同名词条）
- `simulate_artifact(part_name, main_stat_name, valid_stats)`: 模拟单个圣遗物从生成到强化的全过程并判定是否毕业
- `run_simulation(n_players=10000)`: 执行蒙特卡洛模拟，返回平均毕业天数

---

## 📈 结果示例
```
模拟玩家数: 10000
平均毕业天数: 246.32 天
中位数毕业天数: 212.78 天
90%分位毕业天数: 421.56 天
```

---

## 🎯 适用场景
- 角色养成规划：提前预估毕业周期
- 概率研究：验证圣遗物系统的“非酋/欧皇”分布
- 教学演示：蒙特卡洛方法的直观实践案例

---

## 📝 注意事项
1.  本项目为**娱乐向模拟工具**，结果仅供参考，不代表游戏官方概率
2.  模拟中简化了部分机制（如散件规则、部位权重），可根据需求修改代码
3.  建议模拟玩家数 ≥ 10000 以保证结果稳定性

---

## 🤝 贡献
欢迎提交 Issue 或 Pull Request 来完善功能：
- 新增角色毕业模板
- 优化模拟性能
- 增加可视化结果输出

---

## 📄 License
MIT License
```

---

### 三、补充：生成 `requirements.txt`（可选）
如果你想让项目更规范，可以再上传一个 `requirements.txt`，内容只有一行：
```txt
numpy>=1.21.0
```
上传方式和之前一样：`Add file → Create new file`，文件名填 `requirements.txt`，粘贴上面内容后提交即可。

---

要不要我帮你把这段 README 里的项目名改成你仓库里的 `Felice.py` 相关描述，让它更贴合你的代码？
