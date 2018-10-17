import excons
import sys
from excons.tools import python
from distutils import sysconfig


version = "5.4.7"
env = excons.MakeBaseEnv()
python_version = excons.GetArgument("with-python", sysconfig.get_python_version())


prjs = []


cppflags = ""
linkflags = ""
defs = ["PSUTIL_VERSION={ver}".format(ver=version.replace(".", ""))]


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
                     "prefix": "psutil/{pyver}/{plat}".format(pyver=python_version, plat=sys.platform),
                     "cppflags": cppflags,
                     "linkflags": linkflags,
                     "incdirs": ["psutil"],
                     "symvis": "default",
                     "srcs": ["psutil/_psutil_common.c",
                              "psutil/_psutil_posix.c",
                              "psutil/_psutil_osx.c",
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
                     "prefix": "psutil/{pyver}/{plat}".format(pyver=python_version, plat=sys.platform),
                     "cppflags": cppflags,
                     "linkflags": linkflags,
                     "incdirs": ["psutil"],
                     "symvis": "default",
                     "srcs": ["psutil/_psutil_common.c",
                              "psutil/_psutil_posix.c",
                              "psutil/_psutil_linux.c"],
                     "deps": [],
                     "custom": [python.SoftRequire]})

    prjs.append({"name": "_psutil_posix",
             "type": "dynamicmodule",
             "alias": "psutil-libs",
             "defs": defs,
             "ext": python.ModuleExtension(),
             "prefix": "psutil/{pyver}/{plat}".format(pyver=python_version, plat=sys.platform),
             "cppflags": cppflags,
             "linkflags": linkflags,
             "incdirs": ["psutil"],
             "symvis": "default",
             "srcs": ["psutil/_psutil_common.c",
                      "psutil/_psutil_posix.c"],
             "deps": [],
             "custom": [python.SoftRequire]})

else:
    cppflags += " /wd4152 /wd4306 /wd4127 /wd4189 /wd4100 /wd4244 /wd4201 /wd4706 /wd4701"
    defs.append("PSUTIL_WINDOWS")

    prjs.append({"name": "_psutil_windows",
                 "type": "dynamicmodule",
                 "alias": "psutil-libs",
                 "defs": defs,
                 "ext": python.ModuleExtension(),
                 "prefix": "psutil/{pyver}/{plat}".format(pyver=python_version, plat=sys.platform),
                 "cppflags": cppflags,
                 "linkflags": linkflags,
                 "incdirs": ["psutil"],
                 "srcs": ["psutil/_psutil_common.c",
                          "psutil/_psutil_windows.c",
                          "psutil/arch/windows/process_info.c",
                          "psutil/arch/windows/process_handles.c",
                          "psutil/arch/windows/security.c",
                          "psutil/arch/windows/inet_ntop.c",
                          "psutil/arch/windows/services.c",],
                 "deps": [],
                 "libs": ["psapi", "kernel32", "advapi32", "shell32", "netapi32", "iphlpapi", "wtsapi32", "ws2_32", "PowrProf"],
                 "custom": [python.SoftRequire]})


prjs.append({"name": "psutil",
             "alias": "psutil-py",
             "type": "install",
             "install": {"psutil": excons.Glob("psutil/*.py")}
             })

excons.DeclareTargets(env, prjs)
