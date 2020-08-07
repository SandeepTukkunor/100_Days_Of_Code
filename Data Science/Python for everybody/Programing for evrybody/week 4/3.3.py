

def computepay(hours, rate):
    
    
    
    if hours >= 40:
        pay= hours * rate
        
        ovt = (hours-40) *(rate*0.5)
        
        totpay = pay + ovt
    else:
        totpay = hours * rate

    return totpay
        

        

hours = float(input("please enter a number"))
rate = float(input("please enter rate"))


p = computepay(hours, rate)
print(p)

        
        
        
        