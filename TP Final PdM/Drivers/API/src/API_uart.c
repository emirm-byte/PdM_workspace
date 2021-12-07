/*
 * API_uart.c
 *
 *  Created on: 22 nov. 2021
 *      Author: emiliano
 */

#include <API_uart.h>

bool_t uartInit(){

	bool_t EstadoUart;

	uint8_t miString[] = "BaudRate = 9600; StopBits = 1; Parity=NONE \n\r";

	  /*##-1- Configure the UART peripheral ######################################*/
	  /* Put the USART peripheral in the Asynchronous mode (UART Mode) */
	  /* UART configured as follows:
	      - Word Length = 8 Bits (7 data bit + 1 parity bit) :
		                  BE CAREFUL : Program 7 data bits + 1 parity bit in PC HyperTerminal
	      - Stop Bit    = One Stop bit
	      - Parity      = ODD parity
	      - BaudRate    = 9600 baud
	      - Hardware flow control disabled (RTS and CTS signals) */
	  UartHandle.Instance        = USARTx;

	  UartHandle.Init.BaudRate   = 9600;
	  UartHandle.Init.WordLength = UART_WORDLENGTH_8B;
	  UartHandle.Init.StopBits   = UART_STOPBITS_1;
	  UartHandle.Init.Parity     = UART_PARITY_NONE;
	  UartHandle.Init.HwFlowCtl  = UART_HWCONTROL_NONE;
	  UartHandle.Init.Mode       = UART_MODE_TX_RX;
	  UartHandle.Init.OverSampling = UART_OVERSAMPLING_16;
	  if (HAL_UART_Init(&UartHandle) != HAL_OK)
	  {
		  EstadoUart = false;
	  }	else {
		  EstadoUart = true;

		  HAL_UART_Transmit(&UartHandle, (uint8_t *) miString, sizeof(miString)/sizeof(char), 1000);
	  }

	  return EstadoUart;

}

void uartSendString(uint8_t *pstring){

	uint8_t largo=0;

	while(*(pstring+largo) != 0) largo++;


	HAL_UART_Transmit(&UartHandle, pstring, largo, 1000);

}

