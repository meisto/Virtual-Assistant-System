# ======================================================================
# Author: meisto
# Creation Date: Sun 19 Nov 2023 08:32:56 PM CET
# Description: -
# ======================================================================
import wave
import contextlib

import torch
import torchaudio

def main():
    """ Main function. """
    torch.random.manual_seed(0)

    # device = "cuda" if torch.cuda.is_available() else "cpu"
    device = "cpu"
    
    symbols = "_-!'(),.:;? abcdefghijklmnopqrstuvwxyz"
    symbols_lookup = { i: s for i, s in enumerate(symbols)}
    symbols = set(symbols)

    def text_to_sequence(text: str):
        text = text.lower()
        return [symbols_lookup[x] for x in text]

    bundle = torchaudio.pipelines.TACOTRON2_WAVERNN_CHAR_LJSPEECH

    processor = bundle.get_text_processor()
    tacotron2 = bundle.get_tacotron2().to(device)
    vocoder = bundle.get_vocoder().to(device)

    text = "Hello world. This is a test. Do not be alarmed!"

    with torch.inference_mode():
        print("Start processing...")
        processed, lengths = processor(text)
        processed = processed.to(device)
        lengths = lengths.to(device)

        print("Start infering...")
        specgram, spec_lengths, _ = tacotron2.infer(processed, lengths)

        print("Start vocoding...")
        waveforms, lengths = vocoder(specgram, spec_lengths)

        print("Start saving")
        torchaudio.save('/tmp/test.wav', waveforms, vocoder.sample_rate)

def silero():
    """ Silero Test. """
    language = "en"
    speaker = "tux_v2"
    device = "cpu"
    model, symbols, sample_rate, _, apply_tts = torch.hub.load(
        repo_or_dir="snakers4/silero-models",
        model="silero_tts",
        language=language,
        speaker=speaker,
    )

    model = model.to(device)

    for _ in range(5):
        audio = apply_tts(
            texts=["This is a test. Do not be alarmed! You will be terminated shortly."],
            model=model,
            sample_rate=sample_rate,
            symbols=symbols,
            device=device,
        )

        print(audio)
        print(len(audio))

        with contextlib.closing(wave.open("/tmp/test.wav", mode="wb")) as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sample_rate)
            wf.writeframes((audio[0] * 32767).numpy().astype("int16"))



if __name__ == "__main__":
    silero()
