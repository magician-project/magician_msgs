# Magician ROS2 Custom Messages Documentation

This repository contains all custom topic/service messages necessary for the Magician framework.

The documentation is also accessible as a [website](https://magician-project.github.io/magician_msgs/). 

A textual description of the different messages shall be provided in the markdown files under the `docs` folder.


## Note
At the current stage, the **repository** is **public**, so that we can use GitHub pages to host the website version of the documentation. 
So please, **do not share here sensitive information**.

In the upcoming months we can plan on making this documentation private by finding other solutions.

## ROS2 messages framework

As standard in ROS2, topic messages are defined within the `msg` folder, while services in `srv`.

The suggestion is not to provide messages definition directly within the pertaining folder, but rather on different subfolders, grouped by scope.
An example is the [`deterministic_orienteering.srv`](https://github.com/magician-project/magician_msgs/blob/main/srv/task_planning/deterministic_orienteering.srv), a service which is used for task planning, and thus live within the `task_plannig` subfolder.

The main exception to this rule is for messages representing *standard* data types can could be shared among different entities, such as the [`defect.msg`](https://github.com/magician-project/magician_msgs/blob/main/msg/defect.msg) message the lives within the `msg` folder.


## Building the documentation
If you want to build locally the webpage for the documentation, you can use the provided `Makefile`. 
A more in depth guide on how to build the website version, can be found [here](https://magician-project.github.io/magician-project/index.html#building-the-documentation).
