#The Calculator App
# Objective: The aim of this assignment is to build a basic calculator that can
# perform addition, subtraction, multiplication, and division.

#Task 1 - Create functions for each arithmetic operation
      

def basic_calculator ():
    print("\n Welcome to the Basic Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
#Task 2 - Use inputs to ask the user what operations they want to perform, 
# and what numbers they want to use
   
    choice = input("Choose an operation: ")
    while True:
        if choice == "1":
            try:
                num1 = float(input("Enter your first number:  "))
                num2 = float(input("Enter your second number:  "))
                print(num1 + num2)
            except: ValueError
            
            print("Invalid Response. Numbers Only)")
        elif choice == "2":
            try:
                num1 = float(input("Enter your first number:  "))
                num2 = float(input("Enter your second number:  "))
                print(num1 - num2)
            except: ValueError
            print("Invalid Response. Numbers Only)")
        elif choice == "3":
            try:
                num1 = float(input("Enter your first number:  "))
                num2 = float(input("Enter your second number:  "))
                print(num1 * num2)
            except: ValueError
            print("Invalid Response. Numbers Only)")
            
        elif choice == "4":
            try:
                num1 = float(input("Enter your first number:  "))
                num2 = float(input("Enter your second number:  "))
                if num2 ==0:
                    print("Zero cannot be the second number")
                else:
                    print(num1 / num2 )
            except: ValueError
            print("Invalid Response. Numbers Only)")
         
        
           
        elif choice == "5":
            print("Exiting Calculator")
            
            break
basic_calculator()





#Task 3 - Ensure your code can handle division by zero and other potential errors.
# So if you divide by 0, there is error handling set up to prevent an error 
# from showing in the console.
