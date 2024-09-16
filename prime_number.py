number=int(input())
factors=0
for i in range(1,number+1):
    if(number%i==0):
        factors+=1 
if(factors==0):
    print("Prime")
else:
    print("Non-Prime")
