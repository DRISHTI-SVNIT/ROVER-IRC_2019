/*
 * GccApplication4.c
 *
 * Created: 7/18/2018 5:43:07 PM
 * Author : HP
 */ 

#include <avr/io.h>
#include "USART_8.h"
#include "ps2new.h"
#include <math.h>
#define DDR_SPI DDRB
#define PORT_SPI PORTB
#define DD_SS PB2
#define DD_MOSI PB3
#define DD_MISO PB4
#define DD_SCK PB5
void SPI_MasterInit(void);
void SPI_MasterTransmit(char);
void SEND(char);
int x,y,j,b,c,d;
int z,w;


void SPI_MasterInit(void)
{
	SPCR=0b01111101;
	DDR_SPI= (1<<DD_MOSI)|(1<<DD_SCK);
	DDR_SPI&=~(1<<DD_MISO);
	SPCR=(1<<SPE)|(1<<MSTR)|(1<<SPR0);
	
}
void SPI_MasterTransmit(char cData)
{
	SPDR=cData;
	while(!(SPSR & (1<<SPIF)))
	{
		_delay_ms(1000);
	}
}
/*void SEND(char *str)
{
	int i=0;
	while(str[i]!='\0')
	{
		SPI_MasterTransmit(str[i]);
		i++;
		_delay_ms(30);

	}
}
*/
void SEND(char str)
{
	
		SPI_MasterTransmit(str);
		
		_delay_us(30);

	
}
int main()
{
	       
			DDRD=0xFF;
			PORTD=0x00;
			SPI_MasterInit();
			while(1)
			{
				scan_PS2();
				_delay_us(500);
				
				x=~data_array[3];
				y=~data_array[4];
				j=~data_array[5];
				b=~data_array[6];
				c=~data_array[7];
				d=~data_array[8];
				z=d*sqrt(1-((c*c)/2));
				w=b*sqrt(1-((j*j)/2));

    
								
				if(z<127)
				{
					
					PORTD|=(1<<PIND0);
					PORTD&=~(1<<PIND1);
					PORTD|=(1<<PIND2);
					PORTD&=~(1<<PIND3);
				}
				else if (z>127)
				{
					PORTD|=(1<<PIND1);
					PORTD&=~(1<<PIND0);
					PORTD|=(1<<PIND3);
					PORTD&=~(1<<PIND2);
				}
				else if (z==127)
				{
					
					PORTD&=~(1<<PIND0);
					PORTD&=~(1<<PIND1);
					PORTD&=~(1<<PIND2);
					PORTD&=~(1<<PIND3);
					
					
				}
				
				if(w<127)
				{
					
					PORTD|=(1<<PIND4);
					PORTD&=~(1<<PIND5);
					PORTD|=(1<<PIND6);
					PORTD&=~(1<<PIND7);
				}
				else if (w>127)
				{
					
					PORTD|=(1<<PIND5);
					PORTD&=~(1<<PIND4);
					PORTD|=(1<<PIND7);
					PORTD&=~(1<<PIND6);
				}
				else if (w==127)
				{
					
					PORTD&=~(1<<PIND4);
					PORTD&=~(1<<PIND5);
					PORTD&=~(1<<PIND6);
					PORTD&=~(1<<PIND7);
					
					
				}
				
		
				_delay_ms(1000);
				
			}
			
			
			return 0;
}
		
	


