import open3d as o3d
import cupy as cp

def point_cloud_to_mesh_poisson(pcd, depth=9):
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
    mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=depth)
    return mesh

def point_cloud_to_mesh_cuda(pcd):
    points = cp.asarray(pcd.points)
    normals = cp.asarray(pcd.normals)
    mesh = cp.poisson_surface_reconstruction(points, normals)
    return mesh
