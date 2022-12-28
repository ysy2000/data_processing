
#-*- coding: utf-8 -*-
import torch
import torchaudio
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import scipy.io as sio
from scipy import signal
import wave
import struct
import matplotlib.pyplot as plt
from math import pi, cos
from scipy.signal import freqz, butter, lfilter
import numpy as np
import os
from scipy.io import wavfile




def plot_specgram(waveform, sample_rate, title="Spectrogram", xlim=None):
 waveform = waveform.numpy()

 num_channels, num_frames = waveform.shape
 time_axis = torch.arange(0, num_frames) / sample_rate
 figure, axes = plt.subplots(num_channels, 1)
 if num_channels == 1:
   axes = [axes]
 for c in range(num_channels):
   axes[c].specgram(waveform[c], Fs=sample_rate)
   if num_channels > 1:
     axes[c].set_ylabel(f'Channel {c+1}')
   if xlim:
     axes[c].set_xlim(xlim)
 figure.suptitle(title)
 plt.show()
 plt.savefig(waveform+'.png', dpi=300)

def plot_audio(file_path):
    data, sampling_rate = torchaudio.load(file_path)
    _, ax = plt.subplots(1, 1, figsize=(8, 4))
    ax.plot(data[0, :])
    plt.show()

def spectrograms(file_path):
    data, sampling_rate = torchaudio.load(file_path)
    # data = data.narrow()
    n_fft = int(np.ceil(0.025 * sampling_rate))
    win_length = int(np.ceil(0.025 * sampling_rate))
    hop_length = int(np.ceil(0.01 * sampling_rate))
    print(f'n_fft: {n_fft}, win_length: {win_length}, hop_length: {hop_length}')

    spectrogram = torch.nn.Sequential(
        torchaudio.transforms.Spectrogram(
            n_fft=n_fft,
            win_length=win_length,
            hop_length=hop_length
        ),
        torchaudio.transforms.AmplitudeToDB()
    )

    mel_spectrogram = torch.nn.Sequential(
        torchaudio.transforms.MelSpectrogram( sample_rate=sampling_rate,
            n_fft=n_fft,
            win_length=win_length,
            hop_length=hop_length,
            n_mels=80
        ),
        torchaudio.transforms.AmplitudeToDB()
    )
    print(type(data))
    spec = spectrogram(data)
    mel = mel_spectrogram(data)
    print(f'spec.shape:{spec.shape}, mel.shape:{mel.shape}')

    _, ax = plt.subplots(1, 2, figsize=(8, 4))
    plt.xlabel('(10ms)')
    plt.ylabel('(Hz)')
    ax[0].pcolor(mel[0])


    ax[1].pcolor(spec[0])
    plt.tight_layout()
    plt.show()
    plt.savefig(file_path[:-4]+".png")

def plot_pitch(file_path):
    data, sampling_rate = torchaudio.load(file_path)
    pitch = torchaudio.functional.detect_pitch_frequency(data, sampling_rate)

    figure, axis = plt.subplots(1, 1)
    axis.set_title("Pitch Feature")
    axis.grid(True)

    end_time = data.shape[1] / sampling_rate
    time_axis = torch.linspace(0, end_time, data.shape[1])
    axis.plot(time_axis, data[0], linewidth=1, color='gray', alpha=0.3)
    axis2 = axis.twinx()
    time_axis = torch.linspace(0, end_time, pitch.shape[1])
    ln2 = axis2.plot(
        time_axis, pitch[0], linewidth=2, label='Pitch', color='green')

    axis2.legend(loc=0)
    plt.show()

def conv_reverb(rir_path, audio_path):
    rir_raw, sampling_rate = torchaudio.load(rir_path)
    # First, we need to clean up the RIR.
    # We extract the main impulse, normalize the signal power, then flip the time axis.
    rir = rir_raw[:, int(sampling_rate * 1.01):int(sampling_rate * 1.3)]
    rir = rir / torch.norm(rir, p=2)
    rir = torch.flip(rir, [1])
 # Then we convolve the speech signal with the RIR filter.
    speech, sampling_rate = torchaudio.load(audio_path)
    speech_ = torch.nn.functional.pad(speech, (rir.shape[1]-1, 0))
    augmented = torch.nn.functional.conv1d(speech_[None, ...], rir[None, ...])[0]
    plot_specgram(speech, sampling_rate, title="Original audio")
    plot_specgram(augmented, sampling_rate, title="Convolution reverb")
    torchaudio.save('conv.wav', augmented, sampling_rate)
# Press the green button in the gutter to run the script.

def butter_bandpass(lowcut, highcut, fs, order=4):
    nyq=0.5*fs
    low = lowcut/nyq
    high = highcut/nyq
    b, a = butter(order,[low,high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=4):
    b,a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

# file_a = "general.wav"
# file_b = "stretch.wav"
# file_c = "test_c.wav"

num_samples = 48000

sampling_rate = 48000
AMPLITUDE = 2000




if __name__ == '__main__':
    # wav = r'C:\Users\나종환\PycharmProjects\pythonProject\song.wav'
    # (file_dir, file_id)=os.path.split(wav)
    # sample_rate, data = wavfile.read(wav)

    # fft=np.fft.fft(data)

    # recovered_a = butter_bandpass_filter(data, 100, 500, 48000, order=4)
    # recovered_b = butter_bandpass_filter(data, 500, 1000, 48000, order=4)
    # recovered_c = butter_bandpass_filter(data, 1000, 1500, 48000, order=4)

    # nframes = num_samples
    # comptype = "NONE"
    # compname = "not compressed"
    # nchannels = 1
    # sampwidth = 2

    # wav_file = wave.open(file_a, 'w')
    # wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
    # for s in recovered_a:
    #     wav_file.writeframes(struct.pack('h', int(s * AMPLITUDE)))

    # wav_file = wave.open(file_b, 'w')
    # wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
    # for s in recovered_b:
    #     wav_file.writeframes(struct.pack('h', int(s * AMPLITUDE)))
    spectrograms('general_cut.wav')
    spectrograms('stretch_cut.wav')




# spectrograms('speech.wav')
 # plot_pitch('speech.wav')
 # conv_reverb('rir.wav', 'speech.wav')
 # plot_audio('drum_loop.wav')
 # spectrograms('drum_loop.wav')
 # spectrograms('song.wav')
