#ifndef PORTDEF_H
#define PORTDEF_H

#define DIR_OUTPUT 1
#define DIR_INPUT 0

#define LED_ON 1
#define LED_OFF 0

#define LED1_DIR PORTH.PODR.BIT.B0
#define LED1_DATA PORTH.PDR.BIT.B0

#endif