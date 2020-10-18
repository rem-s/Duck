/*
   wifi_ducks.h
   shinchokuer: tari

   DESCRIPTION
    This is for using WLAN feature of duck controller.

   DEPENDENCIES
    This header file needs WiFi.h, standard library, and additional
    header file to define connection info.
*/

#include <WiFi.h>
#include "passwd.h"

#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>

extern Adafruit_ST7735 tft;

// These are declared at lcd.h.
extern void disp_string(char*);
extern void disp_stringln(char*);
extern int get_status_button(int);

WiFiClient client;
WiFiServer server(12222);

/*
   void init_wifi(void)

   It establishes connection between controller
   and accesspoint.
*/

void init_wifi(void) {
  Serial.println("FUNCTION    > INIT_WIFI");
  //disp_string("Network init      ");
  int n = 0;
  char buf[64];
  Serial.println("INIT SERV   > WLAN");
  //Serial.println("Enter SSID:");
  WiFi.config(ip, gateway, subnet, DNS);              // Defined at passwd.h
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
  //disp_stringln("[  OK  ]");
  disp_string("AP SSID: ");
  disp_stringln(SSID_WIFIS);
  disp_string("AP PASS: ");
  disp_stringln(PASS_WIFIS);
  disp_string("MY ADDR: ");
  disp_stringln("192.168.0.84");
  Serial.println("START SERV  > WLAN SUCCESS");
  Serial.println("TASK STATUS > DONE SUCCESS");
}

void choose_mode_network() {
  tft.fillScreen(tft.color565(255, 255, 255));
  tft.setTextColor(tft.color565(255, 64, 0));
  tft.setCursor(0, 0);
  tft.setTextSize(5);
  tft.println("Duck");
  tft.setTextSize(1);
  tft.println("Am I server? - Press A.");
  tft.println("Am I client? - Press B.");
  tft.setTextSize(2);
  tft.setTextColor(tft.color565(0, 255, 0));
  while (1) {
    if (get_status_button(0) == 1) {
      MODE_NETWORK_CLIENT = 1;
      tft.println("I am client.");
      break;
    }
    else if (get_status_button(1) == 1) {
      MODE_NETWORK_CLIENT = 0;
      tft.println("I am server.");
      break;
    }
  }
  tft.setTextSize(1);
  delay(1000);
}
