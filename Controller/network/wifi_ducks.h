// wifi_ducks.h
// author: tari

//--- Constant, define by user
const char ssid_wifis[] = "PERL122D-REMs"; // SSID APs.
const char pass_wifis[8];  // Password APs.
//---

#include <WiFi.h>

void init_wifi(void) {
    Serial.println("Connecting wireless, Start.");
    for(n = 0 ; n < 8 ; n++) {
        pass_wifis[n] = Serial.read();
    }
    WiFi.begin(ssid_wifis, pass_wifis);
    while( WiFi.status() != WL_CONNECTED) {
        delay(500);
    }
    disp_string("SSID: ");
    disp_string(ssid_wifis);
    Serial.println("Connected, Wireless.");
}
