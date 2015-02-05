from pDynImporter import checkImports
import __builtin__

for k,v in  __builtin__.modules.iteritems():
    if not k.startswith("_"):
        globals()[k] = v

modules = [ ('test',['x']) ]
checkImports(modules)
    
x()