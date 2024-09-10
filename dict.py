# {} and (key nad value)==> pair == dict


a = {
    "name":"shiva",
    "surname":"majhi",
    "age":28,
    "batch":16,
    "adress":["morang","kathmandu"]
}

print(a["name"])
print(a["age"]) 





bb = {
    "name":"shiva",
    "surname":"majhi",
    "middle name":"kumar",
    "age":28,
    "batch":16,
    "adress":["morang","kathmandu"]
}


bb['adress'] [-1]
print(bb['age'])




# get all keys from aict
print(bb.keys())
print(bb.values())

print(len(bb))
print(bb.get('middle name','-'))


#add key and value in dict

bb['broadway'] = "python"
bb['adress'] = "shiva"
print(bb)


thisdict = {
    
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : '1964'
}

print (thisdict)

print (thisdict.get('model','bugati'))

print (thisdict.get('hypercar','bugati'))




test = {
    
    'name' : 'broadway',
    'company' : 'test',
    'number' : {
        'type' : 'NTC',
        'mobile' : '9842135468'
    }
}
print (test['number'] ['type'])

print (test.keys())

print (test.values())



test = {
    
    'name' : 'broadway',
    'company' : 'test',
    'number' : [
       { 'type' : 'NTC',
        'mobile' : '9842135468'
       },
         {'type' : 'NCELL',
        'mobile' : '9802135468',
        }
     ]
}

print (test['number'] [0] ['type'])
print (test['number'] [1] ['mobile'])

test.update({'name': 'shiva','company':'skm','number':'123'})
print (test)

#del test['number']
##print (test)

##del test
##print (test)


#test.pop('number')
#print(test)
tt = test.pop('number')
print(test)

test.popitem()
print(test)

test.clear
print(test)




