/*
   lcd.h
   Shinchokuer: tari

   DESCRIPTION
    This is for using LCD.
    (Initialize functions are in lcd_init.h.)
    Width: 26 characters at font size 1

   DEPENDENCIES
    This header file needs SPI.h, standard library,
    and some Adafruit libraries.
*/

#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>
#include "canada.h"
#include "lena.h"

// This is declared at lcd_init.h.
extern Adafruit_ST7735 tft;
extern TaskHandle_t th[2];
extern void canada(void);
void disp_staff_flash(void*);
void reset_screen(void);
void screen_format(void);
void disp_image(void*);
int canaflag = 0;

//int tariatoi(char);
/*
   void disp_nw(void)

   This is for displaying network info to LCD.
   call after initialize Wi-Fi!!
*/

void disp_nw() {
  int FLAG_NETWORK_FAIL = 0;
  tft.setCursor(2, 66);
  tft.setTextColor(ST77XX_GREEN);
  tft.setTextSize(1);
  tft.print("SSID: ");
  tft.println(SSID_WIFIS);
  if (FLAG_NETWORK_FAIL == 1) {
    tft.setCursor(2, 74);
    tft.setTextColor(ST77XX_RED);
    tft.print("NETWORK FAILEN");
    tft.setTextColor(ST77XX_GREEN);
  }
}

/*
   void disp_direc(int)

   This is for displaying inputted direction to LCD.
   Example: When "Up-right" is inputted, LCD will display
   -------
   |     |
   |   / |
   |  O  |
   |     |
   |     |
   -------
*/

void disp_direc(int direc_neu) {
  tft.fillCircle(39, 31,  6, tft.color565(0, 128, 0));
  static int direc_old = 7;
  tft.setCursor(0, 10);
  tft.setTextSize(2);
  tft.setTextColor(ST77XX_WHITE);
  if (direc_neu != direc_old) {			// erase old direction
    switch (direc_old) {
      case 1:
        tft.fillTriangle(36, 23, 42, 23, 39, 5, ST77XX_BLACK);
        //        tft.println("   |");
        //        tft.println("");
        //        tft.println("");
        break;
      case 2:
        tft.fillTriangle(34, 25, 31, 28, 10, 10, ST77XX_BLACK);
        //        tft.println("  \\");
        //        tft.println("");
        //        tft.println("");
        break;
      case 3:
        tft.fillTriangle(44, 25, 47, 28, 68, 10, ST77XX_BLACK);
        //        tft.println("    /");
        //        tft.println("");
        //        tft.println("");
        break;
      case 4:
        tft.fillTriangle(36, 40, 42, 40, 39, 58, ST77XX_BLACK);
        //        tft.println("");
        //        tft.println("");
        //        tft.println("   |");
        break;
      case 5:
        tft.fillTriangle(31, 35, 34, 38, 10, 53, ST77XX_BLACK);
        //        tft.println("");
        //        tft.println("");
        //       tft.println("  /");
        break;
      case 6:
        tft.fillTriangle(44, 38, 47, 35, 68, 53, ST77XX_BLACK);
        //        tft.println("");
        //        tft.println("");
        //        tft.println("    \\");
        break;
      case 0:
        //        tft.println("");
        //        tft.println("");
        //        tft.println("");
        break;
      default:
        break;
    }
  }
  tft.setCursor(0, 10);
  tft.setTextSize(2);
  tft.setTextColor(ST77XX_BLACK);
  switch (direc_neu) {
    case 1:
      tft.fillTriangle(36, 23, 42, 23, 39, 5, ST77XX_ORANGE);
      //      tft.println("   |");
      //      tft.println("   O ");
      //      tft.println("");
      break;
    case 2:
      tft.fillTriangle(34, 25, 31, 28, 10, 10, ST77XX_ORANGE);
      //      tft.println("  \\");
      //      tft.println("   O ");
      //      tft.println("");
      break;
    case 3:
      tft.fillTriangle(44, 25, 47, 28, 68, 10, ST77XX_ORANGE);
      //      tft.println("    /");
      //      tft.println("   O ");
      //      tft.println("");
      break;
    case 4:
      tft.fillTriangle(36, 40, 42, 40, 39, 58, ST77XX_ORANGE);
      //      tft.println("");
      //      tft.println("   O ");
      //      tft.println("   |");
      break;
    case 5:
      tft.fillTriangle(31, 35, 34, 38, 10, 53, ST77XX_ORANGE);
      //      tft.println("");
      //      tft.println("   O ");
      //      tft.println("  /");
      break;
    case 6:
      tft.fillTriangle(44, 38, 47, 35, 68, 53, ST77XX_ORANGE);
      //      tft.println("");
      //      tft.println("   O ");
      //      tft.println("    \\");
      break;
    case 0:
    default:
      //      tft.println("");
      //      tft.println("   O ");
      //      tft.println("");
      break;
  }
  direc_old = direc_neu;
}


/*
   void disp_string(char*)

   This is for displaying string to LCD "WITHOUT" newline
   at the end of output.

   char* cont : string to display
*/

void disp_string(char* cont) {
  tft.print(cont);
}


/*
   void disp_stringln(char*)

   This is for displaying string to LCD "WITH" newline
   at the end of output.

   char* cont : string to display
   No return.
*/

void disp_stringln(char* cont) {
  tft.println(cont);
}


/*
   void disp_staff()

   This is for displaying staff credit.

   No arguments.
   No return.
*/

void disp_staff() {
  canaflag = 0;
  int x1, x2, y1, y2, c, c2;
  int  w = tft.width(), h = tft.height();
  reset_screen();
  tft.setCursor(0, 2);
  tft.setTextSize(1);
  disp_string(" ");
  tft.setTextSize(5);
  tft.setTextColor(tft.color565(0, 192, 192));
  tft.print("D");
  tft.setTextColor(tft.color565(192, 0, 0));
  tft.print("u");
  tft.setTextColor(tft.color565(0, 192, 0));
  tft.print("c");
  tft.setTextColor(tft.color565(192, 192, 0));
  tft.println("k");
  tft.setTextSize(1);
  tft.setTextColor(tft.color565(0, 0, 0));
  tft.setCursor(0, 40);
  disp_string(" ");
  tft.setTextSize(2);
  disp_string("Duck");
  tft.setTextSize(1);
  disp_string(" ");
  tft.setTextSize(2);
  disp_stringln("Project");
  tft.setTextSize(1);
  disp_stringln(" by");
  disp_stringln(" HKato");
  disp_stringln(" tari");
  disp_stringln(" Kawabe");
  disp_stringln(" Reon");
  disp_stringln(" GPIOberg");
  disp_stringln(" koshin");
  disp_stringln(" banri");
  disp_stringln(" and Others");
  //xTaskCreatePinnedToCore(pvTaskCode, pcName, usStackDepth, pvParameters, uxPriority, pvCreatedTask, xCoreID)
  xTaskCreatePinnedToCore(canada, "canada", 4096, NULL, 3, &th[0], 1);
  xTaskCreatePinnedToCore(disp_staff_flash, "flash", 4096, NULL, 3, &th[1], 0);
  while (canaflag != 2) {
    Serial.println(canaflag);
  }
  //disp_staff_flash();
}


/*
   void disp_staff()

   This is for displaying staff credit.

   No arguments.
   No return.
*/

void disp_staff_flash(void *pvParameters) {
  static int x1, x2, y1, y2, c, c2;
  int  w = tft.width(), h = tft.height();
  int count;
  x1 = w;
  y1 = h / 4;
  x2 = 0;
  y2 = h;
  for (c2  = 1 ; c2 <= 50 ; c2++) {
    for (c = (w / 2); c < w; c += 10) {
      x2 = c;
      tft.drawLine(x1, y1, x2, y2, tft.color565(192, 0, 128));
      delay(200);
    }
    if (canaflag == 1) {
      break;
    }
    for (c = (w / 2); c < w; c += 10) {
      x2 = c;
      tft.drawLine(x1, y1, x2, y2, tft.color565(0, 128, 192));
      delay(200);
    }
    if (canaflag == 1) {
      break;
    }
    for (c = (w / 2); c < w; c += 10) {
      x2 = c;
      tft.drawLine(x1, y1, x2, y2, tft.color565(128, 192, 0));
      delay(200);
    }
    if (canaflag == 1) {
      break;
    }
  }
  /*for (count = 0 ; count < 59 ; count++) {
    digitalWrite(13, HIGH);
    digitalWrite(14, LOW);
    delay(500);
    digitalWrite(13, LOW);
    digitalWrite(14, HIGH);
    delay(500);
    }
    digitalWrite(13, LOW);
    digitalWrite(14, LOW);*/
  canaflag = 2;
  Serial.println(canaflag);
  vTaskDelete(NULL);

}

/*
   void disp_image(char*)

   This is for displaying image array
   
   void *pvparameters : argument for FreeRTOS
   No return.
   
*/

//char line[128][160];
int area_image_x = 80;
int area_image_y = 60;
int cur_image_x  = 80;
int cur_image_y  = 2;


/*void load_image(char mana) {
  int low, column, digit, buf;
  char rawdt;
  while (low != area_image_y) {
    if (column == area_image_x) {
      low++;
      column = 0;
      digit = 1;
      continue;
    }
    rawdt = Serial.read();
    buf = tariatoi(rawdt);
    if (buf == '\t') {
      column++;
      digit = 1;
    }
    else if (digit == 1) {
      line[low][column] = buf;
      digit = 10;
    }
    else if (digit == 10) {
      line[low][col umn] *= 10;
      line[low][column] += buf;
      digit = 100;
    }
    else if (digit == 100) {
      line[low][column] *= 10;
      line[low][column] += buf;
      if (line[low][column] > 255) {
        line[low][column] = 0;
      }
    }
  }
  }
*/


void disp_image(void *pvParameters) {
  int countx, county;
  for (countx = 0 ; countx < area_image_x ; countx++) {
    for (county = 0 ; county < area_image_y ; county++) {
      tft.drawPixel(countx + cur_image_x, county + cur_image_y, tft.color565(0, line[county][countx], 0));
    }
  }
  vTaskDelete(NULL);
}

int tariatoi(char a) {
  int i;
  i = a - 48;
  return i;
}

void reset_screen() {
  tft.fillScreen(tft.color565(0, 0, 0));
}

void screen_format() {
  //x1,y1,x2,y2
  // tft.drawLine(0, 64, 159, 64, tft.color565(0, 0, 0));
  //tft.drawLine(79, 0, 79, 64, tft.color565(0, 0, 0));
  tft.drawLine(0, 64, 159, 64, tft.color565(255, 255, 255));
  tft.drawFastHLine(0, 64, 160, tft.color565(255, 255, 255));
  tft.drawFastVLine(79, 0, 64, tft.color565(255, 255, 255));
  tft.drawFastHLine(80, 0, 80, tft.color565(0, 0, 0));
  tft.drawFastHLine(80, 1, 80, tft.color565(0, 0, 0));
  tft.drawFastHLine(80, 62, 80, tft.color565(0, 0, 0));
  tft.drawFastHLine(80, 63, 80, tft.color565(0, 0, 0));
}
