// joy_stick.h
// author: tari

/* usage:
 * x: pin number you connected x axis.
 * y: pin number you connected y axis.
 */

extern void disp_direc(int);
extern void cmd_history(int);

int get_value_stick_x(void);
int get_value_stick_y(void);

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

void main_stick(){
    if (get_value_stick_y() > 1024) {
    if (get_value_stick_x() > 1024) {
      send_tcp("3");
      disp_direc(3);
      cmd_history(3);
    }
    else if (get_value_stick_x() < -1024) {
      send_tcp("2");
      disp_direc(2);
      cmd_history(2);
    }
    else {
      send_tcp("1");
      disp_direc(1);
      cmd_history(1);
    }
  }
  else if (get_value_stick_y() < -1024) {
    if (get_value_stick_x() > 1024) {
      send_tcp("6");
      disp_direc(6);
      cmd_history(6);
    }
    else if (get_value_stick_x() < -1024) {
      send_tcp("5");
      disp_direc(5);
      cmd_history(5);
    }
    else {
      send_tcp("4");
      disp_direc(4);
      cmd_history(4);
    }
  }

  else {
    if (get_value_stick_x() > 1024) {
      send_tcp("HKato");
      disp_direc(7);
      cmd_history(7);
    }
    else if (get_value_stick_x() < -1024) {
      send_tcp("8");
      disp_direc(8);
      cmd_history(8);
    }
    else {
      send_tcp("0");
      disp_direc(0);
      cmd_history(0);
    }
  }
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
    //Serial.print("Value X: ");
    //Serial.println(value_x);
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
    //Serial.print("Value Y: ");
    //Serial.println(value_y);
    return value_y;
}
