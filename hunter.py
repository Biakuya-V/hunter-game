import random
print('Welcome to the game of hunter!')
regame=1
while regame>0:
	local_x=random.randint(-999,999)
	local_y=random.randint(-999,999)
	guess_x=int(input('Please input your x-coordinate: '))
	guess_y=int(input('Please input your y-coordinate: '))
	sum_step=1
	while local_x!=guess_x or local_y!=guess_y:
		local=(local_x,local_y)
		guess_local=(guess_x,guess_y)
		if local_y>guess_y:
			if local_x>guess_x:
				print('You did not catch the prey.It is in the northeast.')
			elif local_x<guess_x:
				print('You did not catch the prey.It is in the northwest.')
			else :
				print('you did not catch the prey.It is in the north.')
				pass
		elif local_y<guess_y:
			if local_x>guess_x:
				print('You did not catch the prey.It is in the southeast.')
			elif local_x<guess_x:
				print('You did not catch the prey.It is in the southwest.')
			else:
				print('You did not catch the prey.It is in the south.')
				pass
		else:
			if local_x>guess_x:
				print('You did not catch the prey.It is in the east.')
			else:
				print('You did not catch the prey.It is in the west.')
				pass
			pass
		add_x=random.randint(-99,99)
		add_y=random.randint(-99,99)
		add=(add_x,add_y)
		local_x=local_x+add_x
		local_y=local_y+add_y
		print('You have alarmed the prey.It moved:',add)
		print('Your last location is:',guess_local)
		guess_x=int(input('Please input your x-coordinate again :'))
		guess_y=int(input('Please input your y-coordinate again :'))
		sum_step=sum_step+1
	pass
	print(' ')
	print(' ')
	print('--------------------------------------------------------')
	print(' ')
	print(' ')
	print('SUCCEED!You caught the prey!')
	print(' ')
	print(' ')
	print('--------------------------------------------------------')
	print(' ')
	print(' ')
	regame=int(input('Play Again? (1-yes 0-no) :'))