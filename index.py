from pydub import AudioSegment
from os import listdir

song_dir = "songs"

for filename in listdir(song_dir):
    sample = AudioSegment.from_mp3(song_dir + "/" + filename)
    filtered = sample.low_pass_filter(100)

    combined = (sample - 1).overlay(filtered + 2)
    combined.export("exports/" + filename.replace(".mp3", "") + "-export.mp3", format="mp3")