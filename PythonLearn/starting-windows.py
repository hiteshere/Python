import pyttsx

engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',rate-80)
engine.say('A msg has been sent to the Hitesh Kataria about your actions')
engine.say('taking your photo for identification')
engine.runAndWait()