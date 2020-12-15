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
    createHashTable = tuple()
    for i in range(len(createPassword)):
        bufer = ((createPassword[i][0],createPassword[i][1],),)
        createHashTable += bufer
    

    return (createHashTable)    
    
  
def permissionColission(hashTable):

    collisionPassword = (hashTable[4][0], '345y3gfr')

    finalPasswordHesh = tuple()
    
    for i in hashTable:
            if i[0] == collisionPassword[0]:
                flagsCollision = 1
        
    count = 1
    if flagsCollision == 1:
        for i in hashTable:
            if i[0] == collisionPassword[0]:
                bufer = ((i[0],i[1],collisionPassword[1],),)
                print('Обнаружена коллизия в ',count,' ячейке')
                finalPasswordHesh += bufer
            else:
                count += 1
                bufer = ((i[0],i[1],),)
                finalPasswordHesh += bufer
        print('Коллизия разрешена, ')
        print (finalPasswordHesh)
    else:
        print('Коллизии не существует')
        finalPasswordHesh = hashTable
        

main()
