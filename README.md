# Deterministic_Turing_Machine
Simple Python code for a deterministic Turing machine.

Example of inputs: 

8 <-- acceptance state
22 <-- number of transitions
0 0 1 X D
0 1 2 X D
1 0 1 0 D
1 1 1 1 D
1 # 3 # D
3 X 3 X D
3 0 5 X E
2 0 2 0 D
2 1 2 1 D
2 # 4 # D
4 X 4 X D
4 1 5 X E
5 0 5 0 E
5 1 5 1 E
5 X 5 X E
5 # 6 # E
6 0 6 0 E
6 1 6 1 E
6 X 0 X D
0 # 7 # D
7 X 7 X D
7 B 8 B D
10 <-- number of strings to be tested
-
#
010#010
011011
011010001#011010001
011010001#011010000
111111111#
111111111#111111111
111111111#000000000
101011101#101011001

The machine will work on an inpunt and verify wheter the strings belongs to the language or not.
