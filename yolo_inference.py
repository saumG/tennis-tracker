from ultralytics import YOLO

model = YOLO('yolov8x')

result = model.predict('input_videos/federer-nadal.mp4', save = True)
print(result)
print("boxes: ")
for box in result[0].boxes:
    print(box)