pDynImporter
============

Check for correct modules and import them in globals

```python
    from pDynImporter import checkImports
    
    # this equal: from moduleName import funcName 
    modules = [ ('moduleName',['funcName']) ]
    
    # this equal: from moduleName import funcName,funcName2,funcName3
    modules = [ ('moduleName',['funcName','funcName2','funcName3']) ]
    
    # this equal: 
    # from moduleName import funcName,funcName2,funcName3
    # import moduleName2,moduleName3
    modules = [ ('moduleName',['funcName','funcName2','funcName3']),'moduleName2','moduleName3' ]
    
    # start the task, throw exception in case of wrong import
    checkImports(modules)
        
    # code to import them in this file
    for k,v in  __builtin__.modules.iteritems():
        if not k.startswith("_"):
            globals()[k] = v

```
