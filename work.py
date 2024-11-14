#twting
# Enter your code here
num1= int(input("Choose a number"))
num2= int(input("Choose a number"))
sumOfnums = 0

for i in range(num1, num2+1):
	sumOfnums += i

print(sumOfnums)



# Enter your code here
n= int(input("value of i"))
sumOfN= 1

for i in range(1,n+1):
    sumOfN*=i
    
print(sumOfN)




dice = ["1","2","3","4","5","6"]
def allRolls():
    for i in dice:
        for j in dice:
            print(i + "," + j)
allRolls()