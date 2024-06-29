#!/usr/bin/python3
name = 'kiprop'
new_name = ''
for i in range(len(name)):
    char_now = name[i]
    if char_now == 'p':
        new_name += '_'
    else:
        new_name += char_now

print(new_name)
