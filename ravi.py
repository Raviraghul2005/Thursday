import os
from playsound import playsound
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from PyDictionary import PyDictionary
import webbrowser
import pyautogui
import wolframalpha
import subprocess
import ctypes




dict = PyDictionary()

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening Boss...")
            voice = listener.listen(source)
            command = lis   tener.recognize_google(voice)
            command = command.lower()
            if 'machi' in command:
                command = command.replace("machi", "")
                print(command)


    except Exception as e:
        print('Sorry could not recogonize your voice')
        return 'None'
    return command



def sendEmail(to, content):
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()


    server.login('clause.xd@gmail.com', 'Raviramesh@2005')
    server.sendmail('clause.xd@gmail.com', to, content)
    server.close()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good morning sir, I hope you slept well.")
        talk('Good morning sir, I hope you slept well.')

    elif hour >= 12 and hour < 18:
        print("Half of the day is over;have a wonderful afternoon and enjoy the rest of the day! sir'")
        talk('Half   of    the day     is over;                  have a wonderful afternoon and              enjoy the rest    of the day! sir')

    else:
        print("Good Evening Sir !")
        talk("Good Evening Sir !")


def Alarm(query):
    f1=open("Data.txt","w")
    f1.write(query)
    f1.close()
    os.startfile(r"C:\Users\ravir\Desktop\Alarm.py")


def run_alexa():
    command = take_command()
    print(command)

    if "thursday" in command or "good morning" in command or "good afternoon" in  command:
        wishMe()

    elif "introduce yourself" in command:
        print("I am Thursday. Your desktop Assistant")
        talk("I am Thursday. Your desktop Assistant")

    elif 'how are you' in command:
        print("I am fine, Thank you")
        talk("I am fine, Thank you")
        print("How are you, Sir")
        talk("How are you, Sir")
        cxx2= take_command()
        if "fine" or "good" in cxx2:
            print("It's good to know that your fine")
            talk("It's good to know that your fine")
        else:
            print("""its sad to me that u are not fine
            How could i help u""")
            talk("its sad to me that u are not fine")
            talk("How could i help u")



    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)

    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'joke' in command:
        p1=pyjokes.get_joke()
        print(p1)
        talk(p1)

    elif 'what is mean by the word ' in command:
        word = command.replace('what is mean by the word ', '')
        meaning = dict.meaning(word)
        print(meaning)
        talk(meaning)

    elif 'open google' in command:
        print("opening sir")
        talk("opening sir")
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register("chrome", None,webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get("chrome").open_new_tab('google.com')

    elif 'open youtube' in command:
        print("opening sir")
        talk("opening sir")
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get("chrome").open_new_tab('youtube.com')

    elif "play" in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song )

    elif 'what is the weather on' in command:
        from bs4 import BeautifulSoup
        import requests
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        def weather(city):
            city = city.replace(" ", "+")
            res = requests.get(
                f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
                headers=headers)
            print("Searching...\n")
            soup = BeautifulSoup(res.text, 'html.parser')
            location = soup.select('#wob_loc')[0].getText().strip()
            info = soup.select('#wob_dc')[0].getText().strip()
            weather = soup.select('#wob_tm')[0].getText().strip()
            print(location)
            print(info)
            print(weather + "°C")
            talk(location)
            talk(info)
            talk(weather + "degree celsius")


        city = command.replace('what is the weather on ', '')
        city = city + " weather"
        weather(city)
        print("Have a Nice Day:)")



    elif "stop" in command:
        exit()

    elif "screenshot"in command:
        image = pyautogui.screenshot()
        image.save('screenshot.png')
        talk('Screenshot taken.')
        print('Screenshot taken.')

    elif "rohit" in command:
        print("sleeping sleeping sleeping, rohith dont like it, he avoid, but sleeping likes rohith ,                 rohith cant avoid")
        talk("sleeping sleeping sleeping, rohith dont like it, he avoid, but sleeping likes rohith , rohith cant avoid")



    elif "prashant" in command:
        print("He is the God of Lair,And he is well known as Veddi Muthu")
        talk("He is           the                 God                  of                Lair,And           he is           well known as                            vedi                    Muthu")





    elif 'change background' in command:

        ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       r"C:\Users\ravir\Desktop\IMG_20221204_181348732~2.jpg",
                                                       0)
        talk("Background changed successfully")

    elif "write a note" in command:
        talk("What should i write da")
        note = take_command()
        file = open('rohith.txt', 'a')
        talk("Sir, Should i include date and time da")
        snfm = take_command()
        if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.datetime.now()
            tr1= str(strTime)
            file.write(tr1)
            file.write(" :- ")
            file.write(note)

        else:
            file.write(note)
        talk("Done sir")


    elif "show note" in command:
        talk("Showing Notes")
        file = open("ROhith.txt", "r")
        print(file.read())
        talk(file.read())

    elif "i love you" in command:
        print("sorry im not single")
        talk("sorry im not single  hahahahah")

    elif "will you be my gf" in command or "will you be my bf" in command:
        print("Error 404 - Page not found")
        talk("Error 404 - Page not found")

    elif "news" in command:
        import requests
        from bs4 import BeautifulSoup

        url = 'https://www.bbc.com/news'
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find('body').find_all('h3')
        for x in headlines:
            print(x.text.strip())
            talk(x.text.strip())

    elif "what is" in command or "who is" in command:
        yext= str(command)
        yext= yext.replace("what is","")
        yext = yext.replace("plus", "+")
        yext = yext.replace("into", "*")
        yext = yext.replace("minus", "-")
        yext = yext.replace("divided by", "/")
        yext = yext.replace("square","**2")

        import wolframalpha
        client = wolframalpha.Client("UL3KA9-5P52XYTELP")
        query = str(yext)
        res = client.query(query)
        output = next(res.results).text
        print(output)
        talk(output)



    elif "set alarm for" in command:
        from Alarm import RingerNow
        command = command.replace("set alarm for", "")
        print(command)
        Alarm(command)


    elif 'send a mail' in command:
        try:
            talk("What should I say?")
            cx12 = take_command()
            print(cx12)
            talk("whome should i send")
            to1 = input("Enter the email")
            sendEmail(to1, cx12)
            talk("Email has been sent !")
        except Exception as e:
            print(e)
            talk("I am not able to send this email")

while True:
    run_alexa()

