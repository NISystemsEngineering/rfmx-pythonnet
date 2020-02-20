# Wrappers

Some legacy NI measurement software is shipped with .NET wrapper APIs instead of .NET class libraries. Section 4 of [this page](http://www.ni.com/product-documentation/14434/en/) contains a detailed list of these APIs.

.NET wrappers consist of C# and/or Visual Basic source code that is compiled into the target application. Pythonnet only funcions on built .NET assemblies. Therefore, for each API we plan to use, we must build the wrapper source code into .NET assemblies to be consumed by pythonnet.

# Disclaimer

While NI continues to support many legacy .NET wrappers, they are not recommended for new applications. You should only consider building and using the wrappers if you have a very specific need to do so. The following list contains a few examples of when the wrappers are recommended.

- WLAN dynamic waveform generation
- WLAN MIMO generation and analysis

For WLAN SISO applications, [RFmxWLAN](https://www.ni.com/en-us/support/downloads/drivers/download.rfmx-wlan.html#333999) is the recommended solution.

# Build Process

This subdirectory contains the source code for building a subset of NI wrappers into .NET assemblies. Prebuilt assemblies have already been placed in the [bin](https://github.com/NISystemsEngineering/rfmx-pythonnet/tree/master/bin) directory at the project root.

As new versions of each wrapper are released, new assemblies will have to be built in order to expose the latest features. A Visual Studio solution is provided here as a starting point. For a tutorial on how this project was designed and how to build new assemblies, visit the [.NET Wrapper Solution Build Process](https://github.com/NISystemsEngineering/rfmx-pythonnet/wiki/.NET-Wrapper-Solution-Build-Process) wiki page.