#include "bluetooth.h"
#include "udp.h"
#include "wifi_ducks.h"

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  init_wifi();
  //init_bt();
  init_udp(8888);
}

void loop() {
  // put your main code here, to run repeatedly:
  send_udp('T');
}
