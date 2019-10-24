from werkzeug.security import generate_password_hash, check_password_hash

password = 'hello_my_name123'
password_hash = generate_password_hash(password)
print(password_hash)

res = check_password_hash(password_hash, password)
print(res)