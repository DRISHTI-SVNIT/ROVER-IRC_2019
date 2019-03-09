
#include <DHT.h>
#define DHTTYPE DHT22  
int DHT_pin=A2;

DHT dht(DHT_pin, DHTTYPE); 

float Temp,Hum ;

void setup() 
{
  Serial.begin(9600);
  Serial.println("Sensor is Reading :");
  dht.begin();

}

void loop()
{
    hum = dht.readHumidity();
    temp= dht.readTemperature();

        Serial.print("Temperature : ");
        Serial.print(temp);
        Serial.println("Celsius")

        Serial.print("Humidity : ");
        Serial.println(hum);
        delay(1000);
}
