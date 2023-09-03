import tkinter as tk
from tkinter import ttk
import serial
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time  # Import the time module

# Initialize the serial connection to Arduino
ser = serial.Serial('COM5', 9600) 

# Create the main application window
root = tk.Tk()
root.title("Gas Concentration Monitor")

# Create a label to display the concentration value
label = ttk.Label(root, text="Gas Concentration (ppm):")
label.pack()

# Create a variable to hold the concentration value
concentration = tk.StringVar()
concentration.set("0.00 ppm")

# Create a label to display the current time
time_label = ttk.Label(root, text="")
time_label.pack()

# Create a function to update the concentration value
def update_concentration():
    try:
        # Read data from the serial port (assuming it sends data as "ppm_value\n")
        line = ser.readline().decode().strip()
        ppm_value = float(line)
        concentration.set(f"{ppm_value:.2f} ppm")

        # Update the time label
        current_time = time.strftime("%H:%M:%S")
        time_label.config(text=f"Time: {current_time}")

        # Update the plot
        x_data.append(current_time)
        y_data.append(ppm_value)
        ax.clear()
        ax.plot(x_data, y_data)
        ax.set_xlabel("Time")
        ax.set_ylabel("Concentration (ppm)")
        ax.set_title("Gas Concentration Over Time")
        canvas.draw()

    except Exception as e:
        print(f"Error: {e}")

    # Schedule the function to run again after a delay (in milliseconds)
    root.after(1000, update_concentration)

# Create a figure for the plot
fig, ax = plt.subplots(figsize=(8, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Initialize data for the plot
x_data = []
y_data = []

# Start the update_concentration function
update_concentration()

# Start the GUI main loop
root.mainloop()

# Close the serial connection when the GUI is closed
ser.close()
