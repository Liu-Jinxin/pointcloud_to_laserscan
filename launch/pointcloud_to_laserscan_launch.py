# filepath: /home/jinxin/Desktop/Mobile_manipulator/src/pointcloud_to_laserscan/launch/pointcloud_to_laserscan_launch.py
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
            remappings=[('cloud_in',  ['/cloud_registered_body']),
                        ('scan',  ['/scan'])],
            parameters=[{
                'target_frame': 'body',
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
                'inf_epsilon': 1.0
            }],
            name='pointcloud_to_laserscan'
        )
    ])