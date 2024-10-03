def gen_mat(order, exprs):
  '''
  Given list of mononomial sympy expressions `exprs`, generate matrix 
  of coefficients up to order `order`.
  Converts a monomial into a row of a matrix of coefficients of the monomial terms. 
  Nullspace of the (transpose) matrix and the nullspace of the (transpose) matrix 
  with the column of constant terms deleted, give the linear combinations which sum to 0 
  and to a general constant respectively. If the latter set is larger, there are dependencies.
  See "Generalized extrapolation methods based on compositions of a basic 2nd-order scheme", Blanes et. al. (2024).
  '''
    mat = sympy.Matrix.zeros(rows=len(exprs), cols=order+1)
    for i, p in enumerate(exprs):
        d = p.as_poly().as_dict()
        for k in range(order+1):  # index of a
            try:
                entry = d[(k,)]
            except:
                entry = 0
            mat[i, k] = entry
    return mat

mat = gen_mat(myOrd, exprs)
mat.T.nullspace() #combinations which sum to 0
mat[:, 1:].T.nullspace() #combinations which sum to 0 or any other combination
