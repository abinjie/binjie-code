# 蓝队
import sensor,image,time

# 设置摄像头的分辨率和帧率
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((320,240))
sensor.set_framerate(60)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # 关闭曝光
sensor.set_auto_whitebal(False) # 关闭白平衡
clock = time.clock()

# 定义颜色阈值
red_threshold = (23, 60, 52, 77, 14, 77)
blue_threshold = (24, 51, 6, 34, -75, -46)
yellow_threshold = (75, 87, -29, -6, 45, 127)
green_threshold = (25, 45, -68, -13, -3, 30)

# 初始化图像中心点
img_center_x = sensor.width() // 2
img_center_y = sensor.height() // 2

while(True):
    clock.tick() # 计时开始
    img = sensor.snapshot().lens_corr(1.8) # 获取当前图像,矫正摄像头畸变

    # 查找各色色块
    red_blobs = img.find_blobs([red_threshold])
    blue_blobs = img.find_blobs([blue_threshold])
    yellow_blobs = img.find_blobs([yellow_threshold])
    green_blobs = img.find_blobs([green_threshold])

    if blue_blobs:
        for blob in blue_blobs:
            max_blue_blob = max(blue_blobs,key=lambda b_b:b_b.pixels()) # 找到最大蓝色色块
            # 在图像中画出最大蓝色色块的矩形框和中心点
            img.draw_rectangle(max_blue_blob.rect())

        # 识别黄色色块
        if yellow_blobs:
            print("真宝藏")
            for blob in yellow_blobs:
                max_yellow_blob = max(yellow_blobs,key=lambda y_b:y_b.pixels()) # 找到最大黄色色块
                img.draw_rectangle(max_yellow_blob.rect())

                # 获取矩形框的位置和大小
                x, y, w, h = max_yellow_blob.rect()
                # 计算矩形框的中心坐标
                cx = x + w // 2
                cy = y + h // 2
                img.draw_cross(max_yellow_blob.cx(), max_yellow_blob.cy()) # cx, cy

                # 计算圆形区域中心点与图像中心点之间的距离
                dx = max_yellow_blob.cx() - img_center_x
                dy = img_center_y - max_yellow_blob.cy()
                # 调整舵机角度
                if dx < -30:
                    print("Turn left")
                elif dx > 30:
                    print("Turn right")
                else:
                    print("Go stight")

        #识别绿色色块并避障
        if green_blobs:
            print("伪宝藏")
            for blob in green_blobs:
                max_green_blob = max(green_blobs,key=lambda g_b:g_b.pixels()) # 找到最大绿色色块
                img.draw_rectangle(max_green_blob.rect())# 在图像中画出最大绿色色块的矩形框
                # 获取矩形框的位置和大小
                x, y, w, h = max_green_blob.rect()
                # 计算矩形框的中心坐标
                cx = x + w // 2
                cy = y + h // 2
                img.draw_cross(max_green_blob.cx(), max_green_blob.cy()) # cx, cy

                # 计算圆形区域中心点与图像中心点之间的距离
                dx = max_green_blob.cx() - img_center_x
                dy = img_center_y - max_green_blob.cy()

                # 调整舵机角度
                if dx < -30:
                    print("Turn right")
                elif dx > 30:
                    print("Turn left")
                else:
                    print("Go left")
