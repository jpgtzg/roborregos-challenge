from lib.actions.action_scheduler import ActionScheduler
from lib.actions.wait_action import WaitAction # Works
from lib.actions.instant_action import InstantAction # Works
from lib.actions.sequential_action_group import SequentialActionGroup # Works
from lib.actions.parallel_action_group import ParallelActionGroup # Works
from lib.actions.wait_until_action import WaitUntilAction  # Works
from lib.actions.parallel_deadline_group import ParallelDeadlineGroup # Works
from lib.actions.run_action import RunAction  # Works

scheduler = ActionScheduler()

condition = False

def getCondition():
    return condition

waitAction = WaitUntilAction(getCondition)

printAction = InstantAction(lambda: print("Hello World!"))

newCommand = waitAction.andThen(printAction)

scheduler.schedule_action(newCommand)

import time

startTime = time.time()

while True:
    difference = time.time() - startTime
    print(difference)

    if difference > 5:
        condition = True

    scheduler.run()
    if newCommand.is_finished():
        break


""" printAction = InstantAction("PrintAction", lambda: print("Hello World!"))

parallelAction = SequentialActionGroup(waitAction, printAction)

scheduler.schedule_action(parallelAction)

while True:
    scheduler.run() """