// button.h
// author: tari

void init_button(int a){
	pinMode(a, INPUT);
	Serial.print(a);
	Serial.println(" is my digital pin number, connected button. True.");
}

int get_status_button(int a){
	return digitalRead(a);
}
