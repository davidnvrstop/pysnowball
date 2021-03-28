import json
import os
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls


def skholderchg(symbol,method=cons.JSON_DUMP_MODE):
    url = api_ref.f10_skholderchg+symbol
    return utls.fetch(url,method,method)


def skholder(symbol,method=cons.JSON_DUMP_MODE):
    url = api_ref.f10_skholder+symbol
    return utls.fetch(url,method,method)


def industry(symbol,method=cons.JSON_DUMP_MODE):
    url = api_ref.f10_industry+symbol
    return utls.fetch(url,method)


def holders(symbol,method=cons.JSON_DUMP_MODE):
    url = api_ref.f10_holders+symbol
    return utls.fetch(url,method)


def bonus(symbol,method=cons.JSON_DUMP_MODE,page=1,size=10):
    url = api_ref.f10_bonus+symbol
    url = url + '&page='+str(page)
    url = url + '&size='+str(size)
    return utls.fetch(url,method)


def org_holding_change(symbol,method=cons.JSON_DUMP_MODE):
    url = api_ref.f10_org_holding_change+symbol
    return utls.fetch(url,method)


def industry_compare(symbol,method=cons.JSON_DUMP_MODE):
    url = api_ref.f10_industry_compare+symbol
    return utls.fetch(url,method)


def business_analysis(symbol,method=cons.JSON_DUMP_MODE):
    url = api_ref.f10_business_analysis+symbol
    return utls.fetch(url,method)


def shareschg(symbol, method=cons.JSON_DUMP_MODE,count=5):
    url = api_ref.f10_shareschg+symbol
    url = url + '&count='+str(count)
    return utls.fetch(url,method)


def top_holders(symbol,method=cons.JSON_DUMP_MODE, circula=1):
    url = api_ref.f10_top_holders+symbol
    url = url + '&circula='+str(circula)
    return utls.fetch(url,method)


def main_indicator(symbol,method=cons.JSON_DUMP_MODE):
    url = api_ref.f10_indicator+symbol
    return utls.fetch(url,method)
