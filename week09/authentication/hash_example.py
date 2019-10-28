from werkzeug.security import generate_password_hash, check_password_hash

password = 'a'
password_hash = generate_password_hash(password)
print(password_hash)

res = check_password_hash(password_hash, password)
print(res)