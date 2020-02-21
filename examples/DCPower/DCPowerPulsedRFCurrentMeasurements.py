""" This example demonstrates how to apply a measurement delay to NI-DCPower to take
    hardware timed, single point measurements over active slots in bursty waveforms 
    like LTE/NR TDD.  This example showcases the use case where the marker event of
    the RF waveform is statically placed at sample 0 and can't be moved. """

import nidcpower

# variables
resource_name = "DC_01"
channels = ""

voltage_level = 5.0
current_limit = 100.0e-3
voltage_level_range = 6.0
current_limit_range = 100.0e-3
trigger_delay = 2.0e-3 # how long to wait after recieving a trigger to take a measurement

# initialize and configure sourcing parameters
dc = nidcpower.Session(resource_name,  channels, True)

dc.source_mode = nidcpower.SourceMode.SINGLE_POINT
dc.output_function = nidcpower.OutputFunction.DC_VOLTAGE

dc.voltage_level = voltage_level
dc.current_limit = current_limit
dc.voltage_level_range = voltage_level_range
dc.current_limit_range = current_limit_range

# start sourcing power - no measurements to be taken
dc.initiate() 
dc.wait_for_event(nidcpower.Event.SOURCE_COMPLETE)
dc.abort() # instrument continues to source power after this call

# configure trigger
dc.source_trigger_type = nidcpower.TriggerType.DIGITAL_EDGE
dc.digital_edge_source_trigger_input_terminal = "PXI_Trig0"
dc.source_delay = trigger_delay # amount of time to wait before asserting the source complete event after the source trigger is received
dc.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE

# measure
command = ""
while command.lower() != "exit":
    dc.initiate()
    measurements = dc.fetch_multiple(1, timeout=10.0)
    dc.abort()
    voltage_current_measurements = zip(measurements["voltage"], measurements["current"])
    for voltage, current in voltage_current_measurements:
        print(str(voltage) + "V, " + str(current) + 'A')
    command = input("Press enter to take another measurement. Enter 'exit' to close.")

# close
dc.reset()
dc.close()