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
            pinMode(NUM_PORT_BUTTON_ZERO, INPUT);
            Serial.print(NUM_PORT_BUTTON_ZERO);
            Serial.println(" is my digital pin number, connected button. True.");
            break;
            
        case 1:
            NUM_PORT_BUTTON_ONE = pin;
            pinMode(NUM_PORT_BUTTON_ONE, INPUT);
            Serial.print(NUM_PORT_BUTTON_ONE);
            Serial.println(" is my digital pin number, connected button. True.");
            break;
            
        case 2:
            NUM_PORT_BUTTON_TWO = pin;
            pinMode(NUM_PORT_BUTTON_TWO, INPUT);
            Serial.print(NUM_PORT_BUTTON_TWO);
            Serial.println(" is my digital pin number, connected button. True.");
            break;
            
        case 3:
            NUM_PORT_BUTTON_THREE = pin;
            pinMode(NUM_PORT_BUTTON_THREE, INPUT);
            Serial.print(NUM_PORT_BUTTON_THREE);
            Serial.println(" is my digital pin number, connected button. True.");
            break;

        default:
            break;
    }
}

int get_status_button(int port){
    int value_return;
    switch (port) {
        case 0:
            value_return = 
            break;
            
        default:
            break;
    }
	return digitalRead(a);
}
