#
#        TB6612FNG
#  PWMA, PWMB = PWM (0 - 65535) mapping
#  AIN1, AIN2, BIN1, BIN2 = (HIGH, LOW)
#
#
#    In1In2 PWM	Out1Out2	Mode
#    H	H	H/L	L	L	Short brake
#    L	H	H	L	H	CCW
#    L	H	L	L	L	Short brake
#    H	L	H	H	L	CW
#    H	L	L	L	L	Short brake
#    L	L	H	OFF	OFF	Stop
#

#__auther__ = Terry C.
#__version__ = 1.0

from machine import Pin, PWM

def map(value, minX, minY, maxX, maxY):
    total=value-minX*(maxY-maxX)/(minY-minX)+maxY
    return int(total)

class tb6612xx:
   def __init__(self, AIN1, AIN2, BIN1, BIN2, STBY, PWMA=None, PWMB=None, freq=100000):
       self.AIM1 = ATN1
       self.AIN2 = ATN2
       self.BIN1 = BIN1
       self.BIN2 = BIN2
       self.STBY = STBY #Disable and Endable Pin
       self.PWMA = PWMA #SPEED
       self.PWMB = PWMB #SPEED


       #assign pin to pwm and to board that is used.
       self.motor_A1 = Pin(self.AIN1, Pin.Out)
       self.motor_A2 = Pin(self.AIN2, Pin.Out)
       self.motor_B1 = Pin(self.BIN1, Pin.Out)
       self.motor_B2 = Pin(self.BIN2, Pin.Out)
       self.chiptoff = Pin(self.STBY, Pin.Out)

       if (self.PWMB == None and self.PWMA == None):
           self.speed_A = None
           self.speed_B = None
           self.freq=None
       else:
           self.speed_A = PWM(Pin(self.PWMA))
           self.speed_B = PWM(Pin(self.PWMB))
           self.speed_A.freq(self.freq)
           self.speed_B.freq(self.freq)

  def motor_A(self, drive, power):
     if drive == 0:
         self.motor_A1.value(1)
         self.motor_A2.value(0)
         speed = map(power, 0, 100, 0, 65535)
         self.speed_A.duty_u16(speed)
     elif drive == 1:
         self.motor_A1.value(0)
         self.motor_A2.value(1)
         speed = map(power, 0, 100, 0, 65535)
         self.speed_A.duty_u16(speed)

  def motor_B(self, drive, power):
    if drive == 0:
       self.motor_B1.value(1)
       self.motor_B2.value(0)
       speed = map(power, 0, 100, 0, 65535)
       self.speed_B.duty_u16(speed)
   elif drive == 1:
        self.motor_B1.value(0)
        self.motor_B2.value(1)
        speed = map(power, 0, 100, 0, 65535)
        self.speed_A.duty_u16(speed)

  def foward(self,x=None):
      if x == None:
          self.motor_A(1, 100)
          self.motor_B(1, 100)
      else:
          self.motor_A(1,x)
          self.motor_B(1,x)

  def reverse(self,x=None):
       if x == None:
           self.motor_A(0,100)
           self.motor_B(0,100)
       else:
           self.motor_A(0,x)
           self.motor_B(0,x)

  def turn_left(self,x=None):
      if x == None:
          self.motor_A(1,100)
          self.motor_B(0,100)
      else:
          self.motor_A(1,x)
          self.motor_B(0,x)


  def turn_right(self,x=None):
       if x == None:
           self.motor_A(0,100)
           self.motor_B(1,100)
        else:
            self.motor_A(0,x)
            self.motor_B(1,x)

  def stop(self):
     self.motor_A1.value(0)
     self.motor_A2.value(0)
     self.motor_B1.value(0)
     self.motor_B2.value(0)

  def selinod_A(self, postion=0):
      if postion==0:
          self.motor_A1.value(1)
          self.motor_A2.value(0)
      else:
          self.motor_A1.value(0)
          self.motor_A2.value(1)

  def seliode_B(self, Postion=0):
        if postion==0:
            self.motor_B1.value(1)
            self.motor_B2.value(0)
        else:
            self.motor_B1.value(0)
            self.motor_B2.value(1)

  def deinit(self):
      self.speed_A.deinit()
      self.speed_B.deinit()

  def off_on(self, value=1):
      if value = 1:
          self.chiptoff.value(1)
      else:
          self.chiptoff.value(0)

