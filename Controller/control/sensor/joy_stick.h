// joy_stick.h
// author: tari

/* usage:
 * x: pin number you connected x axis.
 * y: pin number you connected y axis.
 */

static int NUM_PORT_AXIS_X_STICK = 0;
static int NUM_PORT_AXIS_Y_STICK = 0;

void init_stick(int x, int y){
	Serial.print(x);
	Serial.println(" is my analog pin number, connected X axis joystik. True.");
	Serial.print(y);
	Serial.println(" is my analog pin number, connected Y axis joystik. True.");
	
}

int get_status_button(int a){
	return digitalRead(a);
}
