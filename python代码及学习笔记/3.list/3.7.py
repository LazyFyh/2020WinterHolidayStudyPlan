names = ['kobe' , 'embiid' , 'jordan']
for name in names:
    print( "Would you like to have dinner with me ?  " + name)
    
print("Kobe cannot attend dinner")
names[0] = 'james'

print("now ,I have a bigger restaurant , I d like to invite more friends")
names.insert(0,'robert')
names.insert(2,'george')
names.append('michial')

for name in names:
    print( "Would you like to have dinner with me ?  " + name)

print("sorry , I would just invite two friends")

while len(names)>2:
    print("Dear %s, Sorry to inform you that we cannot have dinnder together." % names[-1])
    names.pop()

for name in names:
    print( "Would you like to have dinner with me ?  " + name)

del names[:]

for name in names:
    print( "Would you like to have dinner with me ?  " + name)
