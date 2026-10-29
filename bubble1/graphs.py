from collections import deque

def Flood_Fill(img: list[list[int]], i: int, j: int, new_color: int) -> list[list[int]]:
    n, m = len(img), len(img[0])
    res = img.copy()

    # q = deque()
    # q.append((i, j))
    old_color = img[i][j]
    # visited = set()

    directions = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]

    # while q:
    #     x, y = q.popleft()
    #     res[x][y] = new_color
    #     visited.add((x, y))

    #     for (dx, dy) in directions:
    #         _x, _y = x + dx, y + dy

    #         if 0 <= _x < n and 0 <= _y < m and img[_x][_y] == old_color:
    #             if (_x, _y) not in visited: q.append((_x, _y))

    # return res

    # I could do this shit with DFS too
    stack = [ (i, j) ]
    visited = set( (i, j) )
    res[i][j] = new_color

    while stack:
        x, y = stack.pop()
        for (dx, dy) in directions:
            _x, _y = x + dx, y + dy

            if 0 <= _x < n and 0 <= _y < m and img[_x][_y] == old_color:
                if (_x, _y) not in visited:
                    stack.append((_x, _y))
                    res[_x][_y] = new_color
                    visited.add((_x, _y))

    return res


def Number_Of_Islands(grid: list[list[str]]) -> int:
    res = 0

    visited = set()
    n, m = len(grid), len(grid[0])

    directions = [ (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1) ]

    def _bfs(i: int, j: int):
        q = deque()
        q.append((i, j))

        while q:
            x, y = q.popleft()
            visited.add((x, y))

            for (dx, dy) in directions:
                _x, _y = x + dx, y + dy
                if 0 <= _x < n and 0 <= _y < m and grid[_x][_y] == 'L':
                    if (_x, _y) not in visited:
                        q.append((_x, _y))


    for i in range(n):
        for j in range(m):
            if (i, j) not in visited and grid[i][j] == 'L':
                _bfs(i, j)
                res += 1


    return res


def Connected_Components(adj: list[list[int]]) -> list[list[int]]:
    res = []
    n = len(adj)

    visited = set()
    def _dfs(i: int):
        stack = [ i ]
        order = []

        while stack:
            node = stack.pop()
            visited.add(node)
            order.append(node)

            for child in adj[node]:
                if child not in visited:
                    stack.append(child)

        return order

    for i in range(n):
        if i not in visited:
            res.append(_dfs(i))


    return res


def Detect_Cycle(adj: list[list[int]]) -> bool:
    visited = set()
    # n = len(adj)

    # assuming no disconnected components
    stack = [ (0, -1) ]

    while stack:
        node, parent = stack.pop()
        if node in visited:
            continue
        visited.add(node)

        for child in adj[node]:
            if child == parent:
                continue

            if child in visited:
                return True

            stack.append((child, node))


    return False

def Detect_Cycle_In_Directed(edges: list[list[int]]) -> bool:
    n = len(edges)
    visited, on_path = [False] * n, [False] * n

    def _dfs(u: int, adj: list[list[int]]):
        if on_path[u]: return True
        if visited[u]: return False
        visited[u], on_path[u] = True, True

        for v in adj[u]:
            if _dfs(v, adj):
                return True

        on_path[u] = False
        return False

    adj = [ [] for _ in range(n) ]
    for e in edges:
        adj[e[0]].append(e[1])

    for i in range(n):
        if not visited[i] and _dfs(i, adj):
            return True

    return False


adj = [[0, 1], [1, 2], [2, 0], [2, 3]]
adj = [[0, 1], [0, 2], [1, 2], [2, 3]]
print(Detect_Cycle_In_Directed(adj))
