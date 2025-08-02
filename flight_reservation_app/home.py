import tkinter as tk
from datetime import datetime
from tkinter import ttk, messagebox
import booking
import database

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Reservation App")
        self.create_tabs()

    def create_tabs(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=1, fill='both')

        self.reservation_frame = tk.Frame(self.notebook)
        self.notebook.add(self.reservation_frame, text="Book a flight")
        self.create_reservation_form(self.reservation_frame)

        self.flights = tk.Frame(self.notebook)
        self.notebook.add(self.flights, text="View Reservations")
        self.get_reservations(self.flights)

    def create_reservation_form(self, parent):
        tk.Label(parent, text="Flight Reservation Form", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(parent, text="Name:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.name_entry = tk.Entry(parent)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(parent, text="Flight Number:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.flight_num_entry = tk.Entry(parent)
        self.flight_num_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(parent, text="Destination:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        self.destination_entry = tk.Entry(parent)
        self.destination_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(parent, text="Date (YYYY-MM-DD):").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        self.date_entry = tk.Entry(parent)
        self.date_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(parent, text="Seat Number:").grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
        self.seat_num_entry = tk.Entry(parent)
        self.seat_num_entry.grid(row=5, column=1, padx=10, pady=5)

        self.reserve_button = tk.Button(parent, text="Reserve", command=self.reserve)
        self.reserve_button.grid(row=6, column=0, columnspan=2, pady=10)

    def reserve(self):
        name = self.name_entry.get()
        flight_number = self.flight_num_entry.get()
        destination = self.destination_entry.get()
        seat_number = self.seat_num_entry.get()
        date = self.date_entry.get()
        if not all([name, flight_number, destination, date, seat_number]):
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        try:
            date = datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            messagebox.showerror("Input Error", "Incorrect date format, should be YYYY-MM-DD.")
            return
        


        messagebox.showinfo("Reservation Successful", f"Flight reserved successfully!\n\n"
                                                      f"Name: {name}\n"
                                                      f"Flight Number: {flight_number}\n"
                                                      f"Destination: {destination}\n"
                                                      f"Date: {date}\n"
                                                      f"Seat Number: {seat_number}")
        
        booking.reserve(booking.register_data(name, flight_number, destination, date, seat_number))

    def get_reservations(self, parent):
        for widget in parent.winfo_children():
            widget.destroy()  # Clear previous widgets

        tk.Label(parent, text="Flight Reservations", font=("Arial", 16)).pack(pady=10)

        columns = ("No", "Name", "Flight", "Destination", "Date", "Seat")
        self.tree = ttk.Treeview(parent, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(expand=1, fill='both', padx=10, pady=10)

        reservations = booking.database.fetch_all_reservations()
        if not reservations:
            tk.Label(parent, text="No reservations found.").pack()
            return

        for r in reservations:
            self.tree.insert("", "end", values=r)

        menu = tk.Menu(self.root, tearoff=0)
        menu.add_command(label="Edit", command=self.edit_reservation)
        menu.add_command(label="Delete", command=self.delete_reservation)

        def on_right_click(event):
            selected = self.tree.identify_row(event.y)
            if selected:
                self.tree.selection_set(selected)
                menu.post(event.x_root, event.y_root)

        self.tree.bind("<Button-3>", on_right_click)

    def edit_reservation(self):
        selected = self.tree.selection()
        if not selected:
            return
        values = self.tree.item(selected[0], "values")
        messagebox.showinfo("Edit", f"Edit reservation: {values}")

    def delete_reservation(self):
        selected = self.tree.selection()
        if not selected:
            return
        values = self.tree.item(selected[0], "values")
        database.delete_data(values[0])
        messagebox.showinfo("Delete", f"Delete reservation: {values}")
        self.tree.delete(selected[0])