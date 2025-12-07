from functools import cache

@cache
def is_wall(x: int, y: int, num: int) -> bool:
    val = x*x + 3*x + 2*x*y + y + y*y + num
    return bin(val).count('1') % 2 == 1


@cache
def search_path(startx: int, starty: int, endx: int, endy: int, num: int) -> int:
    from collections import deque

    queue = deque()
    queue.append((startx, starty, 0))
    visited = set()
    visited.add((startx, starty))

    while queue:
        x, y, dist = queue.popleft()

        if x == endx and y == endy:
            return dist

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and not is_wall(nx, ny, num) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))

    return -1


def part1(lines: list[str]) -> int:
    num = int(lines[0])
    return search_path(1, 1, 31, 39, num)


def part2(lines: list[str]) -> int:
    num = int(lines[0])
    from collections import deque

    queue = deque()
    queue.append((1, 1, 0))
    visited = set()
    visited.add((1, 1))

    while queue:
        x, y, dist = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and not is_wall(nx, ny, num) and (nx, ny) not in visited:
                visited.add((nx, ny))
                if dist + 1 < 50:
                    queue.append((nx, ny, dist + 1))

    return len(visited)


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
