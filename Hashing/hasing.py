import hashlib

my_pwd = 'password'
salt = 'ShaftesburySchool'

s = (my_pwd + salt).encode('UTF-8')

hash_object = hashlib.sha1(s)
hex_dig = hash_object.hexdigest()

print(hex_dig)
