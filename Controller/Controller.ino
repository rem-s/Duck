//#include "network/bluetooth.h"
#include "network/udp.h"
#include "network/wifi_ducks.h"
#include "control/sensor/button.h"
#include "control/sensor/joy_stick.h"

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  init_wifi();
  //init_bt();
  init_udp(8888, "192.168.0.56");
  init_button(4);
}

void loop() {
  // put your main code here, to run repeatedly:
  send_udp('T');
  get_status_button(4);
}
