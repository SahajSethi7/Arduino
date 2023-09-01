import serial
import tkinter as tk
from tkinter import ttk
import threading
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class UltrasonicGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("HC-SR04 Distance Sensor GUI")

        self.distance_label = ttk.Label(self.root, text="Distance (cm):")
        self.distance_label.pack()

        self.distance_value = ttk.Label(self.root, text="-")
        self.distance_value.pack()

        self.data = []  # List to store distance data for plotting

        self.connect_sensor()
        self.start_data_thread()
        self.setup_plot()

    def connect_sensor(self):
        self.serial_port = serial.Serial("COM5", 9600)  # Replace with your COM port

    def read_data(self):
        while True:
            line = self.serial_port.readline().decode("utf-8").strip()
            try:
                distance = float(line)
                self.distance_value.config(text=f"{distance:.2f} cm")
                self.data.append(distance)  # Append data for plotting
            except ValueError:
                pass

    def start_data_thread(self):
        thread = threading.Thread(target=self.read_data)
        thread.start()

    def setup_plot(self):
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], lw=2)
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Distance (cm)')
        self.ax.set_title('Real-time Distance Data')

    def animate(self, frame):
        self.line.set_data(range(len(self.data)), self.data)
        self.ax.relim()
        self.ax.autoscale_view()

    def run(self):
        ani = FuncAnimation(self.fig, self.animate, blit=False, interval=1000)
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = UltrasonicGUI(root)
    app.run()
