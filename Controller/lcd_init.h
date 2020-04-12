/*
 * lcd_init.h
 * shinchokuer: tari
 *
 */

#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>

#define TFT_CS         5
#define TFT_RST        4
#define TFT_DC         2

Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_RST);

void init_lcd(){
    tft.initR(INITR_BLACKTAB);
    tft.setRotation(3);
    tft.fillScreen(ST77XX_BLACK);
    tft.setTextWrap(false);
    tft.setCursor(0, 0);
}
