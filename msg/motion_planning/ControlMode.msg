# Describes the behavior of the low-level controller when executing a given motion.

uint8 CONTROL_MODE_KEEPLAST = 1   # use the lastly set control mode; the default behavior
uint8 CONTROL_MODE_IMPEDANCE = 2  # triggers default impedance control mode
uint8 CONTROL_MODE_ADMITTANCE = 3 # triggers admittance control mode along the _z_ axis

uint8 ADMITTANCE_CONSTANT_REFERENCE = 1  # use a message-set constant reference for the force; default behavior
uint8 ADMITTANCE_TOPIC_REFERENCE = 2     # listens to the desired force for admittance on the configured topic

uint8 control_mode 1 # control mode to use
uint8 admittance_reference_mode 1 # specifies how the reference for the admittance control is obtained. Requires ``control_mode == CONTROL_MODE_ADMITTANCE``

float64 reference_force 0.0   # reference force to track. Requires ``control_mode == CONTROL_MODE_ADMITTANCE`` and ``admittance_reference_mode == ADMITTANCE_CONSTANT_REFERENCE``
