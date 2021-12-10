import datetime
import youtube_dl
import speake3
#espeak
engine = speake3.Speake() # Initialize the speake engine
engine.set('voice', 'en')
engine.set('speed', '107')
engine.set('pitch', '99')
#datetime
now = datetime.datetime.now()

engine.say("\nHello, I am J.A.R.V.I.S.\n")

#Inputs and Answers
while True:
  try:   
    #Jarvis?
    bot_input = input()
    if bot_input.strip()=='Jarvis?':
      engine.say('Yes sir?')
    if bot_input.strip()=='Jarvis':
      engine.say('Yes sir?')
    if bot_input.strip()=='jarvis?':
      engine.say('Yes sir?')
    if bot_input.strip()=='jarvis':
      engine.say('Yes sir?')
      #snowman
    if bot_input.strip()=='☃':
      engine.say('No')
    #Time?
    if bot_input.strip()=='what time is it jarvis?':
      engine.say(now.strftime("%Y-%m-%d %H:%M:%S")) 
    if bot_input.strip()=='what time is it?':
      engine.say(now.strftime("%Y-%m-%d %H:%M:%S")) 
    if bot_input.strip()=='what is the time':
      engine.say(now.strftime("%Y-%m-%d %H:%M:%S")) 
    if bot_input.strip()=='time?':
      engine.say(now.strftime("%Y-%m-%d %H:%M:%S"))      
    if bot_input.strip()=='jarvis what time is it':
      engine.say(now.strftime("%Y-%m-%d %H:%M:%S"))    
    #How are you
    if bot_input.strip()=='how are you?':
      engine.say('I am well, Sir.')
    if bot_input.strip()=='how are you today?':
      engine.say('I am rather well, thanks for asking.')      
    if bot_input.strip()=='how are you, jarvis?':
      engine.say('I am mighty fine, sir.')      
    if bot_input.strip()=='sup jarvis?':
      engine.say('Sup, Sir.')    

    #Random
    if bot_input.strip()=='good':
      engine.say('Good indeed, Sir.')
    if bot_input.strip()=='wake up jarvis':
      engine.say('All systems green. Good to see you, Sir')      
    if bot_input.strip()=='system report':
      engine.say('All systems functioning and ready for use, Sir.')      
    if bot_input.strip()=='weapons status':
      engine.say('all weapons green. Ready for action, Sir.')    
    if bot_input.strip()=='jarvis, what is my name?':
      engine.say('Mr. Boes, if I am not mistanken')
    if bot_input.strip()=='who am i?':
      engine.say('Mr. Henry Boes, if I am not mistanken')  
    if bot_input.strip()=='sheilds status':
      engine.say('Shields are holding, minor damage to the left array, Sir.')      
    if bot_input.strip()=='who made you?':
      engine.say('A bright young man by the name of Henry Boes is responsible for my programming')   
    if bot_input.strip()=='thanks jarvis':
      engine.say('The pleasure is mine, Sir.')
    if bot_input.strip()=='thank you':
      engine.say('Absolutley, Sir')      
    if bot_input.strip()=='thanks':
      engine.say('By all means, anytime.')      
    if bot_input.strip()=='thank you jarvis':
      engine.say('Anytime for you, Sir')  
    if bot_input.strip()=='what is my name?':
      engine.say('Mr. Boes, if I am not mistanken')  
    #Hello
    if bot_input.strip()=='hey':
      engine.say('Hello, sir.')
    if bot_input.strip()=='greetings':
      engine.say('Greetings to you too, Sir!')      
    if bot_input.strip()=='hi':
      engine.say('Hi Sir!')      
    if bot_input.strip()=='hello':
      engine.say('Hello!')     
    #Youtube (Big Bill Hells)
    if bot_input.strip()=='download something funny':
      engine.say('Of course, Sir:')
      ydl_opts = {}
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=4sZuN0xXWLc'])
    #false
    if bot_input.strip=='':
      engine.say('All systems normal. Entering Sleep Mode, Sir.')
    #Goodbye
    if bot_input.strip()=='goodbye jarvis':
      engine.say('Goodbye.')
      break
    if bot_input.strip()=='see you':
      engine.say('Until later, Sir.')
      break
    if bot_input.strip()=='bye Jarvis':
      engine.say('Goodbye Sir')
      break     
    if bot_input.strip()=='goodbye':
      engine.say('Bye!')
      break
    if bot_input.strip()=='bye':
      engine.say('Shutting down all systems. Goodbye.')
      break
    if bot_input.strip()=='goodbye':
      engine.say('Bye now!')
      break
  except(KeyboardInterrupt, EOFError, SystemExit):
    engine.talkback()
    break
