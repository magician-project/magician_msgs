# Common Messages

This page will contain the description of general purpose messages, i.e., the one that might suit multiple application topics/services.

## `msg/defect`
This message encodes an already detected defect and reports the following information:
- `location` of the defect, expressed within the CAD reference frame;
- `severity` of the defect, with possible values: 
  - `1` for defects of class A;
  - `2` for defects of class B;
  - `3` for defects of class C;