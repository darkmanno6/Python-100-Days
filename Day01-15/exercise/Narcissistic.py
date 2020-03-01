"""
水仙花数，水仙花数是指一个3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153
"""


def narcissistic():
    for num in range(100, 1000):
        a = num // 100
        b = (num - (100 * a)) // 10
        c = num - 100 * a - 10 * b
        if (a ** 3 + b ** 3 + c ** 3) == num:
            print(num)


if __name__ == "__main__":
    narcissistic()
