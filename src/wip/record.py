# ======================================================================
# Author: meisto
# Creation Date: Mon 20 Nov 2023 01:42:18 AM CET
# Description: -
# ======================================================================
import sys
import queue

import sounddevice as sd
import soundfile as sf

audio_queue = queue.Queue()

def audio_callback(indata, frames, time, status):
    if status:
        print(f"Status at {time}: {status}", file=sys.stderr)
        print(frames)
    audio_queue.put(indata.copy())

def main():
    """ Main function. """
    print("Devices:")
    print(sd.query_devices())
    samplerate=48000
    number_channels=2
    device=12

    try:
        with sf.SoundFile(
            "/tmp/test_record.wav",
            mode="x",
            samplerate=samplerate,
            channels=number_channels,
            # subtype=""
        ) as file:
            with sd.InputStream(
                samplerate=samplerate,
                device=device,
                channels=number_channels,
                callback=audio_callback,
            ):
                print("[Ctrl+C] Stop recording")
                while True:
                    file.write(audio_queue.get())

    except KeyboardInterrupt:
        print("Recording finished")


if __name__ == "__main__":
    main()
