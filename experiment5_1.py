# #Conten1:
# alien0 = {'color': 'green', 'points':5}
# print(alien0['color'])

# print("The "+alien0['color']+" alien just earned "+str(alien0['points'])+" !")
# print("The %s alien just earned %d !"%(alien0['color'], alien0['points']))

# alien0['x_pos'] = 0
# alien0['y_pos'] = 0

# alien0['color'] = 'yellow'

# del alien0['x_pos']

# for key, val in alien0.items():
#     print(key, val)

# cc = {a:-a for a in range(6)}
# print(cc)

# mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
# mcase_frequency = {
#     k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
#     for k in mcase.keys()
#     if k.lower() in ['a','b']
# }

# aliens = []
# for i in range(30):
#     alieni = {'color': 'green', 'points':5, 'speed': 'slow'}
#     aliens += [alieni]
# print(aliens)

# pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese']}
# for topping in pizza['toppings']:
#     print("\t"+topping)
    
# xy = [(x, 2*x+1) for x in range(10)]
# print(xy)



# #Content2:
# secrets = {'seven': '123'}
# for i in range(3):
	# admin = input('Please enter the account: ')
	# secret = input('Please enter the secret: ')
	# if secrets.get(admin) == secret:
		# print("login in successfully")
		# break
	# elif i != 2:
		# print("Please try again")
	# else:
		# print("fail to login in")


# #Content3:
# users = []
# while(input('Do you want to continue?[y]/[n] ') != 'n'):
	# name = input('name: ')
	# age = int(input('age: '))
	# job = input('job: ')
	# hobbie = input('hobbie: ')
	# user = {'name': name, 'age': age, 'job': job, 'hobbie': hobbie}
	# users.append(user)

# print('Here are the information about users: ')

# while users:
	# user = users.pop(0)
	# print('------------ {0} -----------\nName:   {0}\nAge:    {1}\nJob:    {2}\n\
# Hobbie: {3}\n------------ end -------------'.format(user['name']\
	# , user['age'], user['job'], user['hobbie']))
	
	
	
	
	
#Content4:
users = []
while(input('Do you want to continue?[y]/[n] ') != 'n'):
	name = input('name: ')
	age = int(input('age: '))
	job = input('job: ')
	hobbie = input('hobbie: ')
	user = {'name': name, 'age': age, 'job': job, 'hobbie': hobbie}
	users.append(user)

queryes = input('What elements do you want to request(seperate of whitespace)? ')
querys = queryes.split(' ')
answers = []
for query in querys:
	if query == 'age':
		answer = int(input('Please enter the {}: '.format(query)))
	else:
		answer = input('Please enter the {}: '.format(query))
	answers.append(answer)

print("\n\nbBelow are the matched users' information: ")
isTrue = 1
for user in users:
	for i in range(len(querys)):
		if user.get(querys[i], 'none') != answers[i]: isTrue = 0
	if isTrue == 1:
		print('------------ {0} -----------\nName:   {0}\nAge:    {1}\nJob:    {2}\n\
Hobbie: {3}\n------------ end -------------'.format(user['name']\
	, user['age'], user['job'], user['hobbie']))
	isTrue = 1

