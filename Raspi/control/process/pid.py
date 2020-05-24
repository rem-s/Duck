<<<<<<< HEAD

#PID制御
def pid(target, measured, params):

    #パラメーター
    DELTA_T, KP, KI, KD, e_last, integral = params[0], params[1], params[2], params[3], params[4], params[5]

    #偏差、積分、微分値算出
    e = target - measured 
    integral += (e + e_last) / 2.0 * DELTA_T 
    differential = (e - e_last) / DELTA_T 
	
	
    #PID値の算出
    p = KP * e
    i = KI * integral
    d = KD * differential

    #回転数値算出
    turn = p + i + d

    #偏差算出
    params[4] = e
    params[5] = integral

    return turn

=======

#PID制御
def pid(target, measured, params):

    #パラメーター
    DELTA_T, KP, KI, KD, e_last, integral = params[0], params[1], params[2], params[3], params[4], params[5]

    #偏差、積分、微分値算出
    e = target - measured 
    integral += (e + e_last) / 2.0 * DELTA_T 
    differential = (e - e_last) / DELTA_T 
	
	
    #PID値の算出
    p = KP * e
    i = KI * integral
    d = KD * differential

    #回転数値算出
    turn = p + i + d

    #偏差算出
    params[4] = e
    params[5] = integral

    return turn

>>>>>>> 82d59ef54776e13b0daed50bc40928e964e964dc
