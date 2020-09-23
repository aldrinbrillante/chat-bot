# This will give you access to the random module or library.
# choice() will randomly return an element in a list.
# Read more: https://pynative.com/python-random-choice/

from random import choice

#combine functions and conditionals to get a response from the bot
def get_bot_response(user_response):

  #add some bot responses to this list
  bot_response_happy = ["omg! great!", "Keep smiling!", "I love to see you happy!"]
  bot_response_sad = ["im here for you", "sending good vibes"]

  if user_response == "happy":
    return choice(bot_response_happy)
  elif user_response == "sad":
    return choice(bot_response_sad)
  else:
    return "I hope your day gets better"




print("Welcome to Mood Bot")
print("Please enter how you are feeling")

user_response = ""
#TODO: we want to keep repeating until the user enters "done" what should we put here?
while True:
  user_response = input("How are you feeling today?: ")
  
  # Quits program when user responds with 'done'
  if user_response == 'done':
    break

  
  bot_response = get_bot_response(user_response)
  print(bot_response)



