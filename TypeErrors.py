def find_path(graph, start, end, path = []):
    path = path + [start]
    if start == end:
        return path
    if start not in graph.keys():
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


n = int(input())
dict = {}
for i in range(n):
    str = input().replace(':', ' ').split()
    dict[str[0]] = str[1:]
q = int(input())
#lst = []
#for i in range(q):
#    str2 = input()
#    lst.append(str2)
lst = [input() for i in range(q)]
otvet = []
#visited = []
m = len(lst)
print("dict  = ", dict)
print("lst   = ", lst)

for i in range(m-1,0,-1):
    for j in range(i-1,-1,-1):
        if find_path(dict,lst[i],lst[j]) != None:
            otvet.append(lst[i])
    print("OTVET = ", otvet)
#print("dfs   = ", dfs(dict, "coming"))
#print("lst   = ", lst)
#print("otvet = ", otvet)
#print("dict  = ", dict)
