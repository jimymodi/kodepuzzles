
import collections

def main():
    print "Hello World"
    s = "isthebananaofthegreatfruitlikepapayabutfruitofbraziliansoftheworldisineastwestnorthsouththegreatindiasealikn"
    final = ''
    for i in range(2, len(s)):
        sl = []
        for n in range(len(s)):
            sl.append(s[n:n+i])
    
            dup = [x for x, y in collections.Counter(sl).items() if y > 1]
            if dup :
                final = dup
    print final

if __name__ == "__main__":
    main()
