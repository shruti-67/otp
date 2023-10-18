from twilio.rest import Client
import sms
import math
import random
client = Client(sms.account_sid, sms.auth_token)
data = "0123456789"
leng = len(data)
otp = ""

for i in range(6):
    otp += data[math.floor(random.random()*leng)]

message = client.messages.create(
    body="Your 6 digit OTP is "+otp,
    from_=sms.inputNO,
    to=sms.sendNo
)

print(message.body)


# import key
# client = Client(key.account_sid, key.auth_token)

# message = client.messages.create(
#     body="Your 6 digit OTP is ",
#     from_=key.inputNO,
#     to=key.sendNo
# )

# print(message.body)