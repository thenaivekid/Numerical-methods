data_points = [
    [1, 1],
    [2, 4],
    [3, 9],
    [4, 16],
    [5, 25],
    [6, 36]
]

xp = 3.5

sum = 0
for i in range(len(data_points)):
    product_i = 1
    for j in range(len(data_points)):
        if i != j:
            product_i *= (xp - data_points[j][0])/(data_points[i][0] - data_points[j][0])
    sum += product_i*data_points[i][1]
    
print(sum)