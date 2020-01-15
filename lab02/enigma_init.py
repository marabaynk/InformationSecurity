from random import shuffle

rotors_count = 3
letters = 256


rotors_f = []
rotors_b = []

for i in range(rotors_count):
    tmp = [j for j in range(letters)]
    shuffle(tmp) 
    
    rotors_f.append(tmp) 
    
    tmp = [0 for j in range(letters)]
    
    for j, ind in enumerate(rotors_f[-1]):
        tmp[ind] = j

    rotors_b.append(tmp) 



tmp = [i for i in range(letters)]
shuffle(tmp)

reflector = [0 for i in range(letters)] 

for i in range(letters//2):
    a = tmp[i*2]
    b = tmp[i*2+1]
    reflector[a] = b
    reflector[b] = a


with open("rotors.py", "w") as f:
    f.write("letters="+str(letters)+"\n")
    f.write("rotors_f="+str(rotors_f)+"\n")
    f.write("rotors_b="+str(rotors_b)+"\n")
    f.write("reflector="+str(reflector)+"\n")
