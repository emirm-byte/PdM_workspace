/*
 * API_debounce.h
 *
 *  Created on: 9 nov. 2021
 *      Author: emiliano
 */

#ifndef API_INC_API_DEBOUNCE_H_
#define API_INC_API_DEBOUNCE_H_

#include <stdint.h>
#include <stdbool.h>
#include<API_delay.h>

void debounceInit();
uint8_t debounceUpdate();

#define BUTTON_PRESSED 1
#define BUTTON_RELEASED 0

typedef enum{
	BUTTON_UP,
	BUTTON_FALLING,
	BUTTON_DOWN,
	BUTTON_RISING
} estadoMEF_t;



#endif /* API_INC_API_DEBOUNCE_H_ */
