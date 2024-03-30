# viết hàm tạo ma trận 3x3 random có các giá trị trong 1 list

def random_matrix():
    import random
    list_digit = [i for i in range(9)]
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            id = random.randint(0, len(list_digit)-1)
            row.append(list_digit[id])
            del list_digit[id]
        matrix.append(row)
    return matrix

print(random_matrix())