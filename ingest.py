import open3d as o3d
import laspy
import numpy as np

def load_point_cloud(file_path):
    if file_path.endswith(".ply") or file_path.endswith(".pcd") or file_path.endswith(".xyz"):
        pcd = o3d.io.read_point_cloud(file_path)
    elif file_path.endswith(".las"):
        pcd = load_las_file(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_path}")
    return pcd

def load_las_file(file_path):
    las = laspy.read(file_path)
    points = np.vstack([las.x, las.y, las.z]).transpose()
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    return pcd
