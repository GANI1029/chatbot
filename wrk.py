#
from pyngrok import ngrok
from urllib.parse import urljoin
# # def start_ngrok():
# #     # Set up a tunnel on port 5000 for our Flask object to interact locally
# #     url = ngrok.connect(5000).public_url
# #     print(' * Tunnel URL:', url)
# # start_ngrok()
#
# from pyngrok import ngrok
#
# # [<NgrokTunnel: "http://<public_sub>.ngrok.io" -> "http://localhost:80">]
# tunnels = ngrok.get_tunnels()
# print(tunnels)
# ngrok.kill()
# t = ngrok.get_tunnels()
# print(t)
WEBHOOK_URL_SUFFIX = '/messages_webhook'
def start_ngrok():
    # Set up a tunnel on port 5000 for our Flask object to interact locally
    url = ngrok.connect(5000).public_url
    print(' * Tunnel URL:', url)
    return url
ngrok_url = start_ngrok()
#create_webhook(teams_api, 'messages_webhook', '/messages_webhook', 'messages',ngrok_url)
targetUrl=urljoin(ngrok_url, WEBHOOK_URL_SUFFIX)
print(targetUrl)