import random

abc = ["A", "Ä", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "Ö", "P", "Q", "R", "S", "T", "U", "Ü", "V", "W", "X", "Y", "Z", "a", "ä", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "q", "r", "s", "t", "u", "ü", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~", " ", "°"]


zeichen = 0
index = 0


print("Generiere Walzen...")
print(1,"/",12)
W1 = [[60, 57], [87, 38], [19, 94], [21, 65], [39, 18], [64, 36], [59, 97], [45, 8], [56, 60], [69, 23], [89, 29], [32, 68], [72, 71], [11, 45], [9, 82], [25, 20], [23, 43], [34, 83], [10, 22], [13, 96], [85, 13], [38, 1], [73, 75], [95, 74], [66, 53], [62, 55], [75, 25], [50, 56], [90, 26], [91, 79], [67, 92], [7, 61], [76, 41], [37, 72], [40, 24], [61, 34], [78, 12], [52, 70], [94, 87], [83, 90], [17, 27], [96, 69], [6, 93], [4, 48], [5, 19], [70, 52], [49, 28], [30, 84], [81, 7], [18, 6], [44, 88], [84, 77], [8, 76], [86, 4], [58, 0], [77, 59], [28, 33], [51, 54], [74, 9], [0, 91], [41, 10], [12, 73], [36, 67], [46, 15], [43, 21], [54, 2], [48, 85], [35, 37], [27, 86], [65, 44], [55, 58], [80, 31], [82, 51], [71, 50], [97, 3], [92, 49], [3, 46], [15, 64], [2, 17], [33, 30], [99, 89], [31, 14], [57, 78], [63, 32], [29, 66], [53, 39], [22, 40], [47, 81], [20, 63], [98, 11], [88, 99], [93, 98], [14, 42], [24, 16], [16, 80], [68, 47], [79, 5], [26, 62], [42, 95], [1, 35]]
print(W1)

print(2,"/",12)
W2 = [[33, 53], [46, 64], [96, 25], [64, 62], [23, 30], [84, 18], [97, 16], [17, 96], [55, 77], [54, 82], [4, 15], [77, 94], [52, 34], [78, 67], [18, 44], [6, 68], [85, 26], [80, 98], [72, 72], [59, 55], [43, 73], [89, 54], [71, 81], [16, 61], [28, 95], [10, 86], [45, 60], [1, 75], [25, 9], [50, 63], [44, 36], [31, 93], [63, 0], [67, 97], [42, 33], [94, 65], [61, 7], [91, 17], [83, 22], [22, 1], [24, 38], [99, 83], [2, 39], [76, 28], [21, 90], [26, 91], [75, 6], [62, 58], [86, 71], [92, 59], [9, 3], [60, 37], [82, 13], [90, 70], [0, 78], [66, 92], [29, 45], [49, 76], [51, 42], [95, 2], [87, 51], [20, 69], [74, 41], [5, 43], [88, 85], [48, 66], [41, 80], [57, 5], [93, 74], [37, 8], [73, 14], [12, 99], [13, 79], [53, 32], [8, 56], [7, 49], [36, 52], [11, 47], [69, 10], [68, 24], [38, 40], [14, 11], [34, 35], [81, 84], [15, 19], [47, 57], [35, 88], [56, 4], [98, 21], [27, 23], [65, 50], [30, 27], [3, 46], [32, 31], [40, 20], [19, 48], [39, 12], [79, 87], [70, 29], [58, 89]]
print(W2)

print(3,"/",12)
W3 = [[71, 55], [69, 86], [94, 40], [95, 11], [11, 61], [6, 64], [14, 58], [52, 14], [55, 81], [70, 39], [68, 3], [37, 52], [77, 10], [61, 6], [33, 8], [76, 47], [92, 57], [45, 46], [46, 95], [79, 44], [10, 7], [8, 72], [43, 13], [85, 83], [48, 94], [0, 68], [1, 25], [51, 74], [63, 96], [74, 99], [38, 48], [21, 49], [96, 89], [57, 56], [19, 98], [54, 79], [58, 33], [42, 66], [72, 23], [40, 5], [26, 62], [87, 1], [17, 32], [89, 42], [62, 38], [36, 37], [83, 70], [39, 17], [82, 28], [73, 26], [34, 97], [16, 30], [59, 60], [29, 41], [53, 20], [80, 73], [3, 0], [99, 34], [25, 59], [47, 12], [32, 63], [15, 4], [60, 87], [35, 77], [81, 15], [65, 76], [2, 85], [5, 18], [13, 75], [75, 93], [78, 53], [31, 9], [88, 43], [4, 29], [66, 67], [90, 91], [18, 88], [24, 71], [28, 51], [64, 21], [67, 2], [7, 92], [20, 16], [23, 80], [98, 27], [27, 54], [50, 78], [9, 36], [49, 84], [84, 19], [41, 31], [30, 65], [86, 24], [56, 45], [12, 69], [22, 90], [91, 22], [44, 50], [93, 35], [97, 82]]
print(W3)

print(4,"/",12)
W4 = [[27, 68], [14, 66], [79, 8], [76, 79], [60, 95], [6, 81], [67, 53], [78, 96], [10, 48], [58, 18], [87, 22], [65, 26], [15, 57], [20, 84], [41, 52], [48, 51], [68, 21], [54, 44], [32, 93], [1, 14], [0, 29], [51, 69], [40, 65], [71, 59], [8, 27], [90, 58], [75, 3], [44, 41], [25, 54], [63, 37], [18, 2], [56, 28], [99, 97], [36, 47], [53, 36], [34, 55], [26, 70], [46, 5], [42, 4], [30, 15], [9, 31], [86, 56], [55, 46], [28, 98], [17, 63], [69, 30], [64, 74], [47, 71], [66, 87], [62, 9], [61, 67], [59, 11], [77, 39], [35, 16], [7, 34], [84, 10], [13, 85], [24, 89], [29, 77], [38, 60], [89, 73], [3, 25], [31, 90], [50, 23], [52, 1], [93, 88], [74, 12], [49, 82], [81, 76], [5, 6], [16, 86], [97, 38], [98, 33], [37, 75], [57, 20], [19, 40], [45, 7], [88, 94], [12, 72], [83, 0], [95, 42], [11, 80], [70, 61], [94, 62], [73, 32], [80, 64], [92, 43], [96, 13], [22, 91], [33, 78], [39, 49], [2, 19], [82, 99], [43, 17], [4, 50], [91, 83], [72, 24], [85, 45], [23, 92], [21, 35]]
print(W4)

print(5,"/",12)
W5 = [[12, 37], [95, 17], [26, 64], [3, 87], [43, 49], [53, 3], [65, 53], [78, 44], [88, 77], [32, 56], [16, 91], [20, 84], [19, 93], [96, 76], [87, 30], [93, 81], [55, 70], [72, 5], [59, 57], [66, 12], [33, 33], [30, 99], [25, 71], [70, 75], [90, 83], [61, 19], [76, 59], [62, 11], [73, 55], [11, 36], [74, 15], [51, 82], [6, 38], [31, 67], [44, 78], [41, 72], [97, 94], [23, 58], [52, 85], [15, 40], [42, 21], [98, 96], [71, 34], [54, 31], [75, 14], [91, 13], [8, 69], [27, 20], [89, 73], [49, 4], [58, 43], [64, 54], [84, 35], [80, 98], [24, 42], [81, 62], [10, 25], [18, 65], [46, 24], [40, 16], [92, 50], [34, 48], [45, 97], [63, 89], [57, 10], [17, 18], [83, 7], [56, 46], [79, 74], [85, 95], [50, 29], [48, 39], [5, 92], [60, 8], [38, 22], [69, 2], [21, 66], [29, 9], [77, 32], [2, 68], [68, 86], [36, 47], [82, 61], [7, 6], [14, 52], [86, 26], [28, 28], [22, 1], [37, 45], [35, 79], [47, 63], [67, 51], [99, 88], [9, 27], [4, 90], [94, 41], [1, 23], [13, 80], [39, 60], [0, 0]]
print(W5)

print(6,"/",12)
W6 = [[93, 29], [12, 93], [46, 63], [41, 57], [32, 0], [73, 83], [65, 6], [57, 17], [89, 16], [78, 33], [5, 98], [38, 54], [91, 52], [80, 61], [96, 12], [55, 72], [13, 99], [59, 73], [75, 64], [50, 71], [69, 39], [58, 47], [37, 37], [62, 15], [52, 18], [21, 2], [35, 85], [36, 20], [31, 82], [16, 13], [14, 24], [43, 65], [20, 11], [92, 41], [84, 27], [70, 9], [66, 30], [11, 78], [86, 59], [63, 22], [18, 46], [28, 97], [82, 10], [87, 38], [54, 8], [77, 25], [33, 49], [72, 31], [61, 36], [94, 69], [42, 32], [8, 56], [49, 68], [98, 45], [23, 26], [2, 89], [97, 4], [0, 75], [39, 43], [67, 58], [34, 70], [6, 40], [19, 87], [24, 5], [48, 53], [88, 74], [74, 44], [1, 90], [3, 1], [95, 81], [29, 95], [10, 21], [27, 91], [68, 86], [47, 23], [60, 80], [81, 35], [64, 60], [71, 7], [22, 92], [9, 50], [45, 94], [25, 66], [4, 77], [17, 55], [26, 76], [15, 34], [79, 84], [40, 28], [44, 19], [51, 42], [76, 14], [56, 62], [85, 51], [90, 3], [99, 67], [7, 96], [83, 48], [30, 88], [53, 79]]
print(W6)

print(7,"/",12)
W7 = [[13, 13], [16, 43], [81, 0], [91, 37], [95, 99], [57, 45], [72, 17], [44, 81], [22, 16], [31, 5], [58, 92], [23, 31], [65, 65], [37, 91], [46, 29], [19, 58], [96, 14], [48, 38], [1, 60], [74, 11], [82, 55], [26, 77], [39, 66], [43, 33], [61, 36], [89, 73], [49, 93], [75, 94], [17, 96], [92, 97], [18, 71], [56, 3], [2, 39], [54, 19], [86, 47], [80, 98], [0, 20], [53, 62], [8, 83], [70, 79], [73, 44], [35, 51], [88, 86], [14, 27], [6, 75], [67, 9], [50, 68], [36, 87], [41, 78], [45, 69], [9, 15], [79, 76], [10, 74], [20, 8], [5, 7], [59, 34], [29, 56], [62, 63], [33, 50], [99, 53], [85, 49], [68, 80], [63, 88], [83, 42], [38, 22], [84, 67], [25, 2], [42, 46], [28, 57], [32, 82], [97, 18], [52, 59], [12, 25], [66, 72], [98, 89], [94, 12], [76, 61], [93, 26], [40, 23], [24, 41], [27, 64], [55, 10], [71, 85], [21, 95], [7, 6], [11, 35], [30, 28], [64, 48], [90, 24], [51, 4], [4, 52], [87, 70], [60, 90], [47, 84], [77, 32], [15, 40], [3, 54], [69, 30], [78, 1], [34, 21]]
print(W7)

print(8,"/",12)
W8 = [[24, 22], [44, 1], [73, 72], [26, 51], [81, 96], [93, 30], [96, 3], [49, 19], [45, 89], [69, 70], [47, 83], [77, 11], [23, 33], [21, 67], [19, 94], [79, 87], [67, 59], [43, 34], [92, 0], [90, 62], [98, 7], [70, 88], [72, 77], [97, 31], [25, 58], [75, 80], [36, 49], [32, 38], [29, 93], [8, 81], [80, 65], [0, 26], [74, 29], [56, 75], [52, 12], [85, 56], [58, 35], [64, 45], [48, 61], [65, 78], [17, 40], [40, 63], [57, 14], [15, 97], [1, 4], [54, 92], [5, 23], [42, 15], [14, 21], [68, 90], [2, 52], [95, 47], [82, 9], [88, 5], [4, 71], [20, 20], [84, 68], [61, 28], [78, 95], [38, 86], [89, 60], [71, 13], [39, 8], [60, 36], [53, 18], [31, 39], [16, 98], [3, 43], [83, 55], [91, 66], [33, 16], [94, 10], [76, 37], [86, 2], [10, 32], [87, 42], [37, 41], [28, 17], [41, 24], [59, 50], [12, 69], [55, 76], [51, 99], [62, 74], [66, 6], [34, 54], [7, 46], [13, 84], [46, 91], [99, 48], [63, 85], [6, 44], [18, 73], [35, 27], [22, 82], [30, 79], [27, 57], [9, 53], [11, 25], [50, 64]]
print(W8)

print(9,"/",12)
W9 = [[34, 94], [36, 44], [70, 16], [71, 1], [84, 36], [46, 3], [85, 82], [79, 59], [7, 92], [11, 34], [75, 63], [82, 69], [29, 33], [72, 52], [9, 17], [63, 25], [62, 28], [15, 97], [88, 57], [54, 66], [57, 9], [68, 72], [69, 0], [51, 6], [16, 87], [38, 22], [13, 11], [27, 51], [19, 21], [92, 60], [74, 65], [97, 37], [31, 70], [73, 64], [32, 5], [66, 90], [4, 24], [89, 53], [87, 80], [28, 67], [78, 54], [43, 74], [26, 89], [24, 4], [40, 20], [76, 84], [17, 98], [22, 32], [99, 30], [65, 8], [90, 40], [2, 7], [52, 73], [14, 31], [64, 38], [41, 50], [37, 12], [55, 68], [47, 2], [23, 91], [49, 93], [1, 85], [53, 14], [67, 96], [77, 58], [50, 75], [48, 61], [58, 43], [95, 27], [42, 71], [12, 86], [30, 78], [96, 81], [21, 35], [80, 79], [44, 76], [33, 23], [18, 62], [8, 48], [45, 49], [10, 99], [39, 83], [59, 45], [81, 15], [56, 47], [20, 95], [98, 39], [91, 46], [83, 29], [61, 13], [86, 77], [25, 56], [3, 42], [93, 88], [60, 19], [0, 18], [35, 55], [6, 10], [94, 26], [5, 41]]
print(W9)

print(10,"/",12)
W10 = [[53, 27], [39, 22], [12, 83], [92, 98], [66, 21], [48, 52], [13, 0], [98, 69], [99, 37], [24, 49], [18, 53], [50, 71], [63, 84], [19, 76], [91, 86], [28, 73], [93, 79], [68, 32], [7, 25], [76, 89], [94, 34], [31, 1], [30, 97], [1, 65], [79, 64], [71, 20], [38, 56], [96, 41], [5, 54], [46, 13], [29, 48], [52, 75], [85, 43], [70, 23], [9, 88], [40, 78], [42, 38], [82, 3], [32, 70], [25, 60], [43, 4], [35, 74], [14, 87], [54, 96], [0, 81], [16, 61], [90, 68], [64, 26], [62, 16], [75, 95], [97, 6], [22, 29], [72, 17], [4, 24], [81, 28], [65, 91], [3, 51], [47, 90], [87, 15], [77, 39], [15, 35], [57, 30], [27, 44], [2, 2], [41, 62], [23, 8], [45, 80], [20, 46], [26, 36], [55, 59], [6, 93], [80, 82], [37, 99], [84, 5], [61, 77], [60, 33], [36, 67], [33, 58], [34, 9], [78, 40], [11, 57], [21, 12], [69, 19], [58, 66], [17, 55], [67, 14], [89, 92], [83, 7], [44, 50], [56, 94], [73, 47], [10, 72], [88, 45], [74, 31], [49, 63], [86, 10], [95, 18], [51, 42], [59, 11], [8, 85]]
print(W10)

print(11,"/",12)
W11 = [[82, 22], [57, 62], [73, 74], [88, 32], [59, 72], [87, 99], [89, 4], [31, 35], [90, 8], [25, 78], [34, 58], [72, 37], [91, 49], [83, 19], [76, 25], [5, 7], [54, 12], [85, 13], [55, 51], [84, 59], [38, 17], [51, 87], [14, 24], [32, 2], [27, 18], [75, 52], [49, 46], [16, 38], [17, 36], [86, 53], [10, 89], [29, 41], [81, 84], [1, 0], [99, 75], [21, 69], [60, 66], [96, 96], [69, 63], [77, 92], [37, 27], [48, 45], [61, 34], [43, 6], [79, 1], [52, 77], [23, 43], [26, 55], [40, 61], [78, 95], [41, 79], [70, 56], [36, 90], [74, 48], [12, 39], [3, 60], [46, 67], [4, 47], [98, 91], [47, 88], [35, 73], [64, 28], [13, 44], [53, 64], [94, 21], [15, 93], [33, 54], [18, 31], [28, 16], [97, 94], [67, 97], [45, 29], [58, 82], [93, 10], [63, 33], [22, 70], [66, 50], [44, 85], [24, 5], [30, 23], [62, 11], [9, 9], [80, 42], [39, 20], [56, 30], [42, 68], [19, 71], [95, 57], [71, 86], [68, 98], [20, 81], [50, 65], [6, 76], [92, 40], [65, 26], [8, 83], [0, 14], [11, 15], [7, 3], [2, 80]]
print(W11)

print(12,"/",12)
W12 = [[83, 33], [54, 17], [66, 63], [82, 30], [34, 99], [86, 97], [37, 26], [63, 2], [1, 93], [49, 38], [42, 57], [75, 12], [18, 7], [93, 24], [87, 23], [79, 47], [65, 65], [9, 42], [28, 74], [32, 98], [48, 84], [69, 54], [25, 64], [91, 48], [68, 27], [81, 78], [88, 58], [85, 91], [39, 50], [15, 19], [90, 31], [98, 90], [22, 18], [10, 16], [92, 22], [97, 5], [55, 40], [17, 77], [47, 11], [57, 81], [2, 52], [45, 75], [94, 25], [80, 95], [70, 37], [26, 21], [84, 4], [73, 71], [0, 83], [11, 86], [72, 89], [74, 51], [77, 3], [67, 43], [43, 87], [99, 94], [33, 45], [52, 73], [53, 29], [23, 59], [96, 35], [21, 8], [71, 36], [7, 72], [58, 49], [41, 13], [3, 69], [89, 44], [56, 56], [14, 70], [38, 82], [95, 20], [30, 66], [50, 79], [62, 68], [61, 28], [35, 34], [60, 10], [8, 80], [44, 39], [13, 88], [4, 55], [78, 32], [12, 46], [20, 62], [27, 9], [5, 61], [51, 1], [29, 76], [6, 0], [59, 85], [64, 67], [36, 14], [24, 6], [31, 53], [46, 92], [16, 15], [76, 41], [40, 60], [19, 96]]
print(W12)

input = str(input("Welches Zeichen soll verschlüsselt weden?"))
storage = 0

if input in abc:
    index = abc.index(input)

    for x in range(0,len(abc)):

        if index == W1 [x] [0]:
            storage = W1 [x] [1]
            print("W1: ", abc [W1 [x] [0]], " zu ",abc [storage])
    index = storage

    #index = abc.index(storage)

    for x in range(0,len(abc)):

        if index == W2 [x] [0]:
            storage = W2 [x] [1]
            print("W2: ",abc [W2 [x] [0]], " zu ",abc [storage])
    index = storage

    #index = abc.index(storage)

    for x in range(0,len(abc)):

        if index == W3 [x] [0]:
            storage = W3 [x] [1]
            print("W3: ", abc [W3 [x] [0]], " zu ",abc [storage])
    index = storage

    #index = abc.index(storage)

    for x in range(0,len(abc)):

        if index == W4 [x] [0]:
            storage = W4 [x] [1]
            print("W4: ", abc [W4 [x] [0]], " zu ",abc [storage])
    index = storage

    #index = abc.index(storage)

    for x in range(0,len(abc)):

        if index == W5 [x] [0]:
            storage = W5 [x] [1]
            print("W5: ", abc [W5 [x] [0]], " zu ",abc [storage])
    index = storage

    #index = abc.index(storage)

    for x in range(0,len(abc)):

        if index == W6 [x] [0]:
            storage = W6 [x] [1]
            print("W6: ", abc [W6 [x] [0]], " zu ",abc [storage])
    index = storage

    for x in range(0,len(abc)):

        if index == W7 [x] [0]:
            storage = W7 [x] [1]
            print("W7: ", abc [W7 [x] [0]], " zu ",abc [storage])
    index = storage

    for x in range(0,len(abc)):

        if index == W8 [x] [0]:
            storage = W8 [x] [1]
            print("W8: ", abc [W8 [x] [0]], " zu ",abc [storage])
    index = storage

    for x in range(0,len(abc)):

        if index == W9 [x] [0]:
            storage = W9 [x] [1]
            print("W9: ", abc [W9 [x] [0]], " zu ",abc [storage])
    index = storage

    for x in range(0,len(abc)):

        if index == W10 [x] [0]:
            storage = W10 [x] [1]
            print("W10: ", abc [W10 [x] [0]], " zu ",abc [storage])
    index = storage

    for x in range(0,len(abc)):

        if index == W11 [x] [0]:
            storage = W11 [x] [1]
            print("W11: ", abc [W11 [x] [0]], " zu ",abc [storage])
    index = storage

    for x in range(0,len(abc)):

        if index == W12 [x] [0]:
            storage = W12 [x] [1]
            print("W12: ", abc [W12 [x] [0]], " zu ",abc [storage])
    index = storage

    print("Zeichen ", input, " wurde mit ", 12, "Walzen zu ", abc [storage], "verschlüsselt")

else:
    print("Ungültiges Zeichen:" ,input ," wird nicht unterstützt")
