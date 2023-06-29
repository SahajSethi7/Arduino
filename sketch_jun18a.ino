const int sensorPin = 25; // Pin connected to the SIG pin of the sensor

// Calibration parameters
const int baselineValue = 500; // Replace with your calibrated baseline value

void setup() {
  Serial.begin(9600); // Initialize Serial communication
  pinMode(sensorPin, INPUT); // Set the sensor pin as INPUT
}

void loop() {
  int sensorValue = analogRead(sensorPin); // Read the sensor value

  // Calibrate the sensor value based on the baseline value
  float calibratedValue = map(sensorValue, 0, 1023, 0, 100);
  calibratedValue = constrain(calibratedValue, 0, 100);

  // Display the calibrated value
  Serial.print("Oxygen Concentration: ");
  Serial.print(calibratedValue);
  Serial.println("%");

  delay(1000); // Delay between readings
}

