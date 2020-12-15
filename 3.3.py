import random



def main():

    createPasswordKey = createHashTable()
    permissionColission(createPasswordKey)


def createHashTable():

    createPasswordKey = list()
    for i in range(8):
        createPasswordKey.append(random.sample('qwertyu1234567890',6))
        createPasswordKey[i] = createPasswordKey[i][0] + createPasswordKey[i][1] + createPasswordKey[i][2] + createPasswordKey[i][3] + createPasswordKey[i][4] + createPasswordKey[i][5] 
    
    for i in range(len(createPasswordKey)):
        createPasswordKey[i] = [(i+2)*5, createPasswordKey[i]]
                    
    return (createPasswordKey)   
    
def permissionColission(createPasswordKey):

    step = 6
    n_size = 10
    
    heshTable = list()
    
    for i in range(n_size):
        heshTable.append([i, None])
    
    for i in createPasswordKey:
        position_flag = 0
        bufer = i[0]
        while position_flag == 0:
            position = bufer%n_size
            for j in heshTable:
                if  j[0] == position:
                    if j[1] == None:
                        j[1] = i[1]
                        position_flag = 1
            bufer = position + step            
        
    print(heshTable)

main()    
