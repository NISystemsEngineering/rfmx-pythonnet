"""
Example for remote dynamic generation of 5GNR waveforms with the RFmx Waveform Creator Batch Waveform Utility
"""

import rpyc

# connect and import libraries
host_name = 'semoore-pxi'
host_port = 18861
conn = rpyc.connect(host_name, host_port)
os = conn.root.import_module('os')
tempfile = conn.root.import_module('tempfile')

# path to the BatchWaveformCreator exe
wc_dir = os.path.join(os.environ['ProgramFiles'], 'National Instruments', 'RFmxWaveformCreator', 'BatchWaveformCreationUtility')

# define waveform configuration and output directory
nr_cfg = {'Subblock': '0', 'Carrier': '0', 'ChannelBandwidth': '100M', 'LinkDirection': 'Uplink',
          'FrequencyRange': 'Range 1', 'User': '0', 'PUSCHModulationType': 'QAM256'}
out_dir = os.getcwd()  # output directory of tdms file

# create temporary csv file that will hold rows and columns of waveform to create
tf = tempfile.NamedTemporaryFile(mode='w', dir=out_dir, suffix='.csv', delete=False)
tf.write(','.join(nr_cfg.keys()) + '\n')
tf.writelines(','.join(nr_cfg.values()))
tf.close()

# build command string
wc_app = os.path.join(wc_dir, 'RFmxBatchWaveformCreationUtility.exe')
cmd = [f'\"{wc_app}\"', f'\"csvfilepath={tf.name}\"', f'\"outputdirectory={out_dir}\"']
flags = ['-donotKeepRfws', '-singlePrecision']  # optional flags

# execute waveform creator
cmd.extend(flags)  # add flags to command
os.system(f'"{" ".join(cmd)}"')
os.remove(tf.name)
# if a waveform is not created, an error might have occurred
# go to %temp% (typically C:\Users\<USER>\AppData\Local\Temp) and sort by modified date to find a log file
