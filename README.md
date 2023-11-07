# open-gimbal
An open-source gimbal implementation using PX4 autopilot and the ARK cannode

## Setting up the repository and its submodules

Clone this repository:

```bash
git clone git@github.com:bmelanman/open-gimbal.git && cd open-gimbal
```

Initialize its submodules and make sure everything is up-to-date:

```bash
git submodule update --init --recursive && git pull --recurse-submodules
```

Fetch the tags from the main PX4 branch (necessary for building):

```bash
git -C ./PX4-Autopilot/ fetch --tags upstream
```

## Setting up PX4-Autopilot

#### Note: Ubuntu 20.04 LTS is high recommended for the following process. Alternative setup instructions can be found in [PX4's Documentation](https://docs.px4.io/v1.13/en/dev_setup/dev_env).

### Run the PX4-Autopilot setup script:

```bash
bash ./PX4-Autopilot/Tools/setup/ubuntu.sh
```

* Acknowledge any prompts as the script progresses.
* You can use the `--no-nuttx` and `--no-sim-tools` options to omit the NuttX and/or simulation tools.

#### Note : You must restart the computer before the next step!

## Setting up ROS Noetic

Add packages.ros.org to `sources.list` along with its keys:

```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

Install ROS Noetic:

```bash
sudo apt update && sudo apt install -y ros-noetic-ros-base
```

(Optional) Add the setup script to `~/.bashrc`:

```bash
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc && source ~/.bashrc
```
