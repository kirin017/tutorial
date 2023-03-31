# Câu 7:
'''def doubleFact(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return n*(doubleFact(n-2))

if __name__ == '__main__':
    while True:
        n = int(input())
        if n >= 1:
            break
    print(doubleFact(n))'''
# Câu 5
'''import numpy as np
def calEquaSys(x, y):
    A = np.array([[1, 1],
         [2, 4]])
    B = np.array([x ,y])

    return np.linalg.solve(A, B)
if __name__ == '__main__':
    while True:
        x, y= map(int, (input().split()))
        if (x >= 2):
            break
    X = calEquaSys(x, y)
    print(int(X[0]), int(X[1]))   '''

'''def DetMatrixDim2(a1, a2, c1, c2):
    return abs(a1*c2-a2*c1)
def Solve(c1, c2):
    ms = 1*4-1*2
    x = DetMatrixDim2(c1, c2, 1, 4) / ms
    y = DetMatrixDim2(1, 2, c1, c2) / ms
    return x, y
if __name__ == '__main__':
    while True:
        x, y = map(int, input().split())
        if (x>=2 and y >=0):
            break
    a, b =map(int, Solve(x, y))
    print(a, b)'''

    
#Cau 4:
'''import math
def isTriangle(a, b, c):
    return (a+b) > c and (a+c) > b and (c+b) > a
def CalArea(a, b, c):
    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

if __name__=='__main__':
    while(True):
        a, b, c = map(float, input().split())
        if (isTriangle(a, b, c)):
            break
    print(f'{CalArea(a, b, c):.2f}')'''

'''def transPSI_to_kgcm2(n):
    return n/(2.54*2.54 / 0.453592)
n = float(input())
print(round(transPSI_to_kgcm2(n), 6))'''


'''while True:
    x = int(input())
    if (x <= 9 ) and (x>=0):
        break
for i in range(1, 11):  # Draw Rectangle
    if i <=4 :
        for j in range(6):
            if i == 1 or i == 4:
                print(x, end=' ')
            else:
                if j == 0 or j == 5:
                    print(x, end =' ')
                else:
                    print(' ', end= ' ')
        print()
    else:
        for j in range(1, 6+1-(i-4)):
            print("", end = ' ')
        #print('',end=' ')
        for k in range(1, 1 + i-4):
            if (i >=6 and i < 10):
                if k == 1 or k == 1+i-4-1:
                    print(x, end=' ')
                else:
                    print(' ', end=' ')
            else:
                print(x, end= ' ')
        print()'''

#Fibonaci
'''def Fibonaci(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return Fibonaci(x-1) + Fibonaci(x-2)

if __name__=='__main__':
        x = int(input())
        if (x >= 1) and (x <= 30):
            print(Fibonaci(x))
        else:
             print(f'So {x} khong nam trong khoang [1,30].')'''


#so gan may man
'''def sumDivisor(n):
    sum = 1
    a = int(n**(1/2))
    for i in range(2, a + 1):
        if n % i == 0:
            if (i == n/i):
                sum += i
            else:
                sum += i + n/i
    return sum
i = int(input())
print(int(sumDivisor(i)))'''

#Xu li chuoi
'''s = input()
s = s.lower()
s = s.replace('a', '')
s = s.replace('o', '')
s = s.replace('y', '')
s = s.replace('e', '')
s = s.replace('u', '')
s = s.replace('i', '')
lst = []
for i in s:
    lst.append(i)
#s = '.'.join(s.split(''))
ans = '.'.join(lst)
print(f'.{ans}')'''

#So gan may man
'''def luckyNum(n):
    for i in n:
        if i != '4' or i != '7':
            return False
    return True
def neLucky(n):
    if luckyNum(n):
        return False
    sumLuckyNum = 0
    for i in n:
        if i == '4' or i == '7':
            sumLuckyNum += 1
    print(sumLuckyNum)
    if sumLuckyNum == 4 or sumLuckyNum == 7:
        return True
    else:
        return False
if __name__ == '__main__':
    n = input()
    if (neLucky(n)):
        print('YES')
    else:
        print('NO')'''
'''
dem = 0
for i in range(lens - 2)
s[i] != s[i+1]
dem += 1

dem % 2 ==0 Win '''

'''s = input()
dem = 0
for i in range(len(s)-2):
    if s[i] != s[i+1]:
        dem += 1
if dem % 2 != 0:
        print('Win')
else:
    print('Lose')'''
'''k, t = map(int, input().split())
i = t // k
if i == 0:
    print(t)
elif i % 2 == 0:
    print(t % (i*k))
else:
    print((i+1)*k-t)'''


'''def min_fold(n, m, h, w):
    if (n <= h and m <= w) or (n <= w and m <= h):
        return 0
    count = 0
    while (n > max(h, w)):
        n = n/2
        count += 1
    while (m > max(h, w)):
        m = m / 2
        count += 1
    x = min(n, m)
    while (x > min(h, w)):
        x = x / 2
        count += 1
    return count
if __name__ == '__main__':
    n, m, h, w = map(int, input().split())
    minFold = min_fold(n, m, h, w)
    print(minFold)'''
'''import math
a = float(input())
b = float(input())
c = float(input())

delta = b**2 - 4*a*c
if delta < 0:
    print('PTVN')
elif delta == 0:
    print(f'PT co nghiem kep: x1 = x2 = {-b/(2*a):g}')
else:
    sqrt_delta = math.sqrt(delta)
    print('PT co hai nghiem phan biet:')

    print(f'x1 = {(-b + sqrt_delta)/(2*a):g}')
    print(f'x2 = {(-b-sqrt_delta)/(2*a):g}')'''

          
'''        dist = 0
    for i in range 5
        row = llisst )map,input
for j range 4
if row j == 1
dist = abs)i-2 + abs(j-2
                     print(dist))'''
# for i in range(5):
#     row = list(map(int, input().split()))
#     for j in range(5):
#         if row[j] == 1:
#             dist = (abs(i-2)+abs(j-2))
# print(dist)
# n = int(input())

# 1 -> 9  
#  return 9 % 1
# 10 -> 99
# return  13 = 9 + 4
#             29
#             49

# N = int(input())

# Sum = 0
# for i in range(N):
#     tt, SoTien = input().split()
#     if tt == 'D':
#         Sum += int(SoTien)
#     else:
#         Sum -= int(SoTien)
# print(Sum)

'''def demSo(n, m):
    count = 0
    temp = int(n)
    a, b = int(n), int(m)
    if int(n) > int(m):
        return 0
    elif n == m:
        return 1
    else:
        if len(m) == len(n):
            return 1
        else:
            i = len(m)
            num = 0
            while(i > len(n)):
                count += int(m[len(m)-i])*(10**(i-len(n)-1))
                num = int(m[len(m)-i])*(10**(i-1))+num
                i -= 1
            if b >= (num+a):
                count += 1
    return count                
n, m = input().split()
count = demSo(n, m)
print(count)'''


'''def checkPrimeNum(n):
    a = int(n**(1/2))
    for i in range(2, a+1):
        if n % i == 0:
            return False
    return True
def searchSecPriNum(n):
    a = 0
    while n >= 2:
        if checkPrimeNum(n) == True:
            a += 1
        if a == 2:
            return n
        n -= 1
n = int(input())
print(searchSecPriNum(n))
'''

Can = ['CANH', 'TAN', 'NHAM', 'QUY', 'GIAP', 'AT', 'BINH', 'DINH', 'MAU', 'KY']
Chi = ['THAN', 'DAU', 'TUAT', 'HOI', "TY'", 'SUU', 'DAN', 'MAO', 'THIN', 'TY.', 'NGO', 'MUI']
year = input()

if int(year) < 0:
    a = int(year) + 300
    year = str(a)
    print(year)
TenCan = Can[int(year[len(year)-1])]
TenChi = Chi[((int(year)) % 12)]
print(TenCan, TenChi)
