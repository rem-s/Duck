// wifi_ducks.h
// author: tari

//--- Constant, define by user
const char ssid[] = "PERL122D-REMs"; // SSID APs.
const char pass[] = "duckduck";  // Password APs.
//---

#include <WiFi.h>

void init_wifi(void) {
	WiFi.begin(ssid, pass);
  	while( WiFi.status() != WL_CONNECTED) {
		delay(500);
	}
}
