DOTNET=/devel/bin/dotnet-2.1.105/shared/Microsoft.NETCore.App/2.0.7

all: host manlib.dll

run:
	host $(DOTNET)

host: host.cpp coreclrhost.h
	g++ -o $@ $< -ldl

manlib.dll : manlib.cs manlib.csproj
	dotnet build
	cp bin/Debug/netstandard2.0/$@ $@

coreclrhost.h : /devel/00mirror-cvs/00-dotnet/coreclr/src/coreclr/hosts/inc/coreclrhost.h
	cp $< $@

clean:
	-rm -rf bin obj coreclrhost.h host manlib.dll *.pyc

coreclrhost.py: coreclrhost.h
	ctypesgen -o coreclrhost.py -l libcoreclr coreclrhost.h
