/*
 * GccApplication9.c
 *
 * Created: 19-07-2018 18:19:27
 * Author : HP
 */ 

#include <avr/io.h>
#include <util/delay.h>
#include "USART_128.h"

#define DDR_SPI DDRB
#define PORT_SPI PORTB
#define DD_SS PB0
#define DD_MOSI PB2
#define DD_MISO PB3
#define DD_SCK PB1

void pwm1_init()
{
	TCCR1A|=(1<<WGM11 | 1<<COM1A1 | 1<<COM1B1);
	TCCR1B|=(1<<WGM13 | 1<<WGM12 | 1<<CS10);
	DDRD|=(1<<PINB6 | 1<<PINB5);
	ICR1=1000;
}


int main()
{
	DDRB=(1<<DD_MISO);
	DDRB&=~(1<<DD_MOSI);
	DDRB&=~(1<<DD_SS);
	DDRB&=~(1<<DD_SCK);
	SPCR=(1<<SPE);
	SPCR=0b01101101;
	DDRC=0xFF;
	PORTC=0x00;
	int d,b;
	pwm1_init();
	int ratio;
	

		while(1)
	{
		
		while(!(SPSR & (1<<SPIF)));
		
		if(d<127)
		{
			ratio=(((127-d)*999)/127);
			OCR1A=(ratio);
			PORTD|=(1<<PIND0);
			PORTD&=~(1<<PIND1);
			PORTD|=(1<<PIND2);
			PORTD&=~(1<<PIND3);
			
		}
		else if(d>127)
		{
			ratio=(((d-127)*999)/127);
			OCR1A=(ratio);
			PORTD|=(1<<PIND1);
			PORTD&=~(1<<PIND0);
			PORTD|=(1<<PIND3);
			PORTD&=~(1<<PIND2);
			
		}
		else if (d==127)
		{
			ratio=(((127-d)*999)/127);
			OCR1A=(ratio);
			PORTD&=~(1<<PIND0);
			PORTD&=~(1<<PIND1);
			PORTD&=~(1<<PIND2);
			PORTD&=~(1<<PIND3);
			
		}
		
		if(b<127)
		{
			ratio=(((127-b)*999)/127);
			OCR1B=(ratio);
			PORTD|=(1<<PIND4);
			PORTD&=~(1<<PIND5);
			PORTD|=(1<<PIND6);
			PORTD&=~(1<<PIND7);
		}
		else if (b>127)
		{
			ratio=(((b-127)*999)/127);
			OCR1B=(ratio);
			PORTD|=(1<<PIND5);
			PORTD&=~(1<<PIND4);
			PORTD|=(1<<PIND7);
			PORTD&=~(1<<PIND6);
		}
		else if (b==127)
		{
			ratio=(((127-b)*999)/127);
			OCR1B=(ratio);
			PORTD&=~(1<<PIND4);
			PORTD&=~(1<<PIND5);
			PORTD&=~(1<<PIND6);
			PORTD&=~(1<<PIND7);
			
			
		}


		_delay_ms(1000);
	
}
}



