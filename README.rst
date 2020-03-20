Interop with Microsoft .NET Core runtime, called CoreCLR.

Change location of coreclr to proper value in makefile

DOTNET=/devel/bin/dotnet-sdk/shared/Microsoft.NETCore.App/3.1.2

Python demo loading manlib.cs compiled to .dll:
    python3 host.py

C++ demo loading manlib.cs compiled to .dll:
    make run