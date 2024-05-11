#!/usr/bin/env python3

# --- Input Parameters --- #

# Payload envelope Dimensions in `m`
env_l = 0.150
env_w = 0.150
env_h = 0.150

# Payload Mass in `kg`
payload_mass = 0.65

# Motor Mass in `kg`
motor_mass = 0.1

# Distance from motors to payload in `m`
r_roll = 0.15
r_yaw = 0.15
r_pitch = 0.15

# --- Constants --- #

pi = 3.1415926
g = 9.80665


# Convert radians to degrees
def rad2deg(r):
    return r * 180 / pi


# Moment of Inertia of a cube: I = mass * area / 12
def moi_cube(mass, area):
    return mass * area / 12


# Moment of Inertia of a point mass: I = mass * radius^2
def moi_point(mass, radius):
    return mass * (radius * radius)


payload_weight = payload_mass * g
motor_weight = motor_mass * g


def calculate_stationary_torque():
    # Torque applied when accelerating from stationary
    #
    # Inputs:
    #   - Angular Acceleration (rad/sec^2)
    #
    # Outputs:
    #   - Torque (Nm)
    ###################################################

    # --- Moment of Inertia for each axis --- #

    # Angular acceleration of the payload
    # TODO: find realistic acceleration
    # TODO: plot tradeoff between mass and torque
    # TODO: calculate possible acceleration from motor torque
    # TODO: separate static force from payload acceleration
    a = 2 * pi

    # Yaw Axis:

    # Payload
    I_payload_yaw = moi_cube(payload_mass, (env_l * env_w))
    # Motor
    I_motor_yaw = moi_point(motor_mass, r_roll) + moi_point(motor_mass, r_pitch)
    # Total
    I_yaw = I_payload_yaw + I_motor_yaw

    # Pitch Axis:

    # Payload
    I_payload_pitch = moi_cube(payload_mass, (env_w * env_h))
    # Motor
    I_motor_pitch = moi_point(motor_mass, r_roll)
    # Total
    I_pitch = I_payload_pitch + I_motor_pitch

    # Roll Axis:

    # Payload
    I_payload_roll = moi_cube(payload_mass, (env_h * env_l))
    # No motor because the roll axis only moves the payload
    # Total
    I_roll = I_payload_roll

    # --- Torque on the motor for each axis --- #

    # Pitch axis:
    # Note: This is the only motor acting against gravity
    t_pitch_static = g * motor_mass * r_roll
    t_pitch_payload = I_pitch * a
    t_pitch = t_pitch_static + t_pitch_payload

    # Yaw Axis:
    t_yaw = I_yaw * a

    # Roll Axis:
    t_roll = I_roll * a

    # Print output
    print(
        f"Torque on each axis when accelerating from stationary to a rate of {a} rad/sec ({rad2deg(a)} deg/sec)"
    )
    print(f"- Pitch: {t_pitch:.3f} Nm")
    print(f"- Yaw:   {t_yaw:.3f} Nm")
    print(f"- Roll:  {t_roll:.3f} Nm")


if __name__ == "__main__":
    calculate_stationary_torque()
