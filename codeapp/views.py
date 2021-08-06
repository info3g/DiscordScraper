
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os,re
import requests
import time
from bs4 import BeautifulSoup as bs
import csv
import re
import os,ast
from selenium.webdriver.chrome.options import Options
from .models import *

def index(request):
	if request.method =='POST':
		Platforms = request.POST['Platform']
		if Platforms == 'DISCORD' or Platforms == 'discord' or Platforms == 'Discord':
			list_of_user = request.POST.getlist('input_value_text')
			Users = request.POST['Users']
			Passwards = request.POST['Passward']
			Groups = request.POST['Group']
			Nagatar = request.POST['Nagatar']
			RPs = request.POST['RP']
			year = request.POST['years']
			symbol = request.POST['dil']
			democratically = request.POST['democratically']
			Candy = request.POST['Candy']
			Kansas = request.POST['Kansas']
			color = request.POST['color']

			options = Options()
			options.add_argument("--headless") # Runs Chrome in headless mode.
			options.add_argument('--no-sandbox') # # Bypass OS security model
			options.add_argument('start-maximized')
			options.add_argument('disable-infobars')
			options.add_argument("--disable-extensions")
			driver = webdriver.Chrome(chrome_options=options, executable_path='chromedriver.exe')
			# driver = webdriver.Chrome('chromedriver.exe')
			
			driver.get('https://discord.com/login')
			user = driver.find_elements_by_xpath('//input[@name="email"]')
			# time.sleep(5)
			print("Nagatar:0----------",Nagatar)
			try:
				for login in user:
					login.send_keys(Users)
			except:
				pass
			
			users = driver.find_elements_by_xpath('//input[@name="password"]')
			time.sleep(5)
			try:
				for logins in users:
					logins.send_keys(Passwards)
			except:
				pass
			login_user = driver.find_elements_by_xpath('//button[@class="marginBottom8-AtZOdT button-3k0cO7 button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeLarge-1vSeWK fullWidth-1orjjo grow-q77ONN"]')
			time.sleep(5)
			try:
				for log in login_user:
					log.click()
			except:
				pass
			Group = Groups 
			time.sleep(20)
			
			user_data_add = []
			user = []
			time.sleep(10)
			try:
				go_it = driver.find_elements_by_xpath("//body/div[@id='app-mount']/div[6]/div[1]/div[1]/div[1]/div[1]/button[1]")
				for go in go_it:
					go.click()
			except:
				pass
			links = driver.find_elements_by_xpath('//div[@class="wrapper-1BJsBx"]')
			
			serch_list = [Nagatar,RPs,year,symbol,democratically,Candy,Kansas]
			if list_of_user != '':
				for valies in list_of_user:
					serch_list.append(valies)
			obj = search(search=serch_list)
			obj.save()
				# if color != '':
			print('color:---------',color)
			color_obj = listofuser(list_of_user=color)
			color_obj.save()
			for link in links:
			    link.click()
			    try:
			        git = driver.find_element_by_xpath('//button[@class="button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeMedium-1AC_Sl fullWidth-1orjjo grow-q77ONN"]')
			        git.click()
			    except:
			        pass
			user_test_data = []
			links = driver.find_elements_by_xpath('//div[@class="wrapper-1BJsBx"]')
			for link in links:
				link.click()
				group_name = driver.find_elements_by_xpath('//h1[@class="name-1jkAdW"]')
				Text_Channels = driver.find_elements_by_xpath('//div[@class="overflow-WK9Ogt"]')
				for gruop in group_name:
					gruops = gruop.text
					if gruops == Group:
						for textchannel in Text_Channels: 
								time.sleep(1)
								match = textchannel.text
								if match == 'TEXT CHANNELS':
									time.sleep(1)
									all_channels = driver.find_elements_by_xpath('//div[@class="channelName-2YrOjO"]') 
									time.sleep(1)
									for texts in all_channels:
										time.sleep(2)
										texts.click()
										
										
										queryset = search.objects.all().last()
										res = ast.literal_eval(queryset.search)
										without_empty_strings = []
										for string in res:
											if (string != ""):
												without_empty_strings.append(string)

										
										for sd in without_empty_strings:
											for tetx in user_test_data:
												if sd in tetx:
													for tets in user_test_data:
														if tets not in user_data_add:
															print("**")
															user_data_add.append(tets)
										user_test_data = []
										count = 0			
										while True:
											time.sleep(1)
											datt = driver.page_source
											soup = bs(datt, "html.parser")
											data_all = soup.findAll("div", attrs={"class": "contents-2mQqc9"})
											for fin in data_all:
												time.sleep(0.1)
												try:
													text = fin.find("div", attrs={"class": "markup-2BOw-j messageContent-2qWWxC"}).text
													datetime = fin.find("span", attrs={"class": "timestamp-3ZCmNB timestampInline-yHQ6fX"}).text
													user_name = fin.find("span", attrs={"class": "username-1A8OIy desaturateUserColors-1gar-1 clickable-1bVtEA"}).text
													name_date = user_name + str(datetime) + '       '+ text
													if name_date not in user_test_data:
														user_test_data.append(name_date)
												except:
													ele =driver.find_element_by_tag_name('html')
													name_date = user_name + str(datetime) + '       '+ text
													if name_date not in user_test_data:
														user_test_data.append(name_date)
												print(name_date)
											print("******************************************************************",count)
											time.sleep(2)
											try:
												stop_Loop = driver.find_element_by_xpath('//*[@class="container-3RCQyg"]').text
												print('stop_Loop:--------------',stop_Loop)
											except:
												stop_Loop = ''
												element = driver.find_element_by_xpath('//*[@class="markup-2BOw-j messageContent-2qWWxC"]')
												driver.execute_script("return arguments[0].scrollIntoView();", element)
												element = driver.find_element_by_xpath('//*[@class="markup-2BOw-j messageContent-2qWWxC"]')
												driver.execute_script("return arguments[0].scrollIntoView();", element)
												element = driver.find_element_by_xpath('//*[@class="markup-2BOw-j messageContent-2qWWxC"]')
												driver.execute_script("return arguments[0].scrollIntoView();", element)
												element = driver.find_element_by_xpath('//*[@class="markup-2BOw-j messageContent-2qWWxC"]')
												driver.execute_script("return arguments[0].scrollIntoView();", element)
											if stop_Loop != '':
												print("breakkkkkkkkkkkkkkkkkkkk")
												break
											else:
												element = driver.find_element_by_xpath('//*[@class="markup-2BOw-j messageContent-2qWWxC"]')
												driver.execute_script("return arguments[0].scrollIntoView();", element)
												element = driver.find_element_by_xpath('//*[@class="markup-2BOw-j messageContent-2qWWxC"]')
												driver.execute_script("return arguments[0].scrollIntoView();", element)
												element = driver.find_element_by_xpath('//*[@class="markup-2BOw-j messageContent-2qWWxC"]')
												driver.execute_script("return arguments[0].scrollIntoView();", element)
												element = driver.find_element_by_xpath('//*[@class="markup-2BOw-j messageContent-2qWWxC"]')
												driver.execute_script("return arguments[0].scrollIntoView();", element)
											if count == 300:
												print("While loop break")
												break
											count+=1

		user = []
		current_feed = []
		part_one = []
		part_two = []
		part_three = []
		objs = recent(title=user_data_add)
		objs.save()
		queryset = search.objects.all().last()
		querysets = recent.objects.all().last()
		titles = ast.literal_eval(querysets.title)
		res = ast.literal_eval(queryset.search)
		without_empty_strings = []
		for string in res:
			if (string != ""):
				without_empty_strings.append(string)
		for sd in without_empty_strings:
			for tetx in titles:
				if sd in tetx:
					try:
						user.append('DISCORD'+' '+tetx.split('  ')[0])
						current_feed.append(tetx.split('  ')[0])
						strings = tetx.split('       ')[1]
						part_one.append(strings.split(sd)[0])
						part_two.append(sd)
						part_three.append(strings.split(sd)[1])
					except:
						pass
		print(user)
		both = zip(user,part_one,part_two,part_three)
		print('mesage_all:--',user_data_add)
		print('complete process')
		
		return render(request, 'home.html',{'color':color,'mess':user,'matching':both,'current':current_feed,'res':without_empty_strings})
		
	user = []
	current_feed = []
	part_one = []
	part_two = []
	part_three = []
	try:
		queryset = search.objects.all().last()
		querysets = recent.objects.all().last()
		titles = ast.literal_eval(querysets.title)
		res = ast.literal_eval(queryset.search)
		
		without_empty_strings = []
		for string in res:
			if (string != ""):
				without_empty_strings.append(string)
		for sd in without_empty_strings:
			for tetx in titles:
				if sd in tetx:
					try:
						user.append('DISCORD'+' '+tetx.split('  ')[0])
						current_feed.append('DISCORD'+' - '+tetx.split('  ')[0])
						strings = tetx.split('       ')[1]
						part_one.append(strings.split(sd)[0])
						part_two.append(sd)
						part_three.append(strings.split(sd)[1])
					except:
						pass

		both = zip(user,part_one,part_two,part_three)
		chnage = request.GET.get('info')
		users = []
		strings = []
		if chnage != 'None':
			for tetx in titles:
				if str(chnage) in tetx:
					for tetx in titles:
							users.append(tetx.split('  ')[0])
							strings.append(tetx.split('       ')[1])
		all_chat = zip(users,strings)
		ss = len(users)
		print(res)
	except:
		both = '' 
		without_empty_strings = ''
		all_chat = ''
		ss = ''
		pass

	colors = listofuser.objects.all().last()
	
	color = colors.list_of_user
	return render(request, 'home.html',{'color':color,'mess':user,'matching':both,'current':current_feed,'res':without_empty_strings,'all_chat':all_chat,'ss':ss})


def serc(request):
	chnage = request.GET.get('info')
	print(chnage)
	return render(request, 'home1.html')