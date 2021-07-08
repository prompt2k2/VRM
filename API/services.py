import os
import requests

def get_droplets():
    
    url = 'https://vrmapi.victronenergy.com/v2/droplets'
    r = requests.get(url, headers={'Authorization':'Bearer %s' % os.getenv('DO_ACCESS_TOKEN')})
    droplets = r.json()
    droplet_list = []
    for i in range(len(droplets['droplets'])):
        droplet_list.append(droplets['droplets'][i])
    return droplet_list