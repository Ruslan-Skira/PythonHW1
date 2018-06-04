class MatrixShow():
    # class to found the row columns and diagonal in your matrix

    def __init__(self, matrix, number):
        # init our parameters
        self.matrix = matrix
        self.column_number = number
        self.line_number = number

    # method to show the row what you need to look in matrix

    def show_column_agregator(self):
        answer = ([row[self.column_number] for row in self.matrix])
        print(answer)

    def show_line_agregator(self):
        answer = (self.matrix[self.line_number])
        print(answer)

    def show_diagonal_agregator(self):
        answer = [[]]
        print(answer)


    def show_row_cycle(self):
        i = 0

        while i < self.matrix.__len__():
            print(self.matrix[i][self.column_number])
            i += 1

    def show_diagonal_cycle(self):
        i = 0
        k = self.matrix[0].__len__()

        while i < self.matrix.__len__():
            k -= 1
            print(test[i][k])




if __name__ == '__main__':
    M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    test1 = MatrixShow(M, 2)
    test1.show_column_agregator()
