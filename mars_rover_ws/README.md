# Mars Rover Simulation — ROS 2 & Gazebo

A simulated Mars rover built using **ROS 2 Jazzy** and **Gazebo Sim 8**. The rover supports:

* Differential-drive teleoperation
* Camera sensor
* 2D LiDAR sensor
* ROS 2 ↔ Gazebo communication using `ros_gz_bridge`
* RViz2 visualization

## Tech Stack

* Ubuntu 24.04
* ROS 2 Jazzy
* Gazebo Sim 8
* Python
* SDF
* RViz2
* `ros_gz_bridge`

---

# 1. Clone the Repository

Clone the repository:

```bash
git clone https://github.com/aashraeyvaid/Mars_Rover/tree/main.git
cd Mars_Rover
```

Copy the package into your ROS 2 workspace:

```bash
mkdir -p ~/mars_rover_ws/src
cp -r mars_rover_description ~/mars_rover_ws/src/
```

Build the workspace:

```bash
cd ~/mars_rover_ws
colcon build --symlink-install
```

Source the workspace:

```bash
source install/setup.bash
```

---

# 2. Run the Project — Manual Method

This method starts Gazebo first and then manually connects each sensor/topic to ROS 2.

## Step 1 — Start Gazebo

```bash
cd ~/mars_rover_ws/src/mars_rover_description/models
gz sim -r basic_rover_test.sdf
```

---

## Step 2 — Start Camera Bridge

Open a **new terminal**:

```bash
source /opt/ros/jazzy/setup.bash
source ~/mars_rover_ws/install/setup.bash
```

Run:

```bash
ros2 run ros_gz_bridge parameter_bridge /camera@sensor_msgs/msg/Image[ignition.msgs.Image --ros-args -r /camera:=/camera/image_raw
```

The camera image is now available on:

```text
/camera/image_raw
```

---

## Step 3 — Start `/cmd_vel` Bridge

Open another terminal:

```bash
source /opt/ros/jazzy/setup.bash
source ~/mars_rover_ws/install/setup.bash
```

Run:

```bash
ros2 run ros_gz_bridge parameter_bridge /cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist
```

---

## Step 4 — Start LiDAR Bridge

Open another terminal:

```bash
source /opt/ros/jazzy/setup.bash
source ~/mars_rover_ws/install/setup.bash
```

Run:

```bash
ros2 run ros_gz_bridge parameter_bridge /scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan
```

LiDAR data is now available on:

```text
/scan
```

---

## Step 5 — Control the Rover

Open another terminal:

```bash
source /opt/ros/jazzy/setup.bash
source ~/mars_rover_ws/install/setup.bash
```

Run:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Use the keyboard controls shown in the terminal to move the rover.

---

## Step 6 — Visualize LiDAR in RViz2

Open another terminal:

```bash
source /opt/ros/jazzy/setup.bash
source ~/mars_rover_ws/install/setup.bash
```

Run:

```bash
rviz2
```

In RViz2:

1. Set the **Fixed Frame** -- **basic_rover/lidar_link/lidar_sensor**.
2. Add a **LaserScan** display.
3. Set the topic to:

```text
/scan
```

The rover's LiDAR scan should now be visible.

---

# 3. Run the Project — Launch File Method

The project also provides a launch file that starts Gazebo and all required ROS-Gazebo bridges automatically.

Build the workspace if required:

```bash
cd ~/mars_rover_ws
colcon build --symlink-install
source install/setup.bash
```

Run:

```bash
ros2 launch mars_rover_description basic_rover.launch.py
```

This automatically starts:

* Gazebo
* Camera bridge
* `/cmd_vel` bridge
* LiDAR bridge

You only need to open **RViz2** manually:

```bash
rviz2
```

And for keyboard control:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

---

# 4. ROS Topics

| Function         | Topic               | Type                        |
| ---------------- | ------------------- | --------------------------- |
| Velocity command | `/cmd_vel`          | `geometry_msgs/msg/Twist`   |
| Camera           | `/camera/image_raw` | `sensor_msgs/msg/Image`     |
| LiDAR            | `/scan`             | `sensor_msgs/msg/LaserScan` |

---

# 5. Project Structure

```text
mars_rover_description/
├── launch/
│   └── basic_rover.launch.py
│
├── models/
│   ├── basic_rover/
│   │   ├── model.config
│   │   └── basic_rover.sdf
│   │
│   ├── ground_plane/
│   │   ├── model.config
│   │   └── my_ground_plane.sdf
│   │
│   └── basic_rover_test.sdf
│
├── resource/
│   └── mars_rover_description
│
├── package.xml
├── setup.py
└── README.md
```

---

## 6. Quick Start

After cloning and building the workspace:

```bash
cd ~/mars_rover_ws
source install/setup.bash
ros2 launch mars_rover_description basic_rover.launch.py
```

Then, in separate terminals:

```bash
rviz2
```

and:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

The rover is ready to drive, visualize LiDAR, and access the camera.

