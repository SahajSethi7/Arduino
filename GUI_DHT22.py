import tkinter as tk
from tkinter import ttk
import Adafruit_DHT
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

# DHT sensor setup
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 9  # Change this to the appropriate GPIO pin number

# Create the main application window
root = tk.Tk()
root.title("Temperature and Humidity Monitor")

# Create labels to display temperature and humidity
temperature_label = ttk.Label(root, text="Temperature: N/A °C")
temperature_label.pack()

humidity_label = ttk.Label(root, text="Humidity: N/A %")
humidity_label.pack()

# Create a label to display the current time
time_label = ttk.Label(root, text="")
time_label.pack()

# Create a function to update temperature and humidity values
def update_sensor_values():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        if humidity is not None and temperature is not None:
            temperature_label.config(text=f"Temperature: {temperature:.2f} °C")
            humidity_label.config(text=f"Humidity: {humidity:.2f} %")
        else:
            temperature_label.config(text="Temperature: N/A")
            humidity_label.config(text="Humidity: N/A")

        # Update the time label
        current_time = time.strftime("%H:%M:%S")
        time_label.config(text=f"Time: {current_time}")

        # Delay for reading and updating every 2 seconds
        time.sleep(2)

# Create a figure for plotting
fig, ax = plt.subplots(figsize=(8, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Start the sensor update function in a separate thread
import threading
sensor_thread = threading.Thread(target=update_sensor_values)
sensor_thread.daemon = True
sensor_thread.start()

# Start the GUI main loop
root.mainloop()
