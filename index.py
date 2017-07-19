from pydub import AudioSegment
from os import listdir
import numpy as np
import matplotlib.pyplot as plt


song_dir = "songs"
attenuate_db = 1
accentuate_db = 2


def bass_line_freq(track):
    sample_track = list(track)

    # c-value
    est_mean = np.mean(sample_track)

    # a-value
    est_std = 3 * np.std(sample_track) / (2 ** 0.5)

    # d-value
    est_phase = 0

    # k-value 4 radians
    t = np.linspace(0, 8 * np.pi, len(sample_track))

    # f(x) = a[sin(kx + t)] + c
    estimate_function = est_std * np.sin(t + est_phase) + est_mean

    plt.plot(estimate_function)
    plt.show()
    
    return

for filename in listdir(song_dir):
    sample = AudioSegment.from_mp3(song_dir + "/" + filename)
    filtered = sample.low_pass_filter(100)

    bass_line_freq(sample.get_array_of_samples())

    combined = (sample - attenuate_db).overlay(filtered + accentuate_db)
    # combined.export("exports/" + filename.replace(".mp3", "") + "-export.mp3", format="mp3")


