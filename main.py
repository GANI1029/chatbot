import json
from BE import backend
from flask import Flask, request
from utils import create_webhook,start_ngrok
from webexteamssdk import WebexTeamsAPI, Webhook
from cards import generate_start_poll_card, bio_start_poll_card, reply, card_all, all_choices_card, help_card, any_card

WEBEX_TEAMS_ACCESS_TOKEN = 'MGNiYmY0ZGQtNTRkOC00MGE5LTk1NTAtZjZhYTVmMzFlNDU2MjI4MDgxYzQtYzRh_P0A1_50a80e81-b1e7-4c1b-a6ff-3c9233784457'

teams_api = None
app = Flask(__name__)

@app.route('/messages_webhook', methods=['POST','GET'])
def messages_webhook():
    if request.method == 'GET':
        return ('this get request running in ec2 instance /messages_webhook')
    if request.method == 'POST':
        webhook_obj = Webhook(request.json)
        print(webhook_obj)
        return process_message(webhook_obj.data)

def process_message(data):
    print(data.personId)
    print(teams_api.people.me().id)
    if data.personId == teams_api.people.me().id:
        # Message sent by bot, do not respond
        return '200'
    else:
        message = teams_api.messages.get(data.id).text
        print(message)
        commands_split = (message.split())[1:]
        command = ' '.join(commands_split)
        print('commands_split', command)
        parse_message(command, data.personEmail, data.roomId)
        return '200'

def parse_message(command, sender, roomId): #sender is bot
    if command == "bio metric":
        create_poll(command,roomId, sender)

    elif command == "bio":
        create_poll(command,roomId, sender)

    elif command == "all":
        create_poll(command, roomId, sender)
    elif command == "help" or command == "HELP":
        create_poll(command, roomId, sender)
    else:
        create_poll(command, roomId, sender)

    return



def create_poll(command,roomId, sender):
    if command == "bio metric":
        teams_api.messages.create(toPersonEmail=sender, text="Cards Unsupported", attachments=[generate_start_poll_card(roomId)])
    elif command == "bio":
        teams_api.messages.create(toPersonEmail=sender, text="Cards Unsupported",attachments=[bio_start_poll_card(roomId)])
    elif command == "all":
        teams_api.messages.create(toPersonEmail=sender, text="Cards Unsupported",attachments=[all_choices_card(roomId)])
    elif command == "help" or command == "HELP":
        teams_api.messages.create(toPersonEmail=sender, text="Cards Unsupported",attachments=[help_card(roomId)])
    else:
        teams_api.messages.create(toPersonEmail=sender, text="Cards Unsupported", attachments=[any_card(roomId)])


    print('msg sent')

@app.route('/attachmentActions_webhook', methods=['POST','GET'])
def attachmentActions_webhook():
    print('msg recived by /')
    if request.method == 'GET':
        return ('this get request running in ec2 instance /messages_webhook')
    if request.method == 'POST':
        print("attachmentActions POST!")
        webhook_obj = Webhook(request.json)
        print('data after card :', webhook_obj)
        return process_card_response(webhook_obj.data)

def process_card_response(data):
    attachment = (teams_api.attachment_actions.get(data.id)).json_data
    print("attachment:",attachment)
    inputs = attachment['inputs']
    if 'AMI' in list(inputs.keys()):
        ticket_info(inputs)
        #add_poll(inputs['AMI'], inputs['GOALS'], inputs['roomId'], teams_api.people.get(data.personId).emails[0],inputs['screening'])
        send_message_in_room(inputs['roomId'], "servicenow ticket updated: " + inputs['AMI'])
    # elif 'option_text' in list(inputs.keys()):
    #     current_poll = all_polls[inputs['roomId']]
    #     current_poll.add_option(inputs['option_text'])
    #     send_message_in_room(inputs['roomId'], "Option added to poll \"" + current_poll.name + "\": " + inputs['option_text'])
    #     print(current_poll.name)
    #     print(current_poll.options)
    # elif 'poll_choice' in list(inputs.keys()):
    #     current_poll = all_polls[inputs['roomId']]
    #     current_poll.votes[int(inputs["poll_choice"])] += 1
    return '200'
def send_message_in_room(room_id, message):
    #teams_api.messages.create(roomId=room_id, text=message)
    teams_api.messages.create(roomId=room_id, text="Cards Unsupported", attachments=[reply(room_id, message)])


def add_poll(AMI,GOALS,room_id,author,scrrening_date):
    data = {}
    data['AMI'] = (AMI).split(",")
    data['goals'] = (GOALS).split(",")
    #data['room_id'] = room_id
    #data['author'] = author
    data['screening_date'] = (scrrening_date).split(",")

    #print(data)
    backend(data)
def ticket_info(inputs):
    data = {}
    data['AMI'] = (inputs['AMI']).split(",")
    data['goals'] = (inputs['GOALS']).split(",")
    data['screening_date'] = (inputs['screening']).split(",")
    data['INC'] = (inputs['INC']).split(",")

    backend(data)

if __name__ == '__main__':
    print("first")
    teams_api = WebexTeamsAPI(access_token=WEBEX_TEAMS_ACCESS_TOKEN,disable_ssl_verify=True)
    #ngrok_url = start_ngrok()
    #print('ngrok url',ngrok_url)
    #create_webhook(teams_api, 'messages_webhook', '/messages_webhook', 'messages',ngrok_url)
    print('first createe')
    #create_webhook(teams_api, 'attachmentActions_webhook', '/attachmentActions_webhook', 'attachmentActions',ngrok_url)
    print('seconnd app')
    app.run(host='0.0.0.0', port=4000)
    print('app.run function running-----')