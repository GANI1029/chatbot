
def card_all(roomId):
   return {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content":{
            "type": "AdaptiveCard",
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "version": "1.1",
            "body": [
                {
                    "type": "TextBlock",
                    "text": "**AMI**",
                    "wrap": True
                },
                {
                    "type": "Input.Text",
                    "id": "AMI",
                    "placeholder": "enter your ami",
                    "maxLength": 100
                },
                {
                    "type": "TextBlock",
                    "text": "**enter your screening date**",
                    "wrap": True
                },
                {
                    "type": "Input.Date",
                    "id": "screening"
                },
                {
                    "type": "TextBlock",
                    "text": "**Goals List**",
                    "wrap": True
                },
                {
                    "type": "ColumnSet",
                    "id": "goals",
                    "columns": [
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "Input.Toggle",
                                    "id": "BMI",
                                    "title": "BMI",
                                    "value": "true",
                                    "valueOn": "true",
                                    "valueOff": "false",
                                    "text": "BMI*"
                                }
                            ],
                            "width": "stretch"
                        },
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "Input.Toggle",
                                    "id": "BP",
                                    "title": "BP",
                                    "value": "true",
                                    "valueOn": "true",
                                    "valueOff": "false",
                                    "text": "BP"
                                }
                            ],
                            "width": "stretch"
                        },
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "Input.Toggle",
                                    "id": "blood sugar",
                                    "title": "blood sugar",
                                    "value": "true",
                                    "valueOn": "true",
                                    "valueOff": "false",
                                    "text": "Blood sugar"
                                }
                            ],
                            "width": "stretch"
                        },
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "Input.Toggle",
                                    "id": "waiste",
                                    "title": "waist size",
                                    "value": "true",
                                    "valueOn": "true",
                                    "valueOff": "false",
                                    "text": "Blood sugar"
                                }
                            ],
                            "width": "stretch"
                        },
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "Input.Toggle",
                                    "id": "LDL",
                                    "title": "LDL Level",
                                    "value": "true",
                                    "valueOn": "true",
                                    "valueOff": "false",
                                    "text": "LDL Level"
                                }
                            ],
                            "width": "stretch"
                        },
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "Input.Toggle",
                                    "id": "bio screen",
                                    "title": "bio screening",
                                    "value": "true",
                                    "valueOn": "true",
                                    "valueOff": "false",
                                    "text": "bio screening"
                                }
                            ],
                            "width": "stretch"
                        },
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "Input.Toggle",
                                    "id": "Targets",
                                    "title": "targets",
                                    "value": "true",
                                    "valueOn": "true",
                                    "valueOff": "false",
                                    "text": "all goals"
                                }
                            ],
                            "width": "stretch"
                        },
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "Input.Toggle",
                                    "id": "CH_Ratio",
                                    "title": "cholesterol ratio",
                                    "value": "true",
                                    "valueOn": "true",
                                    "valueOff": "false",
                                    "text": "cholesterol ratio"
                                }
                            ],
                            "width": "stretch"
                        },
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "Input.Toggle",
                                    "id": "CH_toatal",
                                    "title": "cholesterol total",
                                    "value": "true",
                                    "valueOn": "true",
                                    "valueOff": "false",
                                    "text": "cholesterol total"
                                }
                            ],
                            "width": "stretch"
                        }
                    ]
                }
            ],
            "actions": [
                {
                    "type": "Action.Submit",
                    "title": "ok"
                }
            ]
        }
    }


def bio_start_poll_card(roomId):
    return {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "type": "AdaptiveCard",
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "version": "1.1",
            "body": [
                {
                    "type": "TextBlock",
                    "text": "ami here",
                    "wrap": True
                },
                {
                    "type": "Input.Text",
                    "id": "AMI",
                    "placeholder": "enter your ami",
                    "maxLength": 100
                },
                {
                    "type": "TextBlock",
                    "text": "enter your screening date",
                    "wrap": True
                },
                {
                    "type": "Input.Date",
                    "id": "screening"
                },
                {
                    "type": "TextBlock",
                    "text": "goals list",
                    "wrap": True
                },
                {
                    "type": "Input.ChoiceSet",
                    "id": "GOALS",
                    "choices": [
                        {
                            "title": "BP",
                            "value": "BLOOD PRESSURE"
                        },
                        {
                            "title": "BMI",
                            "value": "BODY MASS INDEX"
                        }
                    ],
                    "placeholder": "BIO METRIC GOLAS LIST"
                },
         {
                    "type": "Input.Text",
                    "id": "roomId",
                    "value": roomId,
                    "isVisible": False
                }
            ],
            "actions": [
                {
                    "type": "Action.Submit",
                    "title": "OK"
                }
            ]
        }

    }

def generate_start_poll_card(roomId):
    return {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.1",
            "body": [
                {
                    "type": "TextBlock",
                    "text": "Please type your AMI below"
                },
                {
                    "type": "Input.Text",
                    "id": "AMI",
                    "placeholder": "AMI NUMBER",
                    "maxLength": 100
                },
                {
                    "type": "TextBlock",
                    "text": "Please type your Goals below"
                },
                {
                    "type": "Input.Text",
                    "id": "GOALS",
                    "placeholder": "Dream bio metric golas",
                    "maxLength": 500,
                    "isMultiline": True
                },
                {
                    "type": "TextBlock",
                    "text": "BIO SCRENING DATE"
                },
                {
                    "type": "Input.Date",
                    "id": "screening",
                    "placeholder": "Enter a date"

                },
                {
                    "type": "Input.Text",
                    "id": "roomId",
                    "value": roomId,
                    "isVisible": False
                }
            ],
              "actions": [
                {
                    "type": "Action.Submit",
                    "title": "OK"
                }
              ]
        }
    }

def reply(roomId,message):
    return {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
    "type": "AdaptiveCard",
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.1",
    "body": [
        {
            "type": "TextBlock",
            "text": "**ServiceNow Ticket Updated**",
            "wrap": True
        }
    ]
}

    }

def all_choices_card(roomId):
    return {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content":{
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.0",
            "body": [
                {
                    "type": "TextBlock",
                    "text": "Please type your AMI below"
                },
                {
                    "type": "Input.Text",
                    "id": "AMI",
                    "placeholder": "AMI NUMBER",
                    "maxLength": 100
                },
      {
          "type": "TextBlock",
          "text": "**please select goals you want to test**"
      },
      {
          "type": "Input.ChoiceSet",
          "id": "GOALS",
          "isMultiSelect": True,
          "value": "1",
          "style": "expanded",
          "choices": [
              {
                  "title": "BMI",
                  "value": "BODY MASS INDEX"
              },
              {
                  "title": "BP",
                  "value": "blood pressure"
              },
              {
                  "title": "fasting blood sugar",
                  "value": "fasting blood sugar"
              },
              {
                  "title": "waist size",
                  "value": "waist"
              }
              ,
              {
                  "title": "LDL Level",
                  "value": "LDL LEVEL"
              }
              ,
              {
                  "title": "cholesterol total",
                  "value": "cholesterol total"
              }
              ,
              {
                  "title": "cholesterol ratio",
                  "value": "cholesterol ratio"
              },
              {
                  "title": "bio screening",
                  "value": "screening"
              },
              {
                  "title": "all/targets",
                  "value": "targets"
              }

          ]
      },
                {
                    "type": "Input.Text",
                    "id": "roomId",
                    "value": roomId,
                    "isVisible": False
                },
                {
                    "type": "TextBlock",
                    "text": "**BIO SCRENING DATE**"
                },
                {
                    "type": "Input.Date",
                    "id": "screening",
                    "placeholder": "Enter a date"

                },{
                    "type": "TextBlock",
                    "text": "**Please type your INC**"
                },
                {
                    "type": "Input.Text",
                    "id": "INC",
                    "placeholder": "incident number",
                    "maxLength": 100
                }

  ],
            "actions": [
        {
        "type": "Action.Submit",
        "title": "OK"
        }
            ]

    }
    }

def help_card(roomId):
    return  {
        "contentType": "application/vnd.microsoft.card.adaptive",
                "content":{
                "type": "AdaptiveCard",
                 "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                "version": "1.2",
                "body": [
        {
            "type": "TextBlock",
            "text": "**HI i'm Webex-BOT how can i help you**",
            "wrap": True
        },
        {
            "type": "TextBlock",
            "text": "If you want to test **Dream-BioMetric** Incident",
            "wrap": True
        },
        {
            "type": "TextBlock",
            "text": " please type a command @HELLOBOT all ",
            "wrap": True
        },
                {
                    "type": "Input.Text",
                    "id": "roomId",
                    "value": roomId,
                    "isVisible": False
                }
    ]
}

    }

def any_card(roomId):

    return {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content":{
                "type": "AdaptiveCard",
                "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                "version": "1.2",
                "body": [
        {
            "type": "TextBlock",
            "text": "**HI i'm Webex-BOT how can i help you**",
            "wrap": True
        },
        {
            "type": "TextBlock",
            "text": "For more informtion please type **@HELLOBOT help** command",
            "wrap": True
        },
                {
                    "type": "Input.Text",
                    "id": "roomId",
                    "value": roomId,
                    "isVisible": False
                }

    ]
}
    }


