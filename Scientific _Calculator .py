import math  # استيراد مكتبة الرياضيات للعمليات المتقدمة

def scientific_calculator():
    print("====================================")
    print("   🔥 Casio-Style Calculator 🔥     ")
    print("====================================")
    print("Available Operations:")
    print(" 1. Add (+)\t\t 2. Subtract (-)")
    print(" 3. Multiply (*)\t 4. Divide (/)")
    print(" 5. Power (x^y)\t\t 6. Square Root (Sqrt)")
    print(" 7. Sine (Sin)\t\t 8. Cosine (Cos)")
    print(" 9. Tangent (Tan)\t10. Logarithm (Log10)")
    print("Type 'exit' at any time to quit.")
    print("====================================")

    while True:
        choice = input("\nSelect operation (1-10) or 'exit': ").strip()

        if choice.lower() == 'exit':
            print("Thank you for using Casio Calculator. Goodbye! 👋")
            break

        # Operations that require TWO numbers (1 to 5)
        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("⚠️ Error! Please enter valid numbers.")
                continue

            if choice == '1':
                print(f"➡️ Result: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"➡️ Result: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"➡️ Result: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("⚠️ Error! Division by zero is not allowed.")
                else:
                    print(f"➡️ Result: {num1} / {num2} = {num1 / num2}")
            elif choice == '5':
                print(f"➡️ Result: {num1} ^ {num2} = {math.pow(num1, num2)}")

        # Operations that require ONE number (6 to 10)
        elif choice in ['6', '7', '8', '9', '10']:
            try:
                num = float(input("Enter the number: "))
            except ValueError:
                print("⚠️ Error! Please enter a valid number.")
                continue

            if choice == '6':
                if num < 0:
                    print("⚠️ Error! Cannot calculate square root of a negative number.")
                else:
                    print(f"➡️ Sqrt({num}) = {math.sqrt(num)}")
            
            # Conversion to radians for trigonometric functions
            elif choice == '7':
                print(f"➡️ Sin({num}°) = {math.sin(math.radians(num))}")
            elif choice == '8':
                print(f"➡️ Cos({num}°) = {math.cos(math.radians(num))}")
            elif choice == '9':
                print(f"➡️ Tan({num}°) = {math.tan(math.radians(num))}")
                
            elif choice == '10':
                if num <= 0:
                    print("⚠️ Error! Logarithm must be greater than zero.")
                else:
                    print(f"➡️ Log10({num}) = {math.log10(num)}")

        else:
            print("⚠️ Invalid choice! Please select a number from 1 to 10.")

if __name__ == "__main__":
    scientific_calculator()
