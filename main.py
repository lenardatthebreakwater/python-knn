import math
import statistics
from dataset import gender, dataset

X_train = []
for i in range(len(dataset)):
    X_train.append(dataset[i][:len(dataset[0])-1])


y_train = []
for i in range(len(dataset)):
    y_train.append(dataset[i][-1:][0])

age = int(input("Age: "))
weight = int(input("Weight(kg): "))
gender = input("Gender: ")
if gender == "male":
    g = 1
elif gender == "female":
    g = 0
x_test = []
x_test.append(age)
x_test.append(weight)
x_test.append(g)

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
