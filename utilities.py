from math import atan2, asin, sqrt
from scipy.spatial.transform import Rotation as R

M_PI=3.1415926535

class Logger:
    
    def __init__(self, filename, headers=["e", "e_dot", "e_int", "stamp"]):
        
        self.filename = filename

        with open(self.filename, 'w') as file:
            
            header_str=""

            for header in headers:
                header_str+=header
                header_str+=", "
            
            header_str+="\n"
            
            file.write(header_str)


    def log_values(self, values_list):

        with open(self.filename, 'a') as file:
            
            vals_str=""
            
            for value in values_list:
                vals_str+=f"{value}, "
            
            vals_str+="\n"
            
            file.write(vals_str)
            

    def save_log(self):
        pass

class FileReader:
    def __init__(self, filename):
        
        self.filename = filename
        
        
    def read_file(self):
        
        read_headers=False

        table=[]
        headers=[]
        with open(self.filename, 'r') as file:

            if not read_headers:
                for line in file:
                    values=line.strip().split(',')

                    for val in values:
                        if val=='':
                            break
                        headers.append(val.strip())

                    read_headers=True
                    break
            
            next(file)
            
            # Read each line and extract values
            for line in file:
                values = line.strip().split(',')
                
                row=[]                
                
                for val in values:
                    if val=='':
                        break
                    row.append(float(val.strip()))

                table.append(row)
        
        return headers, table
    
    

# TODO Part 3: Implement the conversion from Quaternion to Euler Angles
def euler_from_quaternion(quat):
    """
    Convert quaternion (w in last place) to euler roll, pitch, yaw.
    quat = [x, y, z, w]
    """
    '''
    q_x = quat[0]
    q_y = quat[1]
    q_z = quat[2]
    q_w = quat[3]

    # Roll
    roll = atan2(2 * (q_w * q_x + q_y * q_z), 1 - 2 * (q_x**2 + q_y**2))
    
    # Pitch
    pitch = asin(2 * (q_w * q_y - q_z * q_x))
    
    # Yaw
    yaw = atan2(2 * (q_w * q_z + q_x * q_y), 1 - 2 * (q_y**2 + q_z**2))
    '''

    r = R.from_quat(quat)

    #Save values as euler = [roll, pitch, yaw]
    euler = r.as_euler('xyz', degrees=False)

    # Only unpack yaw
    return euler[2]



#TODO Part 4: Implement the calculation of the linear error
def calculate_linear_error(current_pose, goal_pose):
        
    # Compute the linear error in x and y
    # Remember that current_pose = [x,y, theta, time stamp] and goal_pose = [x,y]
    # Remember to use the Euclidean distance to calculate the error.
    error_x = goal_pose[0] - current_pose[0]
    error_y = goal_pose[1] - current_pose[1]

    error_linear = sqrt(error_x**2 + error_y**2)

    return error_linear



#TODO Part 4: Implement the calculation of the angular error
def calculate_angular_error(current_pose, goal_pose):

    # Compute the linear error in x and y
    # Remember that current_pose = [x,y, theta, time stamp] and goal_pose = [x,y]
    # Use atan2 to find the desired orientation
    # Remember that this function returns the difference in orientation between where the robot currently faces and where it should face to reach the goal
    error_x = goal_pose[0] - current_pose[0]
    error_y = goal_pose[1] - current_pose[1]

    error_angular = atan2(error_y,error_x)

    # Remember to handle the cases where the angular error might exceed the range [-π, π]

    if error_angular > M_PI:
        while error_angular+M_PI > M_PI:
            error_angular -= 2*M_PI
    elif error_angular < -M_PI:
        while error_angular < -M_PI:
            error_angular += 2*M_PI

    return error_angular
