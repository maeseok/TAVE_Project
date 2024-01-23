import json
import torch
from PIL import Image
from transformers import ViTForImageClassification, ViTFeatureExtractor

# 모델 저장 디렉토리 경로 설정 (이전에 저장한 경로와 일치해야 함)
model_path = ".\\ViT_image_classification_model.pth"

# 저장한 모델 상태 사전 불러오기
model_state_dict = torch.load(model_path, map_location=torch.device('cpu'))

# 모델 정의 (ViTForImageClassification)
model = ViTForImageClassification.from_pretrained("google/vit-base-patch16-224-in21k", num_labels=235)
model.load_state_dict(model_state_dict)

# JSON 파일에서 클래스 레이블 정보 불러오기
class_labels_path = ".\\class_labels.json"
with open(class_labels_path, "r", encoding="utf-8") as json_file:
    class_labels = json.load(json_file)

def model_serving_function(image_url: str):
    image_path = image_url
    # 이미지 로드
    image = Image.open(image_path).convert("RGB")

    # 이미지 전처리
    feature_extractor = ViTFeatureExtractor.from_pretrained("google/vit-base-patch16-224-in21k")
    inputs = feature_extractor(images=image, return_tensors="pt")
    input_data = inputs  # 모델을 CPU로 이동한 후 입력 데이터 생성

    # 모델을 사용하여 예측 수행
    with torch.no_grad():
        outputs = model(**input_data)
        logits = outputs.logits

    # 상위 3개 클래스 예측
    top_k = 3
    probabilities, class_indices = torch.topk(logits, top_k, dim=1)
    class_probabilities = torch.nn.functional.softmax(probabilities, dim=1)[0] * 100.0

    predicted_classes = []

    # 예측 결과 출력
    for i in range(top_k):
        class_idx = class_indices[0, i].item()
        class_probability = class_probabilities[i].item()
        class_name = class_labels[str(class_idx)]
        predicted_classes.append(class_name)

    return predicted_classes
