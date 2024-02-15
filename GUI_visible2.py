import serial
import matplotlib.pyplot as plt
from collections import deque
from matplotlib.animation import FuncAnimation
import re

# Initialize serial port
ser = serial.Serial('COM6', 115200)  # Replace 'COM6' with your Arduino's serial port

# Initialize empty dequeues for storing data
time_data = deque(maxlen=100)
color_data = {
    'Violet': deque(maxlen=100),
    'Blue': deque(maxlen=100),
    'Green': deque(maxlen=100),
    'Yellow': deque(maxlen=100),
    'Orange': deque(maxlen=100),
    'Red': deque(maxlen=100)
}

# Create figure and axis objects
fig, ax = plt.subplots()
ax.set_title('Color Intensity Variation Over Time')
ax.set_xlabel('Time')
ax.set_ylabel('Intensity')

# Initialize empty lines for each color
lines = {
    'Violet': ax.plot([], [], label='Violet', color='indigo')[0],
    'Blue': ax.plot([], [], label='Blue', color='blue')[0],
    'Green': ax.plot([], [], label='Green', color='green')[0],
    'Yellow': ax.plot([], [], label='Yellow', color='gold')[0],
    'Orange': ax.plot([], [], label='Orange', color='orange')[0],
    'Red': ax.plot([], [], label='Red', color='red')[0]
}

# Function to update plot
def update_plot(frame):
    if ser.in_waiting > 0:
        # Read data from serial port
        line = ser.readline().decode().strip()
        
        # Parse the data using regular expressions
        match = re.match(r'Reading: V\[(\d+\.\d+)\] B\[(\d+\.\d+)\] G\[(\d+\.\d+)\] Y\[(\d+\.\d+)\] O\[(\d+\.\d+)\] R\[(\d+\.\d+)\]', line)
        if match:
            violet, blue, green, yellow, orange, red = map(float, match.groups())
            
            # Append data to dequeues
            time_data.append(frame)
            color_data['Violet'].append(violet)
            color_data['Blue'].append(blue)
            color_data['Green'].append(green)
            color_data['Yellow'].append(yellow)
            color_data['Orange'].append(orange)
            color_data['Red'].append(red)
            
            # Update lines data
            for color, line in lines.items():
                line.set_data(time_data, color_data[color])
            
            # Set x-axis limits if deque is not empty
            if time_data:
                ax.set_xlim(min(time_data), max(time_data))
            
    return lines.values()

# Animate the plot with frames as None
ani = FuncAnimation(fig, update_plot, frames=None, interval=1000, save_count=1000)

# Show legend
ax.legend()

# Set y-axis limits
ax.set_ylim(0, 500)

# Show plot
plt.show()
