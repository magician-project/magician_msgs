cmake_minimum_required(VERSION 3.5)
project(magician_msgs)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

set(MAGICIAN_MSGS_DEPENDENCIES
    builtin_interfaces 
    std_msgs  
    geometry_msgs
)

# Make sure all dependencies are available
foreach(DEP ${MAGICIAN_MSGS_DEPENDENCIES})
    find_package(${DEP} REQUIRED)
endforeach()

# Set the custom magician messages paths
set(MAGICIAN_MSGS
    "msg/Defect.msg"
    
    # Motion planning
    "msg/motion_planning/ControlMode.msg"
    "msg/motion_planning/SanderControl.msg"
    "msg/motion_planning/CartesianMotionPlan.msg"
)

# Set the custom magician services paths
set(MAGICIAN_SRVS
    # Task planning
    "srv/task_planning/Orienteering.srv"

    # Motion planning
    "srv/motion_planning/ReachPosition.srv"
    "srv/motion_planning/PointToPointMotion.srv"
    "srv/motion_planning/PointToPointTime.srv"
    "srv/motion_planning/MeshPointToPointMotion.srv"
    "srv/motion_planning/MeshDilation.srv"
    "srv/motion_planning/HoldPosition.srv"
)

rosidl_generate_interfaces(
    ${PROJECT_NAME}
    ${MAGICIAN_MSGS}
    ${MAGICIAN_SRVS}
    DEPENDENCIES ${MAGICIAN_MSGS_DEPENDENCIES}
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()
