# from sympy import ImmutableMatrix, Matrix

def tupleMult(g,h):
    r = (len(g)-1)//2
    return tuple([g[i]+h[i] for i in range(len(g)-1)]) + tuple([g[-1]+h[-1]+sum([g[r+i]*h[i] for i in range(r)])])

def getGens(r):
    gens = set()
    for i in range(2*r):
        gens.add(tuple([0 for _ in range(i)] + [1] + [0 for _ in range(2*r-i-1)] + [0]))
        gens.add(tuple([0 for _ in range(i)] + [-1] + [0 for _ in range(2*r-i-1)] + [0]))
    return gens

def growthHr(r, radius):
    
    ball = {tuple(0 for l in range(2*r+1))}
    sphere = ball
    seq = [1]
    gens = getGens(r)
    
    for _ in range(radius):
        newelts = {tupleMult(g,gen) for g in sphere for gen in gens}

        sphere = {new for new in newelts if new not in ball}
        
        ball.update(sphere)
        seq.append(len(sphere))

    return seq

print(growthHr(6, 4))