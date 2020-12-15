'''
Day 1
Part 1
'''
def main():
    values = open("day1.txt").read().splitlines()
    for i in values:
        for j in values:
            i, j = int(i), int(j)
            num = i+j
            if(i != j and num == 2020):
                solution = i*j
                break
    print(solution)
main()