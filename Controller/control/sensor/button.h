// button.h
// author: tari

static int NUM_PORT_BUTTON_ZERO = 0;
static int NUM_PORT_BUTTON_ONE = 0;
static int NUM_PORT_BUTTON_TWO = 0;
static int NUM_PORT_BUTTON_THREE = 0;

void init_button(int button, int pin){
    Serial.println("FUNCTION    > INIT_BUTTON");
    switch (button) {
        case 0:
            NUM_PORT_BUTTON_ZERO = pin;
            pinMode(NUM_PORT_BUTTON_ZERO, INPUT_PULLDOWN);
            Serial.print("INFORMATION > ZERO BUTTON PORT IS: ");
            Serial.println(NUM_PORT_BUTTON_ZERO);
            break;
            
        case 1:
            NUM_PORT_BUTTON_ONE = pin;
            pinMode(NUM_PORT_BUTTON_ONE, INPUT_PULLDOWN);
            Serial.print("INFORMATION > ONE BUTTON PORT IS: ");
            Serial.println(NUM_PORT_BUTTON_ONE);
            break;
            
        case 2:
            NUM_PORT_BUTTON_TWO = pin;
            pinMode(NUM_PORT_BUTTON_TWO, INPUT_PULLDOWN);
            Serial.print("INFORMATION > TWO BUTTON PORT IS: ");
            Serial.println(NUM_PORT_BUTTON_TWO);
            break;
            
        case 3:
            NUM_PORT_BUTTON_THREE = pin;
            pinMode(NUM_PORT_BUTTON_THREE, INPUT_PULLDOWN);
            Serial.print("INFORMATION > THREE BUTTON PORT IS: ");
            Serial.println(NUM_PORT_BUTTON_THREE);
            break;

        default:
            break;
    }
    Serial.println("TASK STATUS > DONE SUCCESS");
}

int get_status_button(int port){
    Serial.println("FUNCTION    > GET_STATUS_BUTTON");
    int value_return;
    switch (port) {
        case 0:
            value_return = digitalRead(NUM_PORT_BUTTON_ZERO);
            break;
        case 1:
            value_return = digitalRead(NUM_PORT_BUTTON_ONE);
            break;
        case 2:
            value_return = digitalRead(NUM_PORT_BUTTON_TWO);
            break;
        case 3:
            value_return = digitalRead(NUM_PORT_BUTTON_THREE);
            break;
        default:
            break;
    }
    Serial.println("TASK STATUS > DONE SUCCESS");
	return value_return;
}
