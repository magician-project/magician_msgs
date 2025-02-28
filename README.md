# Magician ROS2 Custom Messages Documentation

This repository contains all custom topic/service messages necessary for the Magician framework.

The documentation is also accessible as a [website](https://magician-project.github.io/magician_msgs/). 

A textual description of the different messages shall be provided in the markdown files under the `docs` folder.


## ROS2 messages framework

As standard in ROS2, topic messages are defined within the `msg` folder, while services in `srv`.

The suggestion is not to provide messages definition directly within the pertaining folder, but rather on different subfolders, grouped by scope.
An example is the [`Orienteering.srv`](https://github.com/magician-project/magician_msgs/blob/main/srv/task_planning/Orienteering.srv), a service which is used for task planning, and thus live within the `task_plannig` subfolder.

The main exception to this rule is for messages representing *standard* and *common* data types can could be shared among different entities, such as the [`Defect.msg`](https://github.com/magician-project/magician_msgs/blob/main/msg/Defect.msg) message the lives within the `msg` folder.


### Messages documentation

To ease the documentation, is has been written a [python script](https://github.com/magician-project/magician_msgs/blob/main/process_messages.py) which crawls the content of the repository and automatically generates [restructured text](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) files which, in turn, are used to create the website/pdf documentation.

Such script performs some basic parsing of the content of `msg`/`srv` files to output some file in the `autogen` folder. 
As from the following example:

- you may put arbitrary text at the beginning of the file to document the message content (note that here, everything aside the comment `#` symbol, will be parsed as restructured text); 
- you may document variables/constants by appending a comment at the right of their definition.

```
# Put here some description of the message
# You can also use multiple lines

uint8 MYENUM_A = 1  # enumeration value documentation; cannot go to a newline
uint8 value         # variable documentation; cannot go to a newline
```


### Note
At the current stage, the **repository** is **public**, so that we can use GitHub pages to host the website version of the documentation. 
So please, **do not share here sensitive information**.

In the upcoming months we can plan on making this documentation private by finding other solutions.

## Available message descriptions

```{toctree}
:maxdepth: 1

autogen/messages.md
autogen/services.md
```


## Building the documentation
If you want to build locally the webpage for the documentation, you can use the provided [`Makefile`](./Makefile). 
A more in depth guide on how to build the website version, can be found [here](https://magician-project.github.io/magician-project/index.html#building-the-documentation).

Available targets are:

- `docs` (default), `html`: builds the website version of the documentations;
- `view`: uses the default browser to open the locally built documentation;
- `pdf`: builds the documentation in a `magician_msgs.pdf` file;
- `venv`: initialises a python virtual environment (by default in the `.venv` directory) that is used to build the documentation.
