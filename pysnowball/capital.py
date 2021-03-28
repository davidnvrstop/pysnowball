import json
import os
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls


def margin(symbol,method=cons.JSON_DUMP_MODE,page=1, size=180):
    url = api_ref.capital_margin_url+symbol
    url = url + '&page='+str(page)
    url = url + '&size='+str(size)
    return utls.fetch(url,method)


def blocktrans(symbol,method=cons.JSON_DUMP_MODE, page=1, size=30):
    url = api_ref.capital_blocktrans_url+symbol
    url = url + '&page='+str(page)
    url = url + '&size='+str(size)
    return utls.fetch(url,method)


def capital_assort(symbol,method=cons.JSON_DUMP_MODE):
    url = api_ref.capital_assort_url+symbol
    return utls.fetch(url,method)


def capital_flow(symbol,method=cons.JSON_DUMP_MODE):
    url = api_ref.capital_flow_url+symbol
    return utls.fetch(url,method)


def capital_history(symbol,method=cons.JSON_DUMP_MODE, count=20):
    url = api_ref.capital_history_url+symbol
    url = url + '&count='+str(count)
    return utls.fetch(url,method)
