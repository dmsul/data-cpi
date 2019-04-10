import os

import requests

from util import src_path


def download_all_items_series():
    filepath = src_path('cu.data.1.AllItems.txt')
    if os.path.isfile(filepath):
        return

    all_items_url = \
        r'https://download.bls.gov/pub/time.series/cu/cu.data.1.AllItems'
    with open(filepath, 'w') as f:
        page = requests.get(all_items_url)
        f.write(page.text)


if __name__ == "__main__":
    pass
