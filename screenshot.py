from PIL import Image, ImageGrab
import time
n=int(input("Enter the first number for sequence where you want to add the file name :"))
def screenshot():
    image=ImageGrab.grab()
    image.save(f"{n}.jpg", "JPEG")
if __name__ == "__main__":
    # time.sleep(1)
    # screenshot()
    while(1):
        time.sleep(15) #It gives the 15 sec sleep time , You can adjust it too.
        screenshot()
        n = n + 1


