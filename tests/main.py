from pDynImporter import my_imports

def checkPluginsImports(plugin,modules):
    c = my_imports(modules)
    if c:
        print plugin +" has errors!: module '"+c+"' not found"


def d():
	modules = [ ('test',['x']) ]
    checkPluginsImports('demoPlugin',modules)
    
d()
x()