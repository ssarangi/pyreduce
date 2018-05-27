import platform
import cpuinfo

from protos.models_pb2 import CPUInfo, PythonInfo


def cpu_info_gatherer():
    info = cpuinfo.get_cpu_info()
    cpu_info = CPUInfo()
    cpu_info.arch = info['arch']
    cpu_info.bits = info['bits']
    cpu_info.brand = info['brand']
    cpu_info.count = info['count']
    cpu_info.cpu_version = str(info['cpuinfo_version'])
    cpu_info.family = info['family']
    cpu_info.L2_cache_size = int(info['l2_cache_size'])
    return cpu_info


def python_info_gatherer():
    python_tuple = platform.python_version_tuple()
    python_info = PythonInfo(major_version=int(python_tuple[0]),
                             minor_version=int(python_tuple[1]),
                             revision=int(python_tuple[2]))
    return python_info


def system_info_gatherer():
    cpu_infos = cpu_info_gatherer()
    python_info = python_info_gatherer()

    return cpu_infos, python_info
