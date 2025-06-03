import xml.etree.ElementTree as ET
import re
import html
import pandas as pd

# Списък с възли
nodes = [
    {"id": "AU", "label": "q1", "parent": None},           # корен
    {"id": "T_q2", "label": "q2", "parent": "AU"},
    {"id": "SBS_q3", "label": "q3", "parent": "T_q2"},
    {"id": "SBS_q4", "label": "q4", "parent": "T_q2"},
    {"id": "SBS_q5", "label": "q5", "parent": "T_q2"},
    {"id": "D_q6", "label": "q6", "parent": "SBS_q3"},
    {"id": "RU_q7", "label": "q7", "parent": "D_q6"},
    {"id": "RU_q8", "label": "q8", "parent": "D_q6"},
    {"id": "t_t1", "label": "t1", "parent": "RU_q7"},
    {"id": "t_t2", "label": "t2", "parent": "RU_q7"},
    {"id": "t_t3", "label": "t3", "parent": "RU_q8"},
    {"id": "t_t4", "label": "t4", "parent": "RU_q8"},
    {"id": "RU_q9", "label": "q9", "parent": "SBS_q3"},
    {"id": "D_q10", "label": "q10", "parent": "RU_q9"},
    {"id": "t_t5", "label": "t5", "parent": "D_q10"},
    {"id": "t_t6", "label": "t6", "parent": "D_q10"},
    {"id": "D_q11", "label": "q11", "parent": "SBS_q4"},
    {"id": "RU_q12", "label": "q12", "parent": "D_q11"},
    {"id": "RU_q13", "label": "q13", "parent": "D_q11"},
    {"id": "t_t7", "label": "t7", "parent": "RU_q12"},
    {"id": "t_t8", "label": "t8", "parent": "RU_q12"},
    {"id": "t_t9", "label": "t9", "parent": "RU_q13"},
    {"id": "t_t10", "label": "t10", "parent": "RU_q13"},
    {"id": "RU_q14", "label": "q14", "parent": "SBS_q4"},
    {"id": "D_q15", "label": "q15", "parent": "RU_q14"},
    {"id": "t_t11", "label": "t11", "parent": "D_q15"},
    {"id": "t_t12", "label": "t12", "parent": "D_q15"},
    {"id": "D_q16", "label": "q16", "parent": "SBS_q5"},
    {"id": "RU_q17", "label": "q17", "parent": "D_q16"},
    {"id": "RU_q18", "label": "q18", "parent": "D_q16"},
    {"id": "t_t13", "label": "t13", "parent": "RU_q17"},
    {"id": "t_t14", "label": "t14", "parent": "RU_q17"},
    {"id": "t_t15", "label": "t15", "parent": "RU_q18"},
    {"id": "t_t16", "label": "t16", "parent": "RU_q18"},
    {"id": "RU_q19", "label": "q19", "parent": "SBS_q5"},
    {"id": "D_q20", "label": "q20", "parent": "RU_q19"},
    {"id": "t_t17", "label": "t17", "parent": "D_q20"},
    {"id": "t_t18", "label": "t18", "parent": "D_q20"},

    {"id": "SBS_q21", "label": "q21", "parent": "AU"},
    {"id": "T_q22", "label": "q22", "parent": "SBS_q21"},
    {"id": "D_q23", "label": "q23", "parent": "T_q22"},
    {"id": "D_q26", "label": "q26", "parent": "T_q22"},
    {"id": "D_q29", "label": "q29", "parent": "T_q22"},
    {"id": "RU_q24", "label": "q24", "parent": "D_q23"},
    {"id": "RU_q25", "label": "q25", "parent": "D_q23"},
    {"id": "t_t19", "label": "t19", "parent": "RU_q24"},
    {"id": "t_t20", "label": "t20", "parent": "RU_q24"},
    {"id": "t_t21", "label": "t21", "parent": "RU_q25"},
    {"id": "t_t22", "label": "t22", "parent": "RU_q25"},
    {"id": "RU_q27", "label": "q27", "parent": "D_q26"},
    {"id": "RU_q28", "label": "q28", "parent": "D_q26"},
    {"id": "t_t23", "label": "t23", "parent": "RU_q27"},
    {"id": "t_t24", "label": "t24", "parent": "RU_q27"},
    {"id": "t_t25", "label": "t25", "parent": "RU_q28"},
    {"id": "t_t26", "label": "t26", "parent": "RU_q28"},
    {"id": "RU_q30", "label": "q30", "parent": "D_q29"},
    {"id": "RU_q31", "label": "q31", "parent": "D_q29"},
    {"id": "t_t27", "label": "t27", "parent": "RU_q30"},
    {"id": "t_t28", "label": "t28", "parent": "RU_q30"},
    {"id": "t_t29", "label": "t29", "parent": "RU_q31"},
    {"id": "t_t30", "label": "t30", "parent": "RU_q31"},
    {"id": "T_q32", "label": "q32", "parent": "SBS_q21"},
    {"id": "RU_q33", "label": "q33", "parent": "T_q32"},
    {"id": "RU_q35", "label": "q35", "parent": "T_q32"},
    {"id": "RU_q37", "label": "q37", "parent": "T_q32"},
    {"id": "D_q34", "label": "q34", "parent": "RU_q33"},
    {"id": "D_q36", "label": "q36", "parent": "RU_q35"},
    {"id": "D_q38", "label": "q38", "parent": "RU_q37"},
    {"id": "t_t31", "label": "t31", "parent": "D_q34"},
    {"id": "t_t32", "label": "t32", "parent": "D_q34"},
    {"id": "t_t33", "label": "t33", "parent": "D_q36"},
    {"id": "t_t34", "label": "t34", "parent": "D_q36"},
    {"id": "t_t35", "label": "t35", "parent": "D_q38"},
    {"id": "t_t36", "label": "t36", "parent": "D_q38"}
]

from fractions import Fraction

# Списък с клонове
edges = [
    {"from": "AU", "to": "T_q2", "weight": Fraction(65, 92), "number": 1},
    {"from": "AU", "to": "SBS_q21", "weight": Fraction(27, 92), "number": 2},

    {"from": "T_q2", "to": "SBS_q3", "weight": Fraction(3, 65), "number": 3},
    {"from": "T_q2", "to": "SBS_q4", "weight": Fraction(40, 65), "number": 4},
    {"from": "T_q2", "to": "SBS_q5", "weight": Fraction(22, 65), "number": 5},

    {"from": "SBS_q3", "to": "D_q6", "weight": Fraction(19, 20), "number": 6},
    {"from": "SBS_q3", "to": "RU_q9", "weight": Fraction(1, 20), "number": 7},
    {"from": "SBS_q4", "to": "D_q11", "weight": Fraction(19, 20), "number": 6},
    {"from": "SBS_q4", "to": "RU_q14", "weight": Fraction(1, 20), "number": 7},
    {"from": "SBS_q5", "to": "D_q16", "weight": Fraction(19, 20), "number": 6},
    {"from": "SBS_q5", "to": "RU_q19", "weight": Fraction(1, 20), "number": 7},

    {"from": "D_q6", "to": "RU_q7", "number": 10},
    {"from": "D_q6", "to": "RU_q8", "number": 11},
    {"from": "RU_q7", "to": "t_t1", "number": 13},
    {"from": "RU_q7", "to": "t_t2", "number": 14},
    {"from": "RU_q8", "to": "t_t3", "number": 13},
    {"from": "RU_q8", "to": "t_t4", "number": 14},
    {"from": "RU_q9", "to": "D_q10", "number": 14},
    {"from": "D_q10", "to": "t_t5", "number": 10},
    {"from": "D_q10", "to": "t_t6", "number": 11},
    {"from": "D_q11", "to": "RU_q12", "number": 10},
    {"from": "D_q11", "to": "RU_q13", "number": 11},
    {"from": "RU_q12", "to": "t_t7", "number": 13},
    {"from": "RU_q12", "to": "t_t8", "number": 14},
    {"from": "RU_q13", "to": "t_t9", "number": 13},
    {"from": "RU_q13", "to": "t_t10", "number": 14},
    {"from": "RU_q14", "to": "D_q15", "number": 14},
    {"from": "D_q15", "to": "t_t11", "number": 10},
    {"from": "D_q15", "to": "t_t12", "number": 11},
    {"from": "D_q16", "to": "RU_q17", "number": 10},
    {"from": "D_q16", "to": "RU_q18", "number": 11},
    {"from": "RU_q17", "to": "t_t13", "number": 13},
    {"from": "RU_q17", "to": "t_t14", "number": 14},
    {"from": "RU_q18", "to": "t_t15", "number": 13},
    {"from": "RU_q18", "to": "t_t16", "number": 14},
    {"from": "RU_q19", "to": "D_q20", "number": 14},
    {"from": "D_q20", "to": "t_t17", "number": 10},
    {"from": "D_q20", "to": "t_t18", "number": 11},

    {"from": "SBS_q21", "to": "T_q22", "weight": Fraction(19, 20), "number": 6},
    {"from": "SBS_q21", "to": "T_q32", "weight": Fraction(1, 20), "number": 7},

    {"from": "T_q22", "to": "D_q23", "weight": Fraction(2, 27), "number": 3},
    {"from": "T_q22", "to": "D_q26", "weight": Fraction(16, 27), "number": 4},
    {"from": "T_q22", "to": "D_q29", "weight": Fraction(9, 27), "number": 5},
    {"from": "T_q32", "to": "RU_q33", "weight": Fraction(2, 27), "number": 3},
    {"from": "T_q32", "to": "RU_q35", "weight": Fraction(16, 27), "number": 4},
    {"from": "T_q32", "to": "RU_q37", "weight": Fraction(9, 27), "number": 5},

    {"from": "D_q23", "to": "RU_q24", "number": 10},
    {"from": "D_q23", "to": "RU_q25", "number": 11},
    {"from": "RU_q24", "to": "t_t19", "number": 13},
    {"from": "RU_q24", "to": "t_t20", "number": 14},
    {"from": "RU_q25", "to": "t_t21", "number": 13},
    {"from": "RU_q25", "to": "t_t22", "number": 14},
    {"from": "D_q26", "to": "RU_q27", "number": 10},
    {"from": "D_q26", "to": "RU_q28", "number": 11},
    {"from": "RU_q27", "to": "t_t23", "number": 13},
    {"from": "RU_q27", "to": "t_t24", "number": 14},
    {"from": "RU_q28", "to": "t_t25", "number": 13},
    {"from": "RU_q28", "to": "t_t26", "number": 14},
    {"from": "D_q29", "to": "RU_q30", "number": 10},
    {"from": "D_q29", "to": "RU_q31", "number": 11},
    {"from": "RU_q30", "to": "t_t27", "number": 13},
    {"from": "RU_q30", "to": "t_t28", "number": 14},
    {"from": "RU_q31", "to": "t_t29", "number": 13},
    {"from": "RU_q31", "to": "t_t30", "number": 14},

    {"from": "RU_q33", "to": "D_q34", "number": 14},
    {"from": "RU_q35", "to": "D_q36", "number": 14},
    {"from": "RU_q37", "to": "D_q38", "number": 14},
    {"from": "D_q34", "to": "t_t31", "number": 10},
    {"from": "D_q34", "to": "t_t32", "number": 11},
    {"from": "D_q36", "to": "t_t33", "number": 10},
    {"from": "D_q36", "to": "t_t34", "number": 11},
    {"from": "D_q38", "to": "t_t35", "number": 10},
    {"from": "D_q38", "to": "t_t36", "number": 11}

]

def find_all_paths(tree, start, end, path=None):
    """Рекурсивно намира всички пътища от start до даден end."""
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return [path]
    if start not in tree:
        return []
    paths = []
    for node in tree[start]:
        if node not in path:
            newpaths = find_all_paths(tree, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

#Функция: обхождане в дълбочина (DFS)

from collections import defaultdict

def build_adjacency(edges):
    tree = defaultdict(list)
    for edge in edges:
        tree[edge['from']].append(edge['to'])
    return tree

def dfs_with_labels(tree, start_node_id, nodes_dict, visited=None):
    if visited is None:
        visited = []
    label = nodes_dict[start_node_id]['label']
    visited.append((start_node_id, label))

    for neighbor in tree[start_node_id]:
        if neighbor not in [v[0] for v in visited]:
            dfs_with_labels(tree, neighbor, nodes_dict, visited)

    return visited

nodes_dict = {node['id']: node for node in nodes}
tree = build_adjacency(edges)
visited_nodes = dfs_with_labels(tree, "AU", nodes_dict)

# Построяване на дървото
tree = {}
labels = {}

for node in nodes:
    labels[node["id"]] = node["label"]
    parent = node["parent"]
    if parent:
        tree.setdefault(parent, []).append(node["id"])

# Създаваме речник от (from, to) -> (weight, number)
edge_info = {}
for edge in edges:
    key = (edge["from"], edge["to"])
    weight = edge.get("weight")
    number = edge.get("number")
    edge_info[key] = (weight, number)

# Функция за печат
def print_tree(node_id, prefix="", is_last=True):
    connector = "└── " if is_last else "├── "
    print(prefix + connector + f"{labels[node_id]} ({node_id})")
    
    children = tree.get(node_id, [])
    for i, child_id in enumerate(children):
        is_last_child = i == (len(children) - 1)
        weight, number = edge_info.get((node_id, child_id), (None, None))

        # Изграждане на етикета за реброто
        info_parts = []
        if weight is not None:
            info_parts.append(f"weight: {weight}")
        if number is not None:
            info_parts.append(f"number: {number}")
        info_text = ", ".join(info_parts)

        # Печат
        new_prefix = prefix + ("    " if is_last else "│   ")
        arrow = "└── " if is_last_child else "├── "
        print(new_prefix + arrow + f"[{info_text}]")
        print_tree(child_id, new_prefix + ("    " if is_last_child else "│   "), is_last_child)

# Намиране на корените
roots = [node["id"] for node in nodes if node["parent"] is None]
for root in roots:
    print_tree(root)


#Създаване на стратегиите на играчите
from itertools import product

# 1. Играчи и информационни множества (по labels)
players = {
    "RU": [
        {"q9", "q14", "q19"},
        {"q7", "q8", "q12", "q13", "q17", "q18"},
        {"q24", "q25", "q27", "q28", "q30", "q31"},
        {"q33", "q35", "q37"},
    ],
    "D": [
        {"q6", "q11", "q16"},
        {"q10", "q15", "q20"},
        {"q23", "q26", "q29"},
        {"q34", "q36", "q38"},
    ]
}

# 2. Свързване label → ID и ID → label
label_to_id = {node['label']: node['id'] for node in nodes}
id_to_label = {node['id']: node['label'] for node in nodes}

# 3. Генериране: за всяко множество → съответните 'number' от edges
def get_choices_per_infoset(infoset_labels, edges):
    """Връща множеството от номера на действия (number), налични от възли в това множество."""
    infoset_ids = {label_to_id[label] for label in infoset_labels if label in label_to_id}
    numbers = set()
    for edge in edges:
        if edge['from'] in infoset_ids:
            if 'number' in edge:
                numbers.add(edge['number'])
    return sorted(numbers)

# 4. Генериране на стратегии
def generate_strategies(player, infosets, edges):
    choices_per_set = [get_choices_per_infoset(infoset, edges) for infoset in infosets]
    strategy_combinations = list(product(*choices_per_set))  # всички възможни комбинации
    strategies = []

    for i, combo in enumerate(strategy_combinations, start=1):
        strategies.append({
            "name": f"{player}{i}",
            "combo": combo,
            "details": [
                {
                    "infoset": sorted(list(infosets[j])),
                    "choice": combo[j]
                }
                for j in range(len(combo))
            ]
        })
    return strategies


# Генерирай и покажи стратегиите на RU
ru_strategies = generate_strategies("RU", players["RU"], edges)
d_strategies = generate_strategies("D", players["D"], edges)

def print_strategies(strategies):
    for strat in strategies:
        print(f"{strat['name']} {list(strat['combo'])}")
        for idx, detail in enumerate(strat['details'], start=1):
            group = ", ".join(detail['infoset'])
            print(f"  x{idx}{{ {group} }} = {detail['choice']}")
        print()

print("🎯 Стратегии на RU:")
print_strategies(ru_strategies)

print("🎯 Стратегии на D:")
print_strategies(d_strategies)

#Всеки възел
def build_decision_map(strategy, infosets, player, edges, label_to_id):
    """
    Строи речник {from_node_id: chosen_number} за дадена стратегия
    """
    decision_map = {}
    for i, infoset in enumerate(players[player]):
        node_ids = [label_to_id[label] for label in infoset if label in label_to_id]
        chosen_number = strategy['combo'][i]
        for node_id in node_ids:
            decision_map[node_id] = chosen_number
    return decision_map

from fractions import Fraction

def compute_probabilities(ru_strategy, d_strategy, nodes, edges, label_to_id):
    # Строим речници от стратегията
    ru_map = build_decision_map(ru_strategy, players["RU"], "RU", edges, label_to_id)
    d_map = build_decision_map(d_strategy, players["D"], "D", edges, label_to_id)

    result = {}

    for node in nodes:
        qid = node['id']  # Използваме уникалното ID 
        out_edges = [e for e in edges if e['from'] == qid]
        total_weight = sum(e.get('weight', 0) for e in out_edges)

        result[qid] = {}

        for e in out_edges:
            number = e.get('number')
            if number is None:
                continue  # Прескачаме ребра без номер

            chosen_number = None
            if qid in ru_map:
                chosen_number = ru_map[qid]
            elif qid in d_map:
                chosen_number = d_map[qid]

            if 'weight' in e and total_weight != 0:
                weight = e['weight']
                prob = Fraction(weight, 1) / Fraction(total_weight, 1)
            else:
                prob = Fraction(1, 1) if number == chosen_number else Fraction(0, 1)

            result[qid][number] = prob

    return result


def print_probabilities(probabilities, ru, d, nodes, edges):
    print(f"\n📋 Вероятности по ситуацията: {ru['name']}, {d['name']}")

    # Сортираме q-възлите по номер в label (например "q1", "q2", ..., "q92")
    q_nodes = [n for n in nodes if n["label"].startswith("q")]
    sorted_q_nodes = sorted(q_nodes, key=lambda n: int(n["label"][1:]))

    for node in sorted_q_nodes:
        qid = node["id"]
        qlabel = node["label"]

        if qid not in probabilities:
            continue  # пропускаме ако няма вероятности

        actions = probabilities[qid]
        parts = [f"p({{{ru['name']}, {d['name']}}}, {qlabel}, {a}) = {p}" for a, p in actions.items()]
        print(f"For {qlabel} – " + " ; ".join(parts))

def choose_strategy(name, all_strategies):
    while True:
        strategy_input = input(f"Въведи стратегията на {name} (напр. {name}1): ").strip()
        for strat in all_strategies:
            if strat['name'] == strategy_input:
                return strat
        print("Невалидна стратегия. Опитай отново.")

if __name__ == "__main__":
    print("\n🧠 Стратегии на RU: " + ", ".join([s['name'] for s in ru_strategies]))
    print("🧠 Стратегии на D: " + ", ".join([s['name'] for s in d_strategies]))

    ru = choose_strategy("RU", ru_strategies)
    d = choose_strategy("D", d_strategies)

    probabilities = compute_probabilities(ru, d, nodes, edges, label_to_id)
    print_probabilities(probabilities, ru, d, nodes, edges)


def print_terminal_probabilities_formatted(probabilities, ru, d, nodes, edges, tree):
    id_to_label = {n["id"]: n["label"] for n in nodes}
    label_to_id = {n["label"]: n["id"] for n in nodes}

    # Сортирани терминални възли t1 → t108

    sorted_t_nodes = sorted(
    [node for node in nodes if node['label'].startswith("t") and node['id'].startswith("t_t")],
    key=lambda n: int(n['label'][1:]) if n['label'][1:].isdigit() else float('inf')
    )

    edge_map = {(e["from"], e["to"]): e["number"] for e in edges}

    print(f"\n📊 Tърсените вероятности за стратегията: {ru['name']}, {d['name']}")

    for t_node in sorted_t_nodes:
        all_paths = find_all_paths(tree, "AU", t_node["id"])
        for path in all_paths:
            label_parts = []
            prob_parts = []
            total_prob = 1

            for i in range(len(path) - 1):
                frm = path[i]
                to = path[i + 1]
                q_label = id_to_label[frm]
                number = edge_map.get((frm, to))
                if number is None:
                    continue
                p_val = probabilities.get(frm, {}).get(number, 0)

                label_parts.append(f"p({{{ru['name']}, {d['name']}}}, {q_label}, {number})")
                prob_parts.append(str(p_val))
                total_prob *= p_val

            t_label = t_node["label"]
            print(f"P({{{ru['name']}, {d['name']}}}, {t_label}) = " +
                  " * ".join(label_parts) +
                  " = " + " * ".join(prob_parts) +
                  f" = {total_prob}")
            
            if not all_paths:
                print(f"(⚠️ няма път до {t_node['id']} / {t_node['label']})")
probabilities = compute_probabilities(ru, d, nodes, edges, label_to_id)
print_terminal_probabilities_formatted(probabilities, ru, d, nodes, edges, tree)

# Задаване на W2
W2 = {
    "t1": 100, "t2": 100, "t3": 100, "t4": 100, "t5": 90, "t6": 90, "t7": 90, "t8": 100, "t9": 90, "t10": 100,
    "t11": 70, "t12": 80, "t13": 70, "t14": 80, "t15": 80, "t16": 90, "t17": 50, "t18": 60, "t19": 50, "t20": 60,
    "t21": 60, "t22": 70, "t23": 40, "t24": 50, "t25": 50, "t26": 60, "t27": 30, "t28": 40, "t29": 40, "t30": 40,
    "t31": 20, "t32": 30, "t33": 10, "t34": 20, "t35": 10, "t36": 10
}

from fractions import Fraction

def compute_Eij(ru, d, nodes, edges, tree, W2):
    probabilities = compute_probabilities(ru, d, nodes, edges, label_to_id)
    id_to_label = {n["id"]: n["label"] for n in nodes}
    edge_map = {(e["from"], e["to"]): e.get("number") for e in edges}

    terminal_nodes = [n["id"] for n in nodes if n["label"].startswith("t")]
    total = Fraction(0, 1)
    term_expressions = []

    for t_node in terminal_nodes:
        t_label = id_to_label[t_node]
        w = Fraction(W2.get(t_label, 0), 1)
        all_paths = find_all_paths(tree, "AU", t_node)

        if not all_paths:
            term_expressions.append(f"0*{w}")
            continue

        term_total_prob = Fraction(0, 1)

        for path in all_paths:
            prob = Fraction(1, 1)

            for i in range(len(path) - 1):
                frm = path[i]
                to = path[i + 1]
                number = edge_map.get((frm, to), None)
                if number is None:
                    prob = Fraction(0, 1)
                    break
                p_val = probabilities.get(frm, {}).get(number, Fraction(0, 1))
                prob *= p_val

            term_total_prob += prob

        # Краен израз: W(t_k) * обща P
        prob_str = "0" if term_total_prob == 0 else f"{term_total_prob}"
        expr = f"({prob_str})*{w}"
        term_expressions.append(expr)
        total += term_total_prob * w

    return total, term_expressions
total_value, terms_list = compute_Eij(ru, d, nodes, edges, tree, W2)
expr_str = " + ".join(terms_list)

print(f"\nE({ru['name']}, {d['name']}) = ∑_(k=1)^108 W(t_k)*P({{{ru['name']}, {d['name']}}}) =")
print(f" {expr_str} = {total_value}")

import matplotlib.pyplot as plt
import numpy as np

def build_payoff_matrix(ru_strategies, d_strategies, nodes, edges, tree, W2):
    matrix = []
    for ru in ru_strategies:
        row = []
        for d in d_strategies:
            val, _ = compute_Eij(ru, d, nodes, edges, tree, W2)  # вземаме само дробта
            row.append(val) # НЕ преобразуваме към float!
        matrix.append(row)
    return matrix

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))


# Създай матрицата
payoff_matrix = build_payoff_matrix(ru_strategies[:4], d_strategies[:16], nodes, edges, tree, W2)
transposed_matrix = transpose_matrix(payoff_matrix)

# Печат в табличен вид
from prettytable import PrettyTable
from fractions import Fraction


def print_payoff_matrix_with_prettytable(ru_strategies, d_strategies, nodes, edges, tree, W2):
    # Създаване на матрицата на стойностите E_ij
    payoff_matrix = build_payoff_matrix(ru_strategies, d_strategies, nodes, edges, tree, W2)
    
    # Създаваме таблица с PrettyTable
    table = PrettyTable()

    # Добавяме заглавия на колоните
    table.field_names = ["RU/D"] + [f"D{i+1}" for i in range(len(d_strategies))]

    # Добавяме редове за всяка стратегия на RU
    for i, row in enumerate(payoff_matrix):
        ru_name = f"RU{i+1}"
        table.add_row([ru_name] + [str(val) for val in row])  # Показваме всяка стойност като дроб

    print(table)

def print_transposed_matrix(transposed_matrix):
    table = PrettyTable()
    table.field_names = ["D\\RU"] + [f"RU{i+1}" for i in range(len(transposed_matrix[0]))]
    for i, row in enumerate(transposed_matrix):
        table.add_row([f"D{i+1}"] + row)
    print(table)


# Примерна употреба:
print_payoff_matrix_with_prettytable(ru_strategies[:4], d_strategies[:16], nodes, edges, tree, W2)

print_transposed_matrix(transposed_matrix)

#from Rationals import Rational
from sympy import symbols, Rational, simplify

M_VALUE = 10000
M = symbols("M")

from sympy import Rational

def generate_problem_from_matrix(payoff_matrix, objective_type="min"):
    num_vars = len(payoff_matrix[0])
    objective = [Rational(1) for _ in range(num_vars)]  # f(x) = x1 + x2 + ... + xn
    constraints = []

    sign = ">=" if objective_type == "min" else "<="

    for row in payoff_matrix:
        constraint = [Rational(val.numerator, val.denominator) if isinstance(val, Fraction) else Rational(val) for val in row]
        constraints.append((constraint, sign, Rational(1)))

    return objective, constraints, objective_type, Rational(0)  # свободен член = 0

current_objective = "min"
def get_variable_name(index, objective):
    return f"{'x' if objective == 'min' else 'y'}{index + 1}"

def display_function(coeffs, objective, free_coeff):
    var_prefix = "y" if objective == "max" else "x"
    terms = [f"{coeff}*{get_variable_name(i, objective)}" for i, coeff in enumerate(coeffs)]
    objective_str = "Максимизация" if objective == "max" else "Минимизация"

    # Присъединяване на свободния член само ако е различен от 0
    if free_coeff != 0:
        free_coeff_str = f" + {free_coeff}" if free_coeff > 0 else f" - {-free_coeff}"
    else:
        free_coeff_str = ""

    return f"{objective_str} на: " + " + ".join(terms).replace('+ -', '- ') + free_coeff_str

def display_constraints(constraints):
    result = []
    for coeffs, sign, rhs in constraints:
        terms = [f"{coeff}*{get_variable_name(i, 'min') if coeffs[i] != 0 else '0'}" for i, coeff in enumerate(coeffs)]
        constraint = " + ".join(terms).replace('+ -', '- ') + f" {sign} {rhs}"
        result.append(constraint)
    return "\n".join(result)

def find_basis(constraints):
    """Намира базисните променливи в ограниченията."""
    num_constraints = len(constraints)
    num_vars = len(constraints[0][0]) if constraints else 0
    basis_vars = [-1] * num_constraints  # Индексите на базисните променливи

    for j in range(num_vars):
        count = 0
        row_index = -1
        for i in range(num_constraints):
            if constraints[i][0][j] == 1:
                count += 1
                row_index = i
            elif constraints[i][0][j] != 0:
                count = -1  # Ако има друга ненулева стойност, не е базис
                break
        if count == 1:
            basis_vars[row_index] = j

    return basis_vars

def canonicalize(coefficients, constraints, objective, free_coefficient):
    num_vars = len(coefficients)
    surplus_vars = 0
    
    has_equality_constraints = any(sign == "=" for _, sign, _ in constraints)
    has_inequality_constraints = any(sign == "<=" or sign == ">=" for _, sign, _ in constraints)
    count_equality_constraints = sum(1 for _, sign, _ in constraints if sign == "=")
    
    if has_equality_constraints and has_inequality_constraints:
        # Добавяне на излишъци променливи където е необходимо
        for i, (coeffs, sign, rhs) in enumerate(constraints):
            if sign == "<=":
                coeffs.extend([Rational(1) if j == surplus_vars else Rational(0) for j in range(len(constraints) - count_equality_constraints)])
                surplus_vars += 1
                coefficients.append(Rational(0))
            elif sign == ">=":
                coeffs.extend([Rational(-1) if j == surplus_vars else Rational(0) for j in range(len(constraints) - count_equality_constraints)])
                surplus_vars += 1
                coefficients.append(Rational(0))
            elif sign == "=":
                coeffs.extend([Rational(0)] * (len(constraints) - count_equality_constraints))
            constraints[i] = (coeffs, "=", rhs)
    
        # Актуализация на броя на променливите
        num_vars += surplus_vars
    
        # Проверка за базис
        basis_vars = find_basis(constraints)
    
        # Добавяне на изкуствени променливи, ако няма достатъчно базисни
        artificial_vars = []
        for i in range(len(constraints)):
            if basis_vars[i] == -1:  # Ако няма базисна променлива в това ограничение
                artificial_var_index = num_vars + len(artificial_vars)
                for j in range(len(constraints)):
                    constraints[j][0].append(Rational(1) if j == i else Rational(0))  # Добавяне на изкуствена променлива
                artificial_vars.append(artificial_var_index)
                if objective == "min":
                    coefficients.append(Rational(M_VALUE))
                elif objective == "max":
                    coefficients.append(Rational(-M_VALUE)) # Изкуствените променливи не влияят на целевата функция
    
        num_vars += len(artificial_vars)
    
        # Подготовка и извеждане на каноничния вид
        print("Каноничен вид на задачата:")
        print("Целева функция:")
        print_function(coefficients, num_vars, objective, free_coefficient)
    
        print("Ограничения:")
        for coeffs, sign, rhs in constraints:
            print_constraint(coeffs, rhs)
    else:    
        # Добавяне на излишъци променливи където е необходимо
        for i, (coeffs, sign, rhs) in enumerate(constraints):
            if sign == "<=":
                coeffs.extend([Rational(1) if j == surplus_vars else Rational(0) for j in range(len(constraints))])
                surplus_vars += 1
                coefficients.append(Rational(0))
            elif sign == ">=":
                coeffs.extend([Rational(-1) if j == surplus_vars else Rational(0) for j in range(len(constraints))])
                surplus_vars += 1
                coefficients.append(Rational(0))
            constraints[i] = (coeffs, "=", rhs)
    
        # Актуализация на броя на променливите
        num_vars += surplus_vars
    
        # Проверка за базис
        basis_vars = find_basis(constraints)
    
        # Добавяне на изкуствени променливи, ако няма достатъчно базисни
        artificial_vars = []
        for i in range(len(constraints)):
            if basis_vars[i] == -1:  # Ако няма базисна променлива в това ограничение
                artificial_var_index = num_vars + len(artificial_vars)
                for j in range(len(constraints)):
                    constraints[j][0].append(Rational(1) if j == i else Rational(0))  # Добавяне на изкуствена променлива
                artificial_vars.append(artificial_var_index)
                if objective == "min":
                    coefficients.append(Rational(M_VALUE))
                elif objective == "max":
                    coefficients.append(Rational(-M_VALUE)) # Изкуствените променливи, които се добавят, за да се създаде базис, влияят на целевата функция
    
        num_vars += len(artificial_vars)
    
        # Подготовка и извеждане на каноничния вид
        print("Каноничен вид на задачата:")
        print("Целева функция:")
        print_function(coefficients, num_vars, objective, free_coefficient)
    
        print("Ограничения:")
        for coeffs, sign, rhs in constraints:
            print_constraint(coeffs, rhs)

def canonicalize_for_table(coefficients, constraints, objective):
    num_vars = len(coefficients)
    surplus_vars = 0
    slack_vars = 0
    artificial_vars = 0

    # Добавяне на излишъци и изкуствени променливи
    for i, (coeffs, sign, rhs) in enumerate(constraints):
        if sign == "<=":
            coeffs.extend([Rational(1) if j == slack_vars else Rational(0) for j in range(len(constraints))])
            slack_vars += 1
        elif sign == ">=":
            coeffs.extend([Rational(-1) if j == surplus_vars else Rational(0) for j in range(len(constraints))])
            surplus_vars += 1
        constraints[i] = (coeffs, "=", rhs)

    # Проверка за базисни променливи
    basis_vars = find_basis(constraints)
    artificial_indices = []

    # Добавяне на изкуствени променливи при нужда
    for i in range(len(constraints)):
        if basis_vars[i] == -1:  # Ако няма базисна променлива в това ограничение
            artificial_var_index = num_vars + slack_vars + surplus_vars + artificial_vars
            for j in range(len(constraints)):
                constraints[j][0].append(Rational(1) if j == i else Rational(0))  # Добавяне на изкуствена променлива
            artificial_indices.append(artificial_var_index)
            artificial_vars += 1

    num_slack = slack_vars + surplus_vars
    total_vars = num_vars + num_slack + artificial_vars

    # Добавяне на ред с коефициентите от целевата функция
    objective_row = ['', '', ''] + coefficients + [Rational(0)] * (num_slack + artificial_vars)
    table = [objective_row]

    # Заглавия на колоните
    headers = ['CBx', 'Bx', 'b'] + [get_variable_name(i, objective) for i in range(total_vars)]
    table.append(headers)

    # Генериране на таблицата
    for i, (coeffs, sign, rhs) in enumerate(constraints):
        #base_var = f"x{total_vars - artificial_vars - i}" if surplus_vars > 0 else f"x{num_vars + i + 1 - len(constraints)}"
        #CBx = 0  # Коефициентът на базисната променлива в целевата функция
        basis_index = basis_vars[i] if basis_vars[i] != -1 else total_vars - artificial_vars - i
        base_var = get_variable_name(basis_index, objective)
        CBx = coefficients[basis_index] if basis_index < len(coefficients) else Rational(0)  # Взимаме коефициента от целевата функция
        bx_row = [CBx, base_var, Rational(rhs)] + coeffs
        table.append(bx_row)

    return table

def print_function(coeffs, num_vars, objective, free_coeff):
    var_prefix = "y" if objective == "max" else "x"
    terms = []
    for i, coeff in enumerate(coeffs[:num_vars]):
        if coeff == M_VALUE:
            terms.append(f"{str(coeff).replace(str(M_VALUE), 'M')}*{var_prefix}{i + 1}")
        elif coeff == -M_VALUE:
            terms.append(f"{str(coeff).replace(str(-M_VALUE), '-M')}*{var_prefix}{i + 1}")
        else:
            terms.append(f"{coeff}*{get_variable_name(i, objective)}")

    # Присъединяване на свободния член само ако е различен от 0
    if free_coeff != 0:
        free_coeff_str = f" + {free_coeff}" if free_coeff > 0 else f" - {-free_coeff}"
    else:
        free_coeff_str = ""

    print(f"{'Максимизирай' if objective == 'max' else 'Минимизирай'}: {' + '.join(terms).replace('+ -', '- ')}", free_coeff_str)

def print_constraint(coeffs, rhs):
    terms = []
    for i, coeff in enumerate(coeffs):
        if coeff > 0:
            terms.append(f"{coeff}*{get_variable_name(i, current_objective)}")
        elif coeff < 0:
            terms.append(f"- {abs(coeff)}*x{i + 1}")
        else:
            terms.append(f"{coeff}*{get_variable_name(i, current_objective)}")

    # Заместване на първоначалния знак `+` с празен низ, ако е необходимо
    constraint_str = ' + '.join(terms).replace('+ -', '-')
    print(f"{constraint_str} = {rhs}")


def print_table(table, coefficients):
    approximation = simplify(sum(simplify(row[2]) * simplify(row[0].subs(M_VALUE, M)) for row in table[2:] if isinstance(row[0], (int, Rational, type(M)))))
    table[-1][2] = approximation
    for j in range(3, 3 + len(coefficients)):
        delta = simplify(sum(simplify(row[0].subs(M, M_VALUE)) * simplify(row[j]) for row in table[2:] if isinstance(row[0], (int, Rational, type(M)))) - coefficients[j - 3])
        if delta != 0:
            delta = simplify(sum(simplify(row[j] * simplify(row[0].subs(M_VALUE, M))) for row in table[2:] if isinstance(row[0], (int, Rational, type(M)))) - coefficients[j - 3].subs(M_VALUE, M))
        table[-1][j] = delta
    for row in table:
        print(" | ".join(f"{str(item).replace(str(M_VALUE), 'M'):>15}" for item in row))

def calculate_first_approximation(table, coefficients):
    """
    Пресмята първото приближение за целевата функция и делтите за всички небазисни променливи.
    """
    # Изчисляване на стойността на целевата функция Z
    numeric_coeffs = [c.subs(M, M_VALUE) if c.has(M) else c for c in coefficients]
    approximation = simplify(sum(simplify(row[0]).subs(M, M_VALUE) * simplify(row[2]) for row in table[2:] if isinstance(row[0], (int, Rational))))
    
    # Пресмятане на делтите
    deltas = []
    num_vars = len(coefficients)
    for j in range(3, 3 + num_vars):
        delta = simplify(sum(simplify(row[0]).subs(M, M_VALUE) * simplify(row[j]) for row in table[2:] if isinstance(row[0], (int, Rational))) - numeric_coeffs[j - 3])
        deltas.append(delta)

    return approximation, deltas

def add_approximation_and_deltas(table, coefficients):
    approximation, deltas = calculate_first_approximation(table, coefficients)
    approximation_row = [''] * 3 + deltas
    approximation_row[0] = "Z"
    approximation_row[1] = " = "
    approximation_row[2] = f" {approximation}"
    table.append(approximation_row)

def check_optimality(table, objective):
    # Взимаме делтите от последния ред на таблицата, изключвайки първите три елемента
    deltas = table[-1][3:]

    # За максимизация, проверяваме дали всички делти са >= 0
    if objective == "max":
        if all(delta.subs(M, M_VALUE) >= 0 for delta in deltas):
            print("\nРешението е оптимално.")
            return True
        else:
            print("\nРешението не е оптимално. Необходимо е допълнително итериране.")
            return False
    
    # За минимизация, проверяваме дали всички делти са <= 0
    elif objective == "min":
        if all(delta.subs(M, M_VALUE) <= 0 for delta in deltas):
            print("\nРешението е оптимално.")
            return True
        else:
            print("\nРешението не е оптимално. Необходимо е допълнително итериране.")
            return False

def find_pivot_element(table, objective):
    # Извличане на реда на делтите
    delta_row = table[-1][3:]  # Премахваме първите три колони ('CBx', 'Bx', 'b')
    for i in range(len(delta_row)):
        delta_row[i] = delta_row[i].subs(M, M_VALUE)
    
    # Определяне на най-големият нарушител на критерия за оптималност
    if objective == "max":
        # За максимизация, търсим най-малката (най-голяма отрицателна) делта
        pivot_col = min(enumerate(delta_row), key=lambda x: x[1])
    else:
        # За минимизация, търсим най-голямата (най-голяма положителна) делта
        pivot_col = max(enumerate(delta_row), key=lambda x: x[1])
    
    # Извличане на стойностите от стълба на избраната делта и стълба 'b'
    b_values = [row[2].subs(M, M_VALUE) for row in table[2:-1]]  # Вземаме всички стойности от стълба 'b', пропускайки заглавния ред и реда на делтите
    column_values = [row[pivot_col[0] + 3] for row in table[2:-1]]  # +3 за да компенсираме пропуснатите първите три колони
    
    if all(val <= 0 for val in column_values):
        print("Задачата няма решение, поради липса на положителен елемент в ключовия стълб")
        return None
    
    # Изчисляване на минималната дроб и определяне на ключовия елемент
    ratios = []
    for b, column_val in zip(b_values, column_values):
        if column_val > 0:  # Проверка за предотвратяване на деление на нула
            ratios.append(b / column_val)
        else:
            ratios.append(float('inf'))  # Неизползваемо висока стойност
    
    pivot_row_index = ratios.index(min(ratios))
    pivot_value = table[pivot_row_index + 2][pivot_col[0] + 3]  # +1 за да компенсираме пропуснатия заглавен ред
    
    return pivot_row_index + 2, pivot_col[0] + 3, pivot_value

# Забележка: Тази функция предполага, че 'table' вече съдържа канонизираната форма с добавените ред за делтите.
# Трябва да се адаптира спрямо точната структура на вашата таблица.

def pivot_table(table, pivot_row_index, pivot_col_index, coefficients):
    pivot_element = table[pivot_row_index][pivot_col_index]
    
    # Нормализиране на ключовия ред
    for i in range(2, len(table[pivot_row_index])):
        table[pivot_row_index][i] /= pivot_element
    
    # Обновяване на останалите редове
    for r in range(2, len(table) - 1):
        if r != pivot_row_index:
            factor = table[r][pivot_col_index]
            for c in range(2, len(table[r])):
                table[r][c] = table[r][c] - factor * table[pivot_row_index][c]
    
    # Заместване на променливата в Bx и обновяване на CBx
    bx_var = f"x{pivot_col_index - 2}"  # Адаптирайте според точната структура на таблицата
    table[pivot_row_index][1] = bx_var  # Заместваме в Bx
    table[pivot_row_index][0] = coefficients[pivot_col_index - 3]  # Обновяваме CBx със съответния коефициент от целевата функция

    return table

def print_optimal_solution(table, number_original_variables, objective, free_coeff, prefix):
    from sympy import Rational, simplify

    z_value = Rational(0)
    for row in table[2:-1]:
        z_value += simplify(row[0].subs(M_VALUE, M) * Rational(row[2]))
    z_value += free_coeff

    contains_M_in_first_column = any(row[0].has(M_VALUE) for row in table[2:-1])

    optimal_values = {f"{prefix}{i + 1}": Rational(0) for i in range(number_original_variables)}

    for row in table[2:-1]:
        bx_variable = row[1]
        if bx_variable.startswith("x") or bx_variable.startswith("y"):
            bx_index = int(bx_variable[1:])
            key = f"{prefix}{bx_index}"
            if key in optimal_values:
                optimal_values[key] = row[2]

    print(f"{objective.upper()} Z = {z_value}")
    for var, val in optimal_values.items():
        print(f"{var} = {val}", end=" ")
    print()

    if contains_M_in_first_column or z_value.has(M):
        print("Изходната задача няма решение, заради наличието на изкуствени променливи в базиса.")
      
def main():
    print("Автоматично решаване чрез Симплекс метод.")

    # Построй оригиналната и транспонирана матрица
    payoff_matrix = build_payoff_matrix(ru_strategies[:4], d_strategies[:16], nodes, edges, tree, W2)
    transposed_matrix = list(map(list, zip(*payoff_matrix)))  # Размяна на редове и колони

    for objective in ["min", "max"]:
        matrix_to_use = transposed_matrix if objective == "min" else payoff_matrix
        prefix = "x" if objective == "min" else "y"

        num_vars = len(matrix_to_use[0])
        func_expr = " + ".join([f"{prefix}{i + 1}" for i in range(num_vars)])
        func_label = f"f(x) = {func_expr} → min" if objective == "min" else f"g(y) = {func_expr} → max"

        print(f"\n{'='*30}\n🔍 Решение за {objective.upper()} ({func_label}):\n{'='*30}")

        # Генерирай целевата функция и ограничения
        coefficients, constraints, _, free_coefficient = generate_problem_from_matrix(matrix_to_use, objective_type=objective)

        # Копия за работа
        from copy import deepcopy
        coeffs = deepcopy(coefficients)
        constr = deepcopy(constraints)

        canonicalize(coeffs, constr, objective, free_coefficient)
        canonical_form = canonicalize_for_table(coeffs, constr, objective)

        print('\n📐 Първа симплекс таблица:')
        add_approximation_and_deltas(canonical_form, coeffs)
        print_table(canonical_form, coeffs)

        while not check_optimality(canonical_form, objective):
            pivot = find_pivot_element(canonical_form, objective)
            if pivot is None:
                print("❌ Задачата няма решение.")
                return
            pivot_row, pivot_col, pivot_value = pivot
            print(f"\n➡ Ключов елемент: ({canonical_form[pivot_row][1]}, {canonical_form[1][pivot_col]}) = {pivot_value}")
            canonical_form = pivot_table(canonical_form, pivot_row, pivot_col, coeffs)
            add_approximation_and_deltas(canonical_form, coeffs)
            del canonical_form[-2]
            print_table(canonical_form, coeffs)

        # Покажи решението
        print_optimal_solution(canonical_form, num_vars, objective, free_coefficient, prefix)



if __name__ == "__main__":
    main()
    print("Програмата приключи успешно.")
    input("Натиснете Enter за изход...")

import sys
sys.exit(0)
