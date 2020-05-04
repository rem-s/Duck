/* wifi_ducks.h
 * shinchokuer: tari
 */

#include <WiFi.h>
#include "passwd.h"
extern void disp_string(char*);
extern void disp_stringln(char*);

void init_wifi(void) {
    disp_string("Network init");
    int n=0;
    char buf[64];
    Serial.println("Connecting wireless, Start.");
    //Serial.println("Enter SSID:");
    WiFi.begin(SSID_WIFIS, PASS_WIFIS);
    Serial.println("begin");
    for(n = 0 ; n <= 4 ; n++) {
        if(WiFi.status() != WL_CONNECTED){
            if(n = 4) {
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
    Serial.println("Connected, Wireless.");
}
