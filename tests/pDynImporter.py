class ModulesManager(object):
    errfunc = None
    def __init__(self, modules = {}):
        self.modules = {}
        self.loads(modules, True)
    
    def load(self, module, cache = True):
        if type(module) is tuple:
            module_name = module[0]
            func_names = module[1]
        else:
            module_name = module
            func_names = [] 
        if module_name in self.modules and cache:
            return True
        try: 
            m = __import__(module_name, globals(), locals(), func_names, -1)
            if func_names:
                for func_name in func_names:
                    self.modules[func_name] = getattr(m,func_name)
            else:
                self.modules[module_name] = m
            return True
        except ImportError:
            return False
    
    def loads(self, modules, cache = True):
        for module in modules:
            if not self.load(module,cache):
                if ModulesManager.errfunc is None:
                    raise ImportError("module '"+module+"' not found")
                else:
                    ModulesManager.errfunc(module)
                return
    
    def getGlobals(self):
        return self.modules
    
        
def getCodeForImports(modules, errfunc = None):
    ModulesManager.errfunc = errfunc
    return "map(lambda v: globals().__setitem__(v[0],v[1]) , ModulesManager("+str(modules)+").getGlobals().items())"