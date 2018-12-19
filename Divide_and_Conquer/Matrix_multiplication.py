

def matrix_multiplication(matrix_a, matrix_b):
    if len(matrix_a) == 2:
        m1 = (matrix_a[1][0] + matrix_a[1][1] - matrix_a[0][0])(matrix_b[1][1] - matrix_b[0][1] + matrix_b[0][0])
        #I wont program it now as it's a fairly simple concept and I don't think I'll learn much from it, since is
        #basically just tedious (of course, the difficulty was in the factorization by Strassen)