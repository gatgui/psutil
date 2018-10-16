import excons
import sys
from excons.tools import python

version = "5.4.7"
env = excons.MakeBaseEnv()
python_version = "{}.{}".format(sys.version_info[0], sys.version_info[1])


prjs = []


cppflags = ""
linkflags = ""
defs = ["PSUTIL_VERSION={}".format(version.replace(".", ""))]
posix = ["psutil/_psutil_posix.c", "psutil/_psutil_common.c"]


if sys.platform != "win32":
    cppflags += " -Wno-unused-parameter"

    if sys.platform == "darwin":
        linkflags += " -framework IOKit -framework CoreFoundation"
        defs.append("PSUTIL_OSX")
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

    else:
        defs.append("PSUTIL_LINUX")
        prjs.append({"name": "_psutil_linux",
                     "type": "dynamicmodule",
                     "alias": "psutil-libs",
                     "defs": defs,
                     "ext": python.ModuleExtension(),
                     "prefix": "python/psutil/{}".format(python_version),
                     "cppflags": cppflags,
                     "linkflags": linkflags,
                     "incdirs": ["psutil"],
                     "symvis": "default",
                     "srcs": posix + ["psutil/_psutil_linux.c"],
                     "deps": [],
                     "custom": [python.SoftRequire]})


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


prjs.append({"name": "psutil",
             "type": "install",
             "install": {"python/psutil": excons.Glob("psutil/*.py")}
             })

excons.DeclareTargets(env, prjs)
