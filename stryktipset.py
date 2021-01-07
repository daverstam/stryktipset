#!/usr/bin/env python3
import requests
import json

api_url = 'https://api.www.svenskaspel.se/draw/stryktipset/draws'

with requests.get(api_url) as get_api:
    api_data = get_api.json()

def print_match_teams(match_id):
    try:
        print(f'{match_id + 1}:',
        api_data['draws'][0]['drawEvents'][match_id]['eventDescription'])
    except IndexError:
        print(f'No data available from the api:\n{api_url}')

def print_match_data(output_topic, match_id, data_type):
    try:
        one = api_data['draws'][0]['drawEvents'][match_id][data_type]['one']
        draw = api_data['draws'][0]['drawEvents'][match_id][data_type]['x']
        two = api_data['draws'][0]['drawEvents'][match_id][data_type]['two']

        print(f'{output_topic}: 1: {one} X: {draw} 2: {two}')
    except:
        print(f'{output_topic}: not ready yet')

for match_id in range(0, 13):
    """ Stryktipset is always thirteen games """
    print_match_teams(match_id)
    print_match_data('Odds', match_id, 'odds')
    print_match_data('Svenska folket (%)', match_id, 'svenskaFolket')
    print_match_data('Tio tidningar', match_id, 'tioTidningar')
    print()
