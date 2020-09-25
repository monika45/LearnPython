"""
广度优先搜索:
1.是否有A到B的路径
2.如果有，找到最短路径
"""

from collections import deque


def is_seller(name):
    if name == 'thoms':
        return True
    return False


# 实现图
graph = {
    'you': ['alice', 'bob', 'claire'],
    'alice': ['peggy'],
    'bob': ['anuj', 'peggy'],
    'claire': ['thom', 'jonny', 'you']
}

# 创建一个队列
search_queue = deque()
# 将你的邻居都加入到这个搜索队列中
search_queue += graph['you']

print(search_queue)
searched = []
# 只要队列不为空就继续
while search_queue:
    person = search_queue.popleft()
    if person not in searched:
        if is_seller(person):
            print(f'{person} is mango seller!')
            break
        elif person in graph:
            search_queue += graph[person]
        searched.append(person)
    print(search_queue)
