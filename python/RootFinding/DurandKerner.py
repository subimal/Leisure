

def DurandKerner(c, tol = 1e-20, itermax=1000, check_progress=False, debugfile='DurandKerner.log'):
    from random import random
    from logging import basicConfig, debug, DEBUG
    
    basicConfig(filename=debugfile, encoding='utf-8', level=DEBUG)
    debug("\n\n"+"-"*10+"Debug info")
    debug("Enabled: "+str(check_progress))
    
    err = 2*tol
    err_roots = 2*tol
    stalled_progress=False

    if check_progress:
        debug("\nFinding roots of " + "+".join([str(c[len(c)-1-i])+"x^"+str(i) for i in range(len(c)-1, -1,-1)]) )
        
    while err_roots>tol and (not stalled_progress):
        iters = 0
        r = [complex(random(),random())**i for i in range(len(c)-1)]
        
        if check_progress:
            debug(f"{r}")

        r1 = [0 for i in range(len(c)-1)]
        f = lambda x: sum([c[len(c)-1-i]*(x**i) for i in range(len(c)-1, -1,-1) ]) 

        while (err>tol and iters<=itermax):
            for n in range(len(r)):
                den=1
                for i in range(len(r)):
                    if i!=n:
                        den=den*(r[n]-r[i])


                if den!=0:
                    r1[n] = r[n] - f(r[n])/den
            
            err_r = max([abs((r1[i]-r[i]).real) for i in range(len(r)) ])
            err_i = max([abs((r1[i]-r[i]).imag) for i in range(len(r)) ])
            err_roots = max([abs(f(r[i])) for i in range(len(r)) ])
            errnew = max([err_r, err_i, err_roots])
            r = r1[:]
            if check_progress:
                debug(f"Roots: {r} \nError: {errnew}")
            if errnew==err:
                stalled_progress = True
                break
            err = errnew
            iters = iters+1

    if check_progress:
        for n in range(len(r)):
            debug(f"f({r[n]}) = {f(r[n])}")
    debug("End of debugging\n"+"-"*10+"\n")
    return r, err, iters


tol = 1e-20
itermax = 1000
check_progress = False

c = [1, -3, 3, -5]
print("Final roots, error, iterations: ", DurandKerner(c, tol=tol, itermax=itermax, check_progress=check_progress))
print()



c = [1, -2, 1]
print("Final roots, error, iterations: ", DurandKerner(c, tol=tol, itermax=itermax, check_progress=check_progress))
print()

c = [1, -5,6]
print("Final roots, error, iterations: ", DurandKerner(c, tol=tol, itermax=itermax, check_progress=check_progress))
print()

c = [1, -2, 0]
print("Final roots, error, iterations: ", DurandKerner(c, tol=tol, itermax=itermax, check_progress=check_progress))
print()

c = [1, -3.1415992654]
print("Final roots, error, iterations: ", DurandKerner(c, tol=tol, itermax=itermax, check_progress=check_progress))
print()

c = [1, 2, 1]
print("Final roots, error, iterations: ", DurandKerner(c, tol=tol, itermax=itermax, check_progress=check_progress))
print()

c = [1, 0, 1]
print("Final roots, error, iterations: ", DurandKerner(c, tol=tol, itermax=itermax, check_progress=check_progress))
print()

