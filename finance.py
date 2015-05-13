# This library makes it easy to incorporate common financial calculations.
from __future__ import division
 
# Present Value (PV)
def PV(rate, cf1):
    rate = rate / 100
    pv = cf1 / (1 + rate)
    return round(pv * 100) / 100
        
# Future Value (FV)
def FV(rate, cf0, numOfPeriod):
    rate = rate / 100
    fv = cf0 * (1 + rate)**numOfPeriod
    return round(fv * 100) / 100

# Net Present Value (NPV)
# USE: NPV(rate, initial investment, [cash flows])
# http://www.investopedia.com/articles/fundamental-analysis/09/net-present-value.asp
def NPV(rate, *args):
    rate = rate / 100
    npv = args[1]
    for x in range(2,len(args)):
        npv += (args[x] / (1 + rate)**x-1)
    return round(npv * 100) / 100

# Internal Rate of Return (IRR)
# USE: IRR(initial investment, [cash flows])
#TODO
