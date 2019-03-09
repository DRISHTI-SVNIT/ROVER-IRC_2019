#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>
#include <SFE_BMP180.h>
#include <EEPROM.h>
#include <Wire.h>

#define DHTTYPE DHT22  
int soil_moist= A0;    //fc-28
int air_quality = A1;  //mq135
int DHT_pin = A2;      //dht22
//int temp_press= A3;    //bmp180
float x,y,m = 0;
float Temp,Hum;



DHT dht(DHT_pin, DHTTYPE);
SFE_BMP180 pressure;

#define ALTITUDE 100.0 //write your base altitude


void setup() 
{
   Serial.begin(9600);
  dht.begin();
  pressure.begin(); 
  
}

void loop() 
{
   x=analogRead(soil_moist);
   m=x*100/1023;
   Serial.print(x);
   Serial.print("\t");
   delay(10);

    y=analogRead(air_quality);
    Serial.print(y);
    Serial.print("\t");
    delay(10);

     char status;
  double T, P, p0, a;


  status = pressure.startTemperature();
  if (status != 0)
  {
    delay(status);

    status = pressure.getTemperature(T);
    if (status != 0)
    {
      Serial.print(T, 2);
      Serial.print("\t");
      

      status = pressure.startPressure(3);
      if (status != 0)
      {
        delay(status);

        status = pressure.getPressure(P, T);
        if (status != 0)
        {
          Serial.print(P, 2);
          Serial.print("\t");
        }
        else Serial.println("error retrieving pressure measurement\n");
      }
      else Serial.println("error starting pressure measurement\n");
    }
    else Serial.println("error retrieving temperature measurement\n");
  }
  else Serial.println("error starting temperature measurement\n");  

    Serial.println(" ");

}
