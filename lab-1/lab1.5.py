"""
def basel_rec(n):
    if n == 1:
        return 1/pow(n,2)
    return 1/pow(n,2) + basel_rec(n-1)
"""

def main():
    n = int(input("n: "))
    if n == 0:
        print("Invalid n!")
        return

    basel_sum = 0

    for k in range(1, n + 1):
        basel_sum += 1 / pow(k, 2)

    print("forloop:",basel_sum)

    #rec_sum = basel_rec(n)

    #print("rec:", rec_sum)


if __name__ == '__main__':
    main()

