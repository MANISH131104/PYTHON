age = int(input("Enter your age : "))

# if statement no:1
if(age%2==0):
    print("age is even")
# End of if statement n0:1    


# if statement no:2
if(age>=18): 
    print("Yor are above the age of consent")
    print("Good for you")


elif(age<0):
    print("You are entering an invalid age ")   


elif(age==0):
    print("You are entering 0 which is not a valid age")    


else:
    print("Yor are below the age of consent")
# End of if statement no:2

print("End of Programe")