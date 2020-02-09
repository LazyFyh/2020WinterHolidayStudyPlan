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
