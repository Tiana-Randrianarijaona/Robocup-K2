from CentralComputer import CentralComputer
from Robot import Robot



mediator = CentralComputer()

robot1 = Robot("Robot1", mediator)
robot2 = Robot("Robot2", mediator)


mediator.register_robot(robot1)
mediator.register_robot(robot2)

mediator.update_passer(robot1)



robot1.is_dribbling_the_ball = True

robot1.pass_the_ball(robot2)

