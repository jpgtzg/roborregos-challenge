from lib.actions.run_action import RunAction
from systems.intake import Intake
from ..constants import Constants
import logging

logger = logging.getLogger(__name__)

class ActivateRoller(RunAction):

    def __init__(self,  roller_system: Intake):
        super().__init__("Activate Roller")
        self.roller_system = roller_system

    def execute(self):
        logger.info("Activating Roller")
        self.roller_system.set(Constants().RollerConstants().ROLLER_SPEED)
        pass