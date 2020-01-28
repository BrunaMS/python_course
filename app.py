# -*- coding: UTF-8 -*-
from my_library import *

def menu():
	names = []
	choose = ''
	while(choose != '0'):
		print 'Type...\n 5 to verify if a name is on the list \n 4 to edit a registered name\n 3 to remove a already included name \n 2 to list the registered names\n 1 to register more names \n 0 to finish:'
		choose = raw_input()
		if (choose == '1'):
			names = register()
		elif (choose == '2'):
			list_names(names)
		elif (choose == '3'):
			print 'Type the name that you want to remove:'
			name = raw_input()
			names.remove(name)
		elif (choose == '4'):
			list_names(names)
			edit_name(names)
		elif (choose == '5'):
			search_name(names)
		elif (choose == '0'):
			return
		else:
			print 'Sorry, this option is not a valid option. Try again.'

menu()