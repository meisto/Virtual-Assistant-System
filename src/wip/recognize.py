# ======================================================================
# Author: meisto
# Creation Date: Mon 20 Nov 2023 12:52:26 AM CET
# Description: -
# ======================================================================
import torch
import torchaudio

from torchaudio.models.decoder import ctc_decoder, download_pretrained_files

class GreedyCTCDecoder(torch.nn.Module):
    def __init__(self, labels, blank = 0):
        super().__init__()
        self.labels = labels
        self.blank = blank

    def forward(self, emission: torch.Tensor) -> str:
        """
        TODO

        Parameters:
            emission: torch.Tensor
        Returns:
            Str - The decoded text.
        """
        indices = torch.argmax(emission, dim=-1)

        # Remove sequential duplicate values
        indices = torch.unique_consecutive(indices, dim=-1)

        return "".join([self.labels[i] for i in [i for i in indices if i != self.blank]])

def main():
    """ Main function. """
    device = "cpu"

    bundle = torchaudio.pipelines.WAV2VEC2_ASR_BASE_960H
    # bundle = torchaudio.pipelines.VOXPOPULI_ASR_BASE_10K_DE

    sample_rate = bundle.sample_rate
    labels = bundle.get_labels()

    print(f"Sample rate: {sample_rate}")
    print(f"Labels: {labels}")

    model = bundle.get_model().to(device)

    waveform, given_sample_rate = torchaudio.load("/tmp/test_record.wav")
    waveform = waveform.to(device)

    # Resample audio to wanted rate
    if sample_rate != given_sample_rate:
        waveform = torchaudio.functional.resample(waveform, given_sample_rate, sample_rate)

    # Generate probability distribution
    with torch.inference_mode():
        emission, _ = model(waveform)

    if False:
        # Greedy decoder
        decoder = GreedyCTCDecoder(labels=labels)

        result = decoder(emission[0])
        print(result)
    else:
        #
        files = download_pretrained_files("librispeech-4-gram")
        lm_weight = 3.23
        word_score = -0.26

        decoder = ctc_decoder(
            lexicon=files.lexicon,
            tokens=files.tokens,
            lm=files.lm, # None,
            nbest=3,
            beam_size=1500,
            lm_weight=lm_weight,
            word_score=word_score,
        )

        decoded = decoder(emission)


        transcript = " ".join(decoded[0][0].words).lower().strip()

        print()
        print(decoded)
        print(transcript)
        # print(score)


if __name__ == "__main__":
    main()
