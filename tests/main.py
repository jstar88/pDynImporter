from pDynImporter import *

modules = [ ('test',['x']) ]
#dynamic import
exec(getCodeForImports(modules))
    
x()