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