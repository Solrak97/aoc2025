def rotate(start: int ,dir: str, ticks: int):
    pos = 0
    if dir == 'L':
        pos = start - ticks
    elif dir == 'R':
        pos = start + ticks
    else:
        raise ValueError("No valid direction!!!")
    return pos % 100


def rotate_zros(start: int ,dir: str, ticks: int):
    pos = start
    zros = 0
    
    for tick in range(1, ticks + 1):
        pos = rotate(pos, dir, 1) 
        print(pos)
        if pos == 0:
            zros += 1

    return (pos % 100, zros)


def parse_input(text: str):
    return [(str(l[0]), int(l[1:])) for l in text.splitlines()]


def part1(data):
    pos = 50
    z_counter = 0

    for add, ticks in data:
        pos = rotate(pos, add, ticks)
        
        if pos == 0:
            z_counter += 1
        
    print(z_counter)
    return z_counter


def part2(data):
    pos = 50
    z_counter = 0

    for add, ticks in data:
        (pos, zros) = rotate_zros(pos, add, ticks)
        z_counter += zros
        
    return z_counter




print(rotate_zros(99, "R", 101))