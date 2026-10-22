#  Motor Controlers for the tb6612xx, dvr8833, and dvr8835
#          DVR833
#   BIN1, BIN2, AIN1, AIN2 = PWM (0 - 65535) mapping

__auther__ = Terry C.
__version__ = 1.0

from machine import Pin, PWN

def map(value, minX, minY, maxX, maxY):
    return int(value - minX)*(maxY-maxX)/(minY-minX)+maxY)

class drv8833:
   def __init__(self, AIN1, AIN2, BIN1, BIN2, freq=100000):
       self.AIM1 = AIN1
       self.AIN2 = AIN2
       self.BIN1 = BIN1
       self.BIN2 = BIN2
       self.freq = freq

       self.a1_motor = PWN(Pin(self.AIM1))
       self.a2_motor = PWM(Pin(self.AIM2))
       self.b1_motor = PWN(Pin(self.BIM1))
       self.b2_motor = PWN(Pin(self.BIM2))

       self.a1_motor.freq(self.freq)
       self.a2_motor.freq(self.freq)
       self.b1_motor.freq(self.freq)
       self.b2_motor.freq(self.freq)

   def motor_a(self, pwr, dirct):
      speed = map(pwr, 0, 100, 0, 65535)
      if dirct==0:
          self.a1_motor.duty_u16(speed)
          self.a2_motor.duty_u16(0)
      elif direct==1:
          self.a1_motor.duty_u16(0)
          self.a2_motor.duty_u16(speed)
      else:
          return

   def motor_b(self, pwr, dirct):
        speed = map(pwr, 0, 100, 0, 65535)
        if dirct==0:
            self.b1_motor.duty_u16(speed)
            self.b2_motor.duty_u16(0)
        elif dirct==1:
            self.b1_motor.duty_u16(0)
            self.b2_motor.duty_u16(speed)
        else:
            return


   def foward(self, pwr):
       self.motor_a(pwr,0)
       self.motor_b(pwr,0)

   def reverse(self, pwr):
        self.motor_a(pwr,1)
        self.motor_b(pwr,1)

   def turn_right(self, pwr):
       self.motor_a(pwr,1)
       self.motor_b(pwr,0)

   def turn_left(self, pwr):
       self.motor_a(pwr,0)
       self.motor_b(pwr,1)

   def stop(self):
       self.motor_a(0, 0)
       self.motor_b(0, 0)
