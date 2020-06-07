import re

email = input('input email address:')
ret = re.match(r"[a-zA-Z0-9]{4,20}@163\.com",email)
if ret:
    print('yes')
else:
    print('no')