import math


def main():
    n = int(input("n: "))
    if n < 1:
        print("Invalid n!")
        return

    basel_sum = 0

    for k in range(1, n + 1):
        basel_sum += 1 / k**2

    deviation = math.pi**2 / 6

    print("sum:", basel_sum)
    print("deviation:", deviation-basel_sum)


if __name__ == '__main__':
    main()

