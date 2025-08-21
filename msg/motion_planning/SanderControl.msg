# Message for setting the sander control state

uint8 SANDER_CMD_DISABLE = 0    # command turning off the sander
uint8 SANDER_CMD_ENABLE = 1     # command turning on the sander
uint8 SANDER_CMD_KEEPLAST = 2   # command that doesn't change the sander control state

uint8 commanded_state 0     # which state to command; defaults to ``SANDER_CMD_DISABLE``
