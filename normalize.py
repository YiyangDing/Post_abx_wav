import soundfile as sf
import os

for file in os.listdir('./'):
    if file.startswith('LA'):
        for wav in os.listdir(file):
            data, fs = sf.read(file + os.sep + wav)
            thre = max(abs(data))
            ndata = data / thre * 0.8
            sf.write(file + os.sep + wav, ndata, fs)

