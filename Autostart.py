import time
import subprocess
from clapDetector import ClapDetector, printDeviceInfo

print("Available audio devices:")
printDeviceInfo()

# ВЫБЕРИ НОМЕР МИКРОФОНА
MIC_INDEX = 1  

clap = ClapDetector(inputDevice=MIC_INDEX, logLevel=10)

try:
    clap.initAudio()
except Exception as e:
    print("Audio init failed:", e)
    exit(1)

# Чувствительность
threshold_bias = 2500
lowcut = 100
highcut = 4000

print("Ожидание двойного хлопка...")

try:
    while True:
        data = clap.getAudio()
        result = clap.run(
            thresholdBias=threshold_bias,
            lowcut=lowcut,
            highcut=highcut,
            audioData=data
        )

        if len(result) == 1:
            print("Один хлопок обнаружен")
        if len(result) == 2:
            print("Два хлопка обнаружены! Запускаю Dota 2...")

            subprocess.Popen([
                r"C:\Program Files (x86)\Steam\steam.exe",
                "-applaunch", "570"
            ])
            break

        time.sleep(0.05)

except KeyboardInterrupt:
    print("Завершено пользователем")
finally:
    clap.stop()
