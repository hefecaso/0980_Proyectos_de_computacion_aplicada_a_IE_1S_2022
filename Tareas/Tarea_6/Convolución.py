import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import wave
from scipy.io import wavfile

music = input('Ingrese el nombre del archivo de audio sin la extension: ')
file = wave.open(f'{music}.wav')
audio = file.readframes(-1)
audio = np.frombuffer(audio, dtype=np.int16)

fs, Audiodata = wavfile.read(f'{music}.wav')

alfa = np.array([1.,0.,0.])
audio_modificado = np.convolve(audio, alfa)

audio_modificado = audio_modificado.astype(np.int16)
write('audio_modificado.wav', 40000, audio_modificado)

###
fig = plt.figure(figsize=(15,9))
fig.tight_layout()
plt1 = fig.add_subplot(1,2,1)
plt2 = fig.add_subplot(1,2,2)
###

print(f'\nDuracion = {Audiodata.shape[0]/fs} s  \nFrecuencia de Muestreo = {fs} [=] Muestras/Seg' \
      f' \nWav format = {Audiodata.dtype}')

plt1.plot(Audiodata)
plt1.set_title("Audio original")
plt2.plot(audio_modificado)
plt2.set_title("Audio modificado")
plt.show()
