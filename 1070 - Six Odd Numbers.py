x = int(input())
a = []
i = 0
while True:
    if x%2!=0:
       print(x)
       a.append(x)
       if len(a)==6:
           break
    x+=1
----------------------------------------------------------------------------------------------------------------------------------------
x = int(input())
i = 0
while i<6:
    if x%2!=0:
       print(x)
       i+=1
    x+=1
    
