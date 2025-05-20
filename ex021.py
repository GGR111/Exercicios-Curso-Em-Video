from pygame import mixer
from time import sleep
mixer.init()
mixer.music.load('music.mp3')
mixer.music.play()
while mixer.music.get_busy(): sleep(1)

