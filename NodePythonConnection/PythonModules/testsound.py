__author__ = 'David Jonas'

from audio_control import AudioController

import termios, fcntl, sys, os

ac = AudioController()

ac.add_sound("bg01.wav")
ac.add_sound("bg02.wav")
ac.add_sound("sample2.wav")
ac.add_sound("sample3.wav")
ac.add_sound("sample4.wav")
ac.add_sound("sample5.wav")


v = 0.2

def handle(key):
    global v
    if key == 'q':
        if ac.is_playing("bg01.wav"):
            print "rewind"
            ac.go_to_seconds("bg01.wav", 0)
            ac.pause("bg01.wav")
        else:
            ac.play_sound("bg01.wav")
    if key == 'w':
        if ac.is_playing("bg02.wav"):
            ac.go_to_seconds("bg02.wav", 0)
            ac.pause("bg02.wav")
        else:
            ac.play_sound("bg02.wav")
    if key == 'e':
        if ac.is_playing("sample2.wav"):
            ac.go_to_seconds("sample2.wav", 0)
            ac.pause("sample2.wav")
        else:
            ac.play_sound("sample2.wav")
    if key == 'r':
        if ac.is_playing("sample3.wav"):
            ac.go_to_seconds("sample3.wav", 0)
            ac.pause("sample3.wav")
        else:
            ac.play_sound("sample3.wav")
    if key == 't':
        if ac.is_playing("sample4.wav"):
            ac.go_to_seconds("sample4.wav", 0)
            ac.pause("sample4.wav")
        else:
            ac.play_sound("sample4.wav")
    if key == 'y':
        if ac.is_playing("sample5.wav"):
            ac.go_to_seconds("sample5.wav", 0)
            ac.pause("sample5.wav")
        else:
            ac.play_sound("sample5.wav")
    if key == 'a':
        current = ac.get_volume("bg02.wav")
        if current < 1.0:
            ac.set_volume("bg02.wav", current + v, fade=1.5)
    if key == 'z':
        current = ac.get_volume("bg02.wav")
        if current > 0.0:
            ac.set_volume("bg02.wav", current - v, fade=1.5)



fd = sys.stdin.fileno()

oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

try:
    while 1:
        try:
            c = sys.stdin.read(1)
            handle(c)
        except IOError: pass
finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
