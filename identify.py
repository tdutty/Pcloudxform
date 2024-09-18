import numpy as np
import open3d as o3d
from sklearn.cluster import DBSCAN, KMeans
from deep_learning_models.pointnetpp import PointNetPP
from deep_learning_models.minkowski import MinkowskiNet

pointnetpp_model = PointNetPP(weights="path_to_pointnetpp_weights.h5")
minkowski_model = MinkowskiNet(weights="path_to_minkowski_weights.pth")

def identify_objects(pcd, method="pointnetpp"):
    points = np.asarray(pcd.points)
    if method == "pointnetpp":
        predictions = pointnetpp_model.predict(points)
    elif method == "minkowski":
        predictions = minkowski_model.predict(points)
    else:
        raise ValueError(f"Unsupported method: {method}")
    return predictions

def identify_clusters(pcd, method="dbscan", n_clusters=10):
    points = np.asarray(pcd.points)
    if method == "dbscan":
        clustering = DBSCAN(eps=0.05, min_samples=10).fit(points)
    elif method == "kmeans":
        clustering = KMeans(n_clusters=n_clusters).fit(points)
    else:
        raise ValueError(f"Unsupported clustering method: {method}")
    labels = clustering.labels_
    unique_labels = np.unique(labels)
    clusters = [np.where(labels == label)[0] for label in unique_labels if label != -1]
    return clusters
