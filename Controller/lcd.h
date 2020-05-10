/*
 * lcd.h
 * Shinchokuer: tari
 *
 * DESCRIPTION
 *  This is for using LCD.
 *  (Initialize functions are in lcd_init.h.)
 *  Width: 26 characters at font size 1
 * 
 * DEPENDENCIES
 *  This header file needs SPI.h, standard library,
 *  and some Adafruit libraries.
 */

#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>

// This is declared at lcd_init.h.
extern Adafruit_ST7735 tft;

/*
 * void disp_nw(void)
 * 
 * This is for displaying network info to LCD.
 * call after initialize Wi-Fi!!
 */

void disp_nw() {
	tft.setCursor(0, 0);
	tft.setTextColor(ST77XX_BLUE);
	tft.setTextSize(1);
	tft.print("SSID: ");
	tft.print(SSID_WIFIS);
}

/*
 * void disp_direc(int)
 * 
 * This is for displaying inputted direction to LCD.
 * Example: When "Up-right" is inputted, LCD will display
 * -------
 * |     |
 * |   / |
 * |  O  |
 * |     |
 * |     |
 * -------
 */

void disp_direc(int direc_neu) {
	static int direc_old = 7;
	tft.setCursor(0, 10);
	tft.setTextSize(3);
	tft.setTextColor(ST77XX_BLACK);
	if (direc_neu != direc_old) {			// erase old direction
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

/*
 * void disp_string(char*)
 * 
 * This is for displaying string to LCD "WITHOUT" newline
 * at the end of output.
 */

void disp_string(char* cont) {

	tft.print(cont);
}

/*
 * void disp_stringln(char*)
 * 
 * This is for displaying string to LCD "WITH" newline
 * at the end of output.
 */

void disp_stringln(char* cont) {
	tft.println(cont);
}
