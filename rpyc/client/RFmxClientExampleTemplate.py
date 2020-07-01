"""
Example template for getting started with RFmx and RPyC
"""

import rpyc

# connect and import libraries
host_name = 'localhost'
host_port = 18861
conn = rpyc.connect(host_name, host_port)
InstrMX = conn.root.InstrMX

# local variables
rfsa_resource_name = 'VST2_01'

# initialize instrument session
instr = InstrMX.RFmxInstrMX.GetSession(rfsa_resource_name, "")

try:
    pass
finally:
    # close sessions and connection to server
    instr.Close()
    conn.Close()
