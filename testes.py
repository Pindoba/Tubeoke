from unittest import case
import vlc
import time
video = "123.mp4"
play = vlc.MediaPlayer(video)

play.play()

time.sleep(2)

while play.is_playing():
    print("tocando")
    time.sleep(2)
print('acacou de tocar')
