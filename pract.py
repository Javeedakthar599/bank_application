'''d={"name":"javeed","age":22}
for key in d:
    print(key,d[key])


s=input()
count=0
for ch in s:
    count+=1
print(count)

s=input()
ss=input()
count=0
for ch in s:
    if ch in ss:
        count+=1
print(count)
 Wap to print how many even digits are present in given string

s=input()
count=0
for ch in s:
    if ch.isdigit():
        if int(ch)%2== 0:
            count+=1
print(count)'''

l=[2,56,1,5,8,4]
max_number=l[0]
for i in l:
    if i>max_number:
        max_number=i
print('max number is ',max_number)
