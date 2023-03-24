import sys
import odrive
from odrive.enums import AXIS_STATE_FULL_CALIBRATION_SEQUENCE, AXIS_STATE_IDLE, AXIS_STATE_CLOSED_LOOP_CONTROL, \
    CONTROL_MODE_VELOCITY_CONTROL, CONTROL_MODE_POSITION_CONTROL, CONTROL_MODE_TORQUE_CONTROL

# one rotation for the motor is GEAR_RATIO at the real product
GEAR_RATIO = 1


def setup() -> odrive:
    odrv = odrive.find_any()
    if not odrv:
        sys.exit(1)
    return odrv


def get_current_state():
    return setup().axis0.current_state


def get_pos():
    return setup().axis0.encoder.pos_estimate * GEAR_RATIO


def get_vel():
    return setup().axis0.encoder.vel_estimate * GEAR_RATIO


# https://docs.odriverobotics.com/v/latest/fibre_types/com_odriverobotics_ODrive.html#ODrive.Axis.Config.Motor.torque_constant
def get_torque():
    a = setup()
    return a.axis0.FieldOrientedController.Iq_measured * GEAR_RATIO * a.axis0.Config.Motor.torque_constant


def set_vel(input_vel):
    a = setup()
    a.axis0.controller.config.control_mode = CONTROL_MODE_VELOCITY_CONTROL
    a.axis0.controller.input_vel = input_vel / GEAR_RATIO


def set_pos(input_pos):
    a = setup()
    a.axis0.controller.config.control_mode = CONTROL_MODE_POSITION_CONTROL
    a.axis0.controller.input_pos = input_pos / GEAR_RATIO


def set_torque(input_torque):
    a = setup()
    a.axis0.controller.config.control_mode = CONTROL_MODE_TORQUE_CONTROL
    a.axis0.controller.input_torque = input_torque / GEAR_RATIO


def calibrate():
    setup().axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE


def loop_control():
    setup().axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL


def idle():
    setup().axis0.requested_state = AXIS_STATE_IDLE


def pos_setpoint():
    setup().axis0.controller.pos_setpoint()
