# Message encoding the cartesian motion of the end-effector as a sequence of poses computed with a given sampling period.

uint32 timestep_ns          # sampling period (in nanoseconds)
string frame_id             # reference frame over which poses are defined
geometry_msgs/Pose[] poses  # pose array constituting the motion plan
