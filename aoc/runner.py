import importlib
from utils.input import read_input

def run(day: int):
    module = importlib.import_module(
        f"day{day:02d}.solution"
    )

    raw = read_input(day)
    data = module.parse_input(raw)

    print(f"Part 1: {module.part1(data)}")
    print(f"Part 2: {module.part2(data)}")


if __name__ == "__main__":
    import sys
    run(int(sys.argv[1]))
