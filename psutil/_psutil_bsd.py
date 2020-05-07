import os
import imp
import glob

base_module_name = os.path.splitext(os.path.basename(__file__))[0]
file_pattern = os.path.abspath(os.path.join(os.environ["PSUTIL_PLATFORM_PATH"], "*{mod}.so".format(mod=base_module_name)))

try:
    file_path = glob.glob(file_pattern)[0]
    module_name = os.path.splitext(os.path.basename(file_path))[0]
except:
    raise ImportError("Couldn't find psutil platform module in '%s'" % os.environ["PSUTIL_PLATFORM_PATH"])

mod = imp.load_dynamic(module_name, file_path)
locals().update(mod.__dict__)
