"""
质数又称素数。一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数
对正整数n，如果用2到之间的所有整数去除，均无法整除，则n为质数
"""


# 判断是否为质数
def prime(num):
    if num == 2:
        return True
    if num > 2:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                # print(num, "不是素数")
                return False
        # print(num, "是素数")
        return True
    # print(num, "不是素数")
    return False


if __name__ == '__main__':
    prime(11)
