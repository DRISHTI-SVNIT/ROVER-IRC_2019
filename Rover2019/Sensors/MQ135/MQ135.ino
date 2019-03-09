
int sensor_pin = A1; 
float output_value;

void setup() 
{
  Serial.println("Reading from the sensor....");
  Serial.begin(9600);
  delay(100);

}

void loop()
{
  output_value= analogRead(sensor_pin);
  Serial.println("Air Quality :");
  Serial.println(output_value);
  delay(1000);
}
