import json
import requests
from pyngrok import ngrok
from urllib.parse import urljoin


def start_ngrok():
    # Set up a tunnel on port 5000 for our Flask object to interact locally
    url = ngrok.connect(5000).public_url
    print(' * Tunnel URL:', url)
    return url


def create_webhook(teams_api, name, webhook, resource, ngrok_url):
    delete_webhook(teams_api, name)
    print("URL::",urljoin(ngrok_url, webhook))
    teams_api.webhooks.create(
        name=name, targetUrl= urljoin(ngrok_url, webhook),
        resource=resource, event='created', filter=None,ownedBY="org")

def delete_webhook(teams_api, name):
    for hook in teams_api.webhooks.list():
        if hook.name == name:
            teams_api.webhooks.delete(hook.id)

# def get_ngrok_url(addr='127.0.0.1', port=4040):
#     try:
#         ngrokpage = requests.get("http://{}:{}/api/tunnels".format(addr, port), headers="").text
#     except:
#         raise RuntimeError('Not able to connect to ngrok API')
#     ngrok_info = json.loads(ngrokpage)
#
#     print("get_ngrok_url::: ", ngrok_info['tunnels'][0]['public_url'])
#
#     return ngrok_info['tunnels'][0]['public_url']
