import random

def otp():
    otp = ''
    for i in range(4):
        otp += str(random.randint(1,9))
    print('Your OTP is ')
    print(otp)
otp()
