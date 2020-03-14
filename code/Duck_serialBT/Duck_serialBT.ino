// ****  *   *  ****  **  Duck Projekt Bluetoooth Serial
//     * *   * *     *    tari
//     * *   * *   **
//     * *   * *     *
// ****   ***   ****  **


//This example code is in the Public Domain (or CC0 licensed, at your option.)
//By Evandro Copercini - 2018
//
//This example creates a bridge between Serial and Classical Bluetooth (SPP)
//and also demonstrate that SerialBT have the same functionalities of a normal Serial

#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

#define PIN_X A4 //32
#define PIN_Y A5 //33

BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("DuckSP32"); //Bluetooth device name
  Serial.println("Duckへようこそ。Bluetooth接続できます。");
}

void loop() {
  //SerialBT.write("X");
  SerialBT.print(analogRead(PIN_X));
  Serial.println(analogRead(PIN_X));
  //SerialBT.write("Y");
  SerialBT.print(analogRead(PIN_Y));
  Serial.println(analogRead(PIN_Y));
  delay(1000);
}
