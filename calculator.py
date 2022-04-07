import random
#Pokemon: Machamp
#Type: Fighting
#Attack: Karate Chop

level = 50
power = 50
attack = 200
#Ninetales Sp.Def
defense = 100

target = 1
weather = 1
badge = 1
crit = 1
rndm = round(random.uniform(0.85,1.0),2)
stab = 1.5
type = 0.5
burn = 1
modifier = target*weather*badge*crit*rndm*stab*type*burn*1

damage = ((2*level)/5)+2
damage = (damage*power)*(attack/defense)
damage = ((damage/50)+2)*modifier

print ("Manchop lvl 50: Karate chop"+ " S.p Attack:" + str(attack))
print("Damage on NineTales: " + str( round(damage)))
