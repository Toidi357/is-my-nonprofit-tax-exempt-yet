import json
import datetime
import time
import requests

def monitor(ein: str, webhook: str) -> None:
    while True:
        print(f'{datetime.datetime.now()}: Checking...')

        # check the IRS
        r = requests.get(f'https://apps.irs.gov/prod-east/teos/searchAll/ein?ein={ein}&country=US')

        # if we get an error...
        if r.status_code != 200:
            error = json.loads(r.text)['message']
            # notify the webhook and exit
            requests.post(webhook, data={'content': f'Error: {error}'})

            if error == 'Invalid query format':
                raise Exception('Double check your EIN')
            else:
                raise Exception(error)

        response = json.loads(r.text)
        # if the count is 1, meaning there is information about the nonprofit on the IRS website
        # fire it off to the webhook
        if response['count'] > 0:
            requests.post(webhook, data={'content': f'Found determination letter for EIN {ein}! https://apps.irs.gov/app/eos/'})
            break

        time.sleep(8 * 60 * 60) # 8 hours

if __name__ == "__main__":
    # read config.json
    f = open('config.json')
    data = json.load(f)

    if not data['EIN'] or not data['Webhook']:
        raise Exception('Missing parameters in config.json')
    
    monitor(data['EIN'], data['Webhook'])
