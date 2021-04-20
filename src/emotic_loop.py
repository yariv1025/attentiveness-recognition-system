import threading
import cv2
from src.emotic_app import emotic

class EmoticLoop(threading.Thread):

    def __init__(self, tid, fp, locks):
        threading.Thread.__init__(self)
        self.threadID = tid
        self.fp = fp
        self.locks = locks

    def run(self):
        while self.fp.isOpened():
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.fp.release()
                break
            self.locks[1].acquire()
            print(emotic())
            self.locks[0].release()
