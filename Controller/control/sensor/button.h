// button.h
// author: tari

static int NUM_PORT_BUTTON_ZERO = 0;
static int NUM_PORT_BUTTON_ONE = 0;
static int NUM_PORT_BUTTON_TWO = 0;
static int NUM_PORT_BUTTON_THREE = 0;

void init_button(int button, int pin){
    
    switch (button) {
        case 0:
            NUM_PORT_BUTTON_ZERO = pin;
            pinMode(NUM_PORT_BUTTON_ZERO, INPUT_PULLDOWN);
            Serial.print(NUM_PORT_BUTTON_ZERO);
            Serial.println(" is my digital pin number, connected button zero. True.");
            break;
            
        case 1:
            NUM_PORT_BUTTON_ONE = pin;
            pinMode(NUM_PORT_BUTTON_ONE, INPUT_PULLDOWN);
            Serial.print(NUM_PORT_BUTTON_ONE);
            Serial.println(" is my digital pin number, connected button one. True.");
            break;
            
        case 2:
            NUM_PORT_BUTTON_TWO = pin;
            pinMode(NUM_PORT_BUTTON_TWO, INPUT_PULLDOWN);
            Serial.print(NUM_PORT_BUTTON_TWO);
            Serial.println(" is my digital pin number, connected button two. True.");
            break;
            
        case 3:
            NUM_PORT_BUTTON_THREE = pin;
            pinMode(NUM_PORT_BUTTON_THREE, INPUT_PULLDOWN);
            Serial.print(NUM_PORT_BUTTON_THREE);
            Serial.println(" is my digital pin number, connected button three. True.");
            break;

        default:
            break;
    }
}

int get_status_button(int port){
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
	return value_return;
}
