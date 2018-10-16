import sys
import os
import imp

module_name = os.path.splitext(os.path.basename(__file__))[0]
python_version = "{}.{}".format(sys.version_info[0], sys.version_info[1])
ext = "pyd" if sys.platform == "win32" else "so"
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), python_version, "{}.{}".format(module_name, ext)))
mod = imp.load_dynamic(module_name, file_path)
locals().update(mod.__dict__)
