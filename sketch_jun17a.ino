const int AOUT_PIN = A1;    // Analog pin for AOUT
const int DOUT_PIN = 22;    // Digital pin for DOUT

void setup() {
  Serial.begin(9600);       // Initialize Serial Monitor
  
  pinMode(DOUT_PIN, INPUT); // Set DOUT pin as input
}

void loop() {
  int sensorValue = analogRead(AOUT_PIN);   // Read analog value from AOUT pin
  int digitalValue = digitalRead(DOUT_PIN); // Read digital value from DOUT pin
  
  // Calibration: Determine the baseline value in an environment with no CO
  int baselineValue = 0;                    // Adjust this value based on calibration
  
  // Adjust the sensor value by subtracting the baseline value
  int adjustedSensorValue = sensorValue - baselineValue;
  
  // Print the sensor values to the Serial Monitor
  Serial.print("Analog Value: ");
  Serial.print(sensorValue);
  Serial.print(", Digital Value: ");
  Serial.println(digitalValue);
  
  // Print the adjusted sensor value to the Serial Monitor
  Serial.print("Adjusted Sensor Value: ");
  Serial.println(adjustedSensorValue);
  
  delay(1000);  // Delay for a second before taking the next reading
}
