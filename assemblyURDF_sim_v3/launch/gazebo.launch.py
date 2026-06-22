from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

```
package_name = "assemblyURDF_sim_v3"

urdf_path = os.path.join(
    get_package_share_directory(package_name),
    "urdf",
    "assemblyURDF_sim_v3.urdf"
)

world = "empty.sdf"

return LaunchDescription([

    # Start Gazebo Harmonic
    ExecuteProcess(
        cmd=[
            "gz",
            "sim",
            "-r",
            world
        ],
        output="screen"
    ),

    # Publish robot state
    Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[
            {
                "robot_description":
                open(urdf_path).read()
            }
        ],
        output="screen"
    ),

    # Spawn robot into Gazebo
    Node(
        package="ros_gz_sim",
        executable="create",
        arguments=[
            "-name",
            "assemblyURDF_sim_v3",
            "-file",
            urdf_path
        ],
        output="screen"
    )

])
```
