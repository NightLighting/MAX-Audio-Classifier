from pydub import AudioSegment

def slice(wav_file, time):
    audio = AudioSegment.from_wav(wav_file)
    origin_length = audio.duration_seconds

    if origin_length > time:
      return audio[:time * 1000].export('temp.wav', format='wav')

    return audio[:int(origin_length) * 1000].export('temp.wav', format='wav')