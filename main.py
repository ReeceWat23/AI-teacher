import time
import openai
from gtts import gTTS
import pygame
#import speech_recognition as sp


def get_prompt():
    question = input("What would yu like to know?:")
    return question


def get_response(prompt):
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=64,
                                        top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0, stop=["\"\"\""])
    temp = response["choices"]
    text = temp[0]["text"]

    return str(text.strip())

def output_response_voice(mp3):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.play()


openai.api_key = "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"

course_content = {"lesson1": ["Start will an opener like lets begin then explain supply and demand in simple terms and give an example using bitcoin",
                              "Start will an opener like lets begin then go into detail on how supply gets changed",
                              "Start will an opener like lets begin then go into detail about how demand can be changed", ]}

todays_lesson = course_content["lesson1"]
language = 'en'


# rec = sp.Recognizer()
# my_mic = sp.Microphone(device_index=1)
#
# with my_mic as source:
#     print("What is your question?.......")
#     audio = rec.listen(source)
#     text = rec.recognize_google(audio)
#     print(text)




welcome = get_response("Welcome the class like a 1920's gangster")
my_obj = gTTS(text=welcome, lang=language, slow=False)
my_obj.save("welcome.mp3")
output_response_voice("welcome.mp3")
time.sleep(2.0)

for i in todays_lesson:
    content = i
    my_text = get_response(content)
    my_obj = gTTS(text=my_text, lang=language, slow=False)
    my_obj.save("econ.mp3")
    output_response_voice("econ.mp3")
    # Ask the user if they have any other questions
    questions = input("Does the class have any questions?:")
    while questions.strip().lower() == "yes":
        user_question = get_prompt()
        answer = get_response(user_question)
        Qmyobj = gTTS(text=answer, lang=language, slow=False)
        Qmyobj.save("q&a.mp3")
        output_response_voice("q&a.mp3")
        questions = input("Does the class have any more questions?:")

    print("Alright, perfect we will move on to the next topic")


# # Try and implement a text to speech bot to read off the responses generated


