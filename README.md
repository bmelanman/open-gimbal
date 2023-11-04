# open-gimbal
An open-source gimbal implementation using PX4 autopilot and the ARK cannode

## Command to clone this repo along with its submodules

```bash
git clone git@github.com:bmelanman/open-gimbal.git --recursive
```

## Commands to setup PX4-Autopilot

#### Note: Ubuntu 18.04 LTS is required for the following process. Alternative setup instructions can be found in [PX4's Documentation](https://docs.px4.io/v1.13/en/dev_setup/dev_env).

### Run the PX4-Autopilot setup script:

```bash
bash ./PX4-Autopilot/Tools/setup/ubuntu.sh
```

* Acknowledge any prompts as the script progress.
* You can use the `--no-nuttx` and `--no-sim-tools` options to omit the NuttX and/or simulation tools.

#### Note : You must restart the computer before the next step!

### Download the ROS1 script installer:

```bash
wget https://raw.githubusercontent.com/PX4/Devguide/master/build_scripts/ubuntu_sim_ros_melodic.sh
```

### Run the script:

```bash
bash ubuntu_sim_ros_melodic.sh
```

Some Notes:
* You may need to acknowledge some prompts as the script progresses.
* ROS Melodic is installed with Gazebo9 by default.
* Your catkin (ROS build system) workspace is created at ~/catkin_ws/.
* The script uses instructions from the [ROS Wiki "Melodic" Ubuntu page](http://wiki.ros.org/melodic/Installation/Ubuntu).
