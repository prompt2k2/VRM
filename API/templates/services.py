import os
import requests

def get_droplets():
    access_token = 'dfdfsdsfdsgskjksfhjshf'
    url = 'https://vrmapi.victronenergy.com/v2/droplets'
    r = requests.get(url, headers={'Authorization':'Bearer %s' % access_token})
    droplets = r.json()
    droplet_list = []
    for i in range(len(droplets['droplets'])):
        droplet_list.append(droplets['droplets'][i])
    return droplet_list