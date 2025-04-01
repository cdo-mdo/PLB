from collections import defaultdict

def calcEquation(equations, values, queries):
    graph = defaultdict(dict)

    # build the graph
    for (a, b), value in zip(equations, values):
        graph[a][b] = value
        graph[b][a] = 1/value

    # DFS function to evaluate a query
    def dfs(start, end, visited):
        if (start not in graph or end not in graph):
            return -1.0
        if start == end:
            return 1.0
        visited.add(start)

        for neighbor, weight in graph[start].items():
            if neighbor not in visited:
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return weight * result

        return -1.0

    # evaluation each query
    results = []
    for c, d in queries:
        results.append(dfs(c, d, set()))

    return results

# example usage
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
print(calcEquation(equations, values, queries))
