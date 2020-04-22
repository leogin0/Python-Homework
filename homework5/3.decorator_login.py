#编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）

def login(func):
    def deco():
        account = input('account:')
        password = input('password:')
        if account == 'inin' and password == '12345':
            func()
        else:
            print('login err')
    return deco

@login
def func1():
    print('hello')

@login
def func2():
    print('world')

func1()
func2()