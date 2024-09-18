import open3d as o3d

def visualize_point_cloud(pcd):
    o3d.visualization.draw_geometries([pcd])

def visualize_mesh(mesh):
    o3d.visualization.draw_geometries([mesh])

def export_mesh(mesh, file_path):
    o3d.io.write_triangle_mesh(file_path, mesh)

def export_point_cloud(pcd, file_path):
    o3d.io.write_point_cloud(file_path, pcd)
