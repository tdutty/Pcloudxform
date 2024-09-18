import open3d as o3d

def smooth_mesh(mesh, method="laplacian", num_iterations=10):
    if method == "laplacian":
        mesh = mesh.filter_smooth_simple(number_of_iterations=num_iterations)
    elif method == "bilateral":
        mesh = mesh.filter_smooth_taubin(number_of_iterations=num_iterations)
    else:
        raise ValueError(f"Unsupported smoothing method: {method}")
    return mesh

def decimate_mesh(mesh, target_triangle_count=1000):
    mesh = mesh.simplify_quadric_decimation(target_number_of_triangles=target_triangle_count)
    return mesh

def remesh(mesh, method="isotropic"):
    if method == "isotropic":
        mesh = mesh.compute_vertex_normals()
        mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(mesh, 0.1)
    else:
        raise ValueError(f"Unsupported remeshing method: {method}")
    return mesh
