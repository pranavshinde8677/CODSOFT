def calculator():
    print("=" * 40)
    print("SIMPLE CALCULATOR")
    print("=" * 40)
    
    while True:
        print("\nAvailable Operations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '5':
                print("Thank you for using the calculator!")
                break
            
            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice! Please enter 1-5")
                continue
            
            # Get numbers from user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Perform calculation
            if choice == '1':
                result = num1 + num2
                operator = "+"
            elif choice == '2':
                result = num1 - num2
                operator = "-"
            elif choice == '3':
                result = num1 * num2
                operator = "*"
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed!")
                    continue
                result = num1 / num2
                operator = "/"
            
            # Display result
            print("-" * 30)
            print(f"RESULT: {num1} {operator} {num2} = {result}")
            print("-" * 30)
            
        except ValueError:
            print("Invalid input! Please enter numeric values.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Run the calculator
calculator()