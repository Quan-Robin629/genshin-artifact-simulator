# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 19:31:04 2026

@author: 86177
"""

import numpy as np
import matplotlib.pyplot as plt
import random

# --- 1. 动态权重表 (本代码所有信息基于米游社信息整理，如有则侵权删除) ---
# 定义不同主词条情况下，副词条出现的权重
# 每一列对应图片中不同的主词条背景
WEIGHT_MAP = {
    # 固定生命（花）
    "Flat_HP": {
        "Flat_HP": 0,          # 主词条同名，权重0
        "Flat_ATK": 157.9,     # 小公鸡
        "Flat_DEF": 157.9,     # 小防御
        "HP_Percent": 105.3,   # 大生命
        "DEF_Percent": 105.3,  # 大防御
        "ATK_Percent": 105.3,  # 大攻击
        "ER": 105.3,           # 充能
        "EM": 105.3,           # 精通
        "CR": 78.9,            # 暴击
        "CD": 78.9             # 暴伤
    },
    # 固定攻击（羽）
    "Flat_ATK": {
        "Flat_HP": 157.9,      # 小生命
        "Flat_ATK": 0,         # 主词条同名，权重0
        "Flat_DEF": 157.9,     # 小防御
        "HP_Percent": 105.3,   # 大生命
        "DEF_Percent": 105.3,  # 大防御
        "ATK_Percent": 105.3,  # 大攻击
        "ER": 105.3,           # 充能
        "EM": 105.3,           # 精通
        "CR": 78.9,            # 暴击
        "CD": 78.9             # 暴伤
    },
    # 大生命
    "HP_Percent": {
        "Flat_HP": 150,        # 小生命
        "Flat_ATK": 150,       # 小公鸡
        "Flat_DEF": 150,       # 小防御
        "HP_Percent": 0,       # 主词条同名，权重0
        "DEF_Percent": 100,    # 大防御
        "ATK_Percent": 100,    # 大攻击
        "ER": 100,             # 充能
        "EM": 100,             # 精通
        "CR": 75,              # 暴击
        "CD": 75               # 暴伤
    },
    # 大防御
    "DEF_Percent": {
        "Flat_HP": 150,        # 小生命
        "Flat_ATK": 150,       # 小公鸡
        "Flat_DEF": 150,       # 小防御
        "HP_Percent": 100,     # 大生命
        "DEF_Percent": 0,      # 主词条同名，权重0
        "ATK_Percent": 100,    # 大攻击
        "ER": 100,             # 充能
        "EM": 100,             # 精通
        "CR": 75,              # 暴击
        "CD": 75               # 暴伤
    },
    # 大攻击
    "ATK_Percent": {
        "Flat_HP": 150,        # 小生命
        "Flat_ATK": 150,       # 小公鸡
        "Flat_DEF": 150,       # 小防御
        "HP_Percent": 100,     # 大生命
        "DEF_Percent": 100,    # 大防御
        "ATK_Percent": 0,      # 主词条同名，权重0
        "ER": 100,             # 充能
        "EM": 100,             # 精通
        "CR": 75,              # 暴击
        "CD": 75               # 暴伤
    },
    # 充能
    "ER": {
        "Flat_HP": 150,        # 小生命
        "Flat_ATK": 150,       # 小公鸡
        "Flat_DEF": 150,       # 小防御
        "HP_Percent": 100,     # 大生命
        "DEF_Percent": 100,    # 大防御
        "ATK_Percent": 100,    # 大攻击
        "ER": 0,               # 主词条同名，权重0
        "EM": 100,             # 精通
        "CR": 75,              # 暴击
        "CD": 75               # 暴伤
    },
    # 精通
    "EM": {
        "Flat_HP": 150,        # 小生命
        "Flat_ATK": 150,       # 小公鸡
        "Flat_DEF": 150,       # 小防御
        "HP_Percent": 100,     # 大生命
        "DEF_Percent": 100,    # 大防御
        "ATK_Percent": 100,    # 大攻击
        "ER": 100,             # 充能
        "EM": 0,               # 主词条同名，权重0
        "CR": 75,              # 暴击
        "CD": 75               # 暴伤
    },
    # 属伤/物伤/治疗
    "DMG_Bonus": {
        "Flat_HP": 136.4,      # 小生命
        "Flat_ATK": 136.4,     # 小公鸡
        "Flat_DEF": 136.4,     # 小防御
        "HP_Percent": 90.9,    # 大生命
        "DEF_Percent": 90.9,   # 大防御
        "ATK_Percent": 90.9,   # 大攻击
        "ER": 90.9,            # 充能
        "EM": 90.9,            # 精通
        "CR": 68.2,            # 暴击
        "CD": 68.2             # 暴伤
    },
    # 暴击
    "CR": {
        "Flat_HP": 146.3,      # 小生命
        "Flat_ATK": 146.3,     # 小公鸡
        "Flat_DEF": 146.3,     # 小防御
        "HP_Percent": 97.6,    # 大生命
        "DEF_Percent": 97.6,   # 大防御
        "ATK_Percent": 97.6,   # 大攻击
        "ER": 97.6,            # 充能
        "EM": 97.6,            # 精通
        "CR": 0,               # 主词条同名，权重0
        "CD": 73.2             # 暴伤
    },
    # 暴伤
    "CD": {
        "Flat_HP": 146.3,      # 小生命
        "Flat_ATK": 146.3,     # 小公鸡
        "Flat_DEF": 146.3,     # 小防御
        "HP_Percent": 97.6,    # 大生命
        "DEF_Percent": 97.6,   # 大防御
        "ATK_Percent": 97.6,   # 大攻击
        "ER": 97.6,            # 充能
        "EM": 97.6,            # 精通
        "CR": 73.2,            # 暴击
        "CD": 0                # 主词条同名，权重0
    }
}

# --- 2. 核心功能函数 ---

def simulate_artifact(main_stat, valid_subs):
    """模拟一个圣遗物从掉落到20级是否达标"""
    # 判定起步词条数: 20% 概率 4词条 
    is_init_4 = random.random() < 0.20
    
    # 根据主词条获取对应的副词条池和权重
    pool_dict = WEIGHT_MAP.get(main_stat, WEIGHT_MAP["ATK_Percent"]) # 找不到就默认用大攻击池
    stats = list(pool_dict.keys())
    weights = list(pool_dict.values())
    
    # 初始生成 4 个副词条 (放回抽样)
    artifact_subs = random.choices(stats, weights=weights, k=4)
    
    # 强化机会: 4词条起步有5次, 3词条起步只有4次(因为1次被用来开第4个词条)
    upgrade_chances = 5 if is_init_4 else 4
    
    hits = 0
    # 每次强化, 都是从现有的 4 个词条中等概率(25%)选一个
    for _ in range(upgrade_chances):
        rolled = random.choice(artifact_subs)
        if rolled in valid_subs:
            hits += 1
    return hits >= 3

# --- 3. 模拟一万名玩家 ---

def run_simulation(n_players=10000):
    # 菲林斯的需求配置: (主词条, 主词条掉率, 有效副词条)
    TARGETS = [
        ("Flat_HP", 1.0, ["CR", "CD", "ATK_Percent", "ER"]),     # 花
        ("Flat_ATK", 1.0, ["CR", "CD", "ATK_Percent", "ER"]),    # 羽
        ("ATK_Percent", 0.2666, ["CR", "CD", "ER"]),            # 攻击沙
        ("ATK_Percent", 0.1915, ["CR", "CD", "ER"]),            # 攻击杯
        ("CD", 0.10, ["CR", "ATK_Percent", "ER"])               # 爆伤头
    ]
    
    all_days = []
    for _ in range(n_players):
        days = 0
        collected = [False] * 5
        while not all(collected):
            days += 1
            # 每天 180 体力, 产出 10.5 个金色圣遗物
            for _ in range(11): # 向上取整
                is_set_a = random.random() < 0.5  # 50% 概率是目标套装
                part_idx = random.randint(0, 4)   # 随机掉落 5 个部位之一
                main_stat, main_prob, valid_subs = TARGETS[part_idx]
                
                # 主词条必须先对 (比如爆伤头掉率 10%)
                if random.random() < main_prob:
                    # 散件逻辑: 只有当我只差这最后一个部位时, 散件才管用
                    is_valid_drop = is_set_a or (sum(collected) == 4 and not collected[part_idx])
                    if is_valid_drop:
                        if simulate_artifact(main_stat, valid_subs):
                            collected[part_idx] = True
        all_days.append(days)
    return all_days

# --- 4. 生成直方图 ---

results = run_simulation(10000)
plt.hist(results, bins=50, color='blue', alpha=0.7, edgecolor='black')
plt.title("Expected Days for Felice (Medium Strength)")
plt.xlabel("Days")
plt.ylabel("Number of Players")
plt.axvline(np.mean(results), color='red', label=f"Average: {np.mean(results):.1f} Days")
plt.legend()
plt.show()

print(f"平均毕业时间: {np.mean(results):.2f} 天")