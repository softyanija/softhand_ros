from dynamixel_controllers.joint_position_controller \
    import JointPositionController

from softhand_ros.calib_required_controller import CalibRequiredController


class CalibRequiredJointController(
        JointPositionController, CalibRequiredController
):
    def __init__(self, dxl_io, controller_namespace, port_namespace):
        JointPositionController.__init__(
            self, dxl_io, controller_namespace, port_namespace)
        CalibRequiredController.__init__(self)
