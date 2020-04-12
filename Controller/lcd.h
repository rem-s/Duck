/*
 * tft.h
 * shinchokuer: tari
 *
 */

#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>

extern Adafruit_ST7735 tft;

/*
 * disp_nw
 * call after initialize Wi-Fi!!
 */

void disp_nw() {
    tft.setCursor(0, 0);
    tft.setTextColor(ST77XX_BLUE);
    tft.setTextSize(1);
    tft.print("SSID: ");
    //tft.print(ssid_wifis);
}

void disp_direc(int direc_neu) {
    static int direc_old = 7;
    tft.setCursor(0, 10);
    tft.setTextSize(3);
    tft.setTextColor(ST77XX_BLACK);
    if(direc_neu != direc_old){
        switch (direc_old) {
            case 1:
                tft.println(" |");
                tft.println("");
                tft.println("");
                break;
            case 2:
                tft.println("\\");
                tft.println("");
                tft.println("");
                break;
            case 3:
                tft.println("  /");
                tft.println("");
                tft.println("");
                break;
            case 4:
                tft.println("");
                tft.println("");
                tft.println(" |");
                break;
            case 5:
                tft.println("");
                tft.println("");
                tft.println("/");
                break;
            case 6:
                tft.println("");
                tft.println("");
                tft.println("  \\");
                break;
            case 0:
                tft.println("");
                tft.println("");
                tft.println("");
                break;
            default:
                break;
        }
    }
    tft.setCursor(0, 10);
    tft.setTextSize(3);
    tft.setTextColor(ST77XX_WHITE);
    switch (direc_neu) {
        case 1:
            tft.println(" |");
            tft.println(" O ");
            tft.println("");
            break;
        case 2:
            tft.println("\\");
            tft.println(" O ");
            tft.println("");
            break;
        case 3:
            tft.println("  /");
            tft.println(" O ");
            tft.println("");
            break;
        case 4:
            tft.println("");
            tft.println(" O ");
            tft.println(" |");
            break;
        case 5:
            tft.println("");
            tft.println(" O ");
            tft.println("/");
            break;
        case 6:
            tft.println("");
            tft.println(" O ");
            tft.println("  \\");
            break;
        case 0:
        default:
            tft.println("");
            tft.println(" O ");
            tft.println("");
            break;
    }
    direc_old = direc_neu;
}

void disp_string(char* cont){
    tft.println(cont);
}
