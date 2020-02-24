# rfmx-pythonnet
This repository contains examples for local and remote execution of RFmx in Python.
Local examples can be found in the [examples](https://github.com/NISystemsEngineering/rfmx-pythonnet/tree/master/examples) folder.
Remote example can be found in the [rpyc](https://github.com/NISystemsEngineering/rfmx-pythonnet/tree/master/rpyc) folder.

## Code Auto-completion
Stubs have been created with [ironstubs](https://github.com/gtalarico/ironpython-stubs) to enable code auto-completion.

![](doc/codeautocomplete.gif)

To enable this feature, [configure your editor](https://github.com/gtalarico/ironpython-stubs/wiki) to use the stubs located in the [stubs](https://github.com/NISystemsEngineering/rfmx-pythonnet/tree/master/stubs/) directory.

If you are using Visual Studio Code, a [settings file](https://github.com/NISystemsEngineering/rfmx-pythonnet/tree/master/.vscode) has already been provided. To use it, clone this repo then open the folder in VS Code. 

Notable [known limitations](https://github.com/gtalarico/ironpython-stubs/wiki):
- Wildcard imports are not supported (`from x import *`)
- Since method overloads work differently in python, autocomplete options will look like `func(args)` or something similar

**Note:** The stubs require some additional modifications in order to expose all auto-complete options. Note that not all options will be available, especially as new versions are released. Always refer to the product documentation for a complete list of functionality.

## Remote Execution with RPyC
For RPyC related content, please visit the [RPyC subdirectory.](rpyc)

## Environment Setup
[NI-RFmx](https://www.ni.com/en-us/support/downloads/drivers/download.rfmx.html#333458) - Integrated Instrument Driver & Analysis Software

[NI-RFSA](https://www.ni.com/en-us/support/downloads/drivers/download.ni-rfsa.html#333730) - Analyzer Instrument Driver

[NI-RFSG](https://www.ni.com/en-us/support/downloads/drivers/download.ni-rfsg.html#333282) - Generator Instrument Driver

[pythonnet](https://github.com/pythonnet/pythonnet/wiki/Installation) - .NET Assemblies in Python

[RPyC]() - Remote Execution (Optional)
