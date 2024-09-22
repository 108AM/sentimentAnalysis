def sparseToCSR(matrix):

    #initialises the matrix to be returned and the three rows it contains
    dense_matrix = []
    values = []
    columns = []
    rows = []

    #iterating through each row
    for row in range(len(matrix)):

        #iterating through each element of each row
        for element in range(len(matrix[row])):

            #if the element doesn't equal 0, its value, row and column are appended to the CSR matrix
            if matrix[row][element] != 0:
                values.append(matrix[row][element])
                columns.append(element)
                rows.append(row)
        
    #the three arrays are appended to the CSR matrix
    dense_matrix.append(values)
    dense_matrix.append(columns)
    dense_matrix.append(rows)

    return dense_matrix,len(matrix)


def CSRmatrixVectorMultiplication(CSRmatrix, vector, matrixlength):

    # initialises the vector to be returned as a vector of 0s the same length as the input vector
    product_vector = [0 for i in range(matrixlength)]
    
    #iterates through each non-zero value in the CSR matrix
    for i in range(len(CSRmatrix[0])):

        #'tranposes' matrix
        value = CSRmatrix[0][i]
        rownumber = CSRmatrix[2][i]
        columnnumber = CSRmatrix[1][i]

        #matrix-vector multiplication of each non-zero value with the corresponding parameter in the vector
        product_vector[rownumber] += value * vector[columnnumber]

    return(product_vector)








    