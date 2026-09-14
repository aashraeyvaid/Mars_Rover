from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    package_dir = get_package_share_directory(
        'mars_rover_description'
    )

    world_file = os.path.join(
        package_dir,
        'models',
        'basic_rover_test.sdf'
    )

    return LaunchDescription([

        # =====================================================
        # GAZEBO
        # =====================================================

        ExecuteProcess(
            cmd=[
                'gz', 'sim',
                '-r',
                world_file
            ],
            output='screen'
        ),

        # =====================================================
        # CAMERA BRIDGE
        # =====================================================

        ExecuteProcess(
            cmd=[
                'ros2', 'run',
                'ros_gz_bridge',
                'parameter_bridge',
                '/camera@sensor_msgs/msg/Image[ignition.msgs.Image',
                '--ros-args',
                '-r',
                '/camera:=/camera/image_raw'
            ],
            output='screen'
        ),

        # =====================================================
        # CMD_VEL BRIDGE
        # =====================================================

        ExecuteProcess(
            cmd=[
                'ros2', 'run',
                'ros_gz_bridge',
                'parameter_bridge',
                '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist'
            ],
            output='screen'
        ),

        # =====================================================
        # LIDAR BRIDGE
        # =====================================================

        ExecuteProcess(
            cmd=[
                'ros2', 'run',
                'ros_gz_bridge',
                'parameter_bridge',
                '/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan'
            ],
            output='screen'
        ),

    ])