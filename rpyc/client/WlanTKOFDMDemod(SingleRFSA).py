# DEMO EXAMPLE: Client side execution of WLAN Analysis Toolkit on a remote server
import rpyc

# # # # # RPyC Configuration # # # # #
hostName = 'semoore-pxi'                # Name or IP address of the RPyC server
hostPort = 18861                    # Port number of the RPyC server
print("Opening connection to RFmxService on " + hostName + "..", end = '')
conn = rpyc.connect(hostName, hostPort)
print("done")

# Instantiate exported classes from the service
print("Importing classes from service..", end = '')
System = conn.root.System
ModInstInterop = conn.root.ModularInstrumentsInterop
WlanTK = conn.root.WlanTK
print("done")

# # # # # Analysis Parameters # # # # # #
print("Setting measurement parameters..", end = '')
analyzerResourceName = "VST1_01"       # Resource name of the Analyzer on the Host
analyzerClockSource = "OnboardClock"
refLevel = 0
analyzerExternalAttenuation = 0
ofdmNumOfAverages = 10
ofdmMaximumSymbolsUsed = 16
timeout = 10

# # # # # Generation Parameters # # # # #
generatorResournceName = "VST1_01"
generatorClockSource = "OnboardClock"
powerLevel = -10
generatorExternalAttenuation = 0
mcsIndex = 0

# # # # # Common Parameters # # # # #
chBW = 20.00e6
carrierFrequency = 5.180e9
standard = WlanTK.niWLANAConstants.Standard80211acMimoOfdm
print("done")

# # # # # Measurement Configuration # # # # #
print("Configuring measurement..", end = '')
wlana = WlanTK.niWLANA(WlanTK.niWLANAConstants.CompatibilityVersion050000)
wlana.SetStandard(None, standard)
wlana.SetChannelBandwidth(None, chBW)
wlana.SetOfdmDemodNumberOfAverages(None, ofdmNumOfAverages)
wlana.SetOfdmDemodMaximumSymbolsUsed(None, ofdmMaximumSymbolsUsed)
wlana.SetOfdmDemodAutoComputeAcquisitionLengthEnabled(None, True)
wlana.SelectMeasurements(WlanTK.niWLANAConstants.OfdmDemodMeasurement)
print("done")

# # # # # Analyzer Configuration # # # # #
print("Configuring analyzer..", end = '')
rfsaSession = ModInstInterop.niRFSA(analyzerResourceName, True, False)
rfsaSession.ConfigureRefClock(analyzerClockSource, 10e6)
rfsaSession.SetExternalGain(None, -(analyzerExternalAttenuation))
rfsaSession.ConfigureReferenceLevel(None, refLevel)
rfsaSession.ConfigureIQPowerEdgeRefTrigger("0", refLevel - 20.0, ModInstInterop.niRFSAConstants.RisingSlope, 0.0)
wlana.RFSAConfigureFrequencySingleLO([rfsaSession.Handle], WlanTK.niWLANAConstants.LOSourceOnboard, System.Runtime.InteropServices.HandleRef(), carrierFrequency, False, False)
print("done")

# # # # # Waveform Configuration # # # # #
print("Configuring waveform..", end = '')
wlang = WlanTK.niWLANG(WlanTK.niWLANGConstants.CompatibilityVersion050000)
wlang.SetStandard(None, standard)
wlang.SetChannelBandwidth(None, chBW)
wlang.SetMcsIndex(None, mcsIndex)
print("done")

# # # # # Generator Configuration # # # # #
print("Configuring generator..", end = '')
rfsgSession = ModInstInterop.niRFSG(generatorResournceName, True, False)
rfsgSession.ConfigurePowerLevelType(ModInstInterop.niRFSGConstants.PeakPower)
rfsgSession.ConfigureGenerationMode(ModInstInterop.niRFSGConstants.Script)
rfsgSession.ConfigureRefClock(generatorClockSource, 10e6)
rfsgSession.SetExternalGain(None, -(generatorExternalAttenuation))

wlang.SetRFBlankingEnabled(None, False)
wlang.RFSGConfigureFrequencySingleLO([rfsgSession.Handle], WlanTK.niWLANGConstants.LOSourceOnboard, System.Runtime.InteropServices.HandleRef(), carrierFrequency, False, False)
waveformName = "wlangtkwfm"
wlang.RFSGCreateAndDownloadMIMOWaveforms([rfsgSession.Handle], None, 1, waveformName)
script = "script GenerateWlan\nrepeat forever\ngenerate " + waveformName + "\n end repeat\n end script"
WlanTK.niWLANG.WLANG_RFSGConfigureScript(rfsgSession.Handle, None, script, powerLevel)
wlang.Close()
rfsgSession.Initiate()
print("done")

# # # # # Measure and Print Results # # # # #
print("Measuring..", end = '')
wlana.RFSAMIMOMeasure([rfsaSession.Handle], None, 1, timeout)
print("done")
_, rmsEvm = wlana.GetResultOfdmDemodRmsEvm("stream0", 0.0)
print("RMS EVM Mean (dB): {0:.3f}".format(rmsEvm))

# # # # # Clean Up # # # # #
rfsaSession.Close()
rfsgSession.close()