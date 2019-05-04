import pandas as pd

from data_cpi.clean.raw import cpi_allitems_urban


def cpi_deflator(base: int, frequency: str = 'a') -> pd.DataFrame:
    """ Multiply by this number to get deflated dollars """
    need_monthly = frequency in ('m', 'q')
    df = cpi_allitems_urban(monthly=need_monthly)

    if frequency == 'q':
        df = df.reset_index()
        df['quarter'] = (df['month'] - 1) // 3 + 1
        df = df.groupby(['year', 'quarter'])['value'].mean().to_frame()

    base_avg = df.squeeze().loc[base].mean()

    df[f'deflate_to_{base}'] = base_avg / df['value']
    del df['value']

    return df
