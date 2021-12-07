/*
 * API_frecuency.c
 *
 *  Created on: 5 dic. 2021
 *      Author: emiliano
 */

#include<API_frecuency.h>

#define SAMPLE_TIME 300

static estadoSistema_t estadoActual;

static delay_t tiempo;


char buffer[20];

void MEFInit(void){
	debounceInit();
	delayInit(&tiempo, SAMPLE_TIME);
	estadoActual = MEDICION_FRECUENCIA;

}

void estadoMEFUpdate(uint32_t frecuency) {


	switch (estadoActual) {
	case MEDICION_FRECUENCIA: // Actualizar salida del estado
		if (delayRead(&tiempo)) {
			estadoActual = FRECUENCIA_UART;
		}
		if(BUTTON_FALLING == debounceUpdate()){
			estadoActual = ALMACENAMIENTO_FRECUENCIA;

		}

		break;

	case FRECUENCIA_UART:
		sprintf(buffer, "frec=%ld \n\r",frecuency);
		uartSendString((uint8_t *)buffer);
		estadoActual = MEDICION_FRECUENCIA;
		break;

	case ALMACENAMIENTO_FRECUENCIA: // Actualizar salida del estado
		sprintf(buffer, "store=%ld \n\r",frecuency);
		uartSendString((uint8_t *)buffer);
		estadoActual = MEDICION_FRECUENCIA;
		break;

	default:
		break;
	}
}


