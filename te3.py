import itertools

data1 = [{'name': u'String 2'}, {'name': u'String 1'}]
data2 = [{'name': u'String 1'}, {'name': u'String 1'}, {'name': u'String 2'}, {'name': u'String 3'}]

data1 = [{'nome': 'danilo segura', 'idade': '45', 'email': 'aaaa@ss.com.br'}, {'nome': 'vals segura', 'idade': '45', 'email': 'waaa@ss.com.br'}]

data2 = [{'nome': 'danilo segura', 'idade': '45', 'email': 'aaaa@ss.com.br'}, {'nome': 'vals segura', 'idade': '45', 'email': 'waaa@ss.com.br'}, {'nome': 'maya segura', 'idade': '45', 'email': 'waaa@ss.com.br'}]



r = list(itertools.filterfalse(lambda x: x in data1, data2)) + list(itertools.filterfalse(lambda x: x in data2, data1))
r1 = list(itertools.filterfalse(lambda x: x in data1, data2))
r2 = list(itertools.filterfalse(lambda x: x in data2, data1))

#print(r1)
#print(r2)
#print(r)
#assert r == [{'name': 'String 3'}]
r = [x for x in data2 if x not in data1]
print("r ", r)
print('\n')
r = [x for x in data2 if x in data1]
print("r ", r)

#r = [x for x in data1 + data2 if x not in data1 or x not in data2]
#print("r2 ", r)

#r = [x for x in data1 + data2 if x in data1 and x in data2]
#print("r2 ", r)