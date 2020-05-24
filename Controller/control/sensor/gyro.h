/*
   gyro.h
   shinchokuer: tari
*/

#include<Wire.h>

#define Addr_Accl 0x19
#define Addr_Gyro 0x69
#define Addr_Mag 0x13

void init_gyro() {
  init_BMX(Addr_Accl, 0x0F, 0x03); // Select PMU_Range register // Range = +/- 2g
  init_BMX(Addr_Accl, 0x10, 0x08); // Select PMU_BW register // Bandwidth = 7.81 Hz
  init_BMX(Addr_Accl, 0x11, 0x00); // Select PMU_LPW register // Normal mode, Sleep duration = 0.5ms
  init_BMX(Addr_Gyro, 0x0F, 0x04); // Select Range register // Full scale = +/- 125 degree/s
  init_BMX(Addr_Gyro, 0x10, 0x07); // Select Bandwidth register // ODR = 100 Hz
  init_BMX(Addr_Gyro, 0x11, 0x00); // Select LPM1 register // Normal mode, Sleep duration = 2ms
  init_BMX(Addr_Mag, 0x4B, 0x83); // Select Mag register // Soft reset
  init_BMX(Addr_Mag, 0x4B, 0x01); // Select Mag register //Soft reset
  init_BMX(Addr_Mag, 0x4C, 0x00); // Select Mag register // Normal Mode, ODR = 10 Hz
  init_BMX(Addr_Mag, 0x4E, 0x84); // Select Mag register // X, Y, Z-Axis enabled
  init_BMX(Addr_Mag, 0x51, 0x04); // Select Mag register // No. of Repetitions for X-Y Axis = 9
  init_BMX(Addr_Mag, 0x52, 0x16); // Select Mag register// No. of Repetitions for Z-Axis = 15
  tft.println("Duck");
}

void init_BMX(byte addr, byte reg, byte value) {
  Wire.beginTransmission(addr);
  Wire.write(reg);
  Wire.write(value);
  Wire.endTransmission();
  delay(100);
}

def HKato{

}
