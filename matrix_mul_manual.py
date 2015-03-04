def mat_mul(A,B):
    """
    A Generic matrix multiplication - the hard and complex-er way
    with O(n^3) instead of np.matrix which I suspect uses
    Coppersmith–Winograd algorithm using BLAS
    """
    C = [[0 for _ in xrange(len(B[0]))] for _ in xrange(len(A))]
    for cr in xrange(len(A[0])):
        for r in xrange(len(A)):
            for c in xrange(len(B[0])):
                C[r][c] += A[r][cr]*B[cr][c]
    return C
