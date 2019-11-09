import mysql.connector
from datetime import datetime
import time
from slack import WebClient


#initializing at a back date for smooth first run.
max_created_at = datetime.strptime('2001-01-01 10:55:31', '%Y-%m-%d %H:%M:%S')  

# i = 0

def fetchdata():
    """ To retrieve new messages from the database and sending them to the slack channel"""

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password",
        database="chatbot"
    )
    
    db_cursor = db_connection.cursor()

    global max_created_at
        
    db_cursor.execute(f"SELECT * FROM chat_msgs WHERE created_at > '{max_created_at}'") 
    result = db_cursor.fetchall()
    for data in result:
        username = data[1]
        message = data[2]
        created_at = data[3]
        sending_to_slack(username, message)
        if max_created_at < created_at:    
            max_created_at = created_at
        print(f"{username},{message},{created_at}")
                
    db_cursor.close()
    db_connection.close()    
    time.sleep(60)

def sending_to_slack(user, message):
    """Handles the retrieved messages from db and send to the channel"""
    bot_token = 'xoxb-826875544725-826880162117-D7kg7vFUDYazvcYqfeS1IApr'
    slack_bot = WebClient(bot_token)
    slack_bot.chat_postMessage(
    channel = "#aiml", 
    as_user = "false",
    username = user,
    text = message
    )

def channel_messages():
    """Accessing Channel Messages from the Slack Channel """
    bot_token = 'xoxp-826875544725-818947476049-827227809924-636162f3a2482483198e1dd2fd85d869'
    slack_url = "https://slack.com/api/conversations.history?token=" + bot_token + "&channel=" + '#aiml'
    slack_bot = WebClient(bot_token)
    response = slack_bot.conversations_history(
        channel="CQARHULE4",
        limit=1
    )
    assert response["ok"]
    messages = response['messages']


       
if __name__ == '__main__':
    while True: # for fetching data again again and again
    channel_messages()
    fetchdata()
        # i = i + 1
        # print(i)  #checking if it actually runs or not


    

