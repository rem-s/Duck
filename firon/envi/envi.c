/***********************************************************************/
/*                                                                     */
/*  FILE        :Main.c or Main.cpp                                    */
/*  DATE        :Tue, Oct 31, 2006                                     */
/*  DESCRIPTION :Main Program                                          */
/*  CPU TYPE    :                                                      */
/*                                                                     */
/*  NOTE:THIS IS A TYPICAL EXAMPLE.                                    */
/*                                                                     */
/***********************************************************************/
//#include "typedefine.h"
#ifdef __cplusplus
//#include <ios>                        // Remove the comment when you use ios
//_SINT ios_base::Init::init_cnt;       // Remove the comment when you use ios
#endif

void main(void);
#ifdef __cplusplus
extern "C" {
void abort(void);
}
#endif

#include "machine.h"
#include "iodefine.h"
#include "portdef.h"

void delay(void){
	int i;
	for(i=10000;i>0;i--){
		nop();
	}
}

void main(void)
{
	LED1_DATA=LED_OFF;
	LED1_DIR=DIR_OUTPUT;
	for(;;){
		LED1_DATA^=1;
		delay();
	}
}

#ifdef __cplusplus
void abort(void)
{

}
#endif
