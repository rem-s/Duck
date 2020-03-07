// wifi_ducks.h
// author: tari

//--- Constant, define by user
const char ssid[] = "************"; // SSID APs.
const char pass[] = "************";  // Password APs.
//---

#include <WiFi.h>

void init_wifi(int port) {
	WiFi.begin(ssid, pass);
  	while( WiFi.status() != WL_CONNECTED) {
		delay(500);  
	}
}
