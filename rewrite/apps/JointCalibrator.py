"""
Contains the JointCalibrator class, which is used to calibrate the joint angles of the robot.
"""

class JointCalibrator:
    def __init__(self, config, translator):
        pass

    def __str__(self) -> str:
        return "Joint Calibrator"

    @property
    def name(self) -> str:
        """
        Gets the name of the app.

        Returns:
            The name of the app.
        """
        return self.__str__()

    def rebuildWindow(self):
        """
        Rebuilds the window.
        """
        pass
