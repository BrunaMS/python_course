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
		print 'Put the name: '
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

def list_names(names):
	# print 'Registered names:\n %s' % names
	# using the loop for:
	for name in names:
		print '%s' % name

def edit_name(names):
	print 'What name do you want to edit?'
	name = raw_input()
	if (name in names):
		name_idx = names.index(name)
		print 'Type the new name:'
		new_name = raw_input()
		names[name_idx] = new_name
	else:
		print 'Sorry. This name is not registered.' 

def search_name(names):
	print 'Type the name you want to find:'
	name = raw_input()
	if (name in names):
		print 'Ohh, fine! %s is already on the list!' % (name)
	else:
		print 'Sorry, %s is not registered.' % (name) 