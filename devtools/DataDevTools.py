import pandas as pd
import datetime
import yaml


class TushareDev:

    def __init__(self):
        pass

    @staticmethod
    def csv2yaml(csv_path=None):
        """
        Download CSV stock data in:
        https://tushare.pro/webclient/
        数据接口——沪深股票——行情数据——日线行情
        This method transfer .csv file to .yaml in ../data/test for training, testing or inference.
        """
        if not csv_path:
            print('csv path empty, using example "./tushare_daily_example.csv"')
            csv_path = './tushare_daily_example.csv'

        df = pd.read_csv(csv_path)
        code = df['ts_code'][0].split('.')[0]

        sample = {
            'code': code,
            'date': datetime.datetime.today(),
            'end': '',
            'stdchange': df['pct_chg'],
        }
        with open(f'../data/test/m-{code}.yaml', 'w+') as f:
            yaml.dump(sample, f)

        return

