## Python Debugger (PDB):
    PDB is Python's built-in command-line debugger, offering fine-grained control over program execution.
    Starting PDB:
    From the command line: python -m pdb your_script.py
    Within your code: import pdb; pdb.set_trace() (or breakpoint() in Python 3.7+)

## Common PDB Commands:
    n (next): Execute the next line in the current function. 
    s (step): Step into a function call.
    c (continue): Resume execution until the next breakpoint.
    b (break): Set a breakpoint at a specific line. -> (b line number)
    p (print): Display the value of a variable.
    l (list): List the current code being executed.
    q (quit): Exit the debugger.

## syntax 
 python -m pdb debug.py