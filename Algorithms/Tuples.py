#!/usr/local/bin/python3

ta = 1, 2, 3, 4
tb = (1, 2, 3, 4)

print(ta)
print(tb)

print(ta[0])

#ta[0] = 12

print(ta + tb)


def squares():
    values = []
    for i in range(1, 21):
        values.append(i ** 2)
    return tuple(values)
        
print(squares())


















