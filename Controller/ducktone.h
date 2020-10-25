/*
   ducktone.h
   Shinchokuer: tari

   DESCRIPTION
    This is for tone

   DEPENDENCIES
    This header file needs nothing
*/

#define speaker 19

void noTone(void)
{
  ledcWriteTone(2, 0.0) ;
}
 
void tone(int freq, int len)
{
  ledcSetup(2, 5000, 13) ;
  ledcAttachPin(speaker, 2) ; // CH2をSOUNDERに
  ledcWriteTone(2, freq) ;
  delay(len);
}

// ESPだといらない?
/*
void beep(int oto, int jikan) {
  unsigned long start = millis();
  while(millis() < start + jikan)
  {
    digitalWrite(speaker, HIGH);
    delayMicroseconds((1000000 / oto / 2));
    digitalWrite(speaker, LOW);
    delayMicroseconds((1000000 / oto / 2));
  }
}
*/
