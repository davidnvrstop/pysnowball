import json
import os
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls



def cash_flow(symbol, method=cons.JSON_DUMP_MODE,is_annals=0, count=10):

    url = api_ref.finance_cash_flow_url+symbol
    
    if is_annals == 1:
        url = url + '&type=Q4'
    
    url = url + '&count='+str(count)

    return utls.fetch(url,method)


def indicator(symbol,method=cons.JSON_DUMP_MODE, is_annals=0, count=10):
    
    url = api_ref.finance_indicator_url+symbol
    
    if is_annals == 1:
        url = url + '&type=Q4'
    
    url = url + '&count='+str(count)

    return utls.fetch(url,method)


def balance(symbol, method=cons.JSON_DUMP_MODE,is_annals=0, count=10):

    url = api_ref.finance_balance_url+symbol

    if is_annals == 1:
        url = url + '&type=Q4'

    url = url + '&count='+str(count)

    return utls.fetch(url,method)


def income(symbol,method=cons.JSON_DUMP_MODE, is_annals=0, count=10):
    
    url = api_ref.finance_income_url+symbol

    if is_annals == 1:
        url = url + '&type=Q4'

    url = url + '&count='+str(count)

    return utls.fetch(url,method)


def business(symbol,method=cons.JSON_DUMP_MODE, is_annals=0, count=10):

    url = api_ref.finance_business_url+symbol

    if is_annals == 1:
        url = url + '&type=Q4'

    url = url + '&count='+str(count)

    return utls.fetch(url,method)
 
