from pydub import AudioSegment


def changeSpeed(voice):
    sound = AudioSegment.from_file(Voice)

    def speed_change(sound, speed):
        sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
            "frame_rate": int(sound.frame_rate * speed)
        })
        return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

    return speed_change(sound, 1.5)
