abc = ["A" ,"B" ,"C" ,"D" ,"E" ,"F" ,"G" ,"H" ,"I" ,"J" ,"K" ,"L" ,"M" ,"N" ,"O" ,"P" ,"Q" ,"R","S" ,"T" ,"U" ,"V" ,"W" ,"X" ,"Y" ,"Z" ]
zeichen = 0
index = 0

print(1,"/",6)
W1 = [[21, 4], [19, 13], [11, 14], [8, 15], [3, 2], [0, 23], [1, 21], [16, 8], [10, 7], [6, 6], [9, 11], [25, 20], [13, 24], [2, 3], [24, 12], [22, 17], [14, 25], [5, 1], [4, 10], [20, 0], [17, 5], [23, 9], [15, 22], [7, 19], [12, 18], [18, 16]]
print(W1)

print(2,"/",6)
W2 = [[22, 1], [0, 17], [23, 0], [12, 4], [14, 22], [11, 23], [4, 19], [10, 6], [15, 25], [25, 14], [7, 10], [20, 5], [5, 20], [13, 15], [1, 3], [16, 18], [8, 12], [9, 8], [24, 7], [6, 2], [19, 16], [21, 13], [3, 11], [18, 9], [17, 24], [2, 21]]
print(W2)

print(3,"/",6)
W3 = [[6, 6], [14, 21], [24, 18], [21, 20], [3, 11], [15, 13], [19, 0], [7, 19], [22, 17], [9, 9], [17, 7], [11, 24], [10, 4], [4, 23], [20, 10], [23, 25], [1, 16], [18, 3], [2, 5], [12, 8], [13, 14], [5, 2], [0, 12], [16, 15], [25, 22], [8, 1]]
print(W3)

print(4,"/",6)
W4 = [[23, 17], [5, 24], [8, 23], [7, 11], [24, 21], [2, 14], [16, 5], [3, 20], [13, 22], [25, 3], [15, 2], [17, 25], [4, 0], [11, 9], [12, 8], [22, 1], [20, 12], [6, 7], [1, 10], [21, 16], [0, 18], [19, 4], [10, 15], [14, 6], [18, 13], [9, 19]]
print(W4)

print(5,"/",6)
W5 = [[8, 7], [14, 24], [12, 2], [15, 9], [3, 19], [5, 8], [16, 21], [13, 25], [10, 11], [1, 18], [7, 0], [19, 10], [9, 6], [24, 14], [17, 16], [0, 3], [11, 4], [20, 12], [23, 13], [25, 23], [18, 20], [6, 17], [2, 1], [4, 22], [21, 15], [22, 5]]
print(W5)

print(6,"/",6)
W6 = [[2, 9], [1, 13], [9, 19], [5, 4], [17, 21], [0, 23], [23, 16], [25, 22], [21, 2], [18, 5], [4, 12], [16, 10], [12, 8], [19, 15], [11, 18], [8, 14], [14, 25], [7, 3], [13, 20], [20, 17], [22, 24], [15, 6], [3, 7], [24, 11], [10, 0], [6, 1]]
print(W6)


input = str(input("Welches Zeichen soll verschlüsselt weden? (Es werden nur die 26 Großbuchstaben der Lateinischen Alphabets unterstützt)"))
storage = 0

if input in abc:
    index = abc.index(input)

    for x in range(0,len(abc)):

        if index == W1 [x] [0]:
            storage = W1 [x] [1]
            print("W1: ", abc [W1 [x] [0]], " zu ",abc [storage])
    index = storage

    for x in range(0,len(abc)):

        if index == W2 [x] [0]:
            storage = W2 [x] [1]
            print("W2: ",abc [W2 [x] [0]], " zu ",abc [storage])
    index = storage

    for x in range(0,len(abc)):

        if index == W3 [x] [0]:
            storage = W3 [x] [1]
            print("W3: ", abc [W3 [x] [0]], " zu ",abc [storage])
    index = storage
    
    for x in range(0,len(abc)):

        if index == W4 [x] [0]:
            storage = W4 [x] [1]
            print("W4: ", abc [W4 [x] [0]], " zu ",abc [storage])
    index = storage

    for x in range(0,len(abc)):

        if index == W5 [x] [0]:
            storage = W5 [x] [1]
            print("W5: ", abc [W5 [x] [0]], " zu ",abc [storage])
    index = storage

    for x in range(0,len(abc)):

        if index == W6 [x] [0]:
            storage = W6 [x] [1]
            print("W6: ", abc [W6 [x] [0]], " zu ",abc [storage])
    index = storage

    print("Zeichen ", input, " wurde mit ", 6, "Walzen zu ", abc [storage], "verschlüsselt")

else:
    print("Ungültiges Zeichen:" ,input ," wird nicht unterstützt")
