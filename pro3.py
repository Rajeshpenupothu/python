a="hello"
reversed=""
print(a[::-1])

a="Hello"
reversed=""
index=len(a)-1
while index>=0:
    reversed +=a[index]
    index -=1
print(reversed)    