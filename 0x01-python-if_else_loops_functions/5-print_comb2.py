#!/usr/bin/python3

send = ""

for num in range(0, 100):
    if num in range(0, 10):
        send += "0{}, ".format(num)
    elif num == 99:
        send += "99\n"
    else:
        send += "{}, ".format(num)
print(send, end='')
