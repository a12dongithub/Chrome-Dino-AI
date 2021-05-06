import random
import numpy as np
import tensorflow as tf
import math

def sigmoid(x):
    if x > 100:
        return 1
    if x < -100:
        return 0
    return 1 / (1 + math.exp(-x))
def rand():
    return (2*random.random()-1)*1
def br():
    return random.random() > 0.5
def model():
    a = []
    for d in range(2):
        tempd = []
        for i in range(3):
            temp = []
            for j in range(4):
                temp.append(rand())
            tempd.append(temp)
        a.append(tempd)
    a = np.array(a)
    return a
def predict(a,b):
    res = []
    tres = []
    for i in range(3):
        temp = 0
        for j in range(3):
            temp = temp + a[j]*b[0][i][j]
        temp = temp + b[0][i][3]
        tres.append(temp)
    for i in range(3):
        temp = 0
        for j in range(3):
            temp = temp + tres[j]*b[1][i][j]
        temp = temp + b[1][i][3]
        res.append(sigmoid(temp))
    return res
def models(n):
    for i in range(n):
        np.save('./models/model' + str(i), model())
def crossbreeding(model1,model2):
    a = model1
    b = model2
    for d in range(2):
        for i in range(3):
            for j in range(4):
                temp1 = a[d][i][j]
                temp2 = b[d][i][j]
                if random.random() < 0.3:
                    r1 = random.random()
                    r2 = random.random()
                    a[d][i][j] = temp2
                    
                if random.random() < 0.7:
                    r1 = rand()
                    r2 = rand()
                    b[d][i][j] = temp1
                
    return [a,b]
def muta(model1):
    a = model1
    for d in range(2):
        for i in range(3):
            for j in range(4):
                if random.random() < 0.4:
                    r1 = rand()
                    a[d][i][j] = r1
    return a
def mutation(score,n,models):
    idx = []
    for i in range(n):
        idx.append(i)
    score, idx = zip(*sorted(zip(score, idx)))
    
    top = []
    cross = []
    for i in range(10):
        top.append(models[idx[n-i-1]])
    for i in range(7):
        for j in range(i+1,7):
            temp = crossbreeding(top[i],top[j])
            cross.append(temp[0])
            cross.append(temp[1])
            
            
    newmodels = []
    for i in range(18):
        newmodels.append(model())

    mut = []
    temp = model()
    for j in range(3):
        for i in range(len(top)):
            mut.append(muta(top[i]))
    final = []
    for i in top:
        final.append(i)
    for i in cross:
        final.append(i)
    for i in mut:
        final.append(i)
    for i in newmodels:
        final.append(i)
    print(len(final))
    for i in range(len(final)):
        np.save("./models/model" + str(i),final[i])

def control(distance,speed,height,n,models):
    res = []
    for i in range(n):
        res.append(predict([distance,speed,height],models[i]))
        #res.append([br(),br(),br()])
    return res


