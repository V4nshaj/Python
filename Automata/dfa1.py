from automata.fa.dfa import DFA
# DFA which matches all binary strings ending in an odd number of '1's
dfa = DFA(
 states={'q0', 'q1', 'q2', 'q3'},
 input_symbols={'0', '1'},
 transitions={
 'q0': {'0': 'q1', '1': 'q0'},
 'q1': {'0': 'q2', '1': 'q0'},
 'q2': {'0': 'q2', '1': 'q3'},
 'q3': {'0': 'q3', '1': 'q3'}
 },
 initial_state='q0',
 final_states={'q3'}
)
print(dfa.read_input('00010')) # answer is 'q3'
# dfa.read_input('011') # answer is error
# print(dfa.read_input_stepwise('011'))
if dfa.accepts_input('00110'):
 print('accepted')
else:
 print('rejected')

if dfa.accepts_input('011'):
 print('accepted')
else:
 print('rejected')