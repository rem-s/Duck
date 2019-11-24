
volatile int incomingByte = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(38400);
}

void loop() {
  
  if(Serial.available() > 0) {
    incomingByte = Serial.read();
     
    if(incomingByte == 0x00) Serial.println(0);
    else if(incomingByte == 0x01) Serial.println(1);
    else if(incomingByte == 0x02) Serial.println(2);
    else if(incomingByte == 0x03) Serial.println(3);
  }
  
}
