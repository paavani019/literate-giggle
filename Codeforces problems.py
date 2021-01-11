# 1). 1031A
w,h,k=map(int,input().split())
ans=0
for i in range(k):
    ans+=(w+h)*2-4
    w-=4;h-=4;
print(ans)

# 2). 1030A
n=int(input())
print(('EASY', 'HARD')['1' in input()])

# 3). 1095A
n=int(input());s=input()
ans="";x=0;i=0
while(i<n):
          ans+=s[i]
          x+=1
          i+=x
print(ans)

# 4). 1102A
print((int(input())+1)//2%2)

# 5). 1061A

# 6). 1064A

# 7). 1096A
for _ in [0]*int(input()):
 l,r=map(int,input().split())
 print(l,2*l)

# 8). 965A

# 9). 1208A

# 10). 160A
n = input()
coins = input().split()
coins = list(map(int, coins))
coins.sort(reverse=True)
avg = sum(coins)/2

count = 0
ownCoins = 0

for coin in coins:
    ownCoins += coin
    count += 1
    if ownCoins > avg:
        break

print(count)

# 11). 71A
n = int(input())
for i in range(n):
    s = input()
    ans = s[0] + str(len(s) - 2) + s[-1] if len(s) > 10 else s
    print(ans)
    
# 12). 1A
n,m,a=map(int,input().split()) 

if m%a==0: 
 d1=m//a 
else: 
 d1=m//a+1 
  
if n%a==0: 
 d2=n//a 
else: 
 d2=n//a+1 
  
print(d1*d2)

# 13). 339A
s = input()
n1 = n2 = n3 = 0

for i in range(0, len(s), 2):
    if s[i] == '1':
        n1 += 1
    elif s[i] == '2':
        n2 += 1
    else:
        n3 += 1

x = "1+" * n1 + "2+" * n2 + "3+" * n3
print(x[:-1])

# 14). 263A
for i in range(5):
    a = input().split()
    
    for j in range(5):
        if a[j] == '1':
            x = i
            y = j

print(abs(x-2)+abs(y-2))

# 15). 705A
n = int(input())
a = ["hate", "love"] * n
print("I"," that I ".join(a[:n]),"it")

# 16). 82A
n=int(input())-1
while n>4:
    n=n-5>>1
print(["Sheldon","Leonard","Penny","Rajesh","Howard"][n])

# 17). 96A
s = input()

if '0' * 7 in s or '1' * 7 in s:
    print('YES')
else:
    print('NO')
    
# 18). 112A
a, b = input().lower(), input().lower()
print(-1 if a < b else (1 if a > b else 0))

# 19). 282A

n = int(input(''))
x = 0
list = []

for i in range(0,n):
    s = str(input(''))
    l = s.split("X")

    for items in l:
        
        if(items != ''):
            if(items == '++'):
                x = x + 1
            elif(items == '--'):
                x = x - 1
print(x,end=" ")

# 20). 50A
m, n = map(int, input().split())
if m == 1 and n == 1:
    print(0)
else:
    print(int(m * n) // 2)
