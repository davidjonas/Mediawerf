__author__ = 'David Jonas'

import swmixer

class AudioController(object):
    sounds = {}
    channels = {}
    samplerate = 44100
    chunksize = 1024
    stereo = True
    MAX_SOUNDS = 10

    def __init__(self, samplerate=44100, chunksize=1024, stereo=True):
        self.samplerate = samplerate
        self.chunksize = chunksize
        self.stereo = stereo
        swmixer.init(samplerate=self.samplerate, chunksize=self.chunksize, stereo=self.stereo)
        swmixer.start()

    def add_sound(self, filename):
        if filename not in self.sounds.keys():
            if len(self.sounds.keys()) <= self.MAX_SOUNDS:
                self.sounds[filename] = swmixer.Sound(filename)
            else:
                print "ERROR: Maximum number of sounds loaded."

    def play_sound(self, filename, fade=0, loops=0):
        if filename not in self.sounds.keys():
            self.add_sound(filename)
        if filename not in self.channels.keys():
            self.channels[filename] = self.sounds[filename].play(fadein=int((self.samplerate * fade)), loops=loops)
        elif self.channels[filename].done:
            del self.channels[filename]
            self.play_sound(filename)
        elif not self.channels[filename].active:
            self.unpause(filename)
        else:
            print "Error: Already playing."

    def is_playing(self, filename):
        return filename in self.channels.keys() and self.channels[filename].active

    def jump_seconds(self, filename, seconds):
        if filename in self.sounds.keys():
            if filename in self.channels.keys():
                chan = self.channels[filename]
                chan.set_position(chan.get_position() + int((self.samplerate * seconds)))
            else:
                self.play_sound(filename)
                self.jump_seconds(filename, seconds)
        else:
            print "ERROR: Sound is not loaded."

    def go_to_seconds(self, filename, seconds):
        if filename in self.sounds.keys():
            if filename in self.channels.keys():
                chan = self.channels[filename]
                chan.set_position(int(self.samplerate * seconds))
            else:
                self.play_sound(filename)
                self.go_to_seconds(filename, seconds)
        else:
            print "ERROR: Sound is not loaded."

    def set_volume(self, filename, volume, fade=0):
        if filename in self.sounds.keys():
            if filename in self.channels.keys():
                self.channels[filename].set_volume(volume, fadetime=int((self.samplerate * fade)))
            else:
                print "ERROR: sound is not playing."
        else:
            print "ERROR: Sound is not loaded."

    def stop(self, filename):
        if filename in self.sounds.keys():
            if filename in self.channels.keys():
                self.channels[filename].stop()
                del self.channels[filename]
            else:
                print "ERROR: sound is not playing."
        else:
            print "ERROR: Sound is not loaded."

    def pause(self, filename):
        if filename in self.sounds.keys():
            if filename in self.channels.keys():
                self.channels[filename].pause()
            else:
                print "ERROR: sound is not playing."
        else:
            print "ERROR: Sound is not loaded."

    def unpause(self, filename):
        if filename in self.sounds.keys():
            if filename in self.channels.keys():
                self.channels[filename].unpause()
            else:
                print "ERROR: sound is not playing."
        else:
            print "ERROR: Sound is not loaded."

    def get_volume(self, filename):
        if filename in self.channels.keys():
            return self.channels[filename].get_volume()
        else:
            return 0