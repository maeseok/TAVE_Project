# 필요한 라이브러리 임포트
import cv2
from mtcnn.mtcnn import MTCNN
import matplotlib.pyplot as plt

# 이미지 로드
image_path = '이미지 위치'
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
if image is None:
    print("이미지를 로드할 수 없습니다.")

# MTCNN 모델 인스턴스 생성
detector = MTCNN()

# 얼굴 및 랜드마크 검출
faces = detector.detect_faces(image_rgb)

# 검출 결과 시각화
for face in faces:
    x, y, width, height = face['box']
    keypoints = face['keypoints']

    # 얼굴에 대한 상자 그리기
    cv2.rectangle(image_rgb, (x, y), (x+width, y+height), (255, 255, 255), 2)

    # 눈에 대한 상자 그리기 (빨간색)
    left_eye = keypoints['left_eye']
    right_eye = keypoints['right_eye']
    eye_width = right_eye[0] - left_eye[0]
    eye_height = right_eye[1] - left_eye[1]

    # 가로 길이가 세로 길이보다 크면 세로 길이를 가로 길이의 1/2로 설정
    if eye_width > eye_height:
        eye_height = eye_width // 2
    # 세로 길이가 가로 길이보다 크면 가로 길이를 세로 길이의 2배로 설정
    else:
        eye_width = eye_height * 2

    cv2.rectangle(image_rgb, (left_eye[0] - eye_width//2, left_eye[1] - eye_height//2), (right_eye[0] + eye_width//2, right_eye[1] + eye_height//2), (255, 0, 0), 2)
    
    # 코에 대한 상자 그리기 (초록색)
    nose = keypoints['nose']
    nose_width = nose[0] - left_eye[0]
    nose_height = right_eye[1] - nose[1]
    cv2.rectangle(image_rgb, (nose[0] - nose_width//2, nose[1] - nose_height//2), (nose[0] + nose_width//2, nose[1] + nose_height//2), (0, 255, 0), 2)
    
    # 입에 대한 상자 그리기 (파란색)
    mouth_left = keypoints['mouth_left']
    mouth_right = keypoints['mouth_right']
    mouth_width = mouth_right[0] - mouth_left[0]
    mouth_height = mouth_right[1] - mouth_left[1]

    # 가로 길이가 세로 길이보다 크면 세로 길이를 가로 길이의 1/2로 설정
    if mouth_width > mouth_height:
        mouth_height = mouth_width // 2
    # 세로 길이가 가로 길이보다 크면 가로 길이를 세로 길이의 2배로 설정
    else:
        mouth_width = mouth_height * 2

    cv2.rectangle(image_rgb, (mouth_left[0] - mouth_width//2, mouth_left[1] - mouth_height//2), (mouth_right[0] + mouth_width//2, mouth_right[1] + mouth_height//2), (0, 0, 255), 2)


# 결과 이미지 출력
plt.imshow(image_rgb)
plt.axis('off')
plt.show()