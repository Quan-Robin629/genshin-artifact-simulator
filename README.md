# Genshin Artifact Simulator
> 原神圣遗物毕业概率蒙特卡洛模拟工具

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

# 执行主模拟函数
expected_days = run_simulation(n_players=10000)
print(f"平均毕业天数: {expected_days:.2f} 天")

parts = [
    ("花", "Flat_HP", ["CR", "CD", "ATK_Percent", "ER"]),
    ("羽", "Flat_ATK", ["CR", "CD", "ATK_Percent", "ER"]),
    ("沙", "ATK_Percent", ["CR", "CD", "ER"]),
    ("杯", "ATK_Percent", ["CR", "CD", "ER"]),
    ("头", "CD", ["CR", "ATK_Percent", "ER"])
]

genshin-artifact-simulator/
├── Felice.py          # 主模拟代码
├── README.md           # 项目说明文档
└── requirements.txt    # 依赖清单


