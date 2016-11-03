import re
def mail(m):
	if re.match(r'^\w*\@\w*\.\w{0,3}$',m):
		print('ok')
	else :
		print('failed')

t='someone@gmail.com'
mail(t)






