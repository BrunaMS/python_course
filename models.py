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
		if(len(name) < 3): # Can be used to write something to the user.
			raise InvalidArgument('Each nome into the archive must have 3 characters or more.')
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
	def get_likes(self):
		# print "This post has %s likes :)" % (self.__likes)
		# Can use the return to 'export' the value printing nothing
		return self.__likes


	# Using static method we don't need generate a instance before
	# call the next method. That is, we don't need create a object 
	# of the class before call the following method. With it, 
	# we don't need send the self either.
	# @staticmethod
	# Using class method, we receive the class of the object (the Python do it for us)
	# in the 1st argument and we can use it to avoid a error with the type of the objects. 
	@classmethod
	def read_profiles_arch(obj_class, file_name):
		# The file name also must have the extension 
		archive = None
		try: 
			profiles = []
			archive = open(file_name, 'r')
			for rows in archive:
				values = rows.split(',')
				profiles.append(obj_class(*values)) 
				# The 'Profile'/obj_class in this case, is used to "force" 
				# the variable values to be separated/organized 
				# according to the attributes of the Profile builder,
				# like a Type Casting.
		except IOError as error:
			print("Sorry, we couldn't open the file. Verify if the archive really exists.\n Error: %s") % error
		# 	return ''
		except TypeError as error:
			print("Sorry, we couldn't perform this operation. Verify if there is any incorrect information.\n Error: %s") % error
		# 	return ''
		# We can use only one except block
		except (TypeError, IOError, ValueError) as error:
			print("Sorry, we couldn't perform this operation. \n Error: %s") % error
		
		# Except: # Generic, happenning if there was any error of any type.
		finally: # Executed in any situation
			if(archive is not None):
				archive.close()
			return profiles
class InvalidArgument(Exception):
	def __init__(self, message):
		self.message = message

	def __str__(self):
		return repr(self.message)


class VipProfile(Profile):
	# Old style: Profile()
	# New style: Profile(object) 
	# The new style add a lot of new utilities and tools.
	# Description (optional)
	'Default class for VIP users profiles.'
	# In this case, the nickname is optional and if isn't sent
	# it remains blank.
	def __init__(self, name, number, company, nickname = ''):
		super(VipProfile, self).__init__(name, number, company)
		self.nickname = nickname
		
	def get_credits(self):
		return super(VipProfile, self).get_likes() * 10
		# else:
		# 	return self.__likes

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
        