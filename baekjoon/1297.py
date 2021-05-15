# 1297: TV 크기
# https://www.acmicpc.net/problem/1297

import math

# z, y, x = 52, 9, 16
z, y, x = map(int, input().split())

# a^2 + b^2 = z^2
# a : b = x : y -> b = y*a/x

# b = y*a/x
# a = sqrt(z^2 - b^2)
# a^2 + (y*a/x)^2 = z^2

# (x^2 + y^2) * a^2 / x^2 = z^2
# a^2 = z^2 * x^2 / (x^2 + y^2)
# a = sqrt(z^2 * x^2 / (x^2 + y^2))

a = math.sqrt(z ** 2 * x ** 2 / (x ** 2 + y ** 2))
b = y * a / x
print(int(b), int(a))
