# inputdan kelgan narsalarni ajratish
# x, y ,z = input("give me  ").split()
# print(f"{x} \n {y} \n {z}")


#  Massivdan dobliktan sonlardan tozalash
# a = [1,1,2,3,3,45,4674,5,5,6,7,2,3]
# a = list(set(a))
# print(a)



#  Massivdan dobliktan sonlardan eng kop nechta dublikatligini aniqlash
# a = [1,1,2,3,3,45,4674,5,5,5,5,5,6,7,2,3]
# m = max(set(a), key=a.count)
# print(m)


#  Generator bilan massivga 10 gacha bolgan sonlarni toqlarini kvsini chiqarish
# k = [i**2 for i in range(11) if i%2!=0 ]
# print(k)


# Palindromligini tekshirish
# name = 'adama'
# p = name.find(name[::-1])==0
# print(f"{p} Palindrom")

# dublikatlar sonini va dublikat soni berilgan berilgan soncha dublikat qaysi ekanligini topish
# from collections import Counter

# my_list = [10,10,10,5,5,2,93,3,9,9,9,9,9,9,9]
# c = Counter(my_list)
# print(c[9])

# most= c.most_common(4)
# print(most)


# # join
# l = ["helo" , "my" , "world"]
# my_str = "".join(l)
# print(my_str)


# def to_up(num):
#     return num * num

# a = list(range(1,6))
# for i in map(to_up, a):
#     print(i)
    
# def main():
#     print("main func")
# x = 10
# print(dir(x))
# print(main.__doc__)



# a = list(range(1,6))
# for i in map(lambda x:x+x, a):
#     print(i)




# def func(x,y):
#     for i in range(1,10):
#         yield x*y #yield bu for uchun return

# for x in func(1,10):
#     print(x)