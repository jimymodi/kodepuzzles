#!/usr/bin/python

import sys

def atm(amt, bal):
    charges = 0.5
    status, msg, bal = withdraw(amt, bal, charges).values()
    print msg
    print bal

def withdraw(amt, bal, charges):
    if bal < (amt + charges):
        return {"status" : False,
                "msg" : "Insufficient Funds",
                "bal" : bal}
    elif amt % 5 != 0:
        return {"status" : False,
                "msg" : "Incorrect Withdrawal Amount (not multiple of 5)",
                "bal" : bal}

    bal_left = (bal - amt - 0.5)
    return {"status" : True,
            "msg" : "Successful Transaction",
            "bal" : bal_left}

def withdraw_test():
    #test 1
    status, msg, bal = withdraw(30, 120.00, 0.5).values()
    assert True == status
    assert "Successful Transaction" == msg, msg
    assert 89.5 == bal, bal
    
    #test 2
    status, msg, bal = withdraw(300, 120.00, 0.5).values()
    assert False == status
    assert "Insufficient Funds" == msg, msg
    assert 120.00 == bal, bal

    #test 3
    status, msg, bal = withdraw(29, 120.00, 0.5).values()
    assert False == status
    assert "Incorrect Withdrawal Amount (not multiple of 5)" == msg, msg
    assert 120.00 == bal, bal

    print "Test Passed"

def main():
    #parese command line args
    if sys.argv[1] == 'test':
        withdraw_test()
        exit(1)

    try:
        script, amt, bal = sys.argv
        amt = int(amt)
        bal = float(bal)
        atm(amt, bal)
    except ValueError:
        print " Usage: AmtToWithdraw (int)  InitialBal (float)"

if __name__ == '__main__':
    main()
