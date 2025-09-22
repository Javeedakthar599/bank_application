'''num=5
for row in range(1,num+1):
    for col in range(1,row+1):
        print('*',end=' ')
    print()

n=5
spaces=n-1
stars=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print("*",end=" ")
        spaces-=1
    print()

n=5
stars=1
spaces=0
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print("*",end=" ")
        
    print()
    stars+=1

    Wap to print 
* * * * *  
* * * *  
* * *  
* *  
* 
n=5
stars=n
spaces=0
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print("*",end=" ")
        
    print()
    stars-=1'''

n=5
stars=n
spaces=0
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print("*",end=" ")
        
    print()
    stars-=1
    spaces+=1
