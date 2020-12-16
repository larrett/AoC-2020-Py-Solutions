'''
Day 2
Part 1
'''
import re

def main():
    o = 0
    values = open("data/day2.txt").read().splitlines()
    p = re.compile(r"^(\d+)-(\d+) (\w): (\w+)$")
    for i in values:
        m = p.match(i)
        if m:
            i,k,v = int(m.group(1)),int(m.group(2)),m.group(3)
            z = m.group(4).count(v)
            if not z < i and not z > k:
                o = o+1
    print(o)
main()