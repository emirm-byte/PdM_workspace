/*
 * API_debounce.c
 *
 *  Created on: 9 nov. 2021
 *      Author: emiliano
 */


#include<API_debounce.h>
#include<API_delay.h>

#include "stm32f4xx_hal.h"  		/* <- HAL include */
#include "stm32f4xx_nucleo_144.h" 	/* <- BSP include */

#define DURACION 40

estadoMEF_t estadoActual;

static delay_t tiempo;


void debounceInit(void) {
	estadoActual = BUTTON_UP;
	BSP_PB_Init(BUTTON_USER, BUTTON_MODE_GPIO);
	delayInit(&tiempo, DURACION);

}



uint8_t debounceUpdate(void) {


	switch (estadoActual) {
	case BUTTON_UP: // Actualizar salida del estado
		if (BSP_PB_GetState(BUTTON_USER)) {
			delayRead(&tiempo);
			estadoActual = BUTTON_FALLING;
		}
		break;

	case BUTTON_FALLING:
		if (delayRead(&tiempo)) {
			if (BSP_PB_GetState(BUTTON_USER)) {
				estadoActual = BUTTON_DOWN;
				return BUTTON_PRESSED;
			} else {
				estadoActual = BUTTON_UP;
			}

		}

		break;

	case BUTTON_DOWN: // Actualizar salida del estado
		if (!BSP_PB_GetState(BUTTON_USER)) {
			delayRead(&tiempo);
			estadoActual = BUTTON_RISING;

		}
		break;

	case BUTTON_RISING:
		if (delayRead(&tiempo)) {
			if (!BSP_PB_GetState(BUTTON_USER)) {
				estadoActual = BUTTON_UP;
				return BUTTON_RELEASED;

			} else {
				estadoActual = BUTTON_DOWN;

			}

		}

		break;
	default:
		//Si algo modificó la variable estadoActual
		// a un estado no válido llevo la MEF a un
		// lugar seguro, por ejemplo, la reinicio:
		debounceInit();

		break;
	}
	return 0;
}


