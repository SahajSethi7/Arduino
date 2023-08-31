import serial
import tkinter as tk
from tkinter import ttk
import threading

class UltrasonicGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("HC-SR04 Distance Sensor GUI")

        self.distance_label = ttk.Label(self.root, text="Distance (cm):")
        self.distance_label.pack()

        self.distance_value = ttk.Label(self.root, text="-")
        self.distance_value.pack()

        self.connect_sensor()
        self.start_data_thread()

    def connect_sensor(self):
        self.serial_port = serial.Serial("COM5", 9600)  # Replace with your COM port

    def read_data(self):
        while True:
            line = self.serial_port.readline().decode("utf-8").strip()
            try:
                distance = float(line)
                self.distance_value.config(text=f"{distance:.2f} cm")
            except ValueError:
                pass

    def start_data_thread(self):
        thread = threading.Thread(target=self.read_data)
        thread.start()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = UltrasonicGUI(root)
    app.run()


