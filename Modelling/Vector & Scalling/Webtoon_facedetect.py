import os
import cv2
from google.colab.patches import cv2_imshow
import dlib
import tensorflow as tf
import numpy as np
import time

# 얼굴 감지 및 랜드마크 예측을 위한 Dlib 초기화
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("/content/drive/MyDrive/웹툰 캐릭터/shape_predictor_68_face_landmarks.dat")  # 랜드마크 예측 모델 경로

# TensorFlow 얼굴 특징 벡터 추출을 위한 모델 초기화
model = tf.keras.applications.InceptionResNetV2(weights='imagenet', include_top=False, pooling='avg')

def extract_features_from_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', 'webp')):
                image_path = os.path.join(root, file)
                process_image(image_path)

def process_image(image_path):
    # 이미지 읽어오기
    image = cv2.imread(image_path)

    # 이미지가 제대로 읽혔는지 확인
    if image is None:
        print(f"Error reading the image: {image_path}")
        return

    # 얼굴 감지
    faces = detector(image, upsample_num_times=1)

    # 얼굴이 감지되지 않은 경우
    if len(faces) == 0:
        print(f"No face detected in {image_path}")
        return

    for face in faces:
        # 얼굴 이미지 크기 조정
        face_img = image[face.top():face.bottom(), face.left():face.right()]
        if face_img.shape[0] == 0 or face_img.shape[1] == 0:
            print(f"Error: Empty face image in {image_path}")
            continue

        # 이미지 크기 조정
        resized_face = cv2.resize(face_img, (160, 160))

        # 네트워크 입력으로 사용할 데이터 전처리
        input_data = tf.keras.applications.inception_resnet_v2.preprocess_input(np.expand_dims(resized_face, axis=0))
        features = model.predict(input_data)

        # 얼굴 위치에 사각형 그리기
        cv2.rectangle(image, (face.left(), face.top()), (face.right(), face.bottom()), (255, 0, 0), 2)

        # 특징 벡터를 이미지에 텍스트로 표시
        text = "Features: " + " ".join(f"{val:.2f}" for val in features.flatten())
        cv2.putText(image, text, (face.left(), face.top() - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # 이미지 표시
    cv2_imshow(image)
    time.sleep(5)  # 이미지를 충분히 보기 위해 대기

# 폴더 내 이미지들에 대한 얼굴 특징 벡터 추출 및 표시
folder_path = "/content/drive/MyDrive/웹툰 캐릭터"
extract_features_from_folder(folder_path)