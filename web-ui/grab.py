import tushare as ts
import yaml
import datetime
import json


def getSampleByCode(code, end_date='2024-02-22', time_delta=90):
    code = code
    if code[:2] in ['00', '30']:
        symbol = code + '.SZ'
    elif code[:2] in ['60', '68']:
        symbol = code + '.SH'
    else:
        symbol = code

    with open('config.json', 'r') as f:
        config = json.load(f)
        assert config['tushare_api_token'], "tushare api token not found in config.json"

    pro = ts.pro_api(config['tushare_api_token'])
    df = pro.daily(**{
        "ts_code": symbol,
        "trade_date": "",
        "start_date": "",
        "end_date": int(''.join([str(x) for x in end_date.split('-')])),
        "offset": "",
        "limit": 90 - 1,
    }, fields=[
        "pct_chg",
        "ts_code",
        "trade_date",
        "open",
        "close",
        "high",
        "low"
    ])
    try:
        pct_chg = [*df['pct_chg']][::-1]
        tradedate = [*df['trade_date']][::-1]
        sample = {
            'date': datetime.datetime.today(),
            'end': str(end_date),
            'code': code,
            'stdchange': pct_chg,
            'tradedate': tradedate,

            'open': [*df['open']][::-1],
            'close': [*df['close']][::-1],
            'high': [*df['high']][::-1],
            'low': [*df['low']][::-1]
        }

        with open(f'../data/test/{code}.yaml', 'w+') as f:
            yaml.dump(sample, f)

        return f'../data/test/{code}.yaml'
    except Exception as e:
        print(e)



end_date = '2024-02-22'
getSampleByCode('300002', end_date)
