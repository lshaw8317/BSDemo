def gen_mat(order, exprs):
  '''
  Given list of mononomial sympy expressions `exprs`, generate matrix 
  of coefficients up to order `order`.
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
