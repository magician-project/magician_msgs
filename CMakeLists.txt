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
)

# Set the custom magician services paths
set(MAGICIAN_SRVS
    "srv/task_planning/Orienteering.srv"
)

rosidl_generate_interfaces(
    ${PROJECT_NAME}
    ${MAGICIAN_MSGS}
    ${MAGICIAN_SRVS}
    DEPENDENCIES ${MAGICIAN_MSGS_DEPENDENCIES}
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()