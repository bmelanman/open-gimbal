# OpenGimbal

Now introducing: OpenGimbal - An open-source gimbal implementation utilizing the PX4-Autopilot library.

![gimbal_gif][_gimbal_gif_path]

## Reference Design

This design is based on the the [OpenSAM](https://opensamofficial.github.io/OpenSAM/) 3-axis handheld camera gimbal. The slipring components have been adapted from the [Continuous Rotation Lidar Module](https://www.thingiverse.com/thing:1778878).

The gimbal uses two Vertiq 28-06 motor modules to drive the roll and yaw axes, and two* Vertiq 40-06 motor modules to drive the pitch axis. The motors are controlled by an [ARK CANnode](https://arkelectron.com/product/ark-cannode/) module running the PX4-Autopilot  OpenGimbal firmware. Additionally, a [generic 12-wire slipring](https://www.amazon.com/Taidacent-Wires12-Collector-Electrical-Connector/dp/B07NSPHVTN) is used to allow infinite range in the yaw axis.

_*Two motors were used to decrease each motor's load and heat dissipation, however a single motor may suffice depending on the use case and payload weight._

The design files, as well as any necessary hardware for assembling the gimbal, can be found in the [reference design folder][_ref_design_path] of this repository.

### Assembly Notes

Should you choose to print and assemble the provided reference design, keep in mind:

- The hardware used in the design was simply what I already had on hand at the time. The design can be easily modified to accommodate different hardware, so I would highly recommend first trying to incorporate any hardware you already have before purchasing any new parts.

- I highly recommend printing the parts in PETG with a fairly high infill, as the parts need to be quite strong to support the heat and force imparted by the motors (especially on the pitch axis).

## To Do

* [ ] Enable control over DroneCAN
* [ ] Enable axis range limits
* [ ] Add landing detection
* [ ] Tune rate controller PID values for each axis
* [ ] Add optional telemetry collection
* [ ] Add parameters to the reference design to allow for the use of different motors, sliprings, controllers, etc.
* [ ] "Spruce things up"

## Acknowledgements

* This project was sponsored largely by Alex from [ARK Electronics](https://arkelectron.com/), who provided the ARK CANnode module, the Vertiq motors, and a lot of guidance and support throughout the project. Massive thanks to him for making this project possible!

* This project is based on the work of [PX4-Autopilot](https://github.com/PX4/PX4-Autopilot), an open source flight control software for drones and other unmanned vehicles, providing a flexible set of tools for drone developers to share technologies to create tailored solutions for drone applications.

* The gimbal design is based on the [OpenSAM](https://opensamofficial.github.io/OpenSAM/) 3-axis handheld camera gimbal. 

* The slipring components have been adapted from the [Continuous Rotation Lidar Module](https://www.thingiverse.com/thing:1778878).

[_ref_design_path]: resources/reference_design
[_gimbal_gif_path]: resources/ezgif-2-9b316f240c.gif