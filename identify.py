import numpy as np
import open3d as o3d
from sklearn.cluster import DBSCAN
from tensorflow.keras.models import load_model

pointnet_model = load_model("path_to_pretrained_pointnet_model.h5")

def identify_objects(pcd):
    points = np.asarray(pcd.points)
    predictions = pointnet_model.predict(points)
    return predictions

def identify_clusters(pcd, eps=0.05, min_points=10):
    points = np.asarray(pcd.points)
    clustering = DBSCAN(eps=eps, min_samples=min_points).fit(points)
    labels = clustering.labels_
    unique_labels = np.unique(labels)
    clusters = [np.where(labels == label)[0] for label in unique_labels if label != -1]
    return clusters
