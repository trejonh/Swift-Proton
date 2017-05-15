import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)

class Robot:
	Motor1A = 16
	Motor1B = 18
	Motor1E = 22
	 
	Motor2A = 19
	Motor2B = 21
	Motor2E = 23

	Motor3A = 37
	Motor3B = 35
	Motor3E = 33
	 
	Motor4A = 29
	Motor4B = 31
	Motor4E = 32
	ENGINE_FREQ = 500
	
	def __init__(self):
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
		self.motor1Enable = GPIO.PWM(Motor1E, ENGINE_FREQ)
		self.motor2Enable = GPIO.PWM(Motor2E, ENGINE_FREQ)
		self.motor3Enable = GPIO.PWM(Motor3E, ENGINE_FREQ)
		self.motor4Enable = GPIO.PWM(Motor4E, ENGINE_FREQ)
		
		self.motor1Enable.start(0)
		self.motor2Enable.start(0)
		self.motor3Enable.start(0)
		self.motor4Enable.start(0)
		self.motor1Enable.ChangeDutyCycle(0)
		self.motor2Enable.ChangeDutyCycle(0)
		self.motor3Enable.ChangeDutyCycle(0)
		self.motor4Enable.ChangeDutyCycle(0)
		
	def turnOff(self):
		self.motor1Enable.stop()
		self.motor2Enable.stop()
		self.motor3Enable.stop()
		self.motor4Enable.stop()
		GPIO.cleanup()
	
	def goForward(self):
		GPIO.output(Motor1A,GPIO.HIGH)
		GPIO.output(Motor1B,GPIO.LOW)
		 
		GPIO.output(Motor2A,GPIO.HIGH)
		GPIO.output(Motor2B,GPIO.LOW)

		GPIO.output(Motor3A,GPIO.HIGH)
		GPIO.output(Motor3B,GPIO.LOW)
		 
		GPIO.output(Motor4A,GPIO.HIGH)
		GPIO.output(Motor4B,GPIO.LOW)
		
		self.motor1Enable.start()
		self.motor2Enable.start()
		self.motor3Enable.start()
		self.motor4Enable.start()
		self.motor1Enable.ChangeDutyCycle(100)
		self.motor2Enable.ChangeDutyCycle(100)
		self.motor3Enable.ChangeDutyCycle(100)
		self.motor4Enable.ChangeDutyCycle(100)
	
	def goBackward(self):
		GPIO.output(Motor1A,GPIO.LOW)
		GPIO.output(Motor1B,GPIO.HIGH)
		 
		GPIO.output(Motor2A,GPIO.LOW)
		GPIO.output(Motor2B,GPIO.HIGH)

		GPIO.output(Motor3A,GPIO.LOW)
		GPIO.output(Motor3B,GPIO.HIGH)
		 
		GPIO.output(Motor4A,GPIO.LOW)
		GPIO.output(Motor4B,GPIO.HIGH)
		
		self.motor1Enable.start()
		self.motor2Enable.start()
		self.motor3Enable.start()
		self.motor4Enable.start()
		self.motor1Enable.ChangeDutyCycle(100)
		self.motor2Enable.ChangeDutyCycle(100)
		self.motor3Enable.ChangeDutyCycle(100)
		self.motor4Enable.ChangeDutyCycle(100)
	
	def stop(self):
		self.motor1Enable.stop()
		self.motor2Enable.stop()
		self.motor3Enable.stop()
		self.motor4Enable.stop()