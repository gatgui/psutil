import excons
import sys
from excons.tools import python

version = "5.4.7"
env = excons.MakeBaseEnv()
python_version = "{}.{}".format(sys.version_info[0], sys.version_info[1])


prjs = []
defs = ["PSUTIL_OSX", "PSUTIL_VERSION={}".format(version.replace(".", ""))]
cppflags = ""
linkflags = ""
posix = ["psutil/_psutil_posix.c", "psutil/_psutil_common.c"]


if sys.platform == "darwin":
    cppflags += " -Wno-unused-parameter"
    linkflags += " -framework IOKit -framework CoreFoundation"


if sys.platform == "darwin":
    prjs.append({"name": "_psutil_posix",
                 "type": "dynamicmodule",
                 "alias": "psutil-libs",
                 "defs": defs,
                 "ext": python.ModuleExtension(),
                 "prefix": "python/psutil/{}".format(python_version),
                 "cppflags": cppflags,
                 "linkflags": linkflags,
                 "incdirs": ["psutil"],
                 "symvis": "default",
                 "srcs": posix,
                 "deps": [],
                 "custom": [python.SoftRequire]})

    prjs.append({"name": "_psutil_osx",
                 "type": "dynamicmodule",
                 "alias": "psutil-libs",
                 "defs": defs,
                 "ext": python.ModuleExtension(),
                 "prefix": "python/psutil/{}".format(python_version),
                 "cppflags": cppflags,
                 "linkflags": linkflags,
                 "incdirs": ["psutil"],
                 "symvis": "default",
                 "srcs": posix + ["psutil/_psutil_osx.c",
                                  "psutil/arch/osx/process_info.c"],
                 "deps": [],
                 "custom": [python.SoftRequire]})


prjs.append({"name": "psutil",
             "type": "install",
             "install": {"python/psutil": excons.Glob("psutil/*.py")}
             })

excons.DeclareTargets(env, prjs)
