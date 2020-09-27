"""
贪婪算法：每步都采取最优解，最终得到近似最优解
例子：选出能覆盖50个州的广播台，其中每个广播台能覆盖一部分州，多个广播台能覆盖的州可能有重复
时间复杂度：O(n*n)
"""

# 创建一个集合，包含要覆盖的州
states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}
# 广播台清单，列出每个广播台能覆盖的州
stations = {
    'k1': {'id', 'nv', 'ut'},
    'k2': {'wa', 'id', 'mt'},
    'k3': {'or', 'nv', 'ca'},
    'k4': {'nv', 'ut'},
    'k5': {'ca', 'az'}
}
# 最终选择的广播台
final_stations = set()

# 遍历广播台清单，每次选出覆盖了最多未覆盖州的广播台
while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
            final_stations.add(best_station)
            states_needed -= covered

print(final_stations)





