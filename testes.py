import vlc
import time
video = "Acima do sol - Skank - Karaokê com violão.mp4"
play = vlc.MediaPlayer(video)

play.play()

time.sleep(2)

while play.is_playing():
    print("tocando")
print('acacou de tocar')