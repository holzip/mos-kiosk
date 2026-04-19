# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.12)

'''A pure Python implementation of import.'''
__all__ = [
    '__import__',
    'import_module',
    'invalidate_caches',
    'reload']
import _imp
import sys

try:
    import _frozen_importlib as _bootstrap
    _bootstrap.__name__ = 'importlib._bootstrap'
    _bootstrap.__package__ = 'importlib'
    
    try:
        _bootstrap.__file__ = __file__.replace('__init__.py', '_bootstrap.py')
        sys.modules['importlib._bootstrap'] = _bootstrap
        
        try:
            import _frozen_importlib_external as _bootstrap_external
            _bootstrap_external.__name__ = 'importlib._bootstrap_external'
            _bootstrap_external.__package__ = 'importlib'
            
            try:
                _bootstrap_external.__file__ = __file__.replace('__init__.py', '_bootstrap_external.py')
                sys.modules['importlib._bootstrap_external'] = _bootstrap_external
                _pack_uint32 = _bootstrap_external._pack_uint32
                _unpack_uint32 = _bootstrap_external._unpack_uint32
                import warnings
                from _bootstrap import __import__
                
                def invalidate_caches():
                    '''Call the invalidate_caches() method on all meta path finders stored in
    sys.meta_path (where implemented).'''
                    for finder in sys.meta_path:
                        if not hasattr(finder, 'invalidate_caches'):
                            continue
                        finder.invalidate_caches()

                
                def import_module(name, package = (None,)):
                    """Import a module.

    The 'package' argument is required when performing a relative import. It
    specifies the package to use as the anchor point from which to resolve the
    relative import to an absolute import.

    """
                    level = 0
                    if name.startswith('.'):
                        if not package:
                            raise TypeError(f'''the \'package\' argument is required to perform a relative import for {name!r}''')
                        for character in name:
                            if character != '.':
                                name
                            else:
                                level += 1
                    return _bootstrap._gcd_import(name[level:], package, level)

                _RELOADING = { }
                
                def reload(module):
                    '''Reload the module and return it.

    The module must have been successfully imported before.

    '''
                    pass
                # WARNING: Decompyle incomplete

                return None
                except NameError:
                    continue
                except ImportError:
                    from  import _bootstrap
                    _bootstrap._setup(sys, _imp)
                    continue
            except NameError:
                continue
                except ImportError:
                    from  import _bootstrap_external
                    _bootstrap_external._set_bootstrap_module(_bootstrap)
                    _bootstrap._bootstrap_external = _bootstrap_external
                    continue




