const int sensorPin = 4;  // Pin connected to the output of the proximity sensor

void setup() {
  Serial.begin(9600);  // Initialize the serial communication
  pinMode(sensorPin, INPUT);  // Set the sensor pin as an input
}

void loop() {
  int sensorValue = digitalRead(sensorPin);  // Read the state of the sensor pin

  if (sensorValue == HIGH) {
    Serial.println("Object Detected");  // Print a message if an object is detected
  } else {
    Serial.println("No Object Detected");  // Print a message if no object is detected
  }

  printSensorValue(sensorValue);  // Call the function to print the sensor value

  delay(500);  // Add a small delay between readings
}

void printSensorValue(int value) {
  Serial.print("Sensor Value: ");
  Serial.println(value);
}


