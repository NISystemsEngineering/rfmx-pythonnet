# Wrappers

Some NI measurement software is shipped with .NET wrapper APIs instead of .NET class libraries. Section 4 of [this page](http://www.ni.com/product-documentation/14434/en/) contains a detailed list of these APIs.

.NET wrappers consist of C# or Visual Basic source code that can be compiled into the target application. Pythonnet only funcions on built .NET assemblies. Therefore, for each API we plan to use, we must build the wrapper source code into .NET assemblies to be consumed by pythonnet.

This subdirectoy contains the source code for building these assemblies. Prebuilt assemblies have already been placed in the [bin]() directory at the project root.

As new versions of the API roll out, new assemblies need to be built in order to expose the latest features.