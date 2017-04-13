import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 16
Motor1B = 18
Motor1E = 22
 
Motor2A = 19
Motor2B = 21
Motor2E = 23

Motor3A = 37
Motor3B = 35
Motor3E = 33
 
Motor4A = 36
Motor4B = 38
Motor4E = 40

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

GPIO.setup(Motor3A,GPIO.OUT)
GPIO.setup(Motor3B,GPIO.OUT)
GPIO.setup(Motor3E,GPIO.OUT)
 
GPIO.setup(Motor4A,GPIO.OUT)
GPIO.setup(Motor4B,GPIO.OUT)
GPIO.setup(Motor4E,GPIO.OUT)

 
print "Going forwards, clockwise"
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)
 
GPIO.output(Motor2A,GPIO.HIGH)
GPIO.output(Motor2B,GPIO.LOW)
GPIO.output(Motor2E,GPIO.HIGH)

GPIO.output(Motor3A,GPIO.HIGH)
GPIO.output(Motor3B,GPIO.LOW)
GPIO.output(Motor3E,GPIO.HIGH)
 
GPIO.output(Motor4A,GPIO.HIGH)
GPIO.output(Motor4B,GPIO.LOW)
GPIO.output(Motor4E,GPIO.HIGH)
 
sleep(10)

GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor2E,GPIO.LOW)
GPIO.output(Motor3E,GPIO.LOW)
GPIO.output(Motor4E,GPIO.LOW)
sleep(2)
 
print "Going backwards, counter"
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1E,GPIO.HIGH)
 
GPIO.output(Motor2A,GPIO.LOW)
GPIO.output(Motor2B,GPIO.HIGH)
GPIO.output(Motor2E,GPIO.HIGH)

GPIO.output(Motor3A,GPIO.LOW)
GPIO.output(Motor3B,GPIO.HIGH)
GPIO.output(Motor3E,GPIO.HIGH)
 
GPIO.output(Motor4A,GPIO.LOW)
GPIO.output(Motor4B,GPIO.HIGH)
GPIO.output(Motor4E,GPIO.HIGH)
 
sleep(10)
 
print "Now stop"
GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor2E,GPIO.LOW)
GPIO.output(Motor3E,GPIO.LOW)
GPIO.output(Motor4E,GPIO.LOW)
 
GPIO.cleanup()