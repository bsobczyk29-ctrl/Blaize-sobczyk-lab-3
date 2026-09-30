# Function that adds two numbers
def add(x,y):
    print(x+y)

    


# Function that adds two numbers
def sub(x,y):
    print(x-y)



# Function that adds two numbers
def multi(x,y):
    print(x*y)



# Function that adds two numbers
def div(x,y):
    print(x/y)


print("welcome to my amazing calc app!!!")
print("what would you like to do?")
print("type (a)dd (s)ubtract (m)ultiply (d)ivide (q)uit")

user_choice = input(": ")
#print(user_choice) 
while(True):
    if user_choice == 'a':
        x=int(input("Enter the first number"))
        y=int(input("Enter the second number"))
        add(x,y)
    elif user_choice == 's':
        
        x=int(input("Enter the first number"))
        y=int(input("Enter the second number"))
        sub(x,y)
    elif user_choice == 'm':
        
        x=int(input("Enter the first number"))
        y=int(input("Enter the second number"))
        multi(x,y)

    elif user_choice == 'd':
        
        x=int(input("Enter the first number"))
        y=int(input("Enter the second number"))
        div(x,y)
    elif user_choice == 'q':
        print("shutting down")
        break
    else:
        print("invlid input")