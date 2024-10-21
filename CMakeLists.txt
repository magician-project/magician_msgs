cmake_minimum_required(VERSION 3.5)
project(magician_msgs)


find_package(ament_cmake REQUIRED)
find_package(std_msgs REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(rosidl_default_generators REQUIRED)

set(CUSTOM_MSGS
# Insert path to custom topic messages here
)

set(CUSTOM_SRVS
# Insert path to custom service messages here
)

rosidl_generate_interfaces(
    ${PROJECT_NAME}
    ${CUSTOM_MSGS}
    ${CUSTOM_SRVS}
    DEPENDENCIES 
    builtin_interfaces std_msgs  
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()
