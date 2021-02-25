import clr, sys, os
import unittest
from Support.SignalAnalyzer import DataPostProcessor

clr.AddReference("NationalInstruments.ModularInstruments.NIRfsgPlayback.Fx40")

import NationalInstruments.ModularInstruments.NIRfsgPlayback as RfsgPlayback

waveformDirectory = r"C:\Users\LocalAdmin\Documents\GitHub\stchan-sandbox\BarcelonaSweepSGPhase_ContinuousSA\UnitTests"
cw0_file = r"\cw_0phase.tdms"
cw1_file = r"\cw_35phase.tdms"

class TestPhase(unittest.TestCase):

    def test_phase_diff(self):
        _, cw0 = RfsgPlayback.NIRfsgPlayback.ReadWaveformFromFileComplex(waveformDirectory + cw0_file, None)
        _, cw1 = RfsgPlayback.NIRfsgPlayback.ReadWaveformFromFileComplex(waveformDirectory + cw1_file, None)
        data = [cw0, cw1]
        data_process = DataPostProcessor(data)
        r0, phi0 = data_process.calculate_deltas()
        self.assertTrue(34.9 < phi0 < 35.1)

if __name__ == '__main__':
    unittest.main()