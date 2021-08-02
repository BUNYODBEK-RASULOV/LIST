# massivni hosil qilish va elementlarni kiritish
# 1-misol
# toqsonlar=list(range(1,10,2))
# print(toqsonlar)

# 2-misol
# ikkiningDarajalari=[2,4,8,16,32,64,128,256]
# print(ikkiningDarajalari)

# 3-misol
# ArifmetikProgressiyaHadlari=list(range(0,10,3))
# print(ArifmetikProgressiyaHadlari)

# 4-misol
# a = int(input("a ni kiriting:"))
# d = int(input("d ni kiriting:"))
# n = int(input("n hadlar soni ni kiriting:"))
# geometrikProg = []
# for x in range(n):
#     geometrikProg.append(a)
#     a = a * d
# print(geometrikProg)

# 5-misol
# n = int(input("input n:"))
# fibonanchi = [1, 1]
# for i in range(3, n + 1):
#     fibonanchi.append(fibonanchi[i - 3] + fibonanchi[i - 2])
# print(fibonanchi)

# 6-misol
# n = int(input("input n:"))
# a = int(input("input f(0)=a:"))
# b = int(input("input f(1)=b:"))
#
# fibonanchi = [a, b]
# for i in range(3, n + 1):
#     fibonanchi.append(fibonanchi[i - 3] + fibonanchi[i - 2])
# print(fibonanchi)

# 7-misol
# massiv=[1,2,3,9,8,6,7,11]
# # 1-usul
# massiv2=massiv.copy()
# massiv.reverse()
# print(massiv )
# # 2-usul
# print(massiv2[::-1])

# 8-misol
# massiv=[4,9,7,8,6,3]
# toqsonlar=[]
# for i in massiv:
#     if i%2==1:
#         toqsonlar.append(i)
# toqsonlar.sort()
# print(toqsonlar," elemetlar soni:",len(toqsonlar))


# 9-misol
# massiv=[4,9,7,8,6,3]
# juftsonlar=[]
# for i in massiv:
#     if i%2==0:
#         juftsonlar.append(i)
# juftsonlar.sort()
# print(juftsonlar," elemetlar soni:",len(juftsonlar))

# 10-misol
# massiv=[4,6,8,10,9,3,2,15,20,18]
# toqsonlar=[]
# juftsonlar=[]
# for i in massiv:
#     if i%2==1:
#         toqsonlar.append(i)
#     else:
#         juftsonlar.append(i)
# juftsonlar.sort()
# toqsonlar.sort()
# toqsonlar.reverse()
# print(juftsonlar+toqsonlar)

# 11-misol
# massiv = [2, 3, 4, 5, 2, 6, 7, 2, 7, 9, 10]
# print(massiv.count(2))

# 12-misol
# massiz=[2,6,4,8,7,10,9,3,7,12]
# for i in range(0,10,2):
#     print(massiz[i])

# 13-misol
# massiv=[2,3,4,5,7,10,9,7,12]
# juft=[]
# for i in range(1,8,2):
#     juft.insert(0,massiv[i])
# print(juft)

# 16-misol
# massiv=[1,2,45,65,78,96,36,23]
# n=len(massiv)
# a=True
# for i in range(n//2):
#     print(massiv[i])
#     print(massiv[n-i-1])


# massiv elementlarini taxlil qilish
# 18-misol
# massiv = [80, 70, 45, 30, 45, 8, 9, 65,33]
# n = len(massiv)
# for x in massiv:
#     if x < massiv[n - 1]:
#         print(x)
#         break
#     elif x == massiv[n - 1]:
#         print(0)

# 19-misol
# massiv = [29, 20, 25, 30, 46, 8, 9, 65, 50]
# n = len(massiv)
# a = 0
# for i in range(n - 1):
#     if (massiv[0] < massiv[i] and massiv[i] < massiv[n - 1]):
#         a = i
# print(a)

# 20-misol
# massiv = [29, 20, 25, 30, 46, 8, 9, 65, 50]
# k = int(input("input k:"))
# l = int(input("input l:"))
# if (k < l and l < len(massiv) and 0 < k):
#     # 1-usul
#     # print(sum(massiv[k:l + 1]))
#     # 2-usul
#     s = 0
#     for i in range(k, l + 1):
#         s = s + massiv[i]
#     print(s)

# 21-misol
# massiv = [29, 20, 25, 30, 46, 8, 9, 65, 50]
# k = int(input("input k:"))
# l = int(input("input l:"))
# s=0
# for i in range(k, l + 1):
#     s = s + massiv[i]
# print(s/(l-k+1))

# 22-misol
# massiv = [29, 20, 25, 30, 46, 8, 9, 65, 50]
# k = int(input("input k:"))
# l = int(input("input l:"))
# s=0
# for i in range(len(massiv)-1):
#     if i<k or i>l:
#         s = s + massiv[i]
# print(s)

# 24-misol
# massiv = [2, 4, 6, 8, 10, 12, 14, 16, 18]
# a=True
# for i in range(1,len(massiv)):
#     if massiv[1]-massiv[0]!=massiv[i]-massiv[i-1]:
#         a=False
# if a:
#     print(massiv[1] - massiv[0])
# else:
#     print(0)

# 28-misol
# massiv = [2, 3, 28, 8, 10, 12, 14, 16, 18]
# juft=[]
# for x in range(0,len(massiv),2):
#     juft.append(massiv[x])
# print(min(juft))

# 29-misol
# massiv = [2, 3, 28, 11, 16, 12, 17, 13, 18]
# Maxmas = massiv[1]
# for x in range(1, len(massiv), 2):
#     if Maxmas < massiv[x]:
#         Maxmas = massiv[x]
# print(Maxmas)

# 30-misol
# massiv = [2, 3, 28, 11, 16, 12, 17, 13, 18]
# for i in range(1, len(massiv)):
#     if massiv[i] < massiv[i - 1]:
#         print(i)

# 32-misol
# massiv = [2, 3, 28, 11, 16, 12, 17, 13, 18]
# for i in range(1, len(massiv)):
#     if massiv[i - 1] > massiv[i] and massiv[i] < massiv[i + 1]:
#         print(i)
#         break

# 33-misol
# massiv = [2, 3, 28, 11, 16, 12, 17, 13, 18]
# for i in range(1, len(massiv)):
#     if massiv[i - 1] < massiv[i] and massiv[i] > massiv[i + 1]:
#         a = i
# print(a)


# 34-misol
# massiv = [2, 3, 28, 11, 16, 12, 17, 13, 18]
# lokalmin = []
# for i in range(1, len(massiv)):
#     if massiv[i - 1] > massiv[i] and massiv[i] < massiv[i + 1]:
#         lokalmin.append(massiv[i])
# print(max(lokalmin))

# 40-misol
# massiv = [2, 3, 28, 11, 16, 12, 17, 13, 18]
# r=10
# x=massiv[0]
# for i in range(1,len(massiv)):
#     if abs(r-x)>abs(r-massiv[i]):
#         x=massiv[i]
# print(x)

# 41-misol
# massiv = [2, 3, 28, 11, 16, 12, 17, 13, 18]
# a = massiv[0] + massiv[1]
# for i in range(len(massiv) - 1):
#     if a < massiv[i] + massiv[i + 1]:
#         a = massiv[i] + massiv[i + 1]
# print(a)

# 42-misol
# massiv = [2, 3, 28, 11, 16, 1, 1, 13, 18]
# r=10
# x=massiv[0]+massiv[1]
# for i in range(len(massiv)-1):
#     if abs(r-x)>abs(r-massiv[i]-massiv[i+1]):
#         x=massiv[i]+massiv[i+1]
#         print("element massiv:",massiv[i],",",massiv[i+1])
# print(x)

# 43-misol
# n = 0
# massiv = [0, 1, 2, 3, 4, 5, 6, 7, 9, 9, 10, 11, 12, 12, 14, 15, 16, 17]
# for i in range(len(massiv) - 1):
#     if massiv[i + 1] - massiv[i] == 0:
#         n = n + 1
# print(f"xar xil elimentlar soni:{n}")

# 44-misol
# massiv = [0, 1, 2, 3, 4, 5, 6, 7, 9, 9, 10, 11, 12, 12, 14, 15, 16, 17]
# for i in range(len(massiv)):
#     for j in range(i + 1, len(massiv)):
#         if massiv[i] == massiv[j]:
#             print(f"massinning {i} chi va {j} chi elementlar teng")

# 46-misol
# massiv = [2, 3, 28, 11, 16, 1, 1, 13, 18]
# r=10
# x=massiv[0]+massiv[1]
# for i in range(len(massiv)-1):
#     if abs(r-x)>abs(r-massiv[i]-massiv[i+1]):
#         x=massiv[i]+massiv[i+1]
#         print("element massiv:",massiv[i],",",massiv[i+1])

# 47-misol
# massiv = [1, 1, 2, 3, 5, 5, 6, 7, 9, 9, 10, 11, 12, 12, 14, 15, 17, 17]
# i = 0
# while i < len(massiv):
#     j = i + 1
#     while j < len(massiv):
#         if massiv[i] == massiv[j]:
#             del massiv[j]
#         j = j + 1
#     i = i + 1
#
# print(massiv)

# 3 Bir nechta massiv bilan ishlash
# 51-misol
# aaaa = [1, 1, 2, 3, 5, 5, 6, 7, 9, 9, 10]
# b = [10, 11, 12, 12, 14, 15, 17, 17]
# vaqtincga = []
# vaqtincga = aaaa.copy()
# aaaa.clear()
# aaaa = b.copy()
# b = vaqtincga
# print(aaaa, b)

# 52-misol
# a = [1, 1, 2, 3, 5, 5, 6, 7, 9, 9, 10]
# b = []
# for x in a:
#     if x < 5:
#         b.append(2 * x)
#     else:
#         b.append(x / 2)
# print(b)

# 53-misol
# a = [1, 26, 13, 86, 5, 5, 6, 7]
# b = [10, 11, 12, 12, 14, 15, 17, 108]
# c = []
# for i in range(len(a)):
#     c.append(max(a[i], b[i]))
# print(c)

# 54-misol
# a = [10, 11, 12, 12, 14, 15, 17, 108]
# b=[]
# n=0
# for x in a:
#     if x%2==0:
#         b.append(x)
#         n+=1
# print(f"elementlar soni:{n}  {b}")

# 55-misol
# a = [10, 11, 12, 12, 14, 15, 17, 108]
# b = []
# for i in range(1, len(a), 2):
#     b.append(a[i])
# print(b)

# 56-misol
# a = [10, 11, 12, 12, 14, 15, 17, 108]
# b = []
# for i in range(0, len(a), 3):
#     b.append(a[i])
# print(b)


# 57-misol
# a = [10, 11, 12, 12, 14, 15, 17, 108]
# b = []
# for i in range(0, len(a), 2):
#     b.append(a[i])
# for i in range(1, len(a), 2):
#     b.append(a[i])
# print(b)

# 58-misol
# a = [10, 11, 12, 12, 14, 15, 17, 108]
# b = []
# s = 0
# for x in a:
#     s = s + x
#     b.append(s)
# print(b)

# 59-misol
# a = [10, 11, 12, 12, 14, 15, 17, 108]
# b = []
# s = 0
# n = 0
# for x in a:
#     s = s + x
#     n += 1
#     b.append(s / n)
# print(b)

# 60-misol
# a = [10, 11, 12, 12, 14, 15, 17, 108]
# b = []
# n = len(a)
# for i in range(n):
#     s = 0
#     while i < n:
#         s = s + a[i]
#         i = i + 1
#     b.append(s)
# print(b)

# 61-misol
# a = [10, 11, 12, 12, 14, 15, 17, 108]
# b = []
# n = len(a)
# for i in range(n):
#     s = 0
#     while i < n:
#         s = s + a[i]
#         i = i + 1
#     b.append(s / (i))
# print(b)

# 62-misol
# a = [10, -11, 12, -12, 14, 15, -17, 108]
# b = []
# c = []
# for x in a:
#     if x > 0:
#         b.append(x)
#     else:
#         c.append(x)
# print(f"b massiv elementlar soni:{len(b)} massiv:{b}")
# print(f"c massivelementlar soni:{len(c)} massiv:{c}")

# 63-misol
# a=[1,2,3,4,5]
# b=[10,11,12,13,14]
# c=b+a
# for i in range(len(c)):
#     for j in range(i,len(c)):
#         if c[i]>c[j]:
#             aa=c[i] #c[i] elementni vaqtincha saqlab quyamiz
#             c[i]=c[j]
#             c[j]=aa
# print(c)

# 64-misol
# a = [5, 3, 9, 8, 9]
# b = [10, 45, 20, 30, 6]
# c = [2, 3, 5, 78, 96]
# d = a + b + c
# d.sort()
# print(d)


# Massiv elementlarini o'zgaqrtirish
# 65-misol
# a=[1,5,3,9,7,6,4,52,69,46,95]
# n=len(a)
# k=3
# for i in range(n):
#     a[i]=a[i]+a[k]
# print(a)

# 66-misol
# a=[1,5,3,9,7,6,4,52,69,46,95]
# n=len(a)
# s=0
# kalit=True
# for i in range(n):
#     if a[i]%2==0:
#         a[i]=a[i]+s
#     if a[i]%2==0 and kalit:
#         s=a[i]
#         kalit=False
# print(a)


# 68-misol
# a=[1,5,3,9,7,6,-4,52,69,46,95]
# c=min(a)
# d=max(a)
# Indexmin=a.index(c)
# Indexmax=a.index(d)
# a[Indexmin]=d
# a[Indexmax]=c
# print(a)

# 69-misol
# a = [1, 5, 3, 9, 7, 6, -4, 52, 69, 46]
# n = len(a)
# for i in range(0, n, 2):
#     aa = a[i]
#     a[i] = a[i + 1]
#     a[i + 1] = aa
# print(a)

# 71-misol
# a = [1, 5, 3, 9, 7, 6, -4, 52, 69, 46]
# a.reverse()
# print(a)

# 72-misol
# a = [1, 5, 3, 9, 7, 6, -4, 52, 69, 46]
# aa = []
# k = 3
# l = 6
# for i in range(k, l + 1):
#     aa.append(a.pop(k))
# for x in aa:
#     a.insert(k, x)
# print(a)

# 73-misol
# a = [1, 5, 3, 9, 7, 6, -4, 52, 69, 46]
# aa = []
# k = 3
# l = 6
# for i in range(k+1, l):
#     aa.append(a.pop(k))
# for x in aa:
#     a.insert(k, x)
# print(a)

# 74-misol
# a = [1, 5, 3, 9, 7, 6, -4, 52, 69, 46]
# b=min(a)
# c=max(a)
# indexmin=a.index(b)
# indexmax=a.index(c)
# for i in range(indexmin,indexmax+1):
#     a[i]=0
# print(a)

# 75-misol
# a = [1, 5, 3, 99, 7, 6, -4, 52, -69, 46]
# aa = []
# b = min(a)
# c = max(a)
# indexmin = a.index(b)
# indexmax = a.index(c)
# k = indexmin
# l = indexmax
# for i in range(k, l + 1):
#     aa.append(a.pop(k))
# for x in aa:
#     a.insert(k, x)
# print(a)


# 76-misol
# a = [1, 5, 3, 99, 7, 6, -4, 52, -69, 46]
# n = len(a)
# for i in range(n - 2):
#     if a[i] < a[i + 1] and a[i + 1] > a[i + 2]:
#         a[i + 1] = 0
# print(a)


# 87-misol
# a = [0,1, 5, 3, 99, 7, 6, -4, 52, -69, 46]
# a.sort()
# print(a)


# Massivga element qo'shish va ayirish
# 90-misol
# a = [0,1, 5, 26, 99, 7, 6, -4, 52, -69, 46]
# k=3
# del a[k]
# print(a)

# 91-misol
# a = [0,1, 5, 26, 99, 7, 6, -4, 52, -69, 46]
# k=3
# l=5
# while k<=l:
#     del a[k]
#     k+=1
# print(a)
# print(len(a))

# 94-misol
# a = [0,1, 5, 26, 99, 7, 6, -4, 52, -69, 46]
# i=1
# while i<len(a):
#     del a[i]
#     i=i+1
# print(a)

# 93-misol
# a = [0,1, 5, 26, 99, 7, 6, -4, 52, -69, 46]
# i=0
# while i<len(a):
#     del a[i]
#     i=i+1
# print(a)

# 95-misol
# a = [0,1, 5, 5, 99, 6, 6, -4, 52, 4, 46]
# i=1
# while i<len(a):
#     if a[i-1]==a[i]:
#         del a[i]
#     i=i+1
# print(a)

# 96-misol
# a = [0, 1, 5, 6, 99, 6, 5, -4, 52, 4, 46]
# i = 0
# while i <= len(a):
#     j = i + 1
#     while j < len(a):
#         if a[i] == a[j]:
#             del a[j]
#         j = j + 1
#     i = i + 1
# print(a)

# 98-misol
# a = [0, 1, 5, 6, 99,5,6, 5, -4, 52, 4, 46]
# for x in a:
#     i=0
#     while a.count(x)<=3 and i<a.count(x):
#         a.remove(x)
#     i=i+1
#
# print(a)

# 99-misol
# a = [0, 1, 5, 6, 99, 5, 6, 5, -4, 52, 4, 46]
# for x in a:
#     i = 0
#     if a.count(x) >= 2:
#         while i < a.count(x):
#             a.remove(x)
#     i = i + 1
#
# print(a)

# 100-misol
# a = [0, 1, 5, 6, 99, 5, 6, 5, -4, 52, 4, 46]
# for x in a:
#     i = 0
#     if a.count(x) == 2: #oldingi masalada < bor edi.
#         while i < a.count(x):
#             a.remove(x)
#     i = i + 1
#
# print(a)

# 101-misol
# a = [0, 1, 5, 6, 99, 5, 6, 5, -4, 52, 4, 46]
# k=3
# a.insert(k,0)
# print(a)

# 103-misol
# a = [3, 1, 5, 6, 199, 5, 6, 5, -4, 52, 100, 46]
# indexmin = a.index(min(a))
# indexmax = a.index(max(a))
# if indexmax < indexmin:
#     a.insert(indexmin, 0)
#     a.insert(indexmax + 1, 0)  # sababi massiv eleminti 1 taga ortdi
# else:
#     a.insert(indexmin, 0)
#     a.insert(indexmax + 2, 0)  # sababi massiv eleminti 2 taga ortdi
# print(a)

# 106-misol
# a = [3, 1, 5, 6, 199, 5, 6, 5, -4, 52, 100, 46]
# s=0
# for i in range(0,len(a),2):
#     s=s+a[i]
# print(s)


# 108-misol
# a = [3, 1, 5, 6, 199, 5, 6, 5, -4, 52, 100, 46]
# i = 0
# while i < len(a):
#     if a[i] > 0:
#         a.insert(i+1, 0)
#     i = i + 1
# print(a)

# 109-misol
# a = [3, 1, 5, 6, 199, 5, 6, 5, -4, 52, 100, 46]
# i = 0
# while i < len(a):
#     if a[i] < 0:
#         a.insert(i+1, 0)
#     i = i + 1
# print(a)

# 110-misol
# a = [3, 1, 5, 6, 199, 5, 6, 5, -4, 52, 100, 46]
# b=[]
# b=a.copy()
# for x in a:
#     if x%2==0:
#         b.append(x)
# print(b)

# 111-misol
# a = [3, 1, 5, 6, 199, 5, 6, 5, -4, 52, 100, 46]
# b=[]
# b=a.copy()
# for x in a:
#     if x%2==0:
#         b.append(x)
#         b.append(x)
# print(b)

# Massivni saralash
# 112-misol
# a = [3, 1, 5, 6, 199, 5, 6, 5, -4, 52, 100, 46]
# a.sort()
# print(a)

# 113-misol
# a = [101, 1, 5, 6, 199, -4, 46, 100, 56]
# for i in range(len(a) - 1):
#     x = min(a[i + 1:])
#     if a[i] >= x:
#         a[a.index(x)] = a[i]
#         a[i] = x
# print(a)

# 114-misol
# a = [101, 1, 5, 6, 199, -4, 46, 100, 56]
# for i in range(len(a)):
#     for j in range(0, i):
#         if a[i] < a[j]:
#             aa = a[i]
#             a[i] = a[j]
#             a[j] = aa
# print(a)

# 115-misol
# a = [101, 1, 5, 6, 199, -4, 46, 100, 56]
# b = a.copy()
# c = []
# for i in range(len(a)):
#     for j in range(0, i):
#         if a[i] < a[j]:
#             aa = a[i]
#             a[i] = a[j]
#             a[j] = aa
# for x in a:
#     c.append(b.index(x))
# print(c)

# BUTUN SONLAR SERIYASI
# 116-misol
# a = [7, 7, 7, 7, 7, 9, 9, 9, 9, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 5, 5]
# b = []
# c = []
# for i in range(len(a) - 1):
#     if a[i] != a[i + 1]:
#         c.append(a[i])
# c.append(a[i])
# for x in c:
#     b.append(a.count(x))
# print("massiv b:", b)
# print("massiv c:", c)

# 117-misol
# a = [7, 7, 7, 7, 7, 9, 9, 9, 9, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 5, 5]
# c = []
# for i in range(len(a) - 1):
#     if a[i] != a[i + 1]:
#         c.append(a[i])
# c.append(a[i]) # qaysi elementlar borligini ajratib olamiz
#
# for x in c:
#     indeX = a.index(x) # qiymati x teng element kordinatasini olamiz
#     a.insert(indeX, 0) # indeX kordinataga 0 ni qo'shamiz
# print(a)


# 118-misol
# a = [7, 7, 7, 7, 7, 9, 9, 9, 9, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 5, 5]
# a.reverse() #massivni teskarisiga o'giradi.
# c = []
# for i in range(len(a) - 1):
#     if a[i] != a[i + 1]:
#         c.append(a[i])
# c.append(a[i]) # qaysi elementlar borligini ajratib olamiz
#
# for x in c:
#     indeX = a.index(x) # qiymati x teng element kordinatasini olamiz
#     a.insert(indeX, 0) # indeX kordinataga 0 ni qo'shamiz
# a.reverse()
# print(a)

# 130-misol
# a = [7, 7, 7, 7, 7, 9, 9, 9, 9, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 5, 5]
# c = []
# k = 1000  # 1000 ni o'rniga istalgan son yozish mumkin
# for i in range(len(a) - 1):
#     if a[i] != a[i + 1]:
#         c.append(a[i])
# c.append(a[i])  # qaysi elementlar borligini ajratib olamiz
#
# for x in c:
#     indeX = a.index(x)  # qiymati x teng element kordinatasini olamiz
#     a.insert(indeX, k)  # indeX kordinataga 0 ni qo'shamiz
# print(a)


# TEKISLIKDAGI NUQTALAR TO'PLAMI
# 131-misol
# absislar = [2, 3, 4, 1]
# ordinatalar = [2, 3, 4, 2]
# import math
#
# b = [1, 1]
# k = 0
# x = math.sqrt((absislar[0] - b[0]) ** 2 + (ordinatalar[0] - b[1] ** 2))
# for i in range(len(absislar)):
#     if x > math.sqrt((absislar[i] - b[0]) ** 2 + (ordinatalar[i] - b[1] ** 2)):
#         x = math.sqrt((absislar[i] - b[0]) ** 2 + (ordinatalar[i] - b[1] ** 2))
#         k = i
# print("x=", absislar[k], "y=", ordinatalar[k])

# 132-misol
# absislar = [2, 3, -4, 1]
# ordinatalar = [2, 3, 4, 2]
# import math
#
# b = [0, 0]
# k = 0
# x = math.sqrt((absislar[0] - b[0]) ** 2 + (ordinatalar[0] - b[1] ** 2))
# for i in range(len(absislar)):
#     if x < math.sqrt((absislar[i] - b[0]) ** 2 + (ordinatalar[i] - b[1] ** 2)) and absislar[i]<0 and ordinatalar[i]>0:
#         x = math.sqrt((absislar[i] - b[0]) ** 2 + (ordinatalar[i] - b[1] ** 2))
#         k = i
# print("x=", absislar[k], "y=", ordinatalar[k])

# 133-misol
# absislar = [-2, 3, -4, -1]
# ordinatalar = [2, 3, -4, 2]
# kalit = True
# import math
#
# k = 0
# x = math.sqrt(absislar[0] ** 2 + ordinatalar[0] ** 2)
# for i in range(len(absislar)):
#     if (absislar[i] > 0 and ordinatalar[i] > 0) or (absislar[i] < 0 and ordinatalar[i] < 0):
#         if x < math.sqrt(absislar[i] ** 2 + ordinatalar[i] ** 2):
#             x = math.sqrt(absislar[i] ** 2 + ordinatalar[i] ** 2)
#             k = i
#     else:
#         kalit = False
# if kalit:
#     print("x=", absislar[k], "y=", ordinatalar[k])
# else:
#     print("(0,0)")

# 134-misol
# absislar = [-2, 3, -4, -1]
# ordinatalar = [2, 3, -4, 2]
# import math
#
# k = 0
# y = 0
# x = 0
# for j in range(len(absislar)):
#     for i in range(j + 1, len(absislar)):
#         if x < math.sqrt((absislar[j] - absislar[i]) ** 2 + (ordinatalar[j] - ordinatalar[i]) ** 2):
#             x = math.sqrt((absislar[j] - absislar[i]) ** 2 + (ordinatalar[j] - ordinatalar[i]) ** 2)
#             k = i
#             y = j
# print("x=", absislar[k], "y=", ordinatalar[k])
# print("x=", absislar[y], "y=", ordinatalar[y])

# 135-misol
# absislar = [-2, 3, -4, -1]
# ordinatalar = [2, 3, -4, 2]
# import math
#
# k = 0
# y = 0
#  x = math.sqrt((absislar[0] - absislar[1]) ** 2 + (ordinatalar[0] - ordinatalar[1]) ** 2)
# for j in range(len(absislar)):
#     for i in range(j + 1, len(absislar)):
#         if x > math.sqrt((absislar[j] - absislar[i]) ** 2 + (ordinatalar[j] - ordinatalar[i]) ** 2):
#             x = math.sqrt((absislar[j] - absislar[i]) ** 2 + (ordinatalar[j] - ordinatalar[i]) ** 2)
#             k = i
#             y = j
# print("x=", absislar[k], "y=", ordinatalar[k])
# print("x=", absislar[y], "y=", ordinatalar[y])
# print("ular orasidagi masofa:", x)

# 136-misol
# absislar = [0, 0, 0, 0, 0]
# ordinatalar = [-1, 2, 6, 4, 5]
# import math
#
# b = []
# k = 0
# d = 100000000  # kattaroq son bergan maqsadga muofiq
# x = math.sqrt((absislar[0] - absislar[1]) ** 2 + (ordinatalar[0] - ordinatalar[1]) ** 2)
# for j in range(len(absislar)):
#     s = 0
#     for i in range(len(absislar)):
#         s = s + math.sqrt((absislar[j] - absislar[i]) ** 2 + (ordinatalar[j] - ordinatalar[i]) ** 2)
#     b.append(s)
#     if s < d:
#         d = s
#         k = j
#
# print("x=", absislar[k], "y=", ordinatalar[k])
# print(b)
# print("ular orasidagi masofa:", d)


# 138 - misol
import math

absislar = [0, 0, 10, 10, 0.86]
ordinatalar = [0, 1, 6, 4, 0.5]
n = len(absislar)
d = 100000
a = 0
b = 0
c = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            s = math.sqrt((absislar[i] - absislar[j]) ** 2 + (ordinatalar[i] - ordinatalar[j]) ** 2) + math.sqrt(
                (absislar[i] - absislar[k]) ** 2 + (ordinatalar[i] - ordinatalar[k]) ** 2) + math.sqrt(
                (absislar[k] - absislar[j]) ** 2 + (ordinatalar[k] - ordinatalar[j]) ** 2)
            if s < d:
                d = s
                a = i
                b = j
                c = k
print("x=", absislar[a], "y=", ordinatalar[a])
print("x=", absislar[b], "y=", ordinatalar[b])
print("x=", absislar[c], "y=", ordinatalar[c])
print("Perimetr:", d)

""" Hurmatli o'quvchi bazi bir xil usul bilan ishlanadigan misollardan bir nechtasi qoldirib ketildi.
Siz ishlanish yo'lini o'rganing yuqoridagilardan siz kelajakda bazilarini gina ishlatishingiz mumkin.
Bu mening fikrim asosan ko'proq misollar yechishga harakat qiling.
                                HAMISHA OMAD YOR BO'LSIN!!!                                    """
