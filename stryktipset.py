#!/usr/bin/env python3
import requests
import json

with requests.get("https://api.www.svenskaspel.se/draw/stryktipset/draws") as get_api:
    api_data = get_api.json()

def print_match_teams(match_id):
    print('{}:'.format(match_id + 1),
    api_data['draws'][0]['drawEvents'][match_id]['eventDescription'])

def print_match_data(output_topic, match_id, data_type):
    try:
        print('{topic}: 1: {one} X: {draw} 2: {two}'.format(
                topic=output_topic,
                one=api_data['draws'][0]['drawEvents'][match_id][data_type]['one'],
                draw=api_data['draws'][0]['drawEvents'][match_id][data_type]['x'],
                two=api_data['draws'][0]['drawEvents'][match_id][data_type]['two']))
    except:
        print('{}: not ready yet'.format(output_topic))
        pass

for match_id in range(0, 13):
    """ Stryktipset is always thirteen games """
    print_match_teams(match_id)
    print_match_data('Odds', match_id, 'odds')
    print_match_data('Svenska folket (%)', match_id, 'svenskaFolket')
    print_match_data('Tio tidningar', match_id, 'tioTidningar')
    print()
