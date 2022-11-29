
from urllib.parse import urljoin
from webexteamssdk import WebexTeamsAPI, Webhook
from cards import generate_start_poll_card, bio_start_poll_card, reply, card_all, all_choices_card, help_card, any_card

WEBEX_TEAMS_ACCESS_TOKEN = 'MGNiYmY0ZGQtNTRkOC00MGE5LTk1NTAtZjZhYTVmMzFlNDU2MjI4MDgxYzQtYzRh_P0A1_50a80e81-b1e7-4c1b-a6ff-3c9233784457'

teams_api = None

teams_api = WebexTeamsAPI(access_token=WEBEX_TEAMS_ACCESS_TOKEN, disable_ssl_verify=True)
ngrok_url = 'http://ec2-15-206-203-169.ap-south-1.compute.amazonaws.com:4000'

def create_webhook(teams_api, name, webhook, resource, ngrok_url):
    #delete_webhook(teams_api, name)
    print("URL::",urljoin(ngrok_url, webhook))
    teams_api.webhooks.create(
        name=name, targetUrl= urljoin(ngrok_url, webhook),
        resource=resource, event='created', filter=None,ownedBY="org")
    for hook in teams_api.webhooks.list():
        print(hook)

create_webhook(teams_api, 'messages_webhook', '/messages_webhook', 'messages',ngrok_url)
create_webhook(teams_api, 'attachmentActions_webhook', '/attachmentActions_webhook', 'attachmentActions',ngrok_url)


