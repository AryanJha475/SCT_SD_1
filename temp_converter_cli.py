# temp_converter_cli.py
def c_to_f(c): return (c * 9/5) + 32
def c_to_k(c): return c + 273.15
def f_to_c(f): return (f - 32) * 5/9
def k_to_c(k): return k - 273.15
def f_to_k(f): return f_to_c(f) + 273.15
def k_to_f(k): return c_to_f(k_to_c(k))

def run():
    print("🌡 Temperature Converter (CLI)")
    print("1) Celsius  -> Fahrenheit & Kelvin")
    print("2) Fahrenheit -> Celsius & Kelvin")
    print("3) Kelvin  -> Celsius & Fahrenheit")
    choice = input("Choose (1/2/3): ").strip()
    try:
        if choice == "1":
            c = float(input("Enter °C: "))
            print(f"{c:.2f} °C = {c_to_f(c):.2f} °F")
            print(f"{c:.2f} °C = {c_to_k(c):.2f} K")
        elif choice == "2":
            f = float(input("Enter °F: "))
            print(f"{f:.2f} °F = {f_to_c(f):.2f} °C")
            print(f"{f:.2f} °F = {f_to_k(f):.2f} K")
        elif choice == "3":
            k = float(input("Enter K: "))
            print(f"{k:.2f} K = {k_to_c(k):.2f} °C")
            print(f"{k:.2f} K = {k_to_f(k):.2f} °F")
        else:
            print("❌ Invalid choice")
    except ValueError:
        print("❌ Please enter a valid number")

if __name__ == "__main__":
    run()
