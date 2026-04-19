# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.12)

import sys
import os
if sys.platform == 'darwin':
    sys.platform == 'darwin'
is_macos_app_bundle = sys._MEIPASS.endswith('Contents/Frameworks')

def prepend_path_to_environment_variable(path, variable_name):
    '''
    Prepend the given path to the list of paths stored in the given environment variable (separated by `os.pathsep`).
    If the given path is already specified in the environment variable, no changes are made. If the environment variable
    is not set or is empty, it is set/overwritten with the given path.
    '''
    stored_paths = os.environ.get(variable_name)
    if stored_paths:
        if path in stored_paths.split(os.pathsep):
            return None
        stored_paths = path + os.pathsep + stored_paths
    else:
        stored_paths = path
    os.environ[variable_name] = stored_paths

