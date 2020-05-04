/* wifi_ducks.h
 * shinchokuer: tari
 */

#include <WiFi.h>
#include "passwd.h"
extern void disp_string(char*);
extern void disp_stringln(char*);

void init_wifi(void) {
	disp_string("[DO] Network init");
	int n=0;
	char buf[64];
	Serial.println("[START] Connecting wireless");
	//Serial.println("Enter SSID:");
	WiFi.begin(SSID_WIFIS, PASS_WIFIS);					// Defined at passwd.h, is added to .gitignore so this header file is not on GitHub.
	//Serial.println("begin");
	for(n = 0 ; n <= 4 ; n++) {		  					// Retry count: 4
		if(WiFi.status() != WL_CONNECTED) {
			break;
		}
		if(WiFi.status() != WL_CONNECTED){
			if(n = 4) {
				Serial.println("[FAILEN] Connecting wireless");
				return;
				//disp_stringln("      [FAILEN]");
				//while(1){
				//}
			}
			delay(500);
		}
		
	}
	disp_stringln("          [OK]");
	disp_string("SSID: ");
	disp_stringln(ssid_wifis);
	Serial.println("[SUCCESS] Connecting wireless");
}
