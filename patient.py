import time

class patient:
    def __init__(self, frames, time_to_be_admitted):
        self.start = frames
        self.time_to_be_admitted = time_to_be_admitted

    def time_up(self, frames):
        return frames>self.time_to_be_admitted+self.start