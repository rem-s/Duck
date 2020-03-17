#include "network/bluetooth.h"
#include "network/udp.h"
#include "network/wifi_ducks.h"

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  init_wifi();
  //init_bt();
  init_udp(8888, "192.168.0.56");
}

void loop() {
  // put your main code here, to run repeatedly:
  send_udp('T');
}
