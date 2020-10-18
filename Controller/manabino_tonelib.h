/*
   Manabino Arduino
   manabino_tonelib.h
   CREATED: 2017-11-02

   A = 440Hz

   C   D   E   F   G   A   B
   Do  Re  Mi  Fa  Sol La  Si

   f: flat     s: sharp
*/

void tempo(int);

//key
#define C3    131  //Do
#define Cs3   139
#define D3    146
#define Ds3   156
#define E3    164
#define F3    174
#define Fs3   185
#define G3    196
#define Gs3   208
#define A3    220
#define As3   233
#define Bf3   233
#define B3    247
#define C4    262  //Do
#define Cs4   277
#define D4    294
#define Ds4   311
#define E4    330
#define F4    349
#define Fs4   370
#define G4    392
#define Gs4   415
#define A4    440  //A = 440Hz
#define As4   466
#define Bf4   466
#define B4    494
#define C5    523  //Do
#define Cs5   554
#define D5    587
#define Ds5   622
#define E5    659
#define F5    698
#define Fs5   740
#define G5    784
#define Gs5   831
#define A5    880
#define As5   932
#define B5    988
#define C6    1047 //Do

//length
double wh;  //whole
double hfb; //beamed half
double hf;  //half
double qtb; //beamed quarter
double qt;  //quarter
double etb; //beamed eighth
double et;  //eighth
double stb; //beamed sixteenth
double st;  //sixteenth
double tsb; //beamed thirty-second
double ts;  //thirty-second
double sfb; //beamed sixty-fourth
double sf;  //sixty-fourth

//tempo
void tempo(int t) {
  double l    = 120  / t;
  wh   = 2048 * l;
  hfb  = 1792 * l;
  hf   = 1024 * l;
  qtb  = 768  * l;
  qt   = 512  * l;
  etb  = 384  * l;
  et   = 256  * l;
  stb  = 192  * l;
  st   = 128  * l;
  tsb  = 96   * l;
  ts   = 64   * l;
  sfb  = 48   * l;
  sf   = 32   * l;
}
