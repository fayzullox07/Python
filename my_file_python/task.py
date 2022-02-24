import random
#masala
# k = 15
# n = int(input("N kirit \n :"))
# for i in range(n):
#     print(k)

#masala2
# a = int(input("A kirit \n :"))
# b = int(input("B kirit \n :"))
# c = 0
# for i in range(a,b+1):
#     c += 1
#     print(i)
#     print(f"a = {a}, b = {b}, soni = {c}")
# first.py
#masala3
# a = int(input("A kirit \n :"))
# b = int(input("B kirit \n :"))
# c = 0


# task 1
# k = 15
# n = int(input("N = \n :"))
# for i in range(n):
#     print(k)
# task 2
# a = int(input("A = \n :"))
# b = int(input("B = \n :"))
# c = 0
# for i in range(a,b+1):
#     c += 1
#     print(i)
# print(f"a = {a} , b = {b}, soni = {c}")

# task 3
# a = int(input("A = \n :"))
# b = int(input("B = \n :"))
# c = 0
# nums = [x  for x in range(a , b)]
# nums.reverse()
# del nums[0]
#
# for i in nums:
#     print(i)
# task 4
# k = 15000
# summa = 1
# arr = []
# for i in range(1, 11):
#     summa += i**2
# print(summa)
# f = "1."

# s = 0
# for i in range(5):
#     s = float(f"{f}{i}") - float(f"{f}{i+1}")
#     print(s)
#     s = float(f"{f}{i+1}") + float(f"{f}{i+2}")
#     print(s)

# print(s)

# arr = []
# for i in range(1,5):
#     arr.append(float("1.{}".format(i)))
# print(arr)
# for i in range(len(arr)):
#     s = arr[i] - arr[i+1]
#     print(s)
#     s += arr[i+2]
#     print(s)


#tasklist 1
# arr = list(random.sample(range(50))
# summa = []
# for i in arr:
#     summa += i
# else:
#         print(summa)
#     print(sum(list(random.sample(range(50),20)))) #qisqa yo'li


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
for i in a:
    if i in a:
        a.remove(i)
else:
    for x in b:
        b.remove(x)
    a.extend(b)
print(a)
            


