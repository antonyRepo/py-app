import tkinter as tk
from tkinter import messagebox
import sqlite3

class CarSalesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Sales Application")
        self.root.geometry("400x300")

        # Initialize database
        self.initialize_database()

        # Create input fields
        self.create_widgets()

    def initialize_database(self):
        # Connect to SQLite database (or create it if it doesn't exist)
        self.conn = sqlite3.connect("car_sales.db")
        self.cursor = self.conn.cursor()

        # Create a table to store car sales details
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                car_model TEXT,
                color TEXT,
                price REAL,
                customer_name TEXT
            )
        """)
        self.conn.commit()

    def create_widgets(self):
        # Labels and Entry fields
        tk.Label(self.root, text="Car Model:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.car_model_entry = tk.Entry(self.root)
        self.car_model_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Color:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.color_entry = tk.Entry(self.root)
        self.color_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Price:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.price_entry = tk.Entry(self.root)
        self.price_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Customer Name:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.customer_name_entry = tk.Entry(self.root)
        self.customer_name_entry.grid(row=3, column=1, padx=10, pady=5)

        # Submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_sale)
        self.submit_button.grid(row=4, column=0, columnspan=2, pady=10)

    def submit_sale(self):
        # Get input values
        car_model = self.car_model_entry.get()
        color = self.color_entry.get()
        price = self.price_entry.get()
        customer_name = self.customer_name_entry.get()

        # Validate inputs
        if not car_model or not color or not price or not customer_name:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        try:
            price = float(price)  # Convert price to a float
        except ValueError:
            messagebox.showwarning("Input Error", "Price must be a number.")
            return

        # Save the sale to the database
        self.cursor.execute("""
            INSERT INTO sales (car_model, color, price, customer_name)
            VALUES (?, ?, ?, ?)
        """, (car_model, color, price, customer_name))
        self.conn.commit()

        # Fetch the saved details from the database
        self.cursor.execute("SELECT * FROM sales WHERE id = ?", (self.cursor.lastrowid,))
        sale_details = self.cursor.fetchone()

        # Display the saved details
        if sale_details:
            messagebox.showinfo(
                "Sale Submitted",
                f"Sale Details:\n\n"
                f"Car Model: {sale_details[1]}\n"
                f"Color: {sale_details[2]}\n"
                f"Price: ${sale_details[3]:.2f}\n"
                f"Customer Name: {sale_details[4]}"
            )

        # Clear input fields
        self.car_model_entry.delete(0, tk.END)
        self.color_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.customer_name_entry.delete(0, tk.END)

    def __del__(self):
        # Close the database connection when the program ends
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = CarSalesApp(root)
    root.mainloop()