import random

char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*_"
pass_len=int(input("Enter pass length: "))
pass_count=int(input("enter the number of req.pass: "))

for i in range(0,pass_count):
    password=" "
    for j in range(0,pass_len) :
        pass_char=random.choice(char)
        password=password+pass_char
    print("The genrated pass is: ",password)