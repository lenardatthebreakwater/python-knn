import math
import statistics

gender = {"female": 0, "male": 1}

#labels are age, weight(kg), and height(cm) respectively
dataset = [
        [25, 42, gender["female"], 163], #sakura (le sserafim)
        [23, 43, gender["female"], 163], #chaewon (le sserafim)
        [17, 46, gender["female"], 169], #eunchae (le sserafim)
        [20, 51, gender["female"], 170], #kazuha (le sserafim)
        [22, 54, gender["female"], 172], #yunjin (le sserafim)
        [26, 56, gender["male"], 171], #bangchan (stray kids)
        [25, 58, gender["male"], 172], #lee know (stray kids)
        [24, 68, gender["male"], 167], #changbin (stray kids)
        [23, 58, gender["male"], 179], #hyunjin (stray kids)
        [23, 60, gender["male"], 169], #han (stray kids)
        [23, 56, gender["male"], 171], #felix (stray kids)
        [23, 56, gender["male"], 178], #seungmin (stray kids)
        [22, 55, gender["male"], 170], #I.N (stray kids)
        [23, 43, gender["female"], 162], #lia (itzy)
        [22, 47, gender["female"], 164], #ryujin (itzy)
        [20, 47, gender["female"], 170], #yuna (itzy)
        [23, 69, gender["male"], 185], #soobin (txt)
        [24, 65, gender["male"], 181], #yeonjun (txt)
        [22, 55, gender["male"], 179], #beomgyu (txt)
        [22, 55, gender["male"], 177], #taehyun (txt)
        [21, 67, gender["male"], 183], #kai (txt)
        [27, 45, gender["female"], 161], #miyeon (gidle)
        [26, 48, gender["female"], 164], #minnie (gidle)
        [25, 42, gender["female"], 157], #soyeon (gidle)
        [24, 45, gender["female"], 161], #shuhuah (gidle)
        [24, 47, gender["female"], 162], #yuqi (gidle)
        [19, 45, gender["female"], 169], #minji (new jeans)
        [19, 46, gender["female"], 162], #hanni (nj)
        [18, 46, gender["female"], 165], #danielle (nj)
        [17, 45, gender["female"], 165], #haerin (nj)
        [15, 47, gender["female"], 170], #hyein (nj)
        [23, 45, gender["female"], 168], #karina (aespa)
        [23, 48, gender["female"], 164], #giselle(aespa)
        [23, 41, gender["female"], 163], #winter (aespa)
        [21, 43, gender["female"], 161] #ningnign (aespa) 
]

X_train = []
for i in range(len(dataset)):
    X_train.append(dataset[i][:len(dataset[0])-1])


y_train = []
for i in range(len(dataset)):
    y_train.append(dataset[i][-1:][0])

#suga (bts)
x_test = [21, 44, gender["male"]]
y_test = 165

distances = []
for i in range(len(X_train)):
    num = ((X_train[i][0] - x_test[0]) ** 2) + ((X_train[i][1] - x_test[1]) ** 2) + ((X_train[i][2] - x_test[2]) ** 2)
    distance = math.sqrt(num)
    distances.append(distance)

class Neighbor():
    def __init__(self, x_train_distance, y_train):
        self.x_train_distance = x_train_distance
        self.y_train = y_train

all_neighbors = []
for i in range(len(dataset)):
    y_train = dataset[i][-1:][0]
    x_train_distance = distances[i]
    n = Neighbor(x_train_distance, y_train)
    all_neighbors.append(n)

all_neighbors.sort(key=lambda n: n.x_train_distance)
knearest_neighbors = all_neighbors[:3]

knearest_y_values = []
for i in range(len(knearest_neighbors)):
    knearest_y_values.append(knearest_neighbors[i].y_train)

prediction = statistics.mean(knearest_y_values)
print(prediction)

