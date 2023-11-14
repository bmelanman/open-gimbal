# open-gimbal
An open-source gimbal implementation using PX4 autopilot and the ARK cannode

### ⚠️ IMPORTANT:

Due to PX4's very strict installation process, Ubuntu 20.04 LTS is ___required___ for the following guide. 

These instructions can be followed loosely with the help of PX4's alternative setup instructions, which can be found [HERE](https://docs.px4.io/v1.13/en/dev_setup/dev_env).

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

### Run the PX4-Autopilot setup script:

```bash
bash ./PX4-Autopilot/Tools/setup/ubuntu.sh
```

* Acknowledge any prompts as the script progresses.
* You can use the `--no-nuttx` and `--no-sim-tools` options to omit the NuttX and/or simulation tools.

#### Note : You must restart the computer before the next step!

## Installing ROS Noetic

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

## Installing STLink

Install necessary libraries:

```bash
sudo apt install -y libusb-1.0 libusb-1.0-0-dev
```

Clone the STLink repo:

```bash
git clone https://github.com/stlink-org/stlink.git ~/stlink
cd ~/stlink
```

Build a debian package:

```bash
make clean package
```

Make sure `libstlink1` definitely isn't installed (it can mess everything up), and install the STLink package:

```bash
sudo apt remove --purge -y libstlink1 stlink
sudo dpkg -i ./build/dist/*.deb
```

Finally, copy over the device connection rules:

```bash
sudo cp config/udev/rules.d/* /etc/udev/rules.d/
sudo cp config/modprobe.d/* /etc/modprobe.d/
```

To make sure everything works, the following command should report the number of currently connected STLink programmers:

```bash
st-info --probe
```
