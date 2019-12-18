# import logging
# logging.basicConfig(level=logging.WARNING)
# def foo(s):
#     n=int(s)
#     # assert n!=0,'n is zero'
#     logging.info('n=%s'%n)
#     return 10/n
# def main():
#     foo('0')
#
# main()

# import pdb
# s='0'
# n=int(s)
# pdb.set_trace()
# print(10/n)

import re
t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]'
             r'|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]'
             r'|5[0-9]|[0-9])$', t)
# print(m.groups())
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

# print(re_telephone.match('010-12345').group())
# print(re_telephone.match('010-8086').group())

def is_valid_email(addr):
    re_mail = re.compile(r'')
    return True

def name_of_email(addr):

    return None
# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'

print('ok')