---
layout: post
author:
  name: Paper ID 60
  difficulty: Hard
share: true
title: NATURAL-TTS-SYNTHESIS-BY-CONDITIONING-WAVENET-ON-MEL-SPECTROGRAM-PREDICTIONS(Tacotron2)
categories:
- text to speech
tags: []

---
**Abstract** - This paper describes Tacotron 2, a neural network architecture for speech synthesis directly from text. The system is composed of a recurrent sequence-to-sequence feature prediction network that maps character embeddings to mel-scale spectrograms, followed by a modified WaveNet model acting as a vocoder to synthesize timedomain waveforms from those spectrograms. Our model achieves a mean opinion score (MOS) of 4.53 comparable to a MOS of 4.58 for professionally recorded speech. To validate our design choices, we present ablation studies of key components of our system and evaluate the impact of using mel spectrograms as the input to WaveNet instead of linguistic, duration, and F0 features. We further demonstrate that using a compact acoustic intermediate representation enables significant simplification of the WaveNet architecture.

**Paper** - [https://arxiv.org/pdf/1712.05884.pdf](https://arxiv.org/pdf/1712.05884.pdf)

**Dataset -** [https://keithito.com/lj-speech-dataset/](https://keithito.com/lj-speech-dataset/)
    