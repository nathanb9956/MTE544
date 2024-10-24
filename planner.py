# Type of planner
POINT_PLANNER=0; TRAJECTORY_PLANNER=1

import math

class planner:
    def __init__(self, type_):

        self.type=type_

    
    def plan(self, goalPoint=[-1.0, -1.0]):
        
        if self.type==POINT_PLANNER:
            return self.point_planner(goalPoint)
        
        elif self.type==TRAJECTORY_PLANNER:
            return self.trajectory_planner()


    def point_planner(self, goalPoint):
        x = goalPoint[0]
        y = goalPoint[1]
        return x, y

    # TODO Part 6: Implement the trajectories here
    def trajectory_planner(self):
        TrajectoryType = 0
        x = 0
        y = 0
        Step = 0.1
        Points = []

        if TrajectoryType == 0:
            while x < 1.5:
                y = x**2
                Point = (x,y)
                Points.append(Point)
                x +=Step
                
        if TrajectoryType == 1:
            while x < 2.5:
                y = 2/(1+math.exp(-2*x))-1
                Point = (x,y)
                Points.append(Point)
                x +=Step
        
        return Points
            

        # the return should be a list of trajectory points: [ [x1,y1], ..., [xn,yn]]
        # return 

