abc = ["A", "Ä", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "Ö", "P", "Q", "R", "S", "T", "U", "Ü", "V", "W", "X", "Y", "Z", "a", "ä", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "q", "r", "s", "t", "u", "ü", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~", " ", "°"]
zeichen = 0
index = 0

print("len abc:", len(abc))

print(1,"/",6)
W1 = [[60, 57], [87, 38], [19, 94], [21, 65], [39, 18], [64, 36], [59, 97], [45, 8], [56, 60], [69, 23], [89, 29], [32, 68], [72, 71], [11, 45], [9, 82], [25, 20], [23, 43], [34, 83], [10, 22], [13, 96], [85, 13], [38, 1], [73, 75], [95, 74], [66, 53], [62, 55], [75, 25], [50, 56], [90, 26], [91, 79], [67, 92], [7, 61], [76, 41], [37, 72], [40, 24], [61, 34], [78, 12], [52, 70], [94, 87], [83, 90], [17, 27], [96, 69], [6, 93], [4, 48], [5, 19], [70, 52], [49, 28], [30, 84], [81, 7], [18, 6], [44, 88], [84, 77], [8, 76], [86, 4], [58, 0], [77, 59], [28, 33], [51, 54], [74, 9], [0, 91], [41, 10], [12, 73], [36, 67], [46, 15], [43, 21], [54, 2], [48, 85], [35, 37], [27, 86], [65, 44], [55, 58], [80, 31], [82, 51], [71, 50], [97, 3], [92, 49], [3, 46], [15, 64], [2, 17], [33, 30], [99, 89], [31, 14], [57, 78], [63, 32], [29, 66], [53, 39], [22, 40], [47, 81], [20, 63], [98, 11], [88, 99], [93, 98], [14, 42], [24, 16], [16, 80], [68, 47], [79, 5], [26, 62], [42, 95], [1, 35]]
print(W1)

print(2,"/",6)
W2 = [[33, 53], [46, 64], [96, 25], [64, 62], [23, 30], [84, 18], [97, 16], [17, 96], [55, 77], [54, 82], [4, 15], [77, 94], [52, 34], [78, 67], [18, 44], [6, 68], [85, 26], [80, 98], [72, 72], [59, 55], [43, 73], [89, 54], [71, 81], [16, 61], [28, 95], [10, 86], [45, 60], [1, 75], [25, 9], [50, 63], [44, 36], [31, 93], [63, 0], [67, 97], [42, 33], [94, 65], [61, 7], [91, 17], [83, 22], [22, 1], [24, 38], [99, 83], [2, 39], [76, 28], [21, 90], [26, 91], [75, 6], [62, 58], [86, 71], [92, 59], [9, 3], [60, 37], [82, 13], [90, 70], [0, 78], [66, 92], [29, 45], [49, 76], [51, 42], [95, 2], [87, 51], [20, 69], [74, 41], [5, 43], [88, 85], [48, 66], [41, 80], [57, 5], [93, 74], [37, 8], [73, 14], [12, 99], [13, 79], [53, 32], [8, 56], [7, 49], [36, 52], [11, 47], [69, 10], [68, 24], [38, 40], [14, 11], [34, 35], [81, 84], [15, 19], [47, 57], [35, 88], [56, 4], [98, 21], [27, 23], [65, 50], [30, 27], [3, 46], [32, 31], [40, 20], [19, 48], [39, 12], [79, 87], [70, 29], [58, 89]]
print(W2)

print(3,"/",6)
W3 = [[71, 55], [69, 86], [94, 40], [95, 11], [11, 61], [6, 64], [14, 58], [52, 14], [55, 81], [70, 39], [68, 3], [37, 52], [77, 10], [61, 6], [33, 8], [76, 47], [92, 57], [45, 46], [46, 95], [79, 44], [10, 7], [8, 72], [43, 13], [85, 83], [48, 94], [0, 68], [1, 25], [51, 74], [63, 96], [74, 99], [38, 48], [21, 49], [96, 89], [57, 56], [19, 98], [54, 79], [58, 33], [42, 66], [72, 23], [40, 5], [26, 62], [87, 1], [17, 32], [89, 42], [62, 38], [36, 37], [83, 70], [39, 17], [82, 28], [73, 26], [34, 97], [16, 30], [59, 60], [29, 41], [53, 20], [80, 73], [3, 0], [99, 34], [25, 59], [47, 12], [32, 63], [15, 4], [60, 87], [35, 77], [81, 15], [65, 76], [2, 85], [5, 18], [13, 75], [75, 93], [78, 53], [31, 9], [88, 43], [4, 29], [66, 67], [90, 91], [18, 88], [24, 71], [28, 51], [64, 21], [67, 2], [7, 92], [20, 16], [23, 80], [98, 27], [27, 54], [50, 78], [9, 36], [49, 84], [84, 19], [41, 31], [30, 65], [86, 24], [56, 45], [12, 69], [22, 90], [91, 22], [44, 50], [93, 35], [97, 82]]
print(W3)

print(4,"/",6)
W4 = [[27, 68], [14, 66], [79, 8], [76, 79], [60, 95], [6, 81], [67, 53], [78, 96], [10, 48], [58, 18], [87, 22], [65, 26], [15, 57], [20, 84], [41, 52], [48, 51], [68, 21], [54, 44], [32, 93], [1, 14], [0, 29], [51, 69], [40, 65], [71, 59], [8, 27], [90, 58], [75, 3], [44, 41], [25, 54], [63, 37], [18, 2], [56, 28], [99, 97], [36, 47], [53, 36], [34, 55], [26, 70], [46, 5], [42, 4], [30, 15], [9, 31], [86, 56], [55, 46], [28, 98], [17, 63], [69, 30], [64, 74], [47, 71], [66, 87], [62, 9], [61, 67], [59, 11], [77, 39], [35, 16], [7, 34], [84, 10], [13, 85], [24, 89], [29, 77], [38, 60], [89, 73], [3, 25], [31, 90], [50, 23], [52, 1], [93, 88], [74, 12], [49, 82], [81, 76], [5, 6], [16, 86], [97, 38], [98, 33], [37, 75], [57, 20], [19, 40], [45, 7], [88, 94], [12, 72], [83, 0], [95, 42], [11, 80], [70, 61], [94, 62], [73, 32], [80, 64], [92, 43], [96, 13], [22, 91], [33, 78], [39, 49], [2, 19], [82, 99], [43, 17], [4, 50], [91, 83], [72, 24], [85, 45], [23, 92], [21, 35]]
print(W4)

print(5,"/",6)
W5 = [[12, 37], [95, 17], [26, 64], [3, 87], [43, 49], [53, 3], [65, 53], [78, 44], [88, 77], [32, 56], [16, 91], [20, 84], [19, 93], [96, 76], [87, 30], [93, 81], [55, 70], [72, 5], [59, 57], [66, 12], [33, 33], [30, 99], [25, 71], [70, 75], [90, 83], [61, 19], [76, 59], [62, 11], [73, 55], [11, 36], [74, 15], [51, 82], [6, 38], [31, 67], [44, 78], [41, 72], [97, 94], [23, 58], [52, 85], [15, 40], [42, 21], [98, 96], [71, 34], [54, 31], [75, 14], [91, 13], [8, 69], [27, 20], [89, 73], [49, 4], [58, 43], [64, 54], [84, 35], [80, 98], [24, 42], [81, 62], [10, 25], [18, 65], [46, 24], [40, 16], [92, 50], [34, 48], [45, 97], [63, 89], [57, 10], [17, 18], [83, 7], [56, 46], [79, 74], [85, 95], [50, 29], [48, 39], [5, 92], [60, 8], [38, 22], [69, 2], [21, 66], [29, 9], [77, 32], [2, 68], [68, 86], [36, 47], [82, 61], [7, 6], [14, 52], [86, 26], [28, 28], [22, 1], [37, 45], [35, 79], [47, 63], [67, 51], [99, 88], [9, 27], [4, 90], [94, 41], [1, 23], [13, 80], [39, 60], [0, 0]]
print(W5)

print(6,"/",6)
W6 = [[93, 29], [12, 93], [46, 63], [41, 57], [32, 0], [73, 83], [65, 6], [57, 17], [89, 16], [78, 33], [5, 98], [38, 54], [91, 52], [80, 61], [96, 12], [55, 72], [13, 99], [59, 73], [75, 64], [50, 71], [69, 39], [58, 47], [37, 37], [62, 15], [52, 18], [21, 2], [35, 85], [36, 20], [31, 82], [16, 13], [14, 24], [43, 65], [20, 11], [92, 41], [84, 27], [70, 9], [66, 30], [11, 78], [86, 59], [63, 22], [18, 46], [28, 97], [82, 10], [87, 38], [54, 8], [77, 25], [33, 49], [72, 31], [61, 36], [94, 69], [42, 32], [8, 56], [49, 68], [98, 45], [23, 26], [2, 89], [97, 4], [0, 75], [39, 43], [67, 58], [34, 70], [6, 40], [19, 87], [24, 5], [48, 53], [88, 74], [74, 44], [1, 90], [3, 1], [95, 81], [29, 95], [10, 21], [27, 91], [68, 86], [47, 23], [60, 80], [81, 35], [64, 60], [71, 7], [22, 92], [9, 50], [45, 94], [25, 66], [4, 77], [17, 55], [26, 76], [15, 34], [79, 84], [40, 28], [44, 19], [51, 42], [76, 14], [56, 62], [85, 51], [90, 3], [99, 67], [7, 96], [83, 48], [30, 88], [53, 79]]
print(W6)


input = str(input("Welches Zeichen soll verschlüsselt weden?"))
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
