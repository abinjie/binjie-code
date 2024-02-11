import sensor, image, pyb, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(10)
red_thresholds = [(0, 100, 40, 80, 30, 140)]
green_thresholds = [(0, 100, -70, -50, 20, 70)]
yellow_thresholds = [(0, 100, -40, -10, 60, 105)]
blue_thresholds = [(0, 100, 0, 63, -127, 50)]
def mmain():
    img = sensor.snapshot()
    for blob11 in img.find_blobs(red_thresholds, pixels_threshold=20, area_threshold=20,merge=True):
        left_roi = [blob11.x(), blob11.y(), blob11.x()+blob11.w(), blob11.y()+blob11.h()]
        for blob12 in img.find_blobs(green_thresholds,roi=left_roi, pixels_threshold=10, area_threshold=10,merge=True):
            img.draw_rectangle(blob11.rect())
            img.draw_string(blob11.x(),blob11.y(), "true red")
            print("true red")
            return

        for blob12 in img.find_blobs(yellow_thresholds,roi=left_roi, pixels_threshold=10, area_threshold=10,merge=True):
            img.draw_rectangle(blob11.rect())
            print("false red")
            img.draw_string(blob11.x(),blob11.y(), "false red")
            return

        #img.draw_rectangle(blob.rect())
        #img.draw_cross(blob.cx(), blob.cy())
        #print(blob.code())

    for blob21 in img.find_blobs(blue_thresholds, pixels_threshold=20, area_threshold=20,merge=True):
        left_roi = [blob21.x(), blob21.y(), blob21.x()+blob21.w(), blob21.y()+blob21.h()]
        for blob22 in img.find_blobs(yellow_thresholds,roi=left_roi, pixels_threshold=10, area_threshold=10,merge=True):
            img.draw_rectangle(blob21.rect())
            print("true blue")
            img.draw_string(blob21.x(),blob21.y(), "true blue")
        for blob22 in img.find_blobs(green_thresholds,roi=left_roi, pixels_threshold=10, area_threshold=10,merge=True):
            img.draw_rectangle(blob21.rect())
            print("false blue")
            img.draw_string(blob21.x(),blob21.y(), "false blue")
        #img.draw_rectangle(blob.rect())
        #img.draw_cross(blob.cx(), blob.cy())
        #print(blob.code())

while True:
    mmain()
