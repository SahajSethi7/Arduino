const int sensorPin = A0;
int baselineValue = 0;

void setup() {
  Serial.begin(9600);
  // Perform calibration
  baselineValue = calibrateSensor();
}

void loop() {
  int sensorValue = analogRead(sensorPin);
  float voltage = sensorValue * (5.0 / 1023.0); // Convert sensor value to voltage
  float alcoholConcentration = map(voltage, 0.1, 5.0, 0, 100); // Map voltage to alcohol concentration range

  // Adjust the sensor value by subtracting the baseline value
  float adjustedSensorValue = sensorValue - baselineValue;

  Serial.print("Sensor Value: ");
  Serial.print(sensorValue);
  Serial.print(", Voltage: ");
  Serial.print(voltage);
  Serial.print("V, Alcohol Concentration: ");
  Serial.print(alcoholConcentration);
  Serial.print("%, Adjusted Sensor Value: ");
  Serial.println(adjustedSensorValue);

  delay(1000);
}

int calibrateSensor() {
  // Read the sensor value multiple times and calculate the average
  int totalReadings = 10;
  int sum = 0;

  for (int i = 0; i < totalReadings; i++) {
    int sensorValue = analogRead(sensorPin);
    sum += sensorValue;
    delay(100);
  }

  int averageValue = sum / totalReadings;
  return averageValue;
}
