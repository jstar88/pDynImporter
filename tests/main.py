from pDynImporter import getCodeForImports

modules = [ ('test',['x']) ]
#dynamic import
exec(getCodeForImports(modules))
    
x()