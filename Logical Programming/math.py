#Matching Mathematical Expressio
from kanren import run, var, fact
from kanren.assoccomm import eq_assoccomm as eq
from kanren.assoccomm import commutative, associative

add = 'add'
mul = 'mul'
fact(commutative, mul)
fact(commutative, add)
fact(associative, mul)
fact(associative, add)
a, b = var('a'), var('b')
Original_pattern = (mul, (add, 5, a), b)
exp1 = (mul, (add, 5, 3), 5)
exp2 = (mul, (add, 5, 1), 8)
print(run(0, (a,b), eq(Original_pattern, exp1)))
print(run(0, (a,b), eq(Original_pattern, exp2)))
