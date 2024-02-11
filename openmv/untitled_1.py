import sensor, image, time


yellow_threshold   = (0, 70, 22, 127, -128, 127)
red  =(21, 46, 14, 54, -2, 39)

import sensor, image, time

sensor.reset() # 初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 格式为 RGB565.
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(10) # 跳过10帧，使新设置生效
sensor.set_auto_whitebal(False)               # Create a clock object to track the FPS.
clock = time.clock() # Tracks FPS.

K=2800

while(True):
    clock.tick()
    img = sensor.snapshot().lens_corr(1.5) # 获取当前图像,矫正摄像头畸变

    img = sensor.snapshot()

    blobs = img.find_blobs([yellow_threshold],red)
    if len(blobs) == 1:
        # Draw a rect around the blob.
        b = blobs[0]
        img.draw_rectangle(b[0:4]) # rect
        img.draw_cross(b[5], b[6]) # cx, cy
        Lm = (b[2]+b[3])/2
        length = K/Lm
        print(length)


