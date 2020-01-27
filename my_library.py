def generate_name_invitation(invitation):
	# invitation = 'Flavio Henrique Almeida'
	final_position = len(invitation);
	initial_position = final_position - 4
	first_part = invitation[0:4]
	second_part = invitation[initial_position:final_position]
	# print '%s %s' % (first_part, second_part)
	return first_part + ' ' + second_part
	
def register():
	answer = 'S'
	names = []
	while answer == 'S':
		print 'Put your name: '
		name = raw_input()
		names.append(name)
		print 'Do you want to add a new name? [S/N]'
		answer = raw_input()
	return names

def calculate_age(birth_year):
	from datetime import date
	return date.today().year - int(birth_year)
	# This library let you know the actual year (date.today.year), 
	# month(date.today.month) or day (date.today.day)
