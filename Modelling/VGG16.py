import os
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 이미지를 시각화하기 위한 함수
def display_image(image_path, title):
    try:
        image = Image.open(image_path)
        plt.imshow(image)
        plt.title(title)
        plt.axis('off')
        plt.show()
    except Exception as e:
        print(f"Error displaying image: {e}")

# 대상 이미지
target_image_path = '타겟 이미지(웹툰)'

# 이미지 폴더 경로
image_folder_path = '폴더위치'

# 이미지 폴더 내의 모든 이미지 파일 경로 가져오기
image_paths = [os.path.join(image_folder_path, file) for file in os.listdir(image_folder_path) if file.lower().endswith(('.jpg', '.jpeg', '.png'))]

# VGG16 모델 불러오기
vgg16_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# 대상 이미지 특성 추출
target_image = load_img(target_image_path, target_size=(224, 224))
target_array = img_to_array(target_image)
target_array = np.expand_dims(target_array, axis=0)
target_array = preprocess_input(target_array / 255.0)
target_features = vgg16_model.predict(target_array)

# 각 이미지에 대한 유사성 계산 및 최소 유사성 이미지 찾기
min_similarity = float('inf')
most_similar_image_path = ''

for image_path in image_paths:
    try:
        # 후보 이미지 특성 추출
        candidate_image = load_img(image_path, target_size=(224, 224))
        candidate_array = img_to_array(candidate_image)
        candidate_array = np.expand_dims(candidate_array, axis=0)
        candidate_array = preprocess_input(candidate_array / 255.0)
        candidate_features = vgg16_model.predict(candidate_array)

        # 다양한 유사성 측정 방법 시도
        mse = np.mean(np.square(target_features - candidate_features))
        ssim = 1 / (1 + np.mean(np.abs(target_features - candidate_features)))
        similarity = 0.5 * mse + 0.5 * ssim  # Mean Squared Error와 SSIM의 가중 평균

        # 최소 유사성 업데이트
        if similarity < min_similarity:
            min_similarity = similarity
            most_similar_image_path = image_path

    except Exception as e:
        print(f"Error processing image {image_path}: {e}")

# 결과 출력
print(f"Most Similar Image: {most_similar_image_path} with similarity {min_similarity}")

# 대상 이미지 시각화
display_image(target_image_path, 'Target Image')

# 가장 흡사한 이미지 후보 시각화
display_image(most_similar_image_path, 'Most Similar Candidate Image')