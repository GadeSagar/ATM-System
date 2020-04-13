while True:
	import time
	users=[{'name': 'Dnyanesh','balance':9877,'pin code':3740},{'name': 'Pratik','balance':877,'pin code':2274},{'name': 'Sagar','balance':9077,'pin code':8874},{'name': 'Tejas','balance':987,'pin code':9974},{'name': 'Amol','balance':877,'pin code':1234}]
	cuser={}
	cpincode=0
	
	def openscreen():
		global cuser
		global cpincode
		load(0)
		print('\r='+63*"=")
		print(6*'=','welcome to our ATM',6*'='+64*'=')
		print(32*'=')
		print('        enter your pincode')
		cpincode=int(input('              '))
		for user in users:
			if user['pin code']==cpincode:
				cuser=user
		if bool(cuser):
			selectscreen()
		else:
			errorscreen()
	def errorscreen():
		print(32*"=")
		print(4*'='+'Error pincode not found'+5*'=')
		load(5)
		openscreen()
	def selectscreen():
		print('\r'+31*"=")
		print(5*' ',3*'°','welcome,',cuser['name'],3*'°')
		print('1.cashwithdrawal\n2.balance\n3.setting\n4.donate\n5.exit')
		op=int(input('enter your choice: '))
		operations={1:cashwithdrawal,2:balance,3:setting,4:donate,5:exit}.get(op)
		operations()
	def cashwithdrawal():
		global omoney
		money=int(input('How much money you want:'))
		omoney=cuser['balance']
		if money>omoney:
			print('your balance not enough')
		else:
			print(10*' '+'done')
			rmoney=omoney-money
			print('current balance=',rmoney)
			cuser.update({'balance':rmoney})
		load(3)
		selectscreen()
	def balance():
		print(32*"°")
		b=cuser['balance']
		print('current balance=',b,'\n')
		load(3)
		selectscreen()
	def setting():
		print(32*'=')
		check=int(input('please enter pincode'))
		if check==cpincode:
			s=int(input('1.change my name\n2.change my pincode\n'))
			if s==1:
				nname=input('enter the new name: ')
				cuser.update({'name': nname})
			elif s==2:
				npin=int(input('enter the new pincode: '))
				cuser.update({'pincode':npin})
			else:
				print('invaild')
				load(3)
			selectscreen()
		else:
			print('wrong input')
			load(3)
			openscreen()
	def donate():
		global omoney
		print(32*'✓')
		print('1.57357\n2.Misr el khir\n3.Magdy Yaqoub Heart ')
		ch=int(input('please choose an charitable org : '))
		donatee=int(input('enter the sum of donation: '))
		omoney=cuser['balance']
		if omoney>=donatee:
			rmoney=omoney-donatee
			cuser.update({'balance':rmoney})
			print('\nThank you for doing some thing good:)')
		else:
			print('your balance not enough')
		load(3)
		selectscreen()
	def exit():
		load(3)
		openscreen()
		
	def load(t):
		for i in range(1,t):
			print('\rLoading'+'.'*i,end=' ')
			time.sleep(1)
	openscreen()
	
