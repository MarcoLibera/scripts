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