from graphs import dfs

if __name__ == "__main__":
    graph = {0: set([1, 2]),
             1: set([0, 3, 4]),
             2: set([0]),
             3: set([1]),
             4: set([2, 3])}

    path, path_len, _ = dfs(graph, 0, to=3)
    print(path, path_len)
