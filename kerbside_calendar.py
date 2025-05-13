"""
This script fetches the suburbs and dates for upcoming kerbside collections
in Brisbane. It gets this information from a public API which I found in
the source code for the Brisbane City Council website.
"""

import requests
import json
from datetime import datetime

# Get JSON data on kerbside collection dates from API endpoint as python objects
api_url = "https://www.brisbane.qld.gov.au//bin/brisbanecitycouncil/api/common/external-data.kerbside-large-item-collection-schedule.json"
response = requests.get(api_url)
collection_data = json.loads(response.content)

# Extract dates
dates = []
for item in collection_data['items']:
    suburb = item['suburb_list'].split(', ')[1]
    date = item['items_out_on_footpath']

    # Exclude dates which have already happened
    if datetime.strptime(date, '%Y-%m-%d') > datetime.now():
        print(suburb, date)