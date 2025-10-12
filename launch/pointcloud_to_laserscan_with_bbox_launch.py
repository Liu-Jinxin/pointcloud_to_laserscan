from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.descriptions import ComposableNode
from launch_ros.actions import ComposableNodeContainer


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            name='scanner', default_value='scanner',
            description='Namespace for sample topics'
        ),
        # Use ComposableNodeContainer with MultiThreadedExecutor for better performance
        ComposableNodeContainer(
            name='pointcloud_container',
            namespace='',
            package='rclcpp_components',
            executable='component_container_mt',  # Multi-threaded container
            composable_node_descriptions=[
                ComposableNode(
                    package='pointcloud_to_laserscan',
                    plugin='pointcloud_to_laserscan::PointCloudToLaserScanNode',
                    name='pointcloud_to_laserscan',
                    remappings=[
                        ('cloud_in', '/lidar_points'),
                        ('scan', '/scan')
                    ],
                    parameters=[{
                        'target_frame': 'hesai_lidar',
                        'transform_tolerance': 0.01,
                        'min_height': -0.8,
                        'max_height': 1.0,
                        'angle_min': -3.14159,  # -M_PI
                        'angle_max': 3.14159,  # M_PI
                        'angle_increment': 0.003141592,
                        'scan_time': 0.3333,
                        'range_min': 0.45,
                        'range_max': 40.0,
                        'use_inf': True,
                        'inf_epsilon': 1.0,
                        # Bounding box filter parameters to filter out robot body/parts
                        'use_bounding_box_filter': True,
                        'bbox_min_x': -0.2,  # Filter out points inside this box
                        'bbox_max_x': 3.0,   # Adjust these values based on your robot size
                        'bbox_min_y': -0.9,
                        'bbox_max_y': 0.9,
                        'bbox_min_z': -1.0,
                        'bbox_max_z': 0.5
                    }],
                    extra_arguments=[{'use_intra_process_comms': True}]
                )
            ],
            output='both'
        )
    ])
