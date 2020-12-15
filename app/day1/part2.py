'''
Day 1
Part 2
'''
def main():
    values = open("day1.txt").read().splitlines()
    for i in values:
        for j in values:
            for k in values:
                i, j, k = int(i), int(j), int(k)
                num = i+j+k
                if(num == 2020):
                    solution = i*j*k
                    break
    print(solution)
main()