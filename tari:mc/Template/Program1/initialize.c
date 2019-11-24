#include "initialize.h"
#include "iodefine.h"

void initialize(void)
{
	//レジスタライトプロテクションのOFF
	SYSTEM.PRCR.WORD 	= 0xA50B;
	
	//クロック	
	SYSTEM.SCKCR.BIT.PCKB = 0x0;		//周辺モジュールクロック1分周
	SYSTEM.SCKCR.BIT.PCKD = 0x0;		//周辺モジュールクロック1分周
	SYSTEM.SCKCR.BIT.ICK = 0x0;		//システムクロック1分周
	SYSTEM.SCKCR3.BIT.CKSEL = 0x01;		//主クロックをHOCOに設定
	SYSTEM.HOCOCR2.BIT.HCFRQ = 0x0; 	//HOCO動作周波数を32MHz設定
	SYSTEM.HOCOCR.BIT.HCSTP = 0x0; 		//HOCO動作開始
	SYSTEM.HOCOPCR.BIT.HOCOPCNT = 0x0;	//HOCOの電源ON
	
	//GPIO設定
	
}