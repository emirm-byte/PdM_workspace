/*
 * API_frecuency.h
 *
 *  Created on: 5 dic. 2021
 *      Author: emiliano
 */

#ifndef API_INC_API_FRECUENCY_H_
#define API_INC_API_FRECUENCY_H_

#include <stdint.h>
#include <stdbool.h>
#include<API_debounce.h>
#include<API_delay.h>
#include<API_uart.h>
#include<stdio.h>

typedef enum{
	MEDICION_FRECUENCIA,
	FRECUENCIA_UART,
	ALMACENAMIENTO_FRECUENCIA
} estadoSistema_t;


void MEFInit(void);
void estadoMEFUpdate(uint32_t frecuency);


#endif /* API_INC_API_FRECUENCY_H_ */
