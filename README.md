pDynImporter
============

Check for correct modules and import them in globals

```python
    from pDynImporter import *
    
    # this equal: from moduleName import funcName 
    modules = [ ('moduleName',['funcName']) ]
    
    # this equal: from moduleName import funcName,funcName2,funcName3
    modules = [ ('moduleName',['funcName','funcName2','funcName3']) ]
    
    # this equal: 
    # from moduleName import funcName,funcName2,funcName3
    # import moduleName2,moduleName3
    modules = [ ('moduleName',['funcName','funcName2','funcName3']),'moduleName2','moduleName3' ]
    
    # function to be called in case of import errors, if None as default, an ImportError will be raisen
    errfunc = None
    
    # start the task, throw exception in case of wrong import
    exec(getCodeForImports(modules,errfunc))
    
    # now you can use the imported things, for example
    moduleName.funcName()   

```
