# Chat Bot Project
# run friday.py
# video part 1: https://youtu.be/ubchTOfqHwY
# video part 2: https://youtu.be/w6KTOCk4Fg0


Language used: Python

This project is a chat bot project using Python 3

main class: friday.py

trial and error class: trial-error.py // was used throughout majority of the project for trial/error code purpsoes. 

UNRESOLVED ISSUES: microphone is sometimes not being captured. Not sure yet as to why...

CREDIT: Recognition for assistance goes to Traversy Media (@TraversyMedia) on Youtube for helping me learn the package imports for a speech_recognition chat-bot. My record_audio() and my search and location variables are his code via Youtube, and it was through his explanation that I was able to understand the functionality of speech_recognition and pyaudio to implement and use it for this project. Thank you so much, Traversy Media!!! 


Make sure you credit the Youtuber in your readme for the code that was not original

ASSIGNMENT REQUIREMENTS:

Create a function called get_bot_response(). This function must: 

It should have 1 parameter called user_response, which is a string with the users input. 

It should return a string with the chat bot’s response. 

It should use at least 2 lists to store at least 3 unique responses to different user inputs. For example, if you were building a mood bot and the user entered “happy” for how they were feeling your happy response list could store something like “I’m glad to hear that!”, “Yay!”, “That is awesome!”. 

Use conditionals to decide which of the response lists to select from. For example: if a user entered “sad”, my program would choose a reponse from the of sad response list. If a user entered “happy”, my program would choose a reponse from the of happy response list. 

Use choice() to randomly select one of the three responses. (See example from class.) 

Greet the user using print() statements and explain what the chat bot topic is and what kind of responses it expects.

Get user input using the input() function and pass that user input to the get_bot_response() function you will write

Print out the chat bot’s response that is returned from the get_bot_response() function

Use a while() loop to keep running your chat bot until the user enters "done".

