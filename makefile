DOTNET:=$(shell ls -d -1 /devel/bin/dotnet-sdk/shared/Microsoft.NETCore.App/* | tail -1)
HOSTINC=/devel/00mirror-cvs/00-dotnet/runtime/src/coreclr/src/hosts/inc
HOSTINC=/devel/00mirror-cvs/00-dotnet/runtime/src/coreclr/hosts/inc

.PHONY: all run clean

all: host manlib.dll coreclr.py

run:
	host

host: host.cpp coreclrhost.h
	g++ -o $@ -D DOTNET='"$(DOTNET)"' $< -ldl

manlib.dll : manlib.cs manlib.csproj
	dotnet build
	cp bin/Debug/net6.0/$@ $@

#coreclrhost.h : $(HOSTINC)/coreclrhost.h
#	cp $< $@

clean:
	-rm -rf bin obj host __pycache__

distclean: clean
	-rm coreclr.py manlib.dll

coreclrhost.py: coreclrhost.h
	ctypesgen -o coreclrhost.py -l libcoreclr coreclrhost.h

coreclr.py: coreclr.py.in makefile
	python -c "data = open('coreclr.py.in', 'rt').read().replace('-coredll-', '$(DOTNET)', 1); open('coreclr.py', 'wt').write(data)"
