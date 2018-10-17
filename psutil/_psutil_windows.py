import sys
import os
import imp
from distutils import sysconfig


module_name = os.path.splitext(os.path.basename(__file__))[0]
python_version = sysconfig.get_python_version()
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), python_version, sys.platform, "{mod}.pyd".format(mod=module_name)))
mod = imp.load_dynamic(module_name, file_path)
locals().update(mod.__dict__)
