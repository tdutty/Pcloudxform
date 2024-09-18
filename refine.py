import open3d as o3d

def smooth_mesh(mesh, num_iterations=10):
    mesh = mesh.filter_smooth_simple(number_of_iterations=num_iterations)
    return mesh

def decimate_mesh(mesh, target_triangle_count):
    mesh = mesh.simplify_quadric_decimation(target_number_of_triangles=target_triangle_count)
    return mesh
