import tkinter as tk
from tkinter import ttk
import serial
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

# Initialize the serial connection to Arduino
ser = serial.Serial('COM5', 9600)  

# Create the main application window
root = tk.Tk()
root.title("Oxygen Concentration Monitor")

# Create a label to display the concentration value
label = ttk.Label(root, text="O2 Concentration (ppm):")
label.pack()

# Create a variable to hold the concentration value
concentration = tk.StringVar()
concentration.set("0.00 ppm")

# Create a label to display the current time
time_label = ttk.Label(root, text="")
time_label.pack()

# Create a figure for the plot
fig, ax = plt.subplots(figsize=(8, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Initialize data for the plot
x_data = []
y_data = []

# Function to update the concentration value and plot
def update_concentration():
    try:
        # Read data from the serial port (assuming it sends data as "o2_value\n")
        line = ser.readline().decode().strip()
        o2_value = float(line)
        concentration.set(f"{o2_value:.2f} ppm")

        # Append data to the plot
        x_data.append(time.strftime("%H:%M:%S"))
        y_data.append(o2_value)
        ax.clear()
        ax.plot(x_data, y_data, marker='o', linestyle='-')
        ax.set_xlabel("Time")
        ax.set_ylabel("O2 Concentration (ppm)")
        ax.set_title("O2 Concentration Over Time")
        canvas.draw()

        # Update the time label
        time_label.config(text=f"Time: {time.strftime('%H:%M:%S')}")

        # Schedule the function to run again after a delay (in milliseconds)
        root.after(1000, update_concentration)

    except Exception as e:
        print(f"Error: {e}")

# Start the update_concentration function
update_concentration()

# Start the GUI main loop
root.mainloop()

# Close the serial connection when the GUI is closed
ser.close()
