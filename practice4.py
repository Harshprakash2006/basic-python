def factorial(n):
 
    if n==0 or n==1:
        return 1
    else :
 
        return n*factorial(n-1)
i=int(input("enter a number: "))

print("the factorial of ",i,"is",factorial(i))