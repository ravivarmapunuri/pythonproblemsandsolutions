#2nd program gateway gala
l=list(map(str,input().split()))
N=int(input())
S=[i[0] for i in l]
s=""
for i in S:
    s+=i
print(s)
v=[]
for i in range(0,len(s)):
    for j in range(i+1,len(s)+1):
        d=s[i:j]
        if s[i:j]==d[::-1] and len(s[i:j])>2:
            v.append(i+2)
l1=[]
for i in range(len(l)):
    if i not in v:
        l1.append(l[i])
print(l1)
while True:
    for i in range(len(l1)):
        if i==N-1:
            l1.remove(l1[i])
    if len(l1)==1:
        break
print(l1)
