'''
Day 2
Part 2
'''
import re


def main(o):
    values = open("data/day2.txt").read().splitlines()
    p = re.compile(r"^(\d+)-(\d+) (\w): (\w+)$")
    for i in values:
        m = p.match(i)
        if m:
            pos1,pos2,letter,pw = int(m.group(1))-1,int(m.group(2))-1,m.group(3),m.group(4)
            if (pw[pos1] == letter) != (pw[pos2] == letter):
                o += 1
    print(o)
main(0)