N = input()[-1]

hon_list = ['2', '4', '5', '7', '9']
pon_list = ['0', '1', '6', '8']

if N in hon_list:
    print('hon')
elif N in pon_list:
    print('pon')
else:
    print('bon')
