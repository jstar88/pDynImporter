pDynImporter
============

Check for correct modules and import them in globals

```python
    from pDynImporter import my_imports
    
    # this equal: from moduleName import funcName 
    modules = [ ('moduleName',['funcName']) ]
    
    # this equal: from moduleName import funcName,funcName2,funcName3
    modules = [ ('moduleName',['funcName','funcName2','funcName3']) ]
    
    # this equal: 
    # from moduleName import funcName,funcName2,funcName3
    # import moduleName2,moduleName3
    modules = [ ('moduleName',['funcName','funcName2','funcName3']),'moduleName2','moduleName3' ]
    
    # in global scope
    errors = my_imports(modules)
    
    # errors contains the first wrong module.
    # if empty then all imports are made
    # Else imports after the wrong one are not made
    if errors:
        print errors
        
        
    # code to import them in this file
    
    for k,v in  __builtin__.modules.iteritems():
        if not k.startswith("_"):
            globals()[k] = v

```
