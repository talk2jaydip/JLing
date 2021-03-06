# -*- coding: utf-8 -*-
from . import snowboydecoder
import sys
import signal


class Snowboy_JLing:
    def __init__(self, model, sensitivity):
        self.interrupted = False
        self.model = model
        self.sensitivity = sensitivity
        self.detector = snowboydecoder.HotwordDetector(self.model, sensitivity=self.sensitivity)

    def signal_handler(self):
        snowboydecoder.play_audio_file()
        self.interrupted = True

    def interrupt_callback(self):
        return self.interrupted

    # 播放音频
    def play_audio(self, fileList):
        snowboydecoder.play_audio_file(fileList)

    def Vcad(self):
        print("asd")

    def start(self):
        try:
            print('JLing等待唤醒')
            self.detector.start(detected_callback=self.signal_handler,
                                interrupt_check=self.interrupt_callback,
                                sleep_time=0.03)
            self.interrupted = False
        except:
            exit()
