import tushare as ts
import yaml
import datetime
import json


def get_sample_by_code(symbol, end_date='2024-02-22', time_delta=90):
    stdcode = symbol[:-3]
    # old API
    # df = ts.get_hist_data(stdcode, start=str(start_date), end=str(end_date))

    # new API require token
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
        "trade_date"
    ])
    try:
        pct_chg = [*df['pct_chg']][::-1]
        sample = {
            'date': datetime.datetime.today(),
            'end': str(end_date),
            'code': stdcode,
            'stdchange': pct_chg,
        }

        with open(f'../data/test/{stdcode}.yaml', 'w+') as f:
            yaml.dump(sample, f)
    except Exception as e:
        print(e)
    print(f'Done.')
    print(f'Sample saved in [../data/test/{stdcode}.yaml]')
    print(f'Seqlen of this sample: [{len(pct_chg)}], while time delta is [{time_delta}]')
    return f'../data/test/{stdcode}.yaml'


end_date = '2024-02-22'
get_sample_by_code('300001.SZ', end_date)
