from turtle import *
import cmath
from math import pi
import string

print(cmath.sqrt(-1))
print("hello!")
print("hello,\nworld")
print('kanyuanzhi'.encode("UTF-32"))

a = [1, 2, 3]
b = a[:]
b[1] = 5
print(b)
print(a)

name = "pi"
print("{name} is approximately {value:.2f}".format(name="pi", value=pi))
print(f"{name} is approximately {pi:.2f}")

print(string.ascii_letters)

str1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(str1.center(39, "*"))

str2 = "@@ get rich now ~~~"
print(str2.find("get"))
print("ge1" in str2)
