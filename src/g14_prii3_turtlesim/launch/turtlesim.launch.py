from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    turtlesim_node = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtlesim'
    )

    control_node = Node(
        package='g14_prii3_turtlesim',
        executable='control_turtle',
        name='turtle_controller'
    )

    return LaunchDescription([
        turtlesim_node,
        control_node
    ])