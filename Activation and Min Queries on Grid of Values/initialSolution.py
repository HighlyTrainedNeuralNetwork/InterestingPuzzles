def solution(n, m, queries):
    grid = []
    for i in range(n):
        grid.append([])
        for j in range(m):
            grid[i].append((i + 1) * (j + 1))
    deactivated = {"rows": set(), "columns": set()}
    # minLoc = [42, None]
    def minActive(grid):
        values = []
        for i in range(n):
            if i not in deactivated["rows"]:
                for j in range(m):
                    if j not in deactivated["columns"]:
                        values.append(grid[i][j])
                else:
                    pass
            else:
                continue
        return min(values)

    def deactiveRow(grid, row):
        deactivated["rows"].add(row - 1)

    def deactiveColumn(grid, column):
        deactivated["columns"].add(column - 1)

    calculated = []
    for query in queries:
        if query in queries:
            if query[0] == 0:
                calculated.append(minActive(grid))
            elif query[0] == 1:
                deactiveRow(grid, query[1])
            elif query[0] == 2:
                deactiveColumn(grid, query[1])
    return calculated


if __name__ == "__main__":
    n = 3
    m = 4
    queries = [[0], [1, 2], [0], [2, 1], [0], [1, 1], [0]]
    print(solution(n, m, queries))