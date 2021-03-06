import sys

# Assumes files are well formatted
# If you have errors, make sure you double check our input and output format


def main(argv):
    if len(argv) != 2:
        print "Usage: python scorer_single.py [path_to_instance] [path_to_answer]"
        return
    print processTest(argv[0], argv[1])


def processTest(inst, sol):
    fin = open(inst, "r")
    N = int(fin.readline().split()[0])
    d = [[0 for j in range(N)] for i in range(N)]
    for i in xrange(N):
        d[i] = map(int, fin.readline().split())

    fin = open(sol, "r")
    ans = map(lambda x: (int(x) - 1), fin.readline().split())

    count = 0.0
    for i in xrange(N):
        for j in xrange(i + 1, N):
            if d[ans[i]][ans[j]] == 1:
                count += 1
    return "solution value is %d" % count


def scoreSolution(inst, sol):
    '''
    Identical to processTest, but returns the value of the solution,
    and uses the instance matrix and solution list, instead of files
    as inputs.
    '''
    N = len(inst)

    count = 0.0
    for i in xrange(N):
        for j in xrange(i + 1, N):
            if inst[sol[i]][sol[j]] == 1:
                count += 1
    return count


if __name__ == '__main__':
    main(sys.argv[1:])
