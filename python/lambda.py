temp = [1, 2, 3, 4, 5, 6]
temp1 = [(lambda x: x*2)(x) for x in temp]
temp2 = list(map(lambda x: x*2, temp))
print(temp1, '\n', temp2)
