import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from tensorflow.keras.layers import Input, Dense, Flatten, Reshape
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras import backend as K
import shutil

def load_images_from_folder(folder):
    images = []
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        if not filename.lower().endswith(tuple(allowed_extensions)):
            continue

        try:
            img = load_img(file_path, target_size=(224, 224))
            img_array = img_to_array(img) / 255.0
            images.append(img_array)
        except Exception as e:
            print(f"Error loading image {file_path}: {e}")

    return np.array(images)

def cluster_and_save(folder_path, cluster_0_folder, cluster_1_folder):
    images = load_images_from_folder(folder_path)

    model = VGG16(weights='imagenet', include_top=False)
    features = model.predict(images)

    features = features.reshape(features.shape[0], -1)
    kmeans = KMeans(n_clusters=2, random_state=42).fit(features)
    labels = kmeans.labels_

    os.makedirs(cluster_0_folder, exist_ok=True)
    os.makedirs(cluster_1_folder, exist_ok=True)

    save_images_by_cluster(images, labels, cluster_0_folder, cluster_1_folder)

def save_images_by_cluster(images, labels, cluster_folder_0, cluster_folder_1):
    for idx, (image, label) in enumerate(zip(images, labels)):
        image_folder = cluster_folder_0 if label == 0 else cluster_folder_1
        image_path = os.path.join(image_folder, f'image_{idx}.png')

        img = array_to_img(image, scale=True)
        img.save(image_path)

#이 부분 시작 ======================================
def cluster_and_save_all_folders(List):
    for i in List:
        folder_path = "./여자배우/"+i+"_수정본/"  #이 부분 경로 수정 필요
        if os.path.isdir(folder_path):
            cluster_0_folder = folder_path+f'{i}_cluster_0'
            cluster_1_folder = folder_path+f'{i}_cluster_1'
            cluster_and_save(folder_path, cluster_0_folder, cluster_1_folder)
            print("success "+i)
        
f = open("./여자배우/여자배우.txt", 'r',encoding="utf-8") #이 부분 경로 수정 필요
lines = f.readlines()
data=[]
List=[]
for i in lines:
    data.append(i.strip())
print(len(data))
for i in data:
    if not i=="":
        if os.path.isdir(f"./여자배우/{i}_수정본"): #이 부분 경로 수정 필요
            List.append(i)
List.sort() #존재하는 배우 리스트 추출하여 정렬
cluster_and_save_all_folders(List)