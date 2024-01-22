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
from tensorflow.keras.preprocessing.image import array_to_img
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

        img = array_to_img(image, scale=False)
        img.save(image_path)

def cluster_and_save_all_folders(root_folder):
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            cluster_0_folder = f'{folder_name}_cluster_0'
            cluster_1_folder = f'{folder_name}_cluster_1'
            cluster_and_save(folder_path, cluster_0_folder, cluster_1_folder)

cluster_and_save_all_folders('./여자배우')