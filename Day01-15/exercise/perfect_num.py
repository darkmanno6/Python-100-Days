"""
如果一个数恰好等于它的因子之和，则称该数为“完全数”
找出1~9999之间的所有完美数
如果p是质数，且2^p-1也是质数，那么（2^p-1）X2^（p-1）便是一个完全数
"""
import prime_num


def perfect_num():
    for num in range(1, 10000):
        b = 2 ** num - 1
        if prime_num.prime(num) and prime_num.prime(b):
            # print(num)
            a = 2 ** (num - 1)
            print("完全数：", a * b, "\n")


if __name__ == '__main__':
    perfect_num()
