# Introduction
This project is an example of using RPyC to make measurements in Python by calling into an RPyC server hosting NI software such as RFmx and RFSG.

# Software
## Server
1. NI Software
  * RFmx and personalities 3.0 or newer. The Wireless Test Suite installer 2019.01 contains all of these.
  * RFSA 18.2.1
  * RFSG 18.2.1
2. Python interpreter.
  * The example was tested and developed using python 3.6
3. Python modules
  *  RPyC
  *  pythonnet: provides clr (Common Language Runtime)
4. Launce the server by running RFmxService.py

## Client
1. Python interpreter
  * The example was tested and developed using python 3.6
2. Python modules
  * RPyC
3. Run the examples in the client folder.

# Hardware Setup
* All hardware is to be installed on the server.
* The example requires a vector signal generator and a vector signal analyzer.  The example was tested and developed using an NI 5840 VST.

# Contribute
* Do you have some examples to contribute? Let us know!
