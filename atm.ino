#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP085.h>
#include <ros.h>
#include <std_msgs/Float64MultiArray.h>
 
ros::NodeHandle nh;
 
std_msgs::Float64MultiArray atm_data;
ros::Publisher chatter("atm_data", &atm_data);
 
// Define sensor pins
const int MQ3Pin = A9;
const int MQ4Pin = A3;
const int MQ7Pin = A6;
const int MIX8410Pin = A4;
const int BMP180PinSDA = 20;
const int BMP180PinSCL = 21;
const int MG811Pin = A1;
 
// Calibration values
const float MQ3_RL = 10.0;  // Resistance of the load resistor for MQ3 sensor
const float MQ4_RL = 10.0;  // Resistance of the load resistor for MQ4 sensor
const float MQ7_RL = 10.0;  // Resistance of the load resistor for MQ7 sensor
const float MG811_ZeroPointVoltage = 0.22; // Replace with your MG811 sensor's zero point voltage
 
// Objects for sensors
Adafruit_BMP085 bmp;
 
void setup() {
  Serial.begin(9600);
  Wire.begin();
  bmp.begin();
  nh.initNode();
  nh.advertise(chatter);
}
 
void loop() {
  // Read analog values from sensors
  int MQ3Value = analogRead(MQ3Pin);
  int MQ4Value = analogRead(MQ4Pin);
  int MQ7Value = analogRead(MQ7Pin);
  int MIX8410Value = analogRead(MIX8410Pin);
  int MG811Value = analogRead(MG811Pin);
 
  // Convert analog values to physical quantities
  float MQ3AlcoholConcentration = calculateMQ3AlcoholConcentration(MQ3Value);
  float MQ4MethaneConcentration = calculateMQ4MethaneConcentration(MQ4Value);
  float MQ7COConcentration = calculateMQ7COConcentration(MQ7Value);
  float OxygenConcentration = calculateOxygenConcentration(MIX8410Value);
  float Pressure = bmp.readPressure() / 100.0;  // Pressure in hPa
  float CO2Concentration = calculateCO2Concentration(MG811Value);
 
  // Print the sensor readings
  Serial.print("MQ3 Alcohol Concentration: ");
  Serial.print(MQ3AlcoholConcentration, 5);
  Serial.println(" ppm");
 
  Serial.print("MQ4 Methane Concentration: ");
  Serial.print(MQ4MethaneConcentration, 5);
  Serial.println(" ppm");
 
  Serial.print("MQ7 CO Concentration: ");
  Serial.print(MQ7COConcentration, 5);
  Serial.println(" ppm");
 
  Serial.print("Oxygen Concentration: ");
  Serial.print(OxygenConcentration, 5);
  Serial.println(" ppm");
 
  Serial.print("Pressure: ");
  Serial.print(Pressure);
  Serial.println(" hPa");
 
  Serial.print("CO2 Concentration: ");
  Serial.print(CO2Concentration, 5);
  Serial.println(" ppm");
 
 
  float data[6] = {MQ3AlcoholConcentration,MQ4MethaneConcentration,MQ7COConcentration,OxygenConcentration,Pressure,CO2Concentration};
  atm_data.data = data;
  atm_data.data_length = 6;
  chatter.publish(&atm_data);
  nh.spinOnce();
 
  delay(1000);
}
 
// Define your calibration functions for each sensor here
float calculateMQ3AlcoholConcentration(int rawValue) {
  
  return map(rawValue, 0, 1023, 0, 1);  
}
 
float calculateMQ4MethaneConcentration(int rawValue) {
 
  return map(rawValue, 0, 1023, 1.7, 1.9); 
}
 
float calculateMQ7COConcentration(int rawValue) {
 
  return map(rawValue, 0, 1023, 0, 0.1); 
}
 
float calculateOxygenConcentration(int rawValue) {
  
  return map(rawValue, 0, 1023, 190000, 210000);  
}
 
float calculateCO2Concentration(int rawValue) {
  
  return map(rawValue, 0, 1023, 300, 400);  
}
