from automata.fa.nfa import NFA
# NFA which matches strings beginning with 'a', ending with 'a', and 
# containing
# no consecutive 'b's
nfa = NFA(
 states={'q0', 'q1', 'q2'},
 input_symbols={'a', 'b'},
 transitions={
 'q0': {'a': {'q1'}},
 # Use '' as the key name for empty string (lambda/epsilon) 
# transitions
 'q1': {'a': {'q1'}, '': {'q2'}},
 'q2': {'b': {'q0'}}
 },
 initial_state='q0',
 final_states={'q1'}
)

print(nfa.read_input('aba') )

if nfa.accepts_input('aba'):
 print('accepted')
else:
 print('rejected')
print(nfa.validate())