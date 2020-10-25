/*
  controller.ino
  shinchokuer: tari

  This, program for controller, ESP32 based.
  This will read input value of buttons and joysticke, then send
  some collllands to Ducks Raspberry Pi via TCP connection over Wi-Fi.


  RAM CAPACITY:

  327 680 BYTES


  COMMANDS:

  FRONT : 1
  BACK  : 2
  LEFT  : 3
  RIGHT : 4
  STOP  : 0
  A     : 7
  B     : 8


  CONTROLLER PIN:

  BUTTON LEFT  : 35
  BUTTON RIGHT : 27
  LIGHT LEFT   : 14
  LIGHT RIGHT  : 13
  GYRO SDA     : 21
  GYRO SCL     : 22
  JOY STICK X  : 32
  JOY STICK Y  : 33
  TFT CS       :  5
  TFT DC       : 26
  TFT RST      : 25
  SPEAKER      : 19

*/

#include <Wire.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
//#include "network/bluetooth.h"
//#include "network/udp.h"
#include "network/tcp.h"
#include "network/wifi_ducks.h"
#include "control/sensor/button.h"
#include "control/sensor/joy_stick.h"
//#include "control/sensor/gyro.h"
#include "lcd_init.h"
#include "lcd.h"


extern void disp_string(char*);
extern void disp_stringln(char*);
extern void disp_staff(void);
extern void beep(int, int);
extern void canada(void);
extern void main_stick(void);

int flag_button0 = 0;
int flag_button1 = 0;
TaskHandle_t th[2];
int MODE_NETWORK_CLIENT = 3;

/*
   void setup(void)

   This is for initialize modules and setup some parameter.
*/
//canary: add BMX055 feature
#include "control/sensor/gyro.h"

void setup() {
  // put your setup code here, to run once:
  /*
    beep(2000, 100);
    beep(1000,100);
  */
  tone(2000, 100);
  tone(1000, 100);
  noTone();
  Serial.begin(115200);
  Serial.println("");
  //Initiali3e LCD
  init_lcd();
  //Initiali3e I2C Wire
  Serial.println("INIT SERV   > WIRE");
  Wire.begin();
  Serial.println("START SERV  > WIRE SUCCESS");
  //Initiali3e LED
  Serial.println("INIT SERV   > LED");
  pinMode(13, OUTPUT);
  pinMode(14, OUTPUT);
  digitalWrite(13, HIGH);
  digitalWrite(14, HIGH);
  Serial.println("START SERV  > LED SUCCESS");
  //init_gyro();
  disp_stringln("\nDuck controller taris\n");
  //Initiali3e Button
  init_button(0, 35);
  init_button(1, 27);
  init_button(2, 0);
  init_button(3, 0);
  init_stick(32, 33);
  //Initiali3e WirelessFi
  init_wifi();
  //init_bt();
  choose_mode_network();
  init_tcp(); // (port, address)
  //tft.setRotation(3);
  //delay(5000);
  //tft.fillScreen(tft.color565(255, 64, 0));
  //tft.fillScreen(tft.color565(0, 0, 0));
  reset_screen();
  screen_format();
  disp_nw();

}

/*
   void loop(void)

   This is main program.

   ↓ direction / command

   FRONT
   213
   546

*/

void loop() {
  // put your main code here, to run repeatedly:
  if(!client.connect(addr_ip_remote, port_tcp_remote)){
    FLAG_CONNECT_FAIL = 1;
  }
  void ensure();
  static String sendval;
  if (get_status_button(0) == 1 && flag_button0 == 0) {
    digitalWrite(13, HIGH);
    flag_button0 = 1;
    cmd_history(9);
  } else if (get_status_button(0) == 0) {
    digitalWrite(13, LOW);
    flag_button0 = 0;
  }
  if (get_status_button(1) == 1 && flag_button1 == 0) {
    digitalWrite(14, HIGH);
    flag_button1 = 1;
    cmd_history(10);
  } else if (get_status_button(1) == 0) {
    digitalWrite(14, LOW);
    flag_button1 = 0;
  }
  main_stick();
  xTaskCreatePinnedToCore(disp_image, "lena", 4096, NULL, 3, &th[0], 1);
  delay(20);
}

/*
   void ensure(void)

   This is for ensure connection.
*/

/*void ensure(){
  client.readStringUntil('\r');
  }

*/

/*
   void cmd_history(int)

   KONAMI COMMAND
*/

void cmd_history(int cmd) {
  static int old = 0;
  static int history[10];
  static int init_flag = 0;
  int count = 0;
  if (cmd == 0) {
    old = 0;
    return;
  }
  if (old == cmd) {
    return;
  }
  if (init_flag == 0) {
    for (count = 0 ; count <= 9 ; count++) {
      history[count] = 0;
    }
    init_flag = 1;
  }
  //14148787X9
  for (count = 0 ; count <= 9 ; count++) {
    history[count] = history[count + 1];
  }
  history[9] = cmd;
  old = cmd;
  Serial.print("History is: ");
  for (count = 0 ; count <= 9 ; count++) {
    Serial.print(history[count]);
    Serial.print(" ");
  }
  Serial.println(" ");
  if (history[0] == 1) {
    if (history[1] == 1) {
      if (history[2] == 4) {
        if (history[3] == 4) {
          if (history[4] == 8) {
            if (history[5] == 7) {
              if (history[6] == 8) {
                if (history[7] == 7) {
                  if (history[8] == 9) {
                    if (history[9] == 10) {
                      disp_staff();
                      reset_screen();
                      screen_format();
                      disp_nw();
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
