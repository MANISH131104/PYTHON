def sum(n):
    if(n==0):
        return 0
    else:
        return n+sum(n-1)
    

n = int(input("Enter number: "))
print(f"The sum of first {n} natural no. is = {sum(n)}")    