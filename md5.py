import hashlib

def calc_md5(password):
    password=hashlib.md5()
    password.update('password'.encode('utf-8'))
    return password

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    password=calc_md5(password)
    if(user==db.keys()&password==db.value):
        print('success')
    else:
        print('fail')

	
login('bob','abc999')		