#!/usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
import time

initialized_pins = []

def init_door(gpio_pin_on, gpio_pin_off):
	init_pin(gpio_pin_on)
	init_pin(gpio_pin_off)
	# init_pin(gpio_pin_on)
	# init_pin(gpio_pin_off)
	# initialized_pins.append(gpio_pin_on)
	# initialized_pins.append(gpio_pin_off)

def init_pin(gpio_pin):
	if gpio_pin not in initialized_pins:
		GPIO.setup(gpio_pin, GPIO.OUT)
		GPIO.output(gpio_pin, GPIO.LOW)
		initialized_pins.append(gpio_pin)

def operate_door(gpio_pin):
	# door is een object:
	#	door.title
	#	door.gpio_pin
	#	door. [......]

	for x in range(1, 2):
		GPIO.output(gpio_pin, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(gpio_pin, GPIO.LOW)
		time.sleep(0.5)

def close_door(door):
	init_door(door.gpio_on, door.gpio_off)
	operate_door(door.gpio_off)

def open_door(door):
	init_door(door.gpio_on, door.gpio_off)
	operate_door(door.gpio_on)

GPIO.cleanup()
