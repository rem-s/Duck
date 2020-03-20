// joy_stick.h
// author: tari

/* usage:
 * x: pin number you connected x axis.
 * y: pin number you connected y axis.
 */

static int NUM_PORT_AXIS_X_STICK = 0;
static int NUM_PORT_AXIS_Y_STICK = 0;

void init_stick(int x, int y){
    NUM_PORT_AXIS_X_STICK = x;
	Serial.print(NUM_PORT_AXIS_X_STICK);
	Serial.println(" is my analog pin number, connected X axis joystik. True.");
    NUM_PORT_AXIS_Y_STICK = y;
	Serial.print(NUM_PORT_AXIS_Y_STICK);
	Serial.println(" is my analog pin number, connected Y axis joystik. True.");
}

int get_value_stick_x(){
    int value_x;
    value_x = analogRead(NUM_PORT_AXIS_X_STICK);
    if(value_x < 2048) {
        value_x = (2048 - value_x) * (-1);
    }
    else {
        value_x = value_x - 2048;
    }
    Serial.print("Value X: ");
    Serial.println(value_x);
	return value_x;
}

int get_value_stick_y(){
    int value_y;
    value_y = analogRead(NUM_PORT_AXIS_Y_STICK);
    if(value_y < 2048) {
        value_y = (2048 - value_y) * (-1);
    }
    else {
        value_y = value_y - 2048;
    }
    Serial.print("Value Y: ");
    Serial.println(value_y);
    return value_y;
}
