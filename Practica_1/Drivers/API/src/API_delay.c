/*
 * API_delay.c
 *
 *  Created on: 5 nov. 2021
 *      Author: emiliano
 */

#include <API_delay.h>

void delayInit(delay_t *delay, tick_t duration);
bool_t delayRead(delay_t *delay);
void delayWrite(delay_t *delay,tick_t duration);

void delayInit(delay_t *delay, tick_t duration){
	if(duration>0){
		delay->duration =duration;
		delay->running = false;
		delay->startTime=0;  //control de los parametros
	}
}

bool_t delayRead(delay_t *delay){
	bool_t timeOk=false;

	if(delay->running){
		if(((tick_t)HAL_GetTick()-delay->startTime)>= delay->duration){
			timeOk=true;
			delay->running = false;
		}
	}
	else{
		delay->startTime = (tick_t)HAL_GetTick();
		delay->running = true;
	}

	return timeOk;
}

void delayWrite(delay_t *delay,tick_t duration){
	if(duration>0){
		delay->duration=duration;
		delay->running=true;
	}
}

