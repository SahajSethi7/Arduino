// MQ-131 Ozone Gas Sensor integration with Arduino Mega

int analogPin = A2;   // Analog input pin for the MQ-131 sensor

float ozoneConcentration;   // Variable to store ozone concentration

// Calibration values
const float sensorMin = 0.0;   // Minimum analog reading from the sensor
const float sensorMax = 1023.0;   // Maximum analog reading from the sensor
const float ozoneMin = 0.0;   // Minimum ozone concentration
const float ozoneMax = 10.0;   // Maximum ozone concentration

void setup() {
  Serial.begin(9600);
}

void loop() {
  // Read the analog voltage from the sensor
  int sensorValue = analogRead(analogPin);
  
  // Map the analog value to ozone concentration
  ozoneConcentration = mapFloat(sensorValue, sensorMin, sensorMax, ozoneMin, ozoneMax);
  
  // Print the ozone concentration
  Serial.print("Ozone Concentration: ");
  Serial.print(ozoneConcentration);
  Serial.println(" ppm");
  
  delay(1000);  // Delay between readings
}

// Map a float value from one range to another range
float mapFloat(float x, float inMin, float inMax, float outMin, float outMax) {
  return (x - inMin) * (outMax - outMin) / (inMax - inMin) + outMin;
}

