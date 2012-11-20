

def isvowelable(word):
    vowels = 'aeiou'
    l = [c for c in word if c in vowels]
    return l == list(vowels)

def acending_order(word):
    return list(word)[:-1] == sorted(word)[1:]

def main():
    print "Hello World"
    vowelable_words = []
    acending_words = []
    with open('words.txt', 'r') as words:
        for word in words:
            if isvowelable(word):
                vowelable_words.append(word)
            if len(word) >= 7 and acending_order(word):
                acending_words.append(word)

    print "Words containing exactly five vowels (a, e, i, o and u) in ascending order"
    print len(vowelable_words)
    print  ''.join(vowelable_words)
    print "Words of length at least six that contain letters in strictly ascending alphabetical order"
    print len(acending_words)
    print ''.join(acending_words)

if __name__ == "__main__":
    main()
