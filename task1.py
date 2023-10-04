def calculate(num1, num2, operator):
    if operator == 'Addition':
        return num1 + num2
    elif operator == 'Subtraction':
        return num1 - num2
    elif operator == 'Multiplication':
        return num1 * num2
    elif operator == 'Division':
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by zero is not allowed."
    else:
        return "Invalid operator."

def main():
    print("Simple Calculator")
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter the operation (Addition, Subtraction, Multiplication, Division): ")
            
            result = calculate(num1, num2, operator)
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        
        again = input("Do you want to calculate again? (yes/no): ")
        if again != 'yes':
            break
            
       
if __name__ == "__main__":
    main()


