abc = ["A", "Ä", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "Ö", "P", "Q", "R", "S", "T", "U", "Ü", "V", "W", "X", "Y", "Z", "a", "ä", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "q", "r", "s", "t", "u", "ü", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~", " ", "°"]

zeichen = 0
index = 0


print(1,"/",24)
W1 = [[60, 57], [87, 38], [19, 94], [21, 65], [39, 18], [64, 36], [59, 97], [45, 8], [56, 60], [69, 23], [89, 29], [32, 68], [72, 71], [11, 45], [9, 82], [25, 20], [23, 43], [34, 83], [10, 22], [13, 96], [85, 13], [38, 1], [73, 75], [95, 74], [66, 53], [62, 55], [75, 25], [50, 56], [90, 26], [91, 79], [67, 92], [7, 61], [76, 41], [37, 72], [40, 24], [61, 34], [78, 12], [52, 70], [94, 87], [83, 90], [17, 27], [96, 69], [6, 93], [4, 48], [5, 19], [70, 52], [49, 28], [30, 84], [81, 7], [18, 6], [44, 88], [84, 77], [8, 76], [86, 4], [58, 0], [77, 59], [28, 33], [51, 54], [74, 9], [0, 91], [41, 10], [12, 73], [36, 67], [46, 15], [43, 21], [54, 2], [48, 85], [35, 37], [27, 86], [65, 44], [55, 58], [80, 31], [82, 51], [71, 50], [97, 3], [92, 49], [3, 46], [15, 64], [2, 17], [33, 30], [99, 89], [31, 14], [57, 78], [63, 32], [29, 66], [53, 39], [22, 40], [47, 81], [20, 63], [98, 11], [88, 99], [93, 98], [14, 42], [24, 16], [16, 80], [68, 47], [79, 5], [26, 62], [42, 95], [1, 35]]
print(W1)

print(2,"/",42)
W2 = [[33, 53], [46, 64], [96, 25], [64, 62], [23, 30], [84, 18], [97, 16], [17, 96], [55, 77], [54, 82], [4, 15], [77, 94], [52, 34], [78, 67], [18, 44], [6, 68], [85, 26], [80, 98], [72, 72], [59, 55], [43, 73], [89, 54], [71, 81], [16, 61], [28, 95], [10, 86], [45, 60], [1, 75], [25, 9], [50, 63], [44, 36], [31, 93], [63, 0], [67, 97], [42, 33], [94, 65], [61, 7], [91, 17], [83, 22], [22, 1], [24, 38], [99, 83], [2, 39], [76, 28], [21, 90], [26, 91], [75, 6], [62, 58], [86, 71], [92, 59], [9, 3], [60, 37], [82, 13], [90, 70], [0, 78], [66, 92], [29, 45], [49, 76], [51, 42], [95, 2], [87, 51], [20, 69], [74, 41], [5, 43], [88, 85], [48, 66], [41, 80], [57, 5], [93, 74], [37, 8], [73, 14], [12, 99], [13, 79], [53, 32], [8, 56], [7, 49], [36, 52], [11, 47], [69, 10], [68, 24], [38, 40], [14, 11], [34, 35], [81, 84], [15, 19], [47, 57], [35, 88], [56, 4], [98, 21], [27, 23], [65, 50], [30, 27], [3, 46], [32, 31], [40, 20], [19, 48], [39, 12], [79, 87], [70, 29], [58, 89]]
print(W2)

print(3,"/",24)
W3 = [[71, 55], [69, 86], [94, 40], [95, 11], [11, 61], [6, 64], [14, 58], [52, 14], [55, 81], [70, 39], [68, 3], [37, 52], [77, 10], [61, 6], [33, 8], [76, 47], [92, 57], [45, 46], [46, 95], [79, 44], [10, 7], [8, 72], [43, 13], [85, 83], [48, 94], [0, 68], [1, 25], [51, 74], [63, 96], [74, 99], [38, 48], [21, 49], [96, 89], [57, 56], [19, 98], [54, 79], [58, 33], [42, 66], [72, 23], [40, 5], [26, 62], [87, 1], [17, 32], [89, 42], [62, 38], [36, 37], [83, 70], [39, 17], [82, 28], [73, 26], [34, 97], [16, 30], [59, 60], [29, 41], [53, 20], [80, 73], [3, 0], [99, 34], [25, 59], [47, 12], [32, 63], [15, 4], [60, 87], [35, 77], [81, 15], [65, 76], [2, 85], [5, 18], [13, 75], [75, 93], [78, 53], [31, 9], [88, 43], [4, 29], [66, 67], [90, 91], [18, 88], [24, 71], [28, 51], [64, 21], [67, 2], [7, 92], [20, 16], [23, 80], [98, 27], [27, 54], [50, 78], [9, 36], [49, 84], [84, 19], [41, 31], [30, 65], [86, 24], [56, 45], [12, 69], [22, 90], [91, 22], [44, 50], [93, 35], [97, 82]]
print(W3)

print(4,"/",24)
W4 = [[27, 68], [14, 66], [79, 8], [76, 79], [60, 95], [6, 81], [67, 53], [78, 96], [10, 48], [58, 18], [87, 22], [65, 26], [15, 57], [20, 84], [41, 52], [48, 51], [68, 21], [54, 44], [32, 93], [1, 14], [0, 29], [51, 69], [40, 65], [71, 59], [8, 27], [90, 58], [75, 3], [44, 41], [25, 54], [63, 37], [18, 2], [56, 28], [99, 97], [36, 47], [53, 36], [34, 55], [26, 70], [46, 5], [42, 4], [30, 15], [9, 31], [86, 56], [55, 46], [28, 98], [17, 63], [69, 30], [64, 74], [47, 71], [66, 87], [62, 9], [61, 67], [59, 11], [77, 39], [35, 16], [7, 34], [84, 10], [13, 85], [24, 89], [29, 77], [38, 60], [89, 73], [3, 25], [31, 90], [50, 23], [52, 1], [93, 88], [74, 12], [49, 82], [81, 76], [5, 6], [16, 86], [97, 38], [98, 33], [37, 75], [57, 20], [19, 40], [45, 7], [88, 94], [12, 72], [83, 0], [95, 42], [11, 80], [70, 61], [94, 62], [73, 32], [80, 64], [92, 43], [96, 13], [22, 91], [33, 78], [39, 49], [2, 19], [82, 99], [43, 17], [4, 50], [91, 83], [72, 24], [85, 45], [23, 92], [21, 35]]
print(W4)

print(5,"/",24)
W5 = [[12, 37], [95, 17], [26, 64], [3, 87], [43, 49], [53, 3], [65, 53], [78, 44], [88, 77], [32, 56], [16, 91], [20, 84], [19, 93], [96, 76], [87, 30], [93, 81], [55, 70], [72, 5], [59, 57], [66, 12], [33, 33], [30, 99], [25, 71], [70, 75], [90, 83], [61, 19], [76, 59], [62, 11], [73, 55], [11, 36], [74, 15], [51, 82], [6, 38], [31, 67], [44, 78], [41, 72], [97, 94], [23, 58], [52, 85], [15, 40], [42, 21], [98, 96], [71, 34], [54, 31], [75, 14], [91, 13], [8, 69], [27, 20], [89, 73], [49, 4], [58, 43], [64, 54], [84, 35], [80, 98], [24, 42], [81, 62], [10, 25], [18, 65], [46, 24], [40, 16], [92, 50], [34, 48], [45, 97], [63, 89], [57, 10], [17, 18], [83, 7], [56, 46], [79, 74], [85, 95], [50, 29], [48, 39], [5, 92], [60, 8], [38, 22], [69, 2], [21, 66], [29, 9], [77, 32], [2, 68], [68, 86], [36, 47], [82, 61], [7, 6], [14, 52], [86, 26], [28, 28], [22, 1], [37, 45], [35, 79], [47, 63], [67, 51], [99, 88], [9, 27], [4, 90], [94, 41], [1, 23], [13, 80], [39, 60], [0, 0]]
print(W5)

print(6,"/",24)
W6 = [[93, 29], [12, 93], [46, 63], [41, 57], [32, 0], [73, 83], [65, 6], [57, 17], [89, 16], [78, 33], [5, 98], [38, 54], [91, 52], [80, 61], [96, 12], [55, 72], [13, 99], [59, 73], [75, 64], [50, 71], [69, 39], [58, 47], [37, 37], [62, 15], [52, 18], [21, 2], [35, 85], [36, 20], [31, 82], [16, 13], [14, 24], [43, 65], [20, 11], [92, 41], [84, 27], [70, 9], [66, 30], [11, 78], [86, 59], [63, 22], [18, 46], [28, 97], [82, 10], [87, 38], [54, 8], [77, 25], [33, 49], [72, 31], [61, 36], [94, 69], [42, 32], [8, 56], [49, 68], [98, 45], [23, 26], [2, 89], [97, 4], [0, 75], [39, 43], [67, 58], [34, 70], [6, 40], [19, 87], [24, 5], [48, 53], [88, 74], [74, 44], [1, 90], [3, 1], [95, 81], [29, 95], [10, 21], [27, 91], [68, 86], [47, 23], [60, 80], [81, 35], [64, 60], [71, 7], [22, 92], [9, 50], [45, 94], [25, 66], [4, 77], [17, 55], [26, 76], [15, 34], [79, 84], [40, 28], [44, 19], [51, 42], [76, 14], [56, 62], [85, 51], [90, 3], [99, 67], [7, 96], [83, 48], [30, 88], [53, 79]]
print(W6)

print(7,"/",24)
W7 = [[13, 13], [16, 43], [81, 0], [91, 37], [95, 99], [57, 45], [72, 17], [44, 81], [22, 16], [31, 5], [58, 92], [23, 31], [65, 65], [37, 91], [46, 29], [19, 58], [96, 14], [48, 38], [1, 60], [74, 11], [82, 55], [26, 77], [39, 66], [43, 33], [61, 36], [89, 73], [49, 93], [75, 94], [17, 96], [92, 97], [18, 71], [56, 3], [2, 39], [54, 19], [86, 47], [80, 98], [0, 20], [53, 62], [8, 83], [70, 79], [73, 44], [35, 51], [88, 86], [14, 27], [6, 75], [67, 9], [50, 68], [36, 87], [41, 78], [45, 69], [9, 15], [79, 76], [10, 74], [20, 8], [5, 7], [59, 34], [29, 56], [62, 63], [33, 50], [99, 53], [85, 49], [68, 80], [63, 88], [83, 42], [38, 22], [84, 67], [25, 2], [42, 46], [28, 57], [32, 82], [97, 18], [52, 59], [12, 25], [66, 72], [98, 89], [94, 12], [76, 61], [93, 26], [40, 23], [24, 41], [27, 64], [55, 10], [71, 85], [21, 95], [7, 6], [11, 35], [30, 28], [64, 48], [90, 24], [51, 4], [4, 52], [87, 70], [60, 90], [47, 84], [77, 32], [15, 40], [3, 54], [69, 30], [78, 1], [34, 21]]
print(W7)

print(8,"/",24)
W8 = [[24, 22], [44, 1], [73, 72], [26, 51], [81, 96], [93, 30], [96, 3], [49, 19], [45, 89], [69, 70], [47, 83], [77, 11], [23, 33], [21, 67], [19, 94], [79, 87], [67, 59], [43, 34], [92, 0], [90, 62], [98, 7], [70, 88], [72, 77], [97, 31], [25, 58], [75, 80], [36, 49], [32, 38], [29, 93], [8, 81], [80, 65], [0, 26], [74, 29], [56, 75], [52, 12], [85, 56], [58, 35], [64, 45], [48, 61], [65, 78], [17, 40], [40, 63], [57, 14], [15, 97], [1, 4], [54, 92], [5, 23], [42, 15], [14, 21], [68, 90], [2, 52], [95, 47], [82, 9], [88, 5], [4, 71], [20, 20], [84, 68], [61, 28], [78, 95], [38, 86], [89, 60], [71, 13], [39, 8], [60, 36], [53, 18], [31, 39], [16, 98], [3, 43], [83, 55], [91, 66], [33, 16], [94, 10], [76, 37], [86, 2], [10, 32], [87, 42], [37, 41], [28, 17], [41, 24], [59, 50], [12, 69], [55, 76], [51, 99], [62, 74], [66, 6], [34, 54], [7, 46], [13, 84], [46, 91], [99, 48], [63, 85], [6, 44], [18, 73], [35, 27], [22, 82], [30, 79], [27, 57], [9, 53], [11, 25], [50, 64]]
print(W8)

print(9,"/",24)
W9 = [[34, 94], [36, 44], [70, 16], [71, 1], [84, 36], [46, 3], [85, 82], [79, 59], [7, 92], [11, 34], [75, 63], [82, 69], [29, 33], [72, 52], [9, 17], [63, 25], [62, 28], [15, 97], [88, 57], [54, 66], [57, 9], [68, 72], [69, 0], [51, 6], [16, 87], [38, 22], [13, 11], [27, 51], [19, 21], [92, 60], [74, 65], [97, 37], [31, 70], [73, 64], [32, 5], [66, 90], [4, 24], [89, 53], [87, 80], [28, 67], [78, 54], [43, 74], [26, 89], [24, 4], [40, 20], [76, 84], [17, 98], [22, 32], [99, 30], [65, 8], [90, 40], [2, 7], [52, 73], [14, 31], [64, 38], [41, 50], [37, 12], [55, 68], [47, 2], [23, 91], [49, 93], [1, 85], [53, 14], [67, 96], [77, 58], [50, 75], [48, 61], [58, 43], [95, 27], [42, 71], [12, 86], [30, 78], [96, 81], [21, 35], [80, 79], [44, 76], [33, 23], [18, 62], [8, 48], [45, 49], [10, 99], [39, 83], [59, 45], [81, 15], [56, 47], [20, 95], [98, 39], [91, 46], [83, 29], [61, 13], [86, 77], [25, 56], [3, 42], [93, 88], [60, 19], [0, 18], [35, 55], [6, 10], [94, 26], [5, 41]]
print(W9)

print(10,"/",24)
W10 = [[53, 27], [39, 22], [12, 83], [92, 98], [66, 21], [48, 52], [13, 0], [98, 69], [99, 37], [24, 49], [18, 53], [50, 71], [63, 84], [19, 76], [91, 86], [28, 73], [93, 79], [68, 32], [7, 25], [76, 89], [94, 34], [31, 1], [30, 97], [1, 65], [79, 64], [71, 20], [38, 56], [96, 41], [5, 54], [46, 13], [29, 48], [52, 75], [85, 43], [70, 23], [9, 88], [40, 78], [42, 38], [82, 3], [32, 70], [25, 60], [43, 4], [35, 74], [14, 87], [54, 96], [0, 81], [16, 61], [90, 68], [64, 26], [62, 16], [75, 95], [97, 6], [22, 29], [72, 17], [4, 24], [81, 28], [65, 91], [3, 51], [47, 90], [87, 15], [77, 39], [15, 35], [57, 30], [27, 44], [2, 2], [41, 62], [23, 8], [45, 80], [20, 46], [26, 36], [55, 59], [6, 93], [80, 82], [37, 99], [84, 5], [61, 77], [60, 33], [36, 67], [33, 58], [34, 9], [78, 40], [11, 57], [21, 12], [69, 19], [58, 66], [17, 55], [67, 14], [89, 92], [83, 7], [44, 50], [56, 94], [73, 47], [10, 72], [88, 45], [74, 31], [49, 63], [86, 10], [95, 18], [51, 42], [59, 11], [8, 85]]
print(W10)

print(11,"/",24)
W11 = [[82, 22], [57, 62], [73, 74], [88, 32], [59, 72], [87, 99], [89, 4], [31, 35], [90, 8], [25, 78], [34, 58], [72, 37], [91, 49], [83, 19], [76, 25], [5, 7], [54, 12], [85, 13], [55, 51], [84, 59], [38, 17], [51, 87], [14, 24], [32, 2], [27, 18], [75, 52], [49, 46], [16, 38], [17, 36], [86, 53], [10, 89], [29, 41], [81, 84], [1, 0], [99, 75], [21, 69], [60, 66], [96, 96], [69, 63], [77, 92], [37, 27], [48, 45], [61, 34], [43, 6], [79, 1], [52, 77], [23, 43], [26, 55], [40, 61], [78, 95], [41, 79], [70, 56], [36, 90], [74, 48], [12, 39], [3, 60], [46, 67], [4, 47], [98, 91], [47, 88], [35, 73], [64, 28], [13, 44], [53, 64], [94, 21], [15, 93], [33, 54], [18, 31], [28, 16], [97, 94], [67, 97], [45, 29], [58, 82], [93, 10], [63, 33], [22, 70], [66, 50], [44, 85], [24, 5], [30, 23], [62, 11], [9, 9], [80, 42], [39, 20], [56, 30], [42, 68], [19, 71], [95, 57], [71, 86], [68, 98], [20, 81], [50, 65], [6, 76], [92, 40], [65, 26], [8, 83], [0, 14], [11, 15], [7, 3], [2, 80]]
print(W11)

print(12,"/",24)
W12 = [[83, 33], [54, 17], [66, 63], [82, 30], [34, 99], [86, 97], [37, 26], [63, 2], [1, 93], [49, 38], [42, 57], [75, 12], [18, 7], [93, 24], [87, 23], [79, 47], [65, 65], [9, 42], [28, 74], [32, 98], [48, 84], [69, 54], [25, 64], [91, 48], [68, 27], [81, 78], [88, 58], [85, 91], [39, 50], [15, 19], [90, 31], [98, 90], [22, 18], [10, 16], [92, 22], [97, 5], [55, 40], [17, 77], [47, 11], [57, 81], [2, 52], [45, 75], [94, 25], [80, 95], [70, 37], [26, 21], [84, 4], [73, 71], [0, 83], [11, 86], [72, 89], [74, 51], [77, 3], [67, 43], [43, 87], [99, 94], [33, 45], [52, 73], [53, 29], [23, 59], [96, 35], [21, 8], [71, 36], [7, 72], [58, 49], [41, 13], [3, 69], [89, 44], [56, 56], [14, 70], [38, 82], [95, 20], [30, 66], [50, 79], [62, 68], [61, 28], [35, 34], [60, 10], [8, 80], [44, 39], [13, 88], [4, 55], [78, 32], [12, 46], [20, 62], [27, 9], [5, 61], [51, 1], [29, 76], [6, 0], [59, 85], [64, 67], [36, 14], [24, 6], [31, 53], [46, 92], [16, 15], [76, 41], [40, 60], [19, 96]]
print(W12)

print(13,"/",24)
W13 = [[24, 20], [50, 78], [2, 61], [40, 3], [6, 76], [82, 95], [94, 45], [93, 56], [86, 81], [69, 48], [9, 83], [29, 68], [41, 10], [70, 35], [49, 59], [52, 93], [81, 77], [65, 41], [14, 1], [0, 21], [54, 13], [92, 32], [34, 29], [72, 85], [57, 72], [4, 17], [13, 88], [95, 38], [36, 9], [97, 0], [17, 2], [66, 5], [12, 11], [60, 60], [71, 99], [91, 64], [39, 6], [19, 40], [74, 87], [80, 82], [38, 44], [37, 15], [22, 12], [90, 70], [31, 19], [48, 90], [43, 57], [18, 52], [46, 84], [84, 34], [73, 7], [16, 24], [75, 30], [28, 65], [59, 73], [64, 91], [83, 18], [25, 74], [44, 37], [20, 80], [55, 8], [56, 26], [5, 33], [33, 16], [10, 51], [15, 63], [79, 4], [61, 23], [67, 69], [1, 86], [87, 53], [3, 42], [47, 46], [85, 49], [76, 89], [11, 98], [78, 96], [53, 47], [30, 94], [42, 43], [89, 79], [99, 27], [77, 39], [63, 66], [7, 22], [32, 31], [51, 55], [62, 62], [21, 58], [27, 28], [88, 92], [23, 54], [45, 25], [26, 50], [35, 36], [58, 97], [68, 14], [96, 75], [8, 71], [98, 67]]
print(W13)

print(14,"/",24)
W14 = [[0, 39], [66, 76], [61, 80], [42, 70], [33, 75], [44, 24], [58, 73], [45, 52], [43, 89], [3, 65], [30, 64], [79, 55], [86, 26], [13, 21], [67, 53], [37, 74], [53, 81], [94, 37], [23, 48], [71, 12], [73, 15], [24, 62], [41, 10], [46, 25], [1, 50], [96, 61], [59, 93], [65, 6], [72, 19], [84, 56], [97, 86], [93, 79], [48, 16], [82, 99], [55, 32], [47, 92], [8, 31], [50, 97], [92, 91], [29, 18], [21, 49], [14, 84], [87, 4], [76, 44], [88, 27], [70, 30], [49, 72], [95, 35], [19, 69], [78, 45], [98, 66], [36, 43], [27, 23], [74, 60], [40, 57], [54, 33], [80, 29], [68, 90], [99, 58], [25, 1], [77, 87], [81, 83], [52, 85], [39, 41], [64, 63], [7, 54], [18, 28], [4, 40], [57, 95], [22, 22], [89, 3], [60, 5], [12, 51], [91, 98], [35, 46], [63, 42], [15, 9], [16, 0], [10, 68], [32, 2], [20, 71], [56, 88], [5, 67], [51, 36], [83, 38], [6, 13], [2, 94], [90, 14], [62, 20], [28, 11], [11, 47], [9, 82], [85, 77], [31, 78], [34, 59], [26, 7], [69, 34], [38, 17], [75, 96], [17, 8]]
print(W14)

print(15,"/",24)
W15 = [[60, 5], [96, 91], [17, 29], [21, 88], [14, 97], [99, 94], [45, 78], [30, 66], [20, 93], [29, 15], [87, 36], [90, 68], [31, 21], [58, 20], [25, 3], [52, 44], [83, 45], [66, 61], [85, 98], [2, 49], [41, 24], [77, 40], [74, 41], [95, 82], [62, 32], [78, 25], [37, 92], [94, 75], [79, 73], [26, 10], [4, 56], [67, 54], [71, 72], [82, 2], [53, 1], [81, 95], [48, 90], [97, 38], [13, 69], [1, 17], [50, 74], [16, 19], [61, 48], [0, 4], [84, 8], [8, 64], [47, 62], [86, 65], [89, 39], [34, 84], [98, 60], [51, 71], [23, 9], [43, 33], [44, 51], [11, 79], [40, 50], [80, 80], [22, 16], [36, 59], [57, 53], [65, 86], [32, 89], [10, 52], [38, 55], [9, 70], [76, 0], [3, 11], [68, 76], [6, 46], [73, 18], [5, 12], [12, 81], [55, 14], [63, 58], [18, 63], [54, 77], [33, 47], [15, 34], [24, 7], [70, 22], [59, 28], [75, 87], [27, 57], [64, 43], [39, 6], [42, 13], [7, 35], [88, 42], [92, 99], [28, 30], [49, 37], [69, 85], [91, 67], [72, 83], [93, 31], [19, 26], [46, 27], [56, 23], [35, 96]]
print(W15)

print(16,"/",24)
W16 = [[25, 19], [49, 65], [79, 44], [52, 58], [57, 4], [4, 46], [43, 91], [74, 6], [41, 45], [93, 5], [76, 78], [21, 17], [30, 0], [31, 64], [67, 16], [98, 29], [81, 7], [24, 39], [16, 41], [97, 11], [87, 68], [92, 36], [36, 26], [26, 1], [60, 60], [33, 3], [55, 96], [0, 59], [37, 42], [2, 54], [20, 22], [91, 62], [47, 72], [96, 47], [61, 12], [42, 95], [51, 30], [58, 57], [34, 13], [3, 35], [48, 63], [54, 99], [59, 48], [69, 97], [6, 10], [95, 49], [28, 37], [62, 38], [85, 81], [77, 66], [88, 74], [10, 93], [35, 23], [11, 34], [75, 8], [56, 21], [53, 71], [19, 80], [12, 32], [90, 24], [13, 50], [45, 52], [14, 55], [32, 31], [7, 40], [29, 86], [15, 14], [84, 2], [68, 28], [94, 9], [99, 18], [89, 53], [86, 73], [9, 77], [1, 85], [63, 61], [5, 56], [73, 25], [8, 69], [82, 82], [78, 70], [17, 27], [40, 67], [65, 75], [64, 98], [71, 79], [44, 51], [66, 87], [83, 94], [38, 90], [23, 20], [27, 88], [18, 84], [80, 76], [46, 92], [39, 83], [70, 89], [72, 43], [50, 15], [22, 33]]
print(W16)

print(17,"/",24)
W17 = [[35, 39], [88, 75], [87, 29], [94, 4], [90, 7], [29, 50], [3, 51], [4, 47], [58, 73], [9, 10], [37, 15], [63, 34], [46, 56], [33, 70], [52, 77], [16, 62], [26, 26], [13, 22], [62, 6], [71, 42], [50, 91], [34, 57], [15, 67], [11, 2], [75, 46], [69, 64], [76, 0], [0, 71], [67, 38], [23, 27], [56, 36], [41, 82], [59, 25], [60, 69], [22, 37], [10, 54], [81, 44], [61, 80], [78, 41], [68, 16], [43, 65], [98, 59], [73, 18], [44, 58], [5, 96], [6, 83], [49, 30], [47, 85], [45, 87], [21, 24], [40, 72], [1, 89], [2, 61], [55, 92], [80, 99], [42, 28], [64, 8], [51, 81], [28, 76], [77, 12], [91, 48], [83, 93], [79, 55], [14, 53], [18, 43], [24, 35], [19, 63], [57, 3], [54, 60], [39, 49], [92, 14], [12, 86], [32, 23], [96, 94], [17, 21], [74, 98], [30, 88], [82, 95], [84, 5], [70, 32], [48, 31], [89, 33], [27, 19], [53, 52], [97, 1], [95, 97], [38, 90], [86, 78], [20, 68], [7, 84], [36, 9], [65, 66], [93, 40], [25, 45], [8, 11], [66, 79], [31, 17], [99, 20], [72, 74], [85, 13]]
print(W17)

print(18,"/",24)
W18 = [[34, 64], [57, 39], [13, 28], [4, 35], [15, 71], [7, 73], [55, 98], [2, 85], [86, 95], [99, 12], [36, 4], [44, 0], [25, 50], [31, 78], [0, 1], [73, 96], [3, 5], [64, 13], [42, 90], [33, 60], [71, 72], [92, 65], [24, 20], [58, 77], [75, 44], [74, 9], [67, 3], [59, 68], [43, 43], [63, 6], [90, 48], [54, 94], [26, 88], [85, 53], [76, 46], [40, 84], [98, 70], [56, 54], [5, 49], [89, 93], [78, 34], [37, 18], [10, 52], [53, 23], [39, 22], [30, 76], [45, 47], [84, 87], [18, 66], [65, 26], [38, 67], [61, 62], [69, 97], [83, 38], [51, 92], [14, 27], [49, 19], [1, 75], [77, 14], [94, 42], [87, 15], [12, 36], [46, 74], [81, 63], [41, 16], [50, 57], [66, 11], [32, 83], [60, 37], [72, 32], [23, 24], [48, 99], [19, 81], [29, 86], [93, 2], [8, 91], [97, 33], [79, 58], [9, 7], [35, 55], [95, 45], [70, 80], [91, 10], [22, 31], [96, 82], [17, 8], [52, 40], [27, 25], [88, 21], [80, 59], [28, 17], [62, 79], [20, 69], [68, 56], [11, 51], [82, 89], [21, 41], [16, 30], [47, 29], [6, 61]]
print(W18)

print(19,"/",24)
W19 = [[37, 87], [84, 55], [39, 14], [93, 88], [23, 91], [46, 44], [78, 8], [82, 5], [7, 93], [89, 82], [9, 79], [49, 97], [68, 15], [96, 30], [83, 80], [8, 7], [13, 43], [10, 52], [34, 54], [21, 3], [44, 6], [52, 35], [36, 78], [67, 10], [77, 22], [88, 28], [61, 60], [51, 31], [53, 19], [79, 95], [35, 9], [71, 46], [1, 34], [99, 32], [28, 41], [70, 50], [63, 38], [47, 58], [31, 23], [22, 69], [33, 72], [32, 59], [87, 75], [74, 16], [60, 27], [91, 67], [85, 26], [66, 25], [41, 4], [16, 98], [86, 94], [48, 86], [73, 29], [54, 61], [3, 33], [55, 11], [11, 84], [56, 51], [2, 66], [18, 36], [92, 39], [29, 68], [58, 24], [14, 2], [19, 37], [81, 13], [38, 53], [80, 17], [4, 1], [97, 42], [98, 62], [76, 18], [72, 48], [12, 74], [42, 81], [25, 96], [24, 40], [17, 21], [0, 85], [64, 57], [95, 63], [43, 83], [6, 65], [26, 92], [75, 0], [90, 64], [69, 47], [50, 49], [94, 56], [45, 45], [62, 99], [30, 70], [59, 71], [57, 12], [65, 90], [20, 89], [5, 76], [27, 20], [15, 73], [40, 77]]
print(W19)

print(20,"/",24)
W20 = [[48, 16], [92, 93], [14, 20], [13, 23], [47, 15], [74, 47], [55, 4], [22, 80], [35, 12], [19, 69], [39, 7], [95, 2], [12, 55], [69, 95], [66, 37], [23, 45], [7, 73], [78, 97], [65, 0], [20, 94], [0, 39], [32, 54], [50, 74], [36, 60], [24, 35], [40, 66], [46, 5], [76, 84], [45, 96], [84, 59], [38, 82], [42, 32], [33, 72], [26, 30], [94, 19], [88, 85], [15, 83], [5, 25], [73, 56], [10, 52], [17, 64], [51, 87], [67, 3], [59, 9], [75, 63], [79, 17], [25, 38], [9, 88], [99, 43], [31, 33], [37, 78], [72, 40], [44, 70], [41, 67], [86, 99], [71, 27], [87, 61], [61, 13], [16, 79], [43, 44], [57, 89], [64, 18], [53, 86], [97, 31], [98, 51], [58, 57], [29, 58], [52, 1], [68, 24], [93, 92], [54, 62], [11, 76], [60, 68], [56, 50], [27, 75], [85, 46], [80, 34], [8, 28], [77, 65], [83, 91], [30, 90], [89, 77], [70, 10], [49, 81], [21, 98], [6, 26], [2, 11], [1, 48], [63, 49], [90, 21], [62, 8], [34, 42], [18, 22], [28, 14], [96, 71], [82, 6], [3, 36], [91, 29], [81, 41], [4, 53]]
print(W20)

print(21,"/",24)
W21 = [[5, 24], [39, 50], [78, 20], [73, 86], [38, 98], [81, 46], [75, 30], [99, 97], [25, 75], [57, 15], [3, 18], [26, 58], [90, 34], [77, 79], [42, 68], [55, 7], [83, 73], [82, 42], [51, 37], [70, 88], [67, 90], [40, 40], [60, 99], [1, 78], [93, 29], [12, 53], [56, 77], [69, 13], [54, 54], [92, 39], [59, 64], [86, 72], [53, 3], [27, 51], [96, 17], [35, 26], [95, 87], [6, 36], [32, 82], [48, 21], [88, 38], [14, 80], [98, 0], [31, 25], [91, 81], [61, 55], [49, 43], [45, 60], [72, 91], [74, 84], [17, 33], [87, 62], [76, 95], [4, 11], [21, 74], [47, 61], [50, 5], [22, 44], [36, 9], [52, 22], [28, 41], [0, 52], [9, 94], [18, 85], [34, 27], [37, 65], [33, 1], [46, 16], [68, 56], [20, 14], [43, 35], [64, 59], [23, 48], [80, 92], [8, 2], [89, 76], [15, 96], [13, 19], [10, 12], [44, 57], [79, 8], [30, 71], [19, 6], [58, 4], [71, 23], [2, 63], [24, 32], [65, 67], [84, 28], [7, 93], [41, 69], [16, 45], [11, 89], [63, 47], [62, 83], [66, 66], [85, 70], [29, 31], [94, 10], [97, 49]]
print(W21)

print(22,"/",24)
W22 = [[10, 53], [99, 63], [44, 52], [50, 17], [64, 71], [2, 83], [98, 66], [4, 72], [79, 19], [36, 82], [29, 97], [89, 80], [76, 74], [12, 51], [65, 41], [49, 1], [39, 35], [75, 81], [19, 3], [57, 88], [7, 95], [81, 22], [38, 30], [46, 94], [18, 77], [87, 14], [32, 48], [55, 38], [26, 75], [45, 13], [94, 86], [23, 65], [1, 27], [77, 78], [8, 56], [16, 42], [11, 60], [52, 79], [51, 87], [20, 96], [90, 25], [61, 58], [58, 21], [3, 34], [72, 10], [47, 49], [67, 76], [15, 2], [40, 70], [95, 31], [14, 43], [53, 44], [33, 84], [80, 18], [30, 5], [88, 92], [24, 26], [22, 67], [62, 89], [17, 28], [37, 98], [59, 61], [86, 50], [92, 91], [84, 39], [6, 99], [74, 36], [48, 7], [69, 4], [78, 73], [0, 93], [68, 24], [31, 6], [82, 69], [91, 47], [60, 8], [56, 54], [83, 15], [34, 32], [42, 11], [27, 57], [93, 90], [41, 40], [5, 68], [35, 62], [96, 23], [71, 59], [97, 9], [13, 46], [9, 85], [25, 55], [43, 29], [70, 45], [85, 16], [63, 0], [21, 33], [28, 37], [54, 64], [73, 12], [66, 20]]
print(W22)

print(23,"/",24)
W23 = [[51, 39], [20, 60], [31, 21], [29, 41], [30, 19], [87, 30], [74, 56], [45, 37], [53, 43], [5, 98], [63, 78], [36, 80], [41, 63], [85, 14], [37, 1], [38, 59], [47, 11], [95, 84], [19, 34], [80, 16], [42, 71], [8, 70], [81, 12], [17, 75], [56, 4], [54, 29], [48, 57], [55, 23], [16, 79], [52, 54], [62, 45], [9, 65], [72, 27], [83, 25], [35, 35], [99, 91], [57, 6], [1, 66], [34, 36], [27, 3], [90, 93], [65, 17], [79, 68], [75, 61], [67, 44], [96, 95], [91, 64], [73, 49], [61, 97], [10, 22], [2, 87], [64, 7], [98, 20], [84, 58], [69, 50], [86, 77], [32, 82], [50, 18], [44, 74], [25, 33], [77, 89], [43, 81], [14, 13], [39, 24], [3, 40], [21, 26], [66, 53], [4, 86], [58, 96], [18, 51], [49, 8], [82, 2], [11, 85], [59, 48], [6, 52], [71, 88], [22, 62], [68, 5], [33, 83], [13, 9], [24, 46], [78, 15], [89, 32], [0, 99], [46, 72], [60, 47], [12, 42], [28, 69], [40, 73], [76, 10], [93, 76], [92, 0], [23, 38], [97, 31], [94, 55], [26, 67], [88, 92], [7, 90], [70, 94], [15, 28]]
print(W23)

print(24,"/",24)
W24 = [[65, 13], [98, 41], [77, 77], [58, 54], [78, 38], [80, 35], [40, 66], [85, 51], [86, 63], [26, 61], [46, 58], [97, 15], [3, 95], [1, 59], [16, 69], [76, 91], [23, 28], [44, 72], [79, 48], [33, 23], [41, 71], [34, 93], [7, 67], [20, 29], [64, 88], [83, 11], [63, 31], [42, 43], [31, 98], [53, 75], [72, 55], [50, 12], [52, 1], [67, 4], [0, 52], [82, 79], [39, 27], [54, 96], [74, 64], [27, 50], [17, 6], [57, 33], [69, 16], [36, 7], [66, 2], [60, 47], [94, 45], [48, 83], [88, 5], [5, 97], [93, 62], [73, 82], [56, 0], [14, 39], [18, 84], [37, 92], [4, 25], [45, 87], [8, 18], [81, 76], [89, 42], [43, 85], [92, 30], [90, 37], [68, 74], [70, 22], [13, 36], [91, 99], [84, 14], [24, 9], [51, 26], [47, 46], [29, 94], [87, 70], [35, 3], [22, 78], [30, 89], [25, 44], [10, 10], [49, 49], [55, 56], [71, 60], [28, 17], [38, 73], [95, 34], [75, 21], [6, 65], [2, 24], [12, 68], [96, 86], [62, 40], [61, 19], [9, 32], [59, 81], [21, 20], [32, 57], [11, 8], [99, 80], [15, 53], [19, 90]]
print(W24)


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

    for x in range(0,len(abc)):

        if index == W13 [x] [0]:
            storage = W13 [x] [1]
            print("W13: ",abc [W13 [x] [0]], " zu ",abc [storage])
    index = storage

    for x in range(0,len(abc)):

        if index == W14 [x] [0]:
            storage = W14 [x] [1]
            print("W14: ", abc [W14 [x] [0]], " zu ",abc [storage])
    index = storage

    for x in range(0,len(abc)):

        if index == W15 [x] [0]:
            storage = W15 [x] [1]
            print("W15: ", abc [W15 [x] [0]], " zu ",abc [storage])
    index = storage

    for x in range(0,len(abc)):

        if index == W16 [x] [0]:
            storage = W16 [x] [1]
            print("W16: ", abc [W16 [x] [0]], " zu ",abc [storage])
    index = storage

    for x in range(0,len(abc)):

        if index == W17 [x] [0]:
            storage = W17 [x] [1]
            print("W17: ", abc [W17 [x] [0]], " zu ",abc [storage])
    index = storage

    for x in range(0,len(abc)):

        if index == W18 [x] [0]:
            storage = W18 [x] [1]
            print("W18: ", abc [W18 [x] [0]], " zu ",abc [storage])
    index = storage

    for x in range(0,len(abc)):

        if index == W19 [x] [0]:
            storage = W19 [x] [1]
            print("W19: ",abc [W19 [x] [0]], " zu ",abc [storage])
    index = storage

    for x in range(0,len(abc)):

        if index == W20 [x] [0]:
            storage = W20 [x] [1]
            print("W20: ", abc [W20 [x] [0]], " zu ",abc [storage])
    index = storage

    for x in range(0,len(abc)):

        if index == W21 [x] [0]:
            storage = W21 [x] [1]
            print("W21: ", abc [W21 [x] [0]], " zu ",abc [storage])
    index = storage

    for x in range(0,len(abc)):

        if index == W22 [x] [0]:
            storage = W22 [x] [1]
            print("W22: ", abc [W22 [x] [0]], " zu ",abc [storage])
    index = storage

    for x in range(0,len(abc)):

        if index == W23 [x] [0]:
            storage = W23 [x] [1]
            print("W23: ",abc [W23 [x] [0]], " zu ",abc [storage])
    index = storage

    for x in range(0,len(abc)):

        if index == W24 [x] [0]:
            storage = W24 [x] [1]
            print("W24: ", abc [W24 [x] [0]], " zu ",abc [storage])
    index = storage



    print("Zeichen ", input, " wurde mit ", 12, "Walzen zu ", abc [storage], "verschlüsselt")

else:
    print("Ungültiges Zeichen:" ,input ," wird nicht unterstützt")

