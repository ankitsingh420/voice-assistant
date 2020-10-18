import pyttsx3 # module install using pip install pyttsx3
import datetime
import time
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
eng=pyttsx3.init('sapi5')# used for audio
voices=eng.getProperty('voices')
eng.setProperty('voice', voices[2].id)

def speak(audio):# set speak audio
    eng.say(audio)
    eng.runAndWait()
def wishMe():# start me wish karega
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("namastey,   Good Morning")
    elif hour>=12 and hour<18:
        speak("namastey,   Good Afternoon")
    else:
        speak("namastey, Good Evening")
    speak(" How may i help you")
def takeCommand():
    #it takes input from microphone and produce string as output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Start Listening.......")
        r.pause_threshold = 1
        r.energy_threshold =300
        audio=r.listen(source)
    try:
        print("Recognising......")
        query=r.recognize_google(audio)
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        print("say that again......")
        return 'None'
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email id','your-password')
    server.sendmail('your-emailid',to,content)
    server.close()



if __name__=="__main__":# ye main funion hoga
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            print("searching wikipedia....")
            query=query.replace("wikipedia",'')
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('http://youtube.com',new=2)
        elif 'open google' in query:
            webbrowser.open('http://google.com',new=2)
        elif 'play music' in query:
            music_dir='E:\\download_a\\songs'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[1]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"samay abhi hai : {strTime}\n")
        elif 'email to ankit' in query:
            try:
                speak('what i should say')
                content=takeCommand()
                to='email-ide-to-whom mail has to be send'
                sendEmail(to,content)
                speak("Email has been send")
            except Exception as e:
                speak("sorry ankit i can't send mail due to network issue")



    
