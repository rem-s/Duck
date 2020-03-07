// bluetooth.h
// author: tari

#include "BluetoothSerial.h"

BluetoothSerial SerialBT;

void init_bt(){
	SerialBT.begin("ESP32 Ducks"); //Bluetooth device name
	Serial.println("I Duck. Welcome. You can connect me: Bluetooth, now!");
}

void send_bt(char content_send){
	SerialBT.print(content_send);
}
