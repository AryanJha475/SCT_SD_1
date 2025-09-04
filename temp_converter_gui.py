# temp_converter_gui.py
import tkinter as tk
from tkinter import ttk, messagebox

def c_to_f(c): return (c * 9/5) + 32
def c_to_k(c): return c + 273.15
def f_to_c(f): return (f - 32) * 5/9
def k_to_c(k): return k - 273.15

def convert():
    try:
        val = float(inp.get())
        scale = sel.get()
        if scale == "Celsius":
            c = val; f = c_to_f(c); k = c_to_k(c)
        elif scale == "Fahrenheit":
            f = val; c = f_to_c(f); k = c_to_k(c)
        else:  # Kelvin
            k = val; c = k_to_c(k); f = c_to_f(c)
        out.set(f"Celsius: {c:.2f} °C\nFahrenheit: {f:.2f} °F\nKelvin: {k:.2f} K")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")

app = tk.Tk()
app.title("Temperature Converter")
app.geometry("360x300"); app.resizable(False, False)

tk.Label(app, text="Enter Temperature:", font=("Arial", 12)).pack(pady=6)
inp = tk.Entry(app, font=("Arial", 12)); inp.pack(pady=4)

tk.Label(app, text="Input Scale:", font=("Arial", 12)).pack(pady=6)
sel = ttk.Combobox(app, values=["Celsius","Fahrenheit","Kelvin"], font=("Arial", 12), state="readonly")
sel.current(0); sel.pack(pady=4)

tk.Button(app, text="Convert", font=("Arial", 12), command=convert).pack(pady=10)
out = tk.StringVar()
tk.Label(app, textvariable=out, font=("Arial", 12), justify="center").pack(pady=10)

app.mainloop()
