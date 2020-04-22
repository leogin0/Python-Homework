#从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中
import base64

l1 = []
for i in range(5):
    print('请输入同学%d的信息：'% (i+1) )    
    name = input('姓名：')
    account = input('账号：')
    password = str(base64.b64encode(input('密码：').encode("utf8")) , encoding='utf8')
    lt = [name , account , password]
    l1.append(lt)
with open('homework4/classmates','w') as f:
    for i in range(5):
        for j in range(3):
            f.write(l1[i][j] + ' ')
        f.write('\n')

