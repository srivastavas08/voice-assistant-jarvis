import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib #for sending mails
import webbrowser as wb #for searching on chrome
import pyjokes as pj #pip install pyjokes
import os #system files
import subprocess 
import random #to get random strings
import tkinter 
import wolframalpha
import pyautogui #pip install pyautogui
import requests
import random 
import psutil
import shutil
import ctypes 
# import pyaudio
import nltk 
from win32com.client import Dispatch 
import sys
import json
import bs4
import selenium
from urllib.request import urlopen
#set up virtual environmentcd 

engine = pyttsx3.init('sapi5') #py -u "c:\Users\Asus\Desktop\jarvis\jarvis.py" to run this file
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id) #You can change voice Id to “0” for Male voice while using assistant here we are using Female voice for all text to speech

# Python program to find current 
# weather details of any city 
# using openweathermap api 

# import required modules 
import requests, json 

def weather():

# Enter your API key here 
    api_key = "26cc04b982183ead03749d76426b613f"

# base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name 
    speak("Please Tell me the Name of the city Sir!")
    ct = takecommand()
    city_name = ct

# complete_url variable to store 
# complete url address 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

# get method of requests module 
# return response object 
    response = requests.get(complete_url) 

# json method of response object 
# convert json format data into 
# python format data 
    x = response.json() 

# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
    if x["cod"] != "404": 
        

	# store the value of "main" 
	# key in variable y 
	    y = x["main"] 

	# store the value corresponding 
	# to the "temp" key of y 
	    current_temperature = y["temp"] - 272.15
    

	# store the value corresponding 
	# to the "pressure" key of y 
	    current_pressure = y["pressure"] 

	# store the value corresponding 
	# to the "humidity" key of y 
	    current_humidiy = y["humidity"] 

	# store the value of "weather" 
	# key in variable z 
	    z = x["weather"] 

	# store the value corresponding 
	# to the "description" key at 
	# the 0th index of z 
	    weather_description = z[0]["description"] 
         

	# print following values 
	    print(" Temperature (in celcius unit) = " +
					str(current_temperature) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidiy) +
		"\n description = " +
					str(weather_description)) 
        
    else: 
	    print(" City Not Found ") 
    speak("Current Temperature  is" )
    speak(current_temperature)
    speak("Current Pressure  is" )
    speak(current_pressure)
    speak("Current Humidity  is" )
    speak(current_humidiy)
    speak("weather is")
    speak(weather_description) 



def speak(audio): #This function contains converted audio
    engine.say(audio) #converts texts inside this say function into speech
    engine.runAndWait()

def time():    #adding time to jarvis
    time = datetime.datetime.now().strftime("%I:%M:%S") #in format hours:minute:second
    speak("Your Current time is")
    speak(time)

def date():      #adding date to jarvis
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Your current date is ")
    speak(date)
    speak(month)
    speak(year)
    speak("Today is")
    dayofweek()

'''def google():
    res = requests.get('https://www.google.com.tr/search?q='+''.join(sys.argv[1:]))
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    a = takecommand()
    linkelements = soup.select(a)
    link_to_open = min(5, len(linkelements))
    for i in range (link_to_open):
        wb.open('http://www.google.com'+ linkelements[i].get('href'))'''

def dayofweek():
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    dayNumber= (datetime.datetime.today().weekday())
    speak(days[dayNumber])



def wishme():
    speak("Welcome Back Sir! Jarvis is at Your service!")
    
    assname =("Jarvis") 
    speak("I am your Personal Assistant") 
    speak(assname) 
    
    time()
    hour = datetime.datetime.now().hour #for greeting Good night Afternoon or morning
    if hour >= 6 and hour < 12:
        speak("It's Morning Sir!")
    elif hour>=12 and hour<18:
        speak("It's Afternoon Sir!")
    else:
        speak("Its Night Sir! Good Night")
    date()
    speak("Please Tell me How can i help you sir!")

def gm():
    
    hour = datetime.datetime.now().hour #for greeting Good night Afternoon or morning
    
    if hour >= 6 and hour < 12:
        speak("It's Morning Sir! Good Morning!!!")
    elif hour>=12 and hour<18:
        speak("It's Afternoon Sir!")
    else:
        speak("Its Night Sir! Good Night")

def jarvis():
    assname =("Jarvis 1 point o") 
    speak("I am your Assistant") 
    speak(assname) 

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at         "+usage)
    battery = psutil.sensors_battery()
    speak("Battery is at      ")
    speak(battery.percent)

def takecommand(): #Takes command from user
    querry = input("Listening....")
    return querry
    # r = sr.Recognizer()
    # with sr.Microphone() as source: #module Pyaudio is installed to access microphone using pip win in scripts
    #     print("Listening....")
    #     r.pause_threshold = 0.5  #so that it listens after 1 second
    #     r.adjust_for_ambient_noise(source)
    #     r.phrase_threshold = 0.5
    #     r.dynamic_energy_threshold = 100
    #     audio = r.listen(source)
        
    # try:
    #     print("Recognizing...")
    #     querry = r.recognize_google(audio, language='en-US') #you can change language here in audio

    #     print(querry) #prints what it listens
    # except Exception as e:
    #     print(e)
    #     print("Say It Again")
    #     return "None"
    # return querry

def sendmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kcsrivastavas08@gmail.com','SHIvam7426')
    server.sendmail('kcsrivastavas08@gmail.com', to, content)
    server.close()

def jokes():
    speak(pj.get_jokes())
    print(pj.get_jokes())

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

def wolfram(z):
    #wolframalpha id = J4ERLH-GPQG9AHP9L
    # Taking input from user
    try:
        question = z
  
    # App id obtained by the above steps 
        app_id = 'J4ERLH-GPQG9AHP9L'
  
    # Instance of wolf ram alpha  
    # client class 
        client = wolframalpha.Client(app_id) 
  
    # Stores the response from  
    # wolf ram alpha 
        res = client.query(question) 
  
    # Includes only text from the response 
        answer = next(res.results).text 
  
        print(answer) 
        speak(answer)

    except Exception as e:
        print(e)
        print("Say It Again")

    return z


def coronavirus():
    url = "https://covid-19-data.p.rapidapi.com/country"
    speak("Enter the name of country sir!   ")
    a = input("name of country")
    querystring = {"format":"json","name": a}

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "1823e002fdmsh4e98afb629c1395p160c0bjsnd9d6717b4c05"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    y = json.loads(response.text)
    print("country")
    speak("country")
    print(y[0]["country"])
    speak(y[0]["country"])
    print("confirmed")
    speak("confirmed")
    print(y[0]["confirmed"])
    speak(y[0]["confirmed"])
    print("recovered")
    speak("recovered")
    print(y[0]["recovered"])
    speak(y[0]["recovered"])
    print("critical")
    speak("critical")
    print(y[0]["critical"])
    speak(y[0]["critical"])
    print("deaths")
    speak("deaths")
    print(y[0]["deaths"])
    speak(y[0]["deaths"])
    print("latitude")
    speak("latitude")
    print(y[0]["latitude"])
    speak(y[0]["latitude"])
    print("longitude")
    speak("longitude")
    print(y[0]["longitude"])
    speak(y[0]["longitude"])
    print("lastChange")
    speak("lastChange")
    print(y[0]["lastChange"])
    speak(y[0]["lastChange"])
    print("lastUpdate")
    speak("lastUpdate")
    print(y[0]["lastUpdate"])
    speak(y[0]["lastUpdate"])

#problem in speaking...api from rapid api
'''def mobile():
    print("Enter the number sir")
    a= input()
    querystring = {"mobilenos":a}
    url = "https://indianmobilenumberinfo.p.rapidapi.com/index.php"

    headers = {
        'x-rapidapi-host': "indianmobilenumberinfo.p.rapidapi.com",
        'x-rapidapi-key': "1823e002fdmsh4e98afb629c1395p160c0bjsnd9d6717b4c05"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    y = json.loads(response.text)
    print(y)'''


def screenshot():
    img = pyautogui.screenshot()
    img.save("C://Users//Asus//Desktop//jarvis//ss.png")

def usrname(): 
    speak("What should i call you sir........") 
    uname = takecommand() 
    speak("Welcome Mister") 
    speak(uname) 
    columns = shutil.get_terminal_size().columns 
      
    print("#####################".center(columns)) 
    print("Welcome Mr.".center(columns)) #to keep it in center
    print(uname.center(columns))
    print("#####################".center(columns)) 
    speak("How can i Help you, Sir") 

def headlines(): 
	#api-key = 0ace5f0941274b69b18251442bb970c0
	# BBC news api 
	main_url = " https://newsapi.org/v1/articles?source=bbc-news&language=en&country=in&sortBy=top&apiKey=0ace5f0941274b69b18251442bb970c0"

	# fetching data in json format 
	open_bbc_page = requests.get(main_url).json() 

	# getting all articles in a string article 
	article = open_bbc_page["articles"] 

	# empty list which will 
	# contain all trending news 
	results = [] 
	
	for ar in article: 
		results.append(ar["title"]) 
		
	for i in range(len(results)): 
		
		# printing all trending news 
		print(i + 1, results[i]) 

	#to read the news out loud for us 
	
	speak = Dispatch("SAPI.Spvoice") 
	speak.Speak(results)			


if __name__== "__main__":
    clear = lambda: os.system('cls') 
    
    # This Function will clean any 
    # command before execution of this python file 
    clear()  
    columns = shutil.get_terminal_size().columns
    print("#####################".center(columns)) 
    print("Welcome Sir ".center(columns)) #to keep it in center
    print("I am Jarvis an AI".center(columns))
    print("#####################".center(columns)) 
    wishme()
    usrname()

    while True:
        querry = takecommand().lower()

        if 'time' in querry:
            time()
        elif 'date' in querry:
            date()
        elif 'wikipedia' in querry:
            speak("Searching Sir... Hold On for a Second...")
            querry = querry.replace("wikipedia","") #replacing wikipedia word with blanck from search querry. so that it dont include wikipedia word in search
            querry = querry.replace("search","")
            result = wikipedia.summary(querry, sentences=5)
            speak("According to Wikipedia") 
            print(result)
            speak(result)

        elif 'open youtube' in querry: 
            speak("Here you go to Youtube\n") 
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            wb.get(chromepath).open_new_tab("youtube.com")
        
        elif 'open google' in querry: 
            speak("Here you go to Google\n") 
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            wb.get(chromepath).open_new_tab("google.com")

        elif 'coronavirus' in querry or 'covid' in querry:
            coronavirus()

        elif 'headline' in querry or 'head lines' in querry or 'news' in querry:
            headlines()

        elif 'send email' in querry:
            try:
                speak("who should i send the mail?")
                to = takecommand()
                print("Sending mail to",to)
                speak(to)
                speak("Okay  What should i say?")
                content = takecommand()
                speak(content)
                sendmail(to,content)
                speak("Your Email is on the way Sir")
                print("Your Email is on the way Sir")
            except Exception as e:
                print(e)
                print("Unable to send the Email")
                speak("Unable to send the Email")

        elif 'search' in querry:
            speak("Okay what should i search for Sir?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab('https://www.google.com.tr/search?q='+ search) #can add a string by typing +.com
        
        elif 'video' in querry:
            speak("Okay what should i search for Sir?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab('https://www.google.com.tr/search?q='+ search)
        
        elif 'music' in querry:
            speak("Okay what should i search for Sir?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab('https://www.google.com.tr/search?q='+ search)

        elif 'joke' in querry or 'jokes' in querry:
            jokes()
        
        elif 'my name' in querry:
            usrname()

        elif "who i am" in querry: 
            speak("If you are talking       then definately you are a human.") 
  
        elif "why you came to world" in querry: 
            speak("Thanks to Shivam. further It's a secret") 
  
        elif 'is love' in querry: 
            speak("It is 7th sense that destroy all other senses") 
  
        elif "who are you" in querry or "what's up" in querry: 
            speak("I am your virtual assistant created by Shivam") 
  
        elif 'reason for creating you' in querry: 
            speak("I was created as a Minor project by Mister Shivam Srivastava ") 
 
        elif 'lock window' in querry: 
                speak("locking the device") 
                ctypes.windll.user32.LockWorkStation() 
  
        elif 'shutdown system' in querry: 
                speak("Hold On a Sec ! Your system is on its way to shut down") 
                subprocess.call('shutdown / p /f') 
  
        elif "where is" in querry: 
            querry = querry.replace("where is", "") 
            location = querry 
            speak("User asked to Locate") 
            speak(location) 
            wb.open("https://www.google.com.tr/search?q=",+ location) 
  
        elif "restart" in querry: 
            subprocess.call(["shutdown", "/r"]) 
              
        elif "hibernate" in querry or "sleep" in querry: 
            speak("Hibernating") 
            subprocess.call("shutdown / h") 
  
        elif "log off" in querry or "sign out" in querry: 
            speak("Make sure all the application are closed before sign-out") 
            time.sleep(5) 
            subprocess.call(["shutdown", "/l"]) 
        
        elif "play movie" in querry:
            movie_dir = 'E:\\Movie' #playing media from local directory
            movie = os.listdir(movie_dir)
            os.startfile(os.path.join(movie_dir, movie[0]))

        elif "write a note" in querry or "take a note" in querry: 
            speak("What should i write, sir") 
            note = takecommand().lower() 
            file = open('jarvis.txt', 'w') 
            speak("Sir, Should i include date and time") 
            sn = takecommand().lower()
            if 'yes' in sn or 'sure' in sn: 
                strTime = datetime.datetime.now().strftime("% H:% M:% S") 
                file.write(strTime) 
                file.write(" :- ") 
                file.write(note) 
            else: 
                file.write(note) 
        
        elif "remember that" in querry:
            speak("What should i remember")
            data = takecommand()
            speak("You asked me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif "what you remember" in querry or "what i asked you to remember" in querry or "to remember" in querry: 
            speak("Showing records what you asked me to rember") 
            file = open("data.txt", "r")  
            speak(file.read(6))
            print(file.read()) 

        

        elif "weather" in querry:
            weather()   

            
        elif "insult" in querry: 
            speak("yo know what sir.............") 
            file = "C://Users//Asus//Desktop//jarvis//insult.txt"
            
            speak(random_line(file)) 
                      

        elif "show note" in querry or "me notes" in querry: 
            speak("Showing Notes") 
            file = open("jarvis.txt", "r")  
            print(file.read()) 
            speak(file.read(6)) 
                      
        # NPPR9-FWDCX-D2C8J-H872K-2YT43 
        elif "jarvis" in querry:
            jarvis()

        # most asked question from google Assistant 
        elif "will you be my gf" in querry or "will you be my bf" in querry:    
            speak("I'm not sure about, may be you should give me some time") 
  
        elif "how are you" in querry: 
            speak("I'm fine, glad to meet you") 
  
        elif "i love you" in querry: 
            speak("It's hard to understand") 
        
        elif "good morning" in querry or "good afternoon" in querry or "good night" in querry: 
            gm()
        
        elif "screenshot" in querry:
            screenshot()
            speak("Done Sir!")

        elif "cpu" in querry:
            cpu()

        elif "what you can do for me" in querry:
            speak("What you want me to do sir?...")
        
        elif "thanks" in querry:
            speak("Always There for you sir..")
        
        elif "made you" in querry or "your creator" in querry or "your father" in querry or "your dad" in querry:
            speak("I am created By Mr. Shivam Srivastava Sir!")
        
        elif "goodbye" in querry or "bye" in querry:
            speak("Nice to meet You!. Have a Nice day sir")
            quit()

        elif "marry me" in querry:
            speak("Have you ever looked after your face.....sorry...Not intrested sir")

        elif "today is" in querry or "is today" in querry:
            dayofweek()

        elif 'offline' in querry:
            quit()

        elif "what" in querry or "calculate" in querry or 'who' in querry or 'find' in querry or 'tell me' in querry or 'number' in querry:
            wolfram(querry)
        
        else:
            wolfram(querry)
            feed = open('querry.txt','a')
            feed.write("{}\n".format(querry)) #appends querry each time in a new line
            feed.close()



#py -u "c:/Users/Asus/Desktop/jarvis/jarvis.py"