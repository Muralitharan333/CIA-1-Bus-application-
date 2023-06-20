#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk

from tkinter import messagebox

class Bus:
    
    def __init__(self, bus_no, driver_nam, route):
        self.bus_no = bus_no
        self.driver_nam = driver_nam
        self.route = route

class BusBookingApplication:
    def __init__(self):
        self.buses = []
        self.selected_bus = None

    def add_bus(self, bus_no, driver_nam, route):
        
        bus = Bus(bus_no, driver_nam, route)
        self.buses.append(bus)

    def book_ticket(self, name, age):
        
        if self.selected_bus is None:
            messagebox.showinfo("No Bus Selected", "Please select a bus before booking a ticket.")
        else:
            
            messagebox.showinfo("Ticket Booked", f"Ticket booked for Bus No: {self.selected_bus.bus_no}\n"
                                                 f"Driver Name: {self.selected_bus.driver_nam}\n"
                                                 f"Route: {self.selected_bus.route}\n"
                                                 f"Passenger Name: {name}\n"
                                                 f"Passenger Age: {age}")

    def select_bus(self, index):
        
        if 0 <= index < len(self.buses):
            
            self.selected_bus = self.buses[index]
            
            messagebox.showinfo("Bus Selected", f"You have selected Bus No: {self.selected_bus.bus_no}")

app = BusBookingApplication()

# Adding default bus details
app.add_bus("TN 55 AR 2233", "M.K.Stalin", "Pune - Chennai")
app.add_bus("KL 07 SS 3467", "Pulimurugan", "Traivandrum - Coimbatore")
app.add_bus("MH 01 FB 1111", "Mukesh Ambani", "Navi Mumbai - Delhi")

def book_ticket():
    name = entry_name.get()
    age = entry_age.get()
    app.book_ticket(name, age)

def select_bus():
    selected_index = listbox_buses.curselection()
    if selected_index:
        app.select_bus(selected_index[0])

window = tk.Tk()
window.title("Bus Booking App")

label_buses = tk.Label(window, text="Available Buses:")
label_buses.pack()

listbox_buses = tk.Listbox(window)
listbox_buses.pack()

for bus in app.buses:
    listbox_buses.insert(tk.END, f"Bus No: {bus.bus_no} | Driver: {bus.driver_nam} | Route: {bus.route}")

label_name = tk.Label(window, text="Passenger Name:")

label_name.pack()

entry_name = tk.Entry(window)
entry_name.pack()

label_age = tk.Label(window, text="Passenger Age:")

label_age.pack()

entry_age = tk.Entry(window)
entry_age.pack()

button_select = tk.Button(window, text="Select Bus", command=select_bus)
button_select.pack()

button_book = tk.Button(window, text="Book Ticket", command=book_ticket)

button_book.pack()
window.mainloop()


# In[ ]:




