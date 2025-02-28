import os
from pathlib import Path
from typing import List
from abc import ABC, abstractmethod

FILEDIR = os.path.dirname(__file__)


def main():
    if not os.path.exists("autogen"):
        os.makedirs("autogen")

    msgs_files = get_all_files_from(os.path.join(FILEDIR, "msg"), "msg")
    serialised_content = list()
    for file in msgs_files:
        obj = parse_file(file)
        serialised_content.append(obj.to_rst())

    with open("autogen/messages.rst", "w") as f:
        f.write("\n\n".join(serialised_content))

    srvs_files = get_all_files_from(os.path.join(FILEDIR, "srv"), "srv")
    serialised_content = list()
    for file in srvs_files:
        obj = parse_file(file)
        serialised_content.append(obj.to_rst())

    with open("autogen/services.rst", "w") as f:
        f.write("\n\n".join(serialised_content))


def get_all_files_from(basepath: str, extension: str) -> List[str]:
    print(f"Searching all files in {basepath} with extension '{extension}'")
    return list(map(str, Path(basepath).glob(f"**/*.{extension}")))

def message_hyperlink(msg_type: str) -> str:
    type_wo_array = msg_type.rstrip("[]")
    base = msg_type.split("/")[0]
    if base == "magician_msgs":
        return f":ref:`{msg_type}<{type_wo_array.split('/')[-1].lower().replace('.', '_')}_msg>`"

    if base in ["std_msgs", "geometry_msgs"]:
        return f"`{msg_type} <https://github.com/ros2/common_interfaces/blob/rolling/{base}/msg/{type_wo_array.split('/', 1)[1]}.msg>`_"
    

    return f"``{msg_type}``"

class Serialisable(ABC):
     
    @abstractmethod
    def to_rst(self) -> str:
        pass

class Variable(Serialisable):

    def __init__(self, line: str):
        contents = line.split()
        self.type = contents[0]
        self.name = contents[1]
        self.description = None

        if line.find("#") != -1:
            self.description = line.split("#", 1)[1].strip()

    def to_rst(self) -> str:
        desc = ""
        if self.description:
            desc = f": {self.description}"
        return f"``{self.name}`` (type: {message_hyperlink(self.type)}){desc}"


class Constant(Variable):

    def __init__(self, line: str):
        super().__init__(line)
        self.value = line.split("=")[1].split("#")[0].strip().rstrip()

    def to_rst(self) -> str:
        desc = ""
        if self.description:
            desc = f": {self.description}"
        return f"``{self.name}`` (value = ``{self.value}``, type: {message_hyperlink(self.type)}){desc}"


class Message(Serialisable):

    def __init__(self, filepath: str):
        self.name = os.path.split(filepath)[1]
        self.full_name = filepath[filepath.find("magician_msgs/msg/"):]
        print(f"Parsing '{self.name}'")

        with open(filepath, "r") as f:
            content = [l.strip().rstrip() for l in f.readlines()]

        self.textcontent: List[str] = list()
        self.constants: List[Constant] = list()
        self.variables: List[Variable] = list()

        for line in content:
            if line == "":
                continue

            if line.find("# ", 0, 2) == 0:
                self.textcontent.append(line.strip("# "))
                continue

            if line.find("=") != -1:
                self.constants.append(Constant(line))
            else:
                self.variables.append(Variable(line))

    def to_rst(self) -> str:
        content: List[str] = list()
        content.append(f".. _{self.name.replace('.', '_').lower()}:")
        content.append(f"``{self.full_name}``")
        content.append((4+ len(self.full_name)) * "=")
        content.append("")

        content += self.textcontent
        content.append("")
        content.append("**Variables:**\n")
        for var in self.variables:
            content.append(f"* {var.to_rst()}")
        
        if self.constants:
            content.append("")
            content.append("**Constants:**\n")
            for var in self.constants:
                content.append(f"* {var.to_rst()}")

        return "\n".join(content)

class Service(Serialisable):

    def __init__(self, filepath: str):
        self.name = os.path.split(filepath)[1]
        self.full_name = filepath[filepath.find("magician_msgs/srv/"):]
        print(f"Parsing '{self.name}'")

        with open(filepath, "r") as f:
            content = [l.strip().rstrip() for l in f.readlines()]

        self.textcontent: List[str] = list()
        self.constants: List[Constant] = list()
        self.in_variables: List[Variable] = list()
        self.out_variables: List[Variable] = list()

        curr_vars = self.in_variables

        for line in content:
            if line == "":
                continue

            if line.find("# ", 0, 2) == 0:
                self.textcontent.append(line.strip("# "))
                continue

            if line.startswith("---"):
                curr_vars = self.out_variables
                continue

            if line.find("=") != -1:
                self.constants.append(Constant(line))
            else:
                curr_vars.append(Variable(line))

    def to_rst(self) -> str:
        content: List[str] = list()
        content.append(f".. _{self.name.replace('.', '_').lower()}:")
        content.append(f"``{self.full_name}``")
        content.append((4+ len(self.full_name)) * "=")
        content.append("")

        content += self.textcontent
        content.append("")
        content.append("**Input variables:**\n")
        for var in self.in_variables:
            content.append(f"* {var.to_rst()}")

        content.append("")
        content.append("**Output variables:**\n")
        for var in self.out_variables:
            content.append(f"* {var.to_rst()}")
        
        if self.constants:
            content.append("")
            content.append("**Constants:**\n")
            for var in self.constants:
                content.append(f"* {var.to_rst()}")

        return "\n".join(content)


def parse_file(filepath: str) -> Serialisable:
    if filepath.endswith(".msg"):
        return Message(filepath)
    if filepath.endswith(".srv"):
        return Service(filepath)


    print("Don't know how to convert file", filepath)
    raise RuntimeError("Error")


if __name__ == "__main__":
    main()
