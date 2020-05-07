import excons
import os
import sys
from excons.tools import python
from distutils import sysconfig
import struct


version = "5.7.0"
env = excons.MakeBaseEnv()
python_version = excons.GetArgument("with-python", sysconfig.get_python_version())
ext = python.ModuleExtension()

prjs = []


cppflags = ""
linkflags = ""
defs = ["PSUTIL_VERSION={ver}".format(ver=version.replace(".", ""))]
outputs = []
out_dir = excons.OutputBaseDirectory()
mod_pfx = excons.GetArgument("module-prefix", "")

if struct.calcsize("l") <= 8:
    defs.append("PSUTIL_SIZEOF_PID_T=4")
else:
    defs.append("PSUTIL_SIZEOF_PID_T=8")

if os.name == "posix":
    defs.append("PSUTIL_POSIX=1")

if sys.platform != "win32":
    cppflags += " -Wno-unused-parameter"

    if sys.platform == "darwin":
        linkflags += " -framework IOKit -framework CoreFoundation"
        modname = "%s_psutil_osx" % mod_pfx
        defs.append("PSUTIL_OSX=1")
        prjs.append({"name": modname,
                     "type": "dynamicmodule",
                     "alias": "psutil-libs",
                     "defs": defs + ["PSUTIL_MODULE_NAME=%s" % modname],
                     "ext": ext,
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
        outputs.append("{outdir}/psutil/{pyver}/{plat}/_psutil_osx{ext}".format(outdir=out_dir, pyver=python_version, plat=sys.platform, ext=ext))

    else:
        modname = "%s_psutil_linux" % mod_pfx
        defs.append("PSUTIL_LINUX=1")
        prjs.append({"name": modname,
                     "type": "dynamicmodule",
                     "alias": "psutil-libs",
                     "defs": defs + ["PSUTIL_MODULE_NAME=%s" % modname],
                     "ext": ext,
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
        outputs.append("{outdir}/psutil/{pyver}/{plat}/_psutil_linux{ext}".format(outdir=out_dir, pyver=python_version, plat=sys.platform, ext=ext))

    modname = "%s_psutil_posix" % mod_pfx
    prjs.append({"name": modname,
                 "type": "dynamicmodule",
                 "alias": "psutil-libs",
                 "defs": defs + ["PSUTIL_MODULE_NAME=%s" % modname],
                 "ext": ext,
                 "prefix": "psutil/{pyver}/{plat}".format(pyver=python_version, plat=sys.platform),
                 "cppflags": cppflags,
                 "linkflags": linkflags,
                 "incdirs": ["psutil"],
                 "symvis": "default",
                 "srcs": ["psutil/_psutil_common.c",
                         "psutil/_psutil_posix.c"],
                 "deps": [],
                 "custom": [python.SoftRequire]})
    outputs.append("{outdir}/psutil/{pyver}/{plat}/_psutil_posix{ext}".format(outdir=out_dir, pyver=python_version, plat=sys.platform, ext=ext))

else:
    def get_winver():
        maj, min = sys.getwindowsversion()[0:2]
        return '0x0%s' % ((maj * 100) + min)

    cppflags += " /wd4152 /wd4306 /wd4127 /wd4189 /wd4100 /wd4244 /wd4201 /wd4706 /wd4701 /wd4214 /wd4057 /wd4204"
    modname = "%s_psutil_windows" % mod_pfx

    defs.extend(["PSUTIL_WINDOWS=1",
                 "PSAPI_VERSION=1",
                 "_WIN32_WINNT=%s" % get_winver(),
                 "_AVAIL_WINVER_=%s" % get_winver(),
                 "_CRT_SECURE_NO_WARNINGS"])

    prjs.append({"name": modname,
                 "type": "dynamicmodule",
                 "alias": "psutil-libs",
                 "defs": defs + ["PSUTIL_MODULE_NAME=%s" % modname],
                 "ext": ext,
                 "prefix": "psutil/{pyver}/{plat}".format(pyver=python_version, plat=sys.platform),
                 "cppflags": cppflags,
                 "linkflags": linkflags,
                 "incdirs": ["psutil"],
                 "srcs": ["psutil/_psutil_common.c",
                          "psutil/_psutil_windows.c",
                          "psutil/arch/windows/process_utils.c",
                          "psutil/arch/windows/process_info.c",
                          "psutil/arch/windows/process_handles.c",
                          "psutil/arch/windows/disk.c",
                          "psutil/arch/windows/net.c",
                          "psutil/arch/windows/cpu.c",
                          "psutil/arch/windows/security.c",
                          "psutil/arch/windows/services.c",
                          "psutil/arch/windows/socks.c",
                          "psutil/arch/windows/wmi.c"],
                 "deps": [],
                 "libs": ["psapi", "kernel32", "advapi32", "shell32", "netapi32", "wtsapi32", "ws2_32", "PowrProf", "pdh"],
                 "custom": [python.SoftRequire]})
    outputs.append("{outdir}/psutil/{pyver}/{plat}/_psutil_windows{ext}".format(outdir=out_dir, pyver=python_version, plat=sys.platform, ext=ext))


prjs.append({"name": "psutil",
             "alias": "psutil-py",
             "type": "install",
             "install": {"psutil": excons.Glob("psutil/*.py")}
             })
outputs += map(lambda x: "{outdir}/{path}".format(outdir=out_dir, path=x.get_path()), excons.Glob("psutil/*.py"))

def PsutilOutputs():
    return outputs


excons.DeclareTargets(env, prjs)


Export("PsutilOutputs")
