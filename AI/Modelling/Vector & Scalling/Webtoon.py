import os
import dlib
import numpy as np

# 얼굴 감지기와 특징점 예측기 로딩
detector = dlib.get_frontal_face_detector()
predictor_path = '/content/drive/MyDrive/웹툰 캐릭터/shape_predictor_68_face_landmarks.dat'
sp = dlib.shape_predictor(predictor_path)

def extract_landmarks(image_path):
    img = dlib.load_rgb_image(image_path)
    detections = detector(img, 1)

    if len(detections) == 0:
        print(f"No face detected in {image_path}")
        return None

    face_box = detections[0]
    face_img = img[face_box.top():face_box.bottom(), face_box.left():face_box.right()]

    shape = sp(img, face_box)
    landmarks = np.array([(shape.part(i).x - face_box.left(), shape.part(i).y - face_box.top()) for i in range(shape.num_parts)])

    return landmarks

def scale_landmarks(landmarks, scale_factor):
    # 31번 랜드마크를 (0, 0)으로 이동
    translation_vector = landmarks[30]  # 31번 랜드마크의 좌표를 기준으로 설정
    landmarks -= translation_vector

    # 스케일링 적용
    landmarks = landmarks * scale_factor

    # 데이터 타입을 명시적으로 지정 (float64)
    landmarks = landmarks.astype('float64')

    return landmarks

def process_images_in_folder(folder_path, scale_factor=1.0):
    all_scaled_landmarks = {}

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            # 파일이면 얼굴 특징점 추출
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                landmarks = extract_landmarks(file_path)

                if landmarks is not None:
                    # 31번 랜드마크를 기준으로 이동 및 스케일링
                    scaled_landmarks = scale_landmarks(landmarks, scale_factor)

                    # 결과 리스트에 추가
                    all_scaled_landmarks[filename] = scaled_landmarks.tolist()

    return all_scaled_landmarks
'''
def standardize_landmarks(landmarks): #스탠다드 스케일링 
    #Landmarks=StandardScaler(landmarks)
    # 각 차원(좌표)에 대해 평균 및 표준 편차 계산
    mean = np.mean(landmarks)
    std = np.std(landmarks)

    # 스탠다드 스케일링 적용
    Landmarks = (landmarks - mean) / std
    mean = np.mean(Landmarks)
    std = np.std(Landmarks)
    print(mean,std)
    return Landmarks

def skl_standard(landmarks): #스탠다드 스케일링 - skl_ver
  # StandardScaler 객체 생성
  standard_scaler = StandardScaler()

  # fit_transform()을 사용해서 학습과 스케일링을 한 번에 적용
  train_standard = standard_scaler.fit_transform(landmarks)
  return train_standard
'''


# 이미지 파일이 들어 있는 폴더 경로
image_folder = '/content/drive/MyDrive/웹툰 캐릭터/최종 캐릭터 사진'
all_scaled_landmarks = process_images_in_folder(image_folder)

# 각 이미지에 대한 스케일링된 랜드마크를 딕셔너리에 저장하고, 결과를 확인
for filename, scaled_landmarks in all_scaled_landmarks.items():
    print(f"Scaled Landmarks for {filename}:\n{scaled_landmarks}")