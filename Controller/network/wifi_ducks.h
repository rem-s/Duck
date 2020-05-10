/* 
 * wifi_ducks.h
 * shinchokuer: tari
 * 
 * DESCRIPTION
 *  This is for using WLAN feature of duck controller.
 * 
 * DEPENDENCIES
 *  This header file needs WiFi.h, standard library, and additional
 *  header file to define connection info.
 */

#include <WiFi.h>
#include "passwd.h"

// These are declared at lcd.h.
extern void disp_string(char*);
extern void disp_stringln(char*);

/*
 * void init_wifi(void)
 * 
 * It establishes connection between controller
 * and accesspoint.
*/

void init_wifi(void) {
	disp_string("Network init      ");
	int n=0;
	char buf[64];
	Serial.println("[START] Connecting wireless");
	//Serial.println("Enter SSID:");
	WiFi.begin(SSID_WIFIS, PASS_WIFIS);					// Defined at passwd.h, is added to .gitignore so this header file is not on GitHub.
	//Serial.println("begin");
	/*for(n = 0 ; n <= 4 ; n++) {		  					// Retry count: 4
		if(WiFi.status() == WL_CONNECTED) {
			break;
		}
		else if(WiFi.status() != WL_CONNECTED){
			if(n = 4) {
				Serial.println("[FAILEN] Connecting wireless");
				disp_stringln("[FAILEN]");
				return;
			}
			delay(500);
		}
	}*/
	disp_stringln("[  OK  ]");
	disp_string("SSID: ");
	disp_stringln(SSID_WIFIS);
	Serial.println("[SUCCESS] Connecting wireless");
}
