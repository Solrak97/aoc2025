import re

def parse_input(text: str):
    return text.split(',')


def part1(data):
   
    sum = 0

    for datum in data:
      ranges = datum.split('-')
      for id in range(int(ranges[0]), int(ranges[1])):
        strid = str(id)
        size = len(strid)
        if size % 2 != 0:
           continue
        
        a = strid[ : (size // 2)]
        b = strid[(size // 2) : ]

        if a == b:
           sum += id

    return sum


def part2(data):
    sum = 0

    for datum in data:
      ranges = datum.split('-')
      for id in range(int(ranges[0]), int(ranges[1])):
        strid = str(id)
        
        m = re.search(r'^(.+?)(?:\1)+$', strid)
        sum += id if m else 0
        
    return sum

