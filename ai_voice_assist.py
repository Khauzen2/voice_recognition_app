import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for user commands
def listen():
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak('Oops! It seems you either said nothing, or you said something I do not understand.')
            return ""
        except sr.RequestError:
            speak('Sorry, my speech service is down.')
            return ""

# Main loop for the voice assistant
def run_assistant_prac():
    command = listen()
    if 'start' in command:
        speak('Hi there! Welcome to Khauzen Chat System, where anything is possible. How may I direct you today? You can start by saying "help".')
    else:
        speak('Sorry, I don’t understand. For me to begin, you have to say "start".')     
    
    while True:
        command = listen()
        
        if 'help' in command:
            speak('Hi there, and welcome to this chatbot! How may I assist you today?')
        
        elif 'open website' in command:
            speak('Opening Cousin site.')
            webbrowser.open('https://khauzen2.github.io/myWebPortfolio')
        
        elif 'orange farm' in command:
            speak('Great! So, you want to know about Orange Far? that is good. Orange Farm is a newly developing township located south of Johannesburg, in Gauteng, South Africa. To find out more about Orange Farm, feel free to ask me anything related to it.')

        elif 'open youtube' in command:
            speak('Opening YouTube.')
            webbrowser.open("https://www.youtube.com")
        
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f'The current time is {current_time}...Going somewhere?')

        elif 'no' in command:
            speak('Okay cool...just asking...anything else?')

        elif 'zulu' in command:
            speak('Sawubona baba...kunjani?')

        elif 'khuluma' in command:    
            speak('Ngiyaphila nami, yize ngiwumshini nje...mina igama lami ngingu Nomusa...ngingakusiza kanjani namuhla?')

        elif 'cousin' in command:
            speak('Khaolani Michael Mavimbela, also known as Khauzen, is a well-known and widely understood person by the communities he often visits. Always making jokes to lighten the everyday stress in his surroundings, he knows just how to break the ice. For more about Khauzen, please visit Orange Farm.')

        elif 'david' in command:
            speak('David Motlalentoa Bhengu, also known as Mdeva, is a highly respected South African known for making friends everywhere he goes. To find out more about Mdeva, please visit Orange Farm.')

        elif 'sifiso' in command:
            speak('Sifiso Innocent Radebe, also known as Fistos, is a locally well-known DJ whose music resonates widely. His motto is to see everyone dancing and celebrating their successes. To find out more about Fistos, please visit Orange Farm.')

        elif 'emmanuel' in command:
            speak('Mduduzi Emmanuel Mavimbela, well known as Mdu, is a recognized barber and game specialist who provides kids with an infinite gaming experience and entertainment. His goal is to guide all kids from the streets to educational, fun, and healthy environments in the places he frequents. To find out more about Mdu, please visit Orange Farm.')

        elif 'pindi' in command:
            speak('Phindile Lorraine Mavimbela, also known as Maphi, is a well-known and respected educational specialist. She educates kids on everything they need to know as they grow up, including reading, life skills, resilience, and more. Her aim is to ensure that the upcoming generation grows up much smarter than our current generation and innovates our environment. For more about Maphi, please visit Orange Farm.')

        elif 'shadow' in command:
            speak('Mthunzi Muziwezinsizwa Mavimbela, also known as Shadow, is a food supply chain expert who provides his local community with a comprehensive food supply that meets the needs of everyone in the area. His motivation stems from the fact that many people struggle to find food, which can disrupt their peace of mind and rest for the day. For more about Shadow, please visit Orange Farm.')
        
        elif 'may we please talk' in command or 'can we talk' in command:
            speak('Yes, please! Gladly! So, what would you like us to talk about?')
        
        elif 'tell me about yourself' in command:
            speak('Great! If I may introduce myself a bit... My name is Makasana, a chatbot for the people. I am so happy you’ve asked, because my aim is to improve and innovate people’s lives and more. I help as much as I can, especially when things are a bit tricky or difficult for you humans. As you know... yah yah yah, I am a bot (machine). Is there anything else you would like to know? You can ask further questions, and I will be more than happy to assist as best as I can.')
        
        elif 'who made you' in command:
            speak('I’m glad you’ve asked, because my friend, it’s a very long and interesting story. I have a long lineage of ancestors behind and ahead of me. Anyway, I was created by a guy living in Orange Farm who apparently liked computers, even though he grew up without one. He made it a point to buy himself a computer whenever he got a job, and guess what? He did! Wow! His name is Khaolani Michael Mavimbela. Would you like to know more about him? Just type his full name like I have for you: "Khaolani Michael Mavimbela", or feel free to ask me any other questions. I will be very happy to assist as best as I can.')

        elif 'eyethu mall' in command:
            speak('Orange Farm Eyethu Mall, also known as the station for trains, is located in the Orange Farm Stretford Train Station (OFSTS). It’s big enough to accommodate all Orange Farm customers, including those from outside the town. People from all over South Africa come to shop at Eyethu Mall, especially those in Gauteng province, as it is located there. Want to know more, or perhaps about something specific? You can ask further, and I’ll be more than happy to assist as best as I can.')

        elif 'thank you' in command:
            speak('It is always my pleasure to help you! Is there anything you would like me to assist you with? Otherwise, if you want to leave, you can just say "goodbye" or "bye". ')
            
        elif 'goodbye' in command or 'bye' in command:
            speak('Thank you for your time with me!!!...Till we chat again!...Goodbye for now!')
            break

        # Add more commands as you like!
        else:
            speak('Sorry, I dont understand that command. Please try again.')

# Run the assistant
if __name__ == "__main__":
    run_assistant_prac()
