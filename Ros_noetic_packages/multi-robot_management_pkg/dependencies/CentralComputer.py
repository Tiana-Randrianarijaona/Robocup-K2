class CentralComputer:
    def __init__(self):
        self.robots = []
        self.current_passer = None

    def register_robot(self, robot):
        self.robots.append(robot)

    def update_passer(self, new_passer):
        # If there's a current passer, switch them to receiver
        if self.current_passer:
            self.current_passer.set_passer_mode(False)

        # Set the new passer
        self.current_passer = new_passer
        self.current_passer.set_passer_mode(True)
        self.show_robot_states()

    def handle_pass(self, passer_robot, receiver_robot):
        # Validate if passer is passing to the correct robot
        if passer_robot == self.current_passer:
            # Pass occurs
            print(f"{passer_robot.id} passed the ball to {receiver_robot.id}")
            # Update the passer and receiver modes
            self.update_passer(receiver_robot)
            # self.show_robot_states()
        else:
            print(f"Invalid pass! {passer_robot.name} is not the current passer.")

    def show_robot_states(self):
        for robot in self.robots:
            print(robot)