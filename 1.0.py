from maix import camera, display, image
camera.config(size=(640, 360))
while True:
    img = camera.capture()
    display.show(img)
