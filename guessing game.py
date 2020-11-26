import pyttsx3
import speech_recognition as sr
import math
import random

engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return query

print("\t\t\t\t\t\tThis is a Guessing game")

speak("In this game you will have to guess a number in a range that will be defined by you. You will be given only 5 guesses")

print("\t\t\tHere you will have to find a random number in a range defined by you")
print("\t\t\t\t\t  You will be given only 5 guesses")

speak("So now let the game begin, Good Luck")

speak("Now ! give the lower limit of your range")
lower = takeCommand()
speak("Now ! give the upper limit of your range")
upper = takeCommand()


number_to_be_guessed = random.randint(int(lower), int(upper))

print(number_to_be_guessed)

no_of_guesses=0

speak("your guess")

while no_of_guesses < 5:
    no_of_guesses += 1
    
    guess = takeCommand()
    
    if int(guess)>int(upper) or int(guess)<int(lower):
        print("\nYour number is \nout of range")
        speak("your guess is out of range. try again")

    elif number_to_be_guessed > int(guess):
        print("\nyour guess is \nsmaller than number")
        speak("your guess is smaller than the number. try again")
    
    elif number_to_be_guessed == int(guess):
        print("\n\t\t\t\t\t\tWINNER!")
        speak("Yay! you have won the game. congratulations")
        print("\n\t\t\tCongratulations you guessed the number in your ",no_of_guesses," try")
        break
      
    elif number_to_be_guessed < int(guess):
        print("\nyour guess is \nlarger than number")
        speak("your guess is larger than the number. try again")

    else:
        print("There was some problem")
        break
           

if no_of_guesses >= 5:
    print("\n\t\t\t\t\t\tThe Correct answer was ", number_to_be_guessed)
    speak("the correct answer was")
    speak(number_to_be_guessed)
    print("\n\t\t\t\t\t    Lets hope you do better next time")





    
 