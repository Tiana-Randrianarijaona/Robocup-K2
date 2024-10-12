class Robot:
    def __init__(self,id,mediator):
        self.id = id
        self.mediator = mediator        
        self.is_on_passer_mode = False
        self.has_found_the_ball = False
        self.is_dribbling_the_ball = False
        self.has_located_robot_mate = False
        
    
    def set_passer_mode(self, passer_mode):
        self.is_on_passer_mode = passer_mode

    # To be defined : locate the ball until is it appears on the camera frame
    def search_the_ball(self):        
        return True

    #To be defined : go toward the ball by aligning the center of the ball with the center of the camera 
    def approach_the_ball(self):
        return True

    # To be defined : locate the robot mate until it appears on the camera frame
    # & align the center of the robot with the center oef the camera view
    def search_robot_mate(self,robot_mate_id):
        return True
    
    #To be defined : Trigger the kicker and set the robot's passer mode to False
    def pass_the_ball(self,robot_mate_id):
        if self.is_dribbling_the_ball:
            print(f"{self.id} is passing the ball to {robot_mate_id.id}")
            # Notify the central computer about the pass
            self.mediator.handle_pass(self, robot_mate_id)
        else:
            print(f"{self.id} cannot pass, it is not in passer mode!")
        self.set_passer_mode(False)

    def __str__(self):
        return f"{self.id}: {self.is_on_passer_mode}"

    
