
def rotate_matrix(M):
    n = len(M)
    assert n == len(M[0])
    N = [[None for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            N[j][n-1-i] = M[i][j]
    return N

def transpose(M):
    for i in range(n):
        for j in range(0, i):
            M[i][j], M[j][i] = M[j][i], M[i][j]

def mirror(M):
    n = len(M)
    if n % 2:
        h = int(n/2)
    else:
        h = int((n - 1) / 2)
    for i in range(n):
        for j in range(0, h+1):
            M[i][j], M[i][n-1-j] = M[i][n-1-j], M[i][j]

def rotate_matrix_two_pass(M):
    transpose(M)
    mirror(M)

def pprint(M):
    for l in M:
        print(l)
    print('\n')

if __name__ == "__main__":
    n = 4
    M = [[i for i in range(j*n+1, (j+1)*n+1)] for j in range(n)]
    pprint(M)
    rotate_matrix_two_pass(M)
    pprint(M)