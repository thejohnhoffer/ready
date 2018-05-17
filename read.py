def lines(f1, f2):
    out = f1.readline() + f2.readline()
    # Skip extra line in double-spaced file
    f2.readline()

    # Print out and try next line
    if out:
        print(out + '\n')
        lines(f1, f2)

def files(single, double):
    lines(open(single), open(double))
