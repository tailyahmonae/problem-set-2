'''
PART 1: ETL the two datasets and save each in `data/` as .csv's
'''

#### tried a few different approaches, did some research, nothing is working
### this seemed to be the most promising, but denied permissions

import pandas as pd
import requests

def download_file(url, output_path):
    response = requests.get(url, verify=False)  # Disable SSL verification
    response.raise_for_status()  # Check if the request was successful
    with open(output_path, 'wb') as file:
        file.write(response.content)

# URLs
pred_universe_url = 'https://www.dropbox.com/scl/fi/69syqjo6pfrt9123rubio/universe_lab6.feather?rlkey=h2gt4o6z9r5649wo6h6ud6dce&dl=1'
arrest_events_url = 'https://www.dropbox.com/scl/fi/wv9kthwbj4ahzli3edrd7/arrest_events_lab6.feather?rlkey=mhxozpazqjgmo6qqahc2vd0xp&dl=1'

# download
download_file(pred_universe_url, 'pred_universe_lab6.feather')
download_file(arrest_events_url, 'arrest_events_lab6.feather')

# load
pred_universe_raw = pd.read_feather('pred_universe_lab6.feather')
arrest_events_raw = pd.read_feather('arrest_events_lab6.feather')

# convert
pred_universe_raw['arrest_date_univ'] = pd.to_datetime(pred_universe_raw.filing_date)
arrest_events_raw['arrest_date_event'] = pd.to_datetime(arrest_events_raw.filing_date)

# drop
pred_universe_raw.drop(columns=['filing_date'], inplace=True)
arrest_events_raw.drop(columns=['filing_date'], inplace=True)

# Save both data frames to `data/` -> 'pred_universe_raw.csv', 'arrest_events_raw.csv'

pred_universe_raw.to_csv('/Users/taliyahmonae/Desktop/School/INST414/problem-set-2/src/data/red_universe_raw.csv', index=false)
arrest_events_raw.to_csv('/Users/taliyahmonae/Desktop/School/INST414/problem-set-2/src/data/arrest_events_raw.csv', index=false)
