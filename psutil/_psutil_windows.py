import os
import imp


module_name = os.path.splitext(os.path.basename(__file__))[0]
file_path = os.path.abspath(os.path.join(os.environ["PSUTIL_PLATFORM_PATH"], "{mod}.pyd".format(mod=module_name)))
mod = imp.load_dynamic(module_name, file_path)
locals().update(mod.__dict__)
