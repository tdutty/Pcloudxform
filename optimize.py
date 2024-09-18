import open3d as o3d
import numpy as np

def icp_registration(source_pcd, target_pcd, threshold=0.02, init_transformation=np.eye(4)):
    reg_p2p = o3d.pipelines.registration.registration_icp(
        source_pcd, target_pcd, threshold, init_transformation,
        o3d.pipelines.registration.TransformationEstimationPointToPoint())
    return reg_p2p.transformation

def global_registration(source_pcd, target_pcd, voxel_size=0.05):
    source_down = source_pcd.voxel_down_sample(voxel_size)
    target_down = target_pcd.voxel_down_sample(voxel_size)
    reg_fgr = o3d.pipelines.registration.registration_fgr_based_on_feature_matching(
        source_down, target_down, voxel_size,
        o3d.pipelines.registration.FastGlobalRegistrationOption())
    return reg_fgr.transformation

def denoise_point_cloud(pcd, nb_neighbors=20, std_ratio=2.0):
    cl, ind = pcd.remove_statistical_outlier(nb_neighbors=nb_neighbors, std_ratio=std_ratio)
    return pcd.select_by_index(ind)
