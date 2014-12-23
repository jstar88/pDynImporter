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
    my_imports(modules)

```
