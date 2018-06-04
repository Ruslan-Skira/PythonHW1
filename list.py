test = [[1,2,3],[4,5,6],[7,8,9]]


#print(test[2][1])
#print(test.__len__())
print("top left diagonal")
i = 0
k = 0
# top left diagonal
while i < test.__len__():
    print(test[i][k])
    i += 1
    k += 1
print("top right diagonal")
# top right diagonal
i = 0
k = test[0].__len__()

while i < test.__len__():
    k -= 1
    print(test[i][k])
    i += 1



print("bottom left diagonal")
# bottom left diagonal
i = test.__len__() - 1
k = 0

while i >= 0:
    print(test[i][k])
    i -= 1
    k += 1



print("bottom rigth diagonal")
# bottom right diagonal

i = test.__len__()-1
k = test[0].__len__()-1

while i >=   0:
        print(test[i][k])
        i -= 1
        k -= 1


'''agregator for diagonal top left'''
c = 0
diagTopLeft = [test[i][i] for i in [c, c+1, c+2]]
print(diagTopLeft)

# diagonal bottom right
c = test[0].__len__()-1
diagTopRight = [test[i][i] for i in [c, c-1, c-2]]
print(diagTopRight)

#diagonal bottom left
c


