# cook your dish here
def find_spoon():
    num_test_cases = int(input())

    for _ in range(num_test_cases):
        rows, columns = map(int, input().split())
        matrix = []
        for _ in range(rows):
            matrix.append(input().lower())
            #print(matrix)
        found_spoon = False
        for row in matrix:
            if 'spoon' in row:
                found_spoon = True
                break
        if not found_spoon:
            for j in range(columns):
                column = ''.join(matrix[i][j] for i in range(rows))
                #print(column)
                if 'spoon' in column:
                    found_spoon = True
                    break

        if found_spoon:
            print("There is a spoon!")
        else:
            print("There is indeed no spoon!")
find_spoon()
