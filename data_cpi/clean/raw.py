import os

import pandas as pd
import requests

from util import data_path, src_path, load_or_build


def cpi_deflator(year: int) -> pd.DataFrame:
    """ Multiply by this number to get deflated dollars """
    df = cpi_allitems_urban()

    df[f'deflate_to_{year}'] = df.loc[year, 'value'] / df['value']
    del df['value']

    return df


@load_or_build(data_path('cpi_allitems_urban_monthly-{monthly}.pkl'))
def cpi_allitems_urban(monthly: bool=False) -> pd.DataFrame:
    """ U.S. All items, 1982-84=100 """
    df = load_raw_allitems_series()

    # Select the right CPI series
    series_id = 'CUUR0000SA0'
    df['series_id'] = df['series_id'].str.strip()
    df = df[df['series_id'] == series_id]
    del df['series_id']

    # Uniform below here (maybe period handling different)
    df['footnote_codes'] = df['footnote_codes'].str.strip()
    if df['footnote_codes'].str.len().max() == 0:
        del df['footnote_codes']

    if monthly:
        df = df[df['period'] != 'M13']
        df['month'] = (df['period']
                       .str.replace('M', '')
                       .astype(int))
        idx_cols = ['year', 'month']
        df = df.set_index()
    else:
        df = df[df['period'] == 'M13']
        idx_cols = 'year'

    df = df.set_index(idx_cols)

    del df['period']

    return df


def load_raw_allitems_series() -> pd.DataFrame:
    download_all_items_series()
    df = pd.read_csv(allitems_src_path(), sep='\t')
    return df


def download_all_items_series() -> None:
    filepath = allitems_src_path()
    if os.path.isfile(filepath):
        return

    all_items_url = \
        r'https://download.bls.gov/pub/time.series/cu/cu.data.1.AllItems'
    with open(filepath, 'w') as f:
        page = requests.get(all_items_url)
        f.write(page.text)


def allitems_src_path() -> str:
    return src_path('cu.data.1.AllItems.txt')


if __name__ == "__main__":
    df = cpi_deflator(2015)
