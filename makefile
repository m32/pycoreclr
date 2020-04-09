DOTNET=/devel/bin/dotnet-sdk/shared/Microsoft.NETCore.App/3.1.3
HOSTINC=/devel/00mirror-cvs/00-dotnet/runtime/src/coreclr/src/hosts/inc

.PHONY: all run clean

all: host manlib.dll coreclr.py

run:
	host $(DOTNET)

host: host.cpp coreclrhost.h
	g++ -o $@ $< -ldl

manlib.dll : manlib.cs manlib.csproj
	dotnet build
	cp bin/Debug/netstandard2.1/$@ $@

coreclrhost.h : $(HOSTINC)/coreclrhost.h
	cp $< $@

clean:
	-rm -rf bin obj coreclrhost.h host manlib.dll *.pyc __pycache__ coreclr.py

coreclrhost.py: coreclrhost.h
	ctypesgen -o coreclrhost.py -l libcoreclr coreclrhost.h

coreclr.py: coreclr.py.in makefile
	python -c "data = open('coreclr.py.in', 'rt').read().replace('-coredll-', '$(DOTNET)', 1); open('coreclr.py', 'wt').write(data)"
