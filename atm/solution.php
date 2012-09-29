<?php


function withdraw($amt, $bal, $charges) {
    if( $bal < ($amt + $charges)) {
        return array("status" => false,
                     "msg" => "Insufficient Funds",
                     "bal" => $bal);
    }
    else if( $amt % 5 != 0) {
        return array("status" => false,
                     "msg" => "Incorrect Withdrawal Amount (not multiple of 5)",
                     "bal" => $bal);
    }

    $bal_left = ($bal - $amt - $charges);
        return array("status" => true,
                     "msg" => "Successful Transaction",
                     "bal" => $bal_left);
}

function withdraw_test() {
    //test 1
    $result = withdraw(30, 120.00, 0.5);
    list($status, $msg, $bal) = array_values($result);
    assert(true == $status);
    assert("Successful Transaction" == $msg);
    assert(89.5 == $bal);
    

    #test 2
    $result = withdraw(300, 120.00, 0.5);
    list($status, $msg, $bal) = array_values($result);
    assert(false == $status);
    assert("Insufficient Funds" == $msg);
    assert(120.00 == $bal);

    #test 3
    $result = withdraw(29, 120.00, 0.5);
    list($status, $msg, $bal) = array_values($result);
    assert(false == $status);
    assert("Incorrect Withdrawal Amount (not multiple of 5)" == $msg);
    assert(120.00 == $bal);
    
    echo "Test Passed\n";
}
withdraw_test();
