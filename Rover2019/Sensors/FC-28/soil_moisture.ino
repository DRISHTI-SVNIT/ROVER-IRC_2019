int sensor_pin = A0; 
int output_value ;
float value=0;

void setup()
{
  Serial.begin(9600);
  Serial.println("Reading From the Sensor ...");
  delay(2000);
  }

void loop()
{

  output_value= analogRead(sensor_pin);
  value= output_value*(100)/1023;
  Serial.println("Moisture :");
  Serial.println(value);
  delay(1000);
  }
