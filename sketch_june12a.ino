int AOUTpin = A3;             // Analog pin connected to AOUT of MQ4 sensor
float calibrationFactor = 1;  // Calibration factor to convert analog value to gas concentration

void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(AOUTpin);

  // Apply the calibration factor to the analog reading
  float gasConcentration = sensorValue * calibrationFactor;

  // Print the gas concentration
  Serial.print("Gas Concentration: ");
  Serial.println(gasConcentration);

  delay(1000);  // Delay between measurements
}
