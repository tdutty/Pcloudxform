import open3d as o3d
import laspy
import multiprocessing as mp
import numpy as np
import os

def load_point_cloud(file_path):
    if file_path.endswith(".ply") or file_path.endswith(".pcd") or file_path.endswith(".xyz"):
        pcd = o3d.io.read_point_cloud(file_path)
    elif file_path.endswith(".las"):
        pcd = load_las_file(file_path)
    elif file_path.endswith(".e57"):
        raise NotImplementedError("E57 format is not yet supported, but can be added.")
    elif file_path.endswith(".bin"):
        pcd = load_bin_file(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_path}")
    return pcd

def load_las_file(file_path):
    las = laspy.read(file_path)
    points = np.vstack([las.x, las.y, las.z]).transpose()
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    return pcd

def load_bin_file(file_path):
    points = np.fromfile(file_path, dtype=np.float32).reshape(-1, 4)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points[:, :3])
    return pcd

def multi_process_load(file_paths):
    with mp.Pool(mp.cpu_count()) as pool:
        point_clouds = pool.map(load_point_cloud, file_paths)
    return point_clouds
