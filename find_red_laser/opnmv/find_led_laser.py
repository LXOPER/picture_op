import sensor,image,time,math
from pyb import UART,LED,Pin
import pyb


sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.RGB565) # use RGB565.
sensor.set_framesize(sensor.QVGA) # use QQVGA for speed.
sensor.set_auto_gain(False)
sensor.skip_frames(20) # Let new settings take affect.
#key point改变曝光度
sensor.set_auto_exposure(False, 1400)

sensor.set_auto_whitebal(False) # turn this off.

#找色块函数
def color_blob(threshold):
        '''
        threshold:阈值
        cx,cy,红色坐标
        '''
    blobs = img.find_blobs([threshold])
    if len(blobs) == 1:
        # Draw a rect around the blob.
        b = blobs[0]
        img.draw_rectangle(b[0:4]) # rect
        cx = b[5]
        cy = b[6]
        img.draw_cross(b[5], b[6]) # cx, cy
        return cx, cy
    return 160, 120

#阈值
r_threshold = (24, 39, 10, 59, 2, 31)

while(True):
        img = sensor.snapshot() # Take a picture and return the image.
        x = 160
        y = 120
        x,y =  color_blob(r_threshold)
        print(cx,cy)
        
