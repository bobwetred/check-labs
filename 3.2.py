import random



def main():

    hashTable = createHashTable()
    permissionColission(hashTable)


def createHashTable():

    createPassword = list()
    for i in range(8):
        createPassword.append(random.sample('qwertyu1234567890',6))
        createPassword[i] = createPassword[i][0] + createPassword[i][1] + createPassword[i][2] + createPassword[i][3] + createPassword[i][4] + createPassword[i][5] 
    
    heshPassword = str()
    for i in range(len(createPassword)):
        for j in createPassword[i]:
            if j.isdigit() == True:
                hesh = hex(int(j))
                heshPassword += hesh
        createPassword[i] = [heshPassword, createPassword[i]]
        heshPassword = str()
        
    createHashTable = list()    
    for i in range(len(createPassword)):
        bufer = [createPassword[i][0],createPassword[i][1]]
        createHashTable.append(bufer)
    
    heshNonePassword = [[ hex(45636), None ], [hex(345632), None], [hex(657848), None]]
    createHashTable += heshNonePassword
    
    
    
    return (createHashTable)    
    
    
def permissionColission(hashTable):

    collisionPassword = (hashTable[4][0], '345y3gfr')
    
    for i in hashTable:
            if i[0] == collisionPassword[0]:
                flagsCollision = 1

    count = 1
    if flagsCollision == 1:
        for i in range(len(hashTable)):
            if hashTable[i][0] == collisionPassword[0]:
                j = i + 1
                while (j != len(hashTable) - 1):
                    if hashTable[j][1] == None:
                        hashTable[j][1] = collisionPassword[1]
                        break
                    else:
                        j += 1
        
        finalPasswordHesh = hashTable
        print('Коллизия разрешена, ')
        print (finalPasswordHesh)
    else:
        print('Коллизии не существует')
        finalPasswordHesh = hashTable
        
        
main()        