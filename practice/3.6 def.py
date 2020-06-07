# def total(weight,price):
#     print('total:'+str(weight*price))
#
# w = int(input('weight:'))
# p = int(input('price:'))
# total(w,p)

def print_list(l1):
    print(l1)
    l1.append(10)
    print(l1)

l1 = [1,2,3]
print('before:' + str(id(l1)))
print_list(l1)
print('after:' + str(id(l1)))

