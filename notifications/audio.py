import simpleaudio as sa

class Audio():
    def __init__(self):
        pass
    def notify(self):
        wave_obj = sa.WaveObject.from_wave_file('./notifications/alarm.wav')
        while True:
            play_obj = wave_obj.play()
            play_obj.wait_done()