n=input()
l=n.split()
a=int(l[0])
b=int(l[1])
s1="-"
s2=".|."
t=(b//2)-1
u=1
for i in range(0,a//2):
    print(s1*t+s2*u+s1*t)
    t=t-3
    u+=2

print("WELCOME".center(b,"-"))

t=3
u=a-2
for i in range(0,a//2):
    print(s1*t+s2*u+s1*t)
    t=t+3
    u-=2

