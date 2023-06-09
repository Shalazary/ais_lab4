def dfs(graph, start, visited=None, to=0, path_len=0):
    # Верефикация
    if start not in graph.keys():
        raise ValueError

    if to not in graph.keys():
        raise ValueError

    if start == to:
        return visited, path_len, True

    # Инициализация
    if visited is None:
        visited = set()

    visited.add(start)

    # Главная часть
    for next in graph[start] - visited:
        path_len += 1
        _, _, is_find = dfs(graph, next, visited, to=to, path_len=path_len)
        # Коммент для конфликта
        if is_find:
            return visited.union({next}), path_len + 1, True

    return visited, path_len, False
