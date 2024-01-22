import tushare as ts
import yaml
import datetime


def get_sample_by_code(symbol, end_date, time_delta=90):
    start_date = end_date - datetime.timedelta(days=time_delta)
    stdcode = symbol[:-3]
    df = ts.get_hist_data(stdcode, start=str(start_date), end=str(end_date))
    try:
        df['lastday'] = df['close'] - df['price_change']
        pct_chg = [*df['p_change']][::-1]
        sample = {
            'date': datetime.datetime.today(),
            'start': str(start_date),
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

