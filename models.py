# -*- coding: UTF-8 -*-

class Profile(object):
	# Old style: Profile()
	# New style: Profile(object) 
	# The new style add a lot of new utilities and tools.
	# Description (optional)
	'Default class for user profiles.'

	# Define the characteristics of our class (builder/constructor)
	# Called every time that we create a parameter throught a class
	# After the 'self' we can add the parameters that we need.
	def __init__(self, name, number, company):
		self.name = name
		self.number = number
		self.company = company
		self.__likes = 0
		# To import: from models import Profile
		# Called (without self): Perfil('Bruna', '000-000', 'undefined')
	

	def print_profile(self):
		print 'Name: %s, Number: %s, Company: %s' % (self.name, self.number, self.company)
		# This 'function' isn't builder, is a method of our class

	def like(self):
		self.__likes+=1

	def print_likes(self):
		print "This post has %s likes :)" % (self.__likes)
		# Can use the return to 'export' the value printing nothing
		# return self.__likes
class Date(object):
    'Default class to configure dates.'
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def print_date(self):
        print '%s/%s/%s' % (self.day, self.month, self.year)
        

class Person(object):
    'Default class to calculate the BMI (Body Mass Index)'
    def __init__(self, name, weight_kg, height_m):
        self.name = name
        self.weight = float(weight_kg)
        self.height = float(height_m)
    def print_bmi(self):
        bmi = self.weight / self.height**2 # pow(self.height,2) = self.height**2
        print '%s\'s BMI: %s' % (self.name, bmi)
        