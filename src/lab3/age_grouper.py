import sys
from typing import List, Tuple

class AgeGrouper:
    def __init__(self, bounds: List[int]):
        self.bounds = bounds

    def group(self, people: List[Tuple[str, int]]) -> List[Tuple[str, List[Tuple[str, int]]]]:
        if not people:
            return []
        groups = []
        prev = 0
        for b in self.bounds:
            groups.append((prev, b))
            prev = b + 1
        groups.append((prev, float('inf')))
        result = []
        for lower, upper in reversed(groups):
            members = []
            for name, age in people:
                if lower <= age <= upper:
                    members.append((name, age))
            if members:
                members.sort(key=lambda x: (-x[1], x[0]))
                if upper == float('inf'):
                    label = f"{lower}+"
                else:
                    label = f"{lower}-{upper}"
                result.append((label, members))
        return result

def parse_bounds(args: List[str]) -> List[int]:
    return [int(x) for x in args]

def read_people() -> List[Tuple[str, int]]:
    people = []
    for line in sys.stdin:
        line = line.strip()
        if line == "END":
            break
        if not line:
            continue
        parts = line.split(',', 1)
        if len(parts) == 2:
            name = parts[0].strip()
            age = int(parts[1].strip())
            people.append((name, age))
    return people

def main():
    if len(sys.argv) < 2:
        print("Usage: python age_grouper.py <bound1> <bound2> ...")
        sys.exit(1)
    bounds = parse_bounds(sys.argv[1:])
    grouper = AgeGrouper(bounds)
    people = read_people()
    grouped = grouper.group(people)
    for label, members in grouped:
        line = f"{label}: " + ", ".join(f"{name} ({age})" for name, age in members)
        print(line)

if __name__ == "__main__":
    main()