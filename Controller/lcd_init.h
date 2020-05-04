/*
   lcd_init.h
   shinchokuer: tari

*/

#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>

#define TFT_CS         5
#define TFT_RST        25
#define TFT_DC         26

Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_RST);

void init_lcd() {
  tft.initR(INITR_BLACKTAB);
  tft.setRotation(3);
  tft.fillScreen(tft.color565(128, 32, 0));
  tft.setTextColor(tft.color565(255, 64, 0));
  tft.setTextWrap(false);
  tft.setCursor(0, 0);
  tft.setTextSize(5);
  tft.println("Duck");
  tft.setTextSize(1);
}