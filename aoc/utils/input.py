from pathlib import Path

def read_input(day: int) -> str:
    path = Path(__file__).parents[2] / f"aoc/day{day:02d}/input.txt"
    return path.read_text().strip()
