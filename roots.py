# Square & cube roots by Newton's method, without loop constructs

def better_guess (x, yguess, errorbar):
    if abs (x - yguess * yguess) < errorbar: return yguess
    else: return better_guess (x,(yguess + x/yguess)/2, errorbar)

def sqrt (x, precision):
    errorbar = x * precision
    return better_guess(x, x/2., errorbar)

def better_cube(x, yguess, errorbar):
    if abs (x - yguess * yguess * yguess) < errorbar: return yguess
    else: return better_cube (x, (x/(yguess * yguess) + 2*yguess)/3., errorbar)

def cubert (x, precision):
    errorbar = x * precision
    return better_cube(x, x/3., errorbar)
