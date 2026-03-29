# Shiva-coder: Engineering Temperature Converter
def temp_converter():
    print("--- Shiva's Thermal Lab ---")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Exit")

    while True:
        choice = input("\nSelect conversion (1/2/3): ")

        if choice == '1':
            c = float(input("Enter Temp in Celsius: "))
            f = (c * 9/5) + 32
            print(f"==> {c}°C is {f}°F")
        
        elif choice == '2':
            c = float(input("Enter Temp in Celsius: "))
            k = c + 273.15
            print(f"==> {c}°C is {k} Kelvin")
            
        elif choice == '3':
            print("Closing Thermal Lab. Good luck in BME tomorrow!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

temp_converter()
