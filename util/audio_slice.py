from pydub import AudioSegment

def slice(wav_file_bytes, time):
    audio = AudioSegment(wav_file_bytes, sample_width=2, frame_rate=44100, channels=2)
    # origin_length = audio.duration_seconds
    return audio.raw_data

    if origin_length > time:
      return audio[:time * 1000].export('temp.wav', format='wav')

    return audio[:int(origin_length) * 1000].export('temp.wav', format='wav')