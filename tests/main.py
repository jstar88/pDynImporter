from pDynImporter import checkImports
import __builtin__

modules = [ ('test',['x']) ]
checkImports(modules)
for k,v in  __builtin__.modules.iteritems():
    if not k.startswith("_"):
        globals()[k] = v
    
x()