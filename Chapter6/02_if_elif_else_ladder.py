age = int(input("Enter your age : "))

if(age>=18): 
    print("Yor are above the age of consent")
    print("Good for you")


elif(age<0):
    print("You are entering an invalid age ")   


elif(age==0):
    print("You are entering 0 which is not a valid age")    


else:
    print("Yor are below the age of consent")


print("End of Programe")