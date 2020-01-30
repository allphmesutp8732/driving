country = input('你的國籍？')
age = int(input('你的年齡？'))
if country == '台灣' or country == "臺灣":
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你不可以考駕照')
elif country == '美國':
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你不可以考駕照')
else:
	print("此程式國籍僅限台灣、美國。")