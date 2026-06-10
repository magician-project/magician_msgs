# TactileDetection.msg
# Represents a tactile defect detection result for a time window

std_msgs/Header header    # Start time of the analyzed window (seconds)
float32 timewindow_size_ms      # End time of the analyzed window (seconds)
string type                 # Type of defect detected (e.g., "no defect", "defect", "NDA", "PDA")
float32 probability         # Confidence/probability of the defect (0.0 to 1.0)
float32 probability_no_defect   # Probability of no defect: prob[class=0] regardless of prediction
