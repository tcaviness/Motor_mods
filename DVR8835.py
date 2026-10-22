
#
#         DVR8835 (MODE 1) if function
#  BENBL, AENBL = PWM (0 - 65535) mapping
#  BPHASE, APHASE = (HIGH, LOW)
#  MODE = (HIGH, LOW) Simplified drive (HIGH), Drive/coast (LOW)
#                 (MODE 2) else
#  AIN1, AIN2, BIN1, BIN2 = PWM (0 - 65535) (DEFALTS IF MODE IS NOT HIGH) mapping
#
__auther__ = Terry C.
__version__ = 1.0

from machine import Pin, PWN

def map(value, minX, minY, maxX, maxY):
    return int(value - minX)*(maxY-maxX)/(minY-minX)+maxY)

class dvr8835:
   def __init__(self,AIN1, AIN2, BIN1, BIN2, Swmode=None, Mode=2, freq=100000):
       self.mode = Mode
       if self.mode==2:
           self.AIM1 = AIN1
           self.AIN2 = AIN2
           self.BIN1 = BIN1
           self.BIN2 = BIN2

           self.motor_a1 = PWN(Pin(self.AIM1))
           self.motor_a2 = PWM(Pin(self.AIM2))
           self.motor_b1 = PWN(Pin(self.BIM1))
           self.motor_b2 = PWN(Pin(self.BIM2))

           self.motor_b1.freq(self.freq)
           self.motor_b2.freq(self.freq)
           self.motor_a1.freq(self.freq)
           self.motor_a2.freq(self.freq)

       elif self.mode==1:
           self.AIM1 = AIN1
           self.AIN2 = AIN2
           self.BIN1 = BIN1
           self.BIN2 = BIN2

           self.Mode = Pin(self.Swmode, Pin.OUT())
           self.AENBL = PWM(Pin(self.AIN2))
           self.BENBL = PWM(Pin(self.BIN2))
           self.APHASE = Pin(self.AIN1, Pin.OUT())
           self.BPHASE = Pin(self.BIN1, Pin.OUT())

           self.AENBL.freq(self.freq)
           self.BENBL.freq(self.freq)

      def MotorA(self, pw, dtr):
          speed = map(pw,0,100,0,65535)
          if self.mode==2:
              if dtr == 0:
                  self.motor_a1.duty_u16(speed)
                  self.motor_a2.duty_u16(0)
              elif dtr == 1:
                  self.motor_a1.duty_u16(0)
                  self.motor_a2.duty_u16(speed)
          elif self.mode==1:
               if dtr == 0:
                   self.APHASE.value(0)
                   self.AENBL.duty_u16(speed)
               elif dtr == 1:
                   self.APHASE.value(1)
                   self.AENBL.duty_u16(speed)

      def MotorB(self, pw, dtr):
           speed = map(pw,0,100,0,65535)
           if self.mode==2:
                if dtr == 0:
                    self.motor_b1.duty_u16(speed)
                    self.motor_b2.duty_u16(0)
                elif dtr == 1:
                    self.motor_b1.duty_u16(0)
                    self.motor_b2.duty_u16(speed)
           elif self.mode==1:
                if dtr == 0:
                     self.BPHASE.value(0)
                     self.BENBL.duty_u16(speed)
                elif dtr == 1:
                    self.BPHASE.value(1)
                    self.BENBL.duty_u16(speed)

      def Foward(self, pw):
          self.MotorA(pw,0)
          self.MotorB(pw,0)

      def Backward(self, pw):
          self.MotorA(pw,1)
          self.MotorB(pw,1)

      def stop():
          self.MotorA(0,0)
          self.MotorB(0,0)

      def Mode(self, on=2):
          if on == 1:
              self.Mode.value(1)
          elif on == 2:
              self.Mode.value(0)
