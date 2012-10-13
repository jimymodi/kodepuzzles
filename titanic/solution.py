
def remove_odds(applicants):
    new = []
    for i,p in applicants:
        if i % 2 == 0:
            new.append(p)
    return new

def best_position(n):
    
    applicants = range(1, n+1)
    while len(applicants) > 1:
        applicants = remove_odds(enumerate(applicants, start=1))

    return applicants[0]

def test():
    assert 4 == best_position(5)
    assert 8 == best_position(12)
    print "Test Passed"

def main():
    test()
    n = 15
    print "Best Position for", n, " applicants"
    print best_position(n)

if __name__ == '__main__' :
    main()
