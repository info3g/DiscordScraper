from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os,re
import requests
import time
from bs4 import BeautifulSoup as bs
import csv
import re
import os



def index(request):
	if request.method =='POST':

		list_of_user = request.POST.getlist('Nagatar')

		
		Users = request.POST['Users']
		Passwards = request.POST['Passward']
		Groups = request.POST['Group']
		print('Group:------------',Groups)

		Nagatar = request.POST['Nagatar']
		RPs = request.POST['RP']
		year = request.POST['years']
		symbol = request.POST['dil']
		democratically = request.POST['democratically']
		Candy = request.POST['Candy']
		Kansas = request.POST['Kansas']
		print('Nagatar:------',Nagatar)
		print('RPs:--------------------',RPs)
		print('year:--------',year)
		print('symbol:--------------------',symbol)
		print('democratically:---',democratically)
		print('Candy:----',Candy)
		print('Kansas:---',Kansas)

		driver = webdriver.Chrome('chromedriver.exe')
		driver.get('https://discord.com/login')
		user = driver.find_elements_by_xpath('//input[@name="email"]')
		time.sleep(1)
		try:
			for login in user:
				login.send_keys(Users)
		except:
			pass
		
		users = driver.find_elements_by_xpath('//input[@name="password"]')
		time.sleep(1)
		try:
			for logins in users:
				logins.send_keys(Passwards)
		except:
			print('sdf')

		login_user = driver.find_elements_by_xpath('//button[@class="marginBottom8-AtZOdT button-3k0cO7 button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeLarge-1vSeWK fullWidth-1orjjo grow-q77ONN"]')
		time.sleep(4)
		try:
			for log in login_user:
				log.click()
		except:
			print('sdf')
		time.sleep(5)
		links = driver.find_elements_by_xpath('//div[@class="wrapper-1BJsBx"]')
		user_data_add = []
		user = []
		mesage_all = []
		
		Group = Groups 
		for link in links:
			link.click()
			time.sleep(0.2)
			group_name = driver.find_elements_by_xpath('//h1[@class="name-1jkAdW"]')
			Text_Channels = driver.find_elements_by_xpath('//div[@class="overflow-WK9Ogt"]')
			for gruop in group_name:
				gruops = gruop.text
				if gruops == Group:
					for textchannel in Text_Channels: 
							time.sleep(1)
							match = textchannel.text
							if match == 'TEXT CHANNELS':
								all_channels = driver.find_elements_by_xpath('//div[@class="channelName-2YrOjO"]') 
								time.sleep(1)
								for texts in all_channels:
									texts.click()
									driver.find_elements_by_xpath('//*[@class="scrollerInner-2YIMLh"]')
									time.sleep(1)
									datt = driver.page_source
									soup = bs(datt, "html.parser")
									driver.find_elements_by_xpath('//*[@class="scrollerInner-2YIMLh"]')
									time.sleep(1)
									data_all = soup.findAll("div", attrs={"class": "message-2qnXI6 cozyMessage-3V1Y8y groupStart-23k01U wrapper-2a6GCs cozy-3raOZG zalgo-jN1Ica"})
									login = driver.find_element_by_xpath('//*[@class="chatContent-a9vAAp"]')
									for d in range(100):
										try:
											stop_Loop = driver.find_element_by_xpath('//*[@class="container-3RCQyg"]').text
											print('stop_Loop:--------------',stop_Loop)
										except:
											stop_Loop = ''
										login.click()
										for message in data_all:
											time.sleep(0.5)
											texts = message.text
											print("*********************************************************************",texts)
											if texts not in user_data_add:
												user_data_add.append(texts)
										ele =driver.find_element_by_tag_name('html')
										ele.send_keys(Keys.HOME)
										ele.send_keys(Keys.HOME)
										if stop_Loop != '':
											print("breakkkkkkkkkkkkkkkkkkkk")
											break
		if Nagatar != '':
			on = 'ons'
		current = []
		part_one = []
		part_two = []
		part_three = []
		
		
		user = []
		current_feed = []
		part_one = []
		part_two = []
		part_three = []
		for tetx in user_data_add:
		    if RPs in tetx:
		        user.append('DISCORD'+' '+tetx.split('  ')[0])
		        current_feed.append(tetx.split('  ')[0])
		        strings = tetx.split('  ')[1]
		        part_one.append(strings.split(RPs)[0])
		        part_two.append(RPs)
        		part_three.append(strings.split(RPs)[1])


		for alls in user_data_add:
			if Nagatar in alls:
				print("545454545454545454545")
				try:
					strings = alls.split('2020''')[1]
					part_one.append(strings.split(Nagatar)[0])
					part_two.append(Nagatar)
					part_three.append(strings.split(Nagatar)[1])
					user.append('DISCORD'+' ' +str(alls.split('2020''')[0]+str('2020')))
					current.append(alls.split(' ' '')[0])

				except:
					strings = alls.split('2021''')[1]
					print(strings.split(Nagatar))
					part_one.append(strings.split(Nagatar)[0])
					part_two.append(Nagatar)
					part_three.append(strings.split(Nagatar)[1])
					user.append('DISCORD'+' ' +str(alls.split('2021''')[0]+str('2021')))
					current.append(alls.split(' ' '')[0])
		
		

		if Nagatar != '':
			on = 'ons'
			for tetx in user_data_add:
				
				if Nagatar in tetx:
					try:
						strings = tetx.split('2020''')[1]
						print(strings.split(Nagatar))
						part_one.append(strings.split(Nagatar)[0])
						part_two.append(Nagatar)
						part_three.append(strings.split(Nagatar)[1])
						user.append('DISCORD'+' ' +str(alls.split('2020''')[0]+str('2020')))
						current.append(alls.split(' ' '')[0])
					except:
						strings = alls.split('2021''')[1]
						print(strings.split(Nagatar))
						part_one.append(strings.split(Nagatar)[0])
						part_two.append(Nagatar)
						part_three.append(strings.split(Nagatar)[1])
						user.append('DISCORD'+' ' +str(alls.split('2021''')[0]+str('2021')))
						current.append(alls.split(' ' '')[0])


		if RPs != '':
			on = 'ons'
			for tetx in user_data_add:
				
				if RPs in tetx:
					try:
						strings = tetx.split('2021''')[1]
						print(strings.split(RPs))
						part_one.append(strings.split(RPs)[0])
						part_two.append(RPs)
						part_three.append(strings.split(RPs)[1])
						user.append('DISCORD'+' ' +str(alls.split('2020''')[0]+str('2020')))
						current.append(alls.split(' ' '')[0])
					except:
						strings = alls.split('2021''')[1]
						print(strings.split(Nagatar))
						part_one.append(strings.split(Nagatar)[0])
						part_two.append(Nagatar)
						part_three.append(strings.split(Nagatar)[1])
						user.append('DISCORD'+' ' +str(alls.split('2021''')[0]+str('2021')))
						current.append(alls.split(' ' '')[0])
		
		if year != '':
			on = 'ons'
			for tetx in user_data_add:
				
				if year in tetx:
					try:
						strings = tetx.split('2021''')[1]
						print(strings.split(year))
						part_one.append(strings.split(year)[0])
						part_two.append(year)
						part_three.append(strings.split(year)[1])
						user.append('DISCORD'+' ' +str(alls.split('2020''')[0]+str('2020')))
						current.append(alls.split(' ' '')[0])
					except:
						strings = alls.split('2021''')[1]
						print(strings.split(Nagatar))
						part_one.append(strings.split(Nagatar)[0])
						part_two.append(Nagatar)
						part_three.append(strings.split(Nagatar)[1])
						user.append('DISCORD'+' ' +str(alls.split('2021''')[0]+str('2021')))
						current.append(alls.split(' ' '')[0])
						pass
		
		if symbol != '':
			on = 'ons'
			for tetx in user_data_add:
				
				if symbol in tetx:
					try:
						strings = tetx.split('2021''')[1]
						print(strings.split(symbol))
						part_one.append(strings.split(symbol)[0])
						part_two.append(symbol)
						part_three.append(strings.split(symbol)[1])
						user.append('DISCORD'+' ' +str(alls.split('2020''')[0]+str('2020')))
						current.append(alls.split(' ' '')[0])
					except:
						strings = alls.split('2021''')[1]
						print(strings.split(Nagatar))
						part_one.append(strings.split(Nagatar)[0])
						part_two.append(Nagatar)
						part_three.append(strings.split(Nagatar)[1])
						user.append('DISCORD'+' ' +str(alls.split('2021''')[0]+str('2021')))
						current.append(alls.split(' ' '')[0])
						pass
		
		if democratically != '':
			on = 'ons'
			for tetx in user_data_add:
				
				if democratically in tetx:
					try:
						strings = tetx.split('2021''')[1]
						print(strings.split(democratically))
						part_one.append(strings.split(democratically)[0])
						part_two.append(democratically)
						part_three.append(strings.split(democratically)[1])
						user.append('DISCORD'+' ' +str(alls.split('2020''')[0]+str('2020')))
						current.append(alls.split(' ' '')[0])
					except:
						strings = alls.split('2021''')[1]
						print(strings.split(Nagatar))
						part_one.append(strings.split(Nagatar)[0])
						part_two.append(Nagatar)
						part_three.append(strings.split(Nagatar)[1])
						user.append('DISCORD'+' ' +str(alls.split('2021''')[0]+str('2021')))
						current.append(alls.split(' ' '')[0])
						pass
		
		if Candy != '':
			on = 'ons'
			for tetx in user_data_add:
				
				if Candy in tetx:
					try:
						strings = tetx.split('2020''')[1]
						print(strings.split(Candy))
						part_one.append(strings.split(Candy)[0])
						part_two.append(Candy)
						part_three.append(strings.split(Candy)[1])
						user.append('DISCORD'+' ' +str(alls.split('2020''')[0]+str('2020')))
						current.append(alls.split(' ' '')[0])
					except:
						strings = alls.split('2021''')[1]
						part_one.append(strings.split(Candy)[0])
						part_two.append(Candy)
						part_three.append(strings.split(Candy)[1])
						user.append('DISCORD'+' ' +str(alls.split('2021''')[0]+str('2021')))
						current.append(alls.split(' ' '')[0])
						pass
		
		if Kansas != '':
			on = 'ons'
			for tetx in user_data_add:
				
				if Kansas in tetx:
					try:
						strings = tetx.split('2020''')[1]
						print(strings.split(Kansas))
						part_one.append(strings.split(Kansas)[0])
						part_two.append(Kansas)
						part_three.append(strings.split(Kansas)[1])
						user.append('DISCORD'+' ' +str(alls.split('2020''')[0]+str('2020')))
						current.append(alls.split(' ' '')[0])
					except:
						strings = alls.split('2021''')[1]
						part_one.append(strings.split(Kansas)[0])
						part_two.append(Kansas)
						part_three.append(strings.split(Kansas)[1])
						user.append('DISCORD'+' ' +str(alls.split('2021''')[0]+str('2021')))
						current.append(alls.split(' ' '')[0])
						pass			




		both = zip(user,part_one,part_two,part_three)
		print('mesage_all:--',mesage_all)
		return render(request, 'home.html',{'mess':user,'matching':both,'on':on,'current':current})
		
	return render(request, 'home.html')