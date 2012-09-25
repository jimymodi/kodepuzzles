#!/usr/bin/python

import sys

def atm(amt, bal):
    if amt > bal:
        print "Insufficient Funds"
        
    elif amt % 5 != 0:
        print "Incorrect Withdrawal Amount (not multiple of 5)"
    else :
        print "Successful Transaction"
        bal_left = (bal - amt - 0.5)
        print "%.2f" % bal_left

def main():
    #parese command line args
    try:
        script, amt, bal = sys.argv
        amt = int(amt)
        bal = float(bal)
    except:
        print " Usage: AmtToWithdraw (int)  InitialBal (float)"
        sys.exit(2)
    
    atm(amt, bal)

if __name__ == '__main__':
    main()
