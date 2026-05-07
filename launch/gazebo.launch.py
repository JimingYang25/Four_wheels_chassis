import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    pkg_gazebo_ros = FindPackageShare('gazebo_ros').find('gazebo_ros')
    pkg_share = FindPackageShare('four_wheels_chassis').find('four_wheels_chassis')
    urdf_path = os.path.join(pkg_share, 'urdf', 'four_wheels_chassis.urdf')

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py')
        )
    )

    
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'four_wheels_chassis', '-file', urdf_path],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        spawn_entity,
    ])