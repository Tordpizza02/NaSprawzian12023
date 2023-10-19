#1 mnożenie 
# a = int(input())
# b = int(input())
# print(a*b)

# #funkcja
# def mnożenie(n, o):
#   wynik = n*o
#   return(wynik)

# int f (n)
# if (n==0) return 3
# else return f(n-1)+2

# tabliczka mnożenia
# for i in range(1,11):
#   for j in range(1,11):
#     wynik = i*j
#     print(f"{i} x {j} = {wynik}")

#Nierówność trójkąta
# a = int(input())
# b = int(input())
# c = int(input())

# Nierówność trójkąta jest kiedy bok jest mniejszy lub od sumy dwóch pozostałych boków lub jest większy od różnicy dwóch pozostałych boków


# if a<(b+c) and a>(b-c) and b<(a+c) and b>(a-c) and c<(a+b) and c>(a-b):
#    print("tak")
# else:
#   print("nie")

# Bajtożabka osiowa oddaje tylko równe skoki o długości s wzdłuż osi. Napisz algorytm, który sprawdzi, czy żabka pokona zadany dystans w trzech skokach. Jako punkt startu przyjmujemy wartość p, a jako punkt końcowy punkt k, gdzie p, k, s >= 0

# p = int(input())
# s = int(input())
# k = int(input())
# if p + (s*3) >= k:
#   print("Tak")
# else:
#   print("Nie")

# ciąg fibonacciego
# n = int(input())
# a, b = 0,1
# for i in range(n):
#   a, b = b, a+b
#   print(a,end=" ")

# Małe Twierdzenie Fermata
# a = int(input())
# p = int(input())

# if (a**p-a) % p == 0:
#   print("Tak")
# else:
#   print("Nie")


