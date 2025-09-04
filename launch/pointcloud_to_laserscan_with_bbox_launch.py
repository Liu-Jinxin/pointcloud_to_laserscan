from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            name='scanner', default_value='scanner',
            description='Namespace for sample topics'
        ),
        Node(
            package='pointcloud_to_laserscan', executable='pointcloud_to_laserscan_node',
            remappings=[('cloud_in',  ['/lidar_points']),
                        ('scan',  ['/scan'])],
            parameters=[{
                'target_frame': 'hesai_lidar',
                'transform_tolerance': 0.01,
                'min_height': -0.4,
                'max_height': 1.0,
                'angle_min': -3.14159,  # -M_PI/2
                'angle_max': 3.14159,  # M_PI/2
                'angle_increment': 0.003141592,
                'scan_time': 0.3333,
                'range_min': 0.45,
                'range_max': 40.0,
                'use_inf': True,
                'inf_epsilon': 1.0,
                # Bounding box filter parameters to filter out robot body/parts
                'use_bounding_box_filter': True,
                'bbox_min_x': -0.2,  # Filter out points inside this box
                'bbox_max_x': 1.5,   # Adjust these values based on your robot size
                'bbox_min_y': -0.5,
                'bbox_max_y': 0.5,
                'bbox_min_z': -1.0,
                'bbox_max_z': 0.8
            }],
            name='pointcloud_to_laserscan'
        )
    ])
