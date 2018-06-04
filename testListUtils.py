if __name__ == '__main__':
    import listUtils

M = [[1,2,3], [4,5,6],[7,8,9]]
#print(M);

# TODO create method by list comprehension expression what show me column row an diag

test1 = listUtils.MatrixShow(M, 2).show_column_agregator()

test2 = listUtils.MatrixShow(M, 0).show_line_agregator()


test3 = listUtils.MatrixShow(M, 2).show_row_cycle()


