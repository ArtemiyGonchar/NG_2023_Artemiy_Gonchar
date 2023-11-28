import platform
import cpuinfo , multiprocessing, os

computerSpecs = {}
computerSpecs["Processor"] = ((cpuinfo.get_cpu_info())['brand_raw'])
computerSpecs["Number of CPUs"] = multiprocessing.cpu_count()
computerSpecs["Operating System"] = platform.platform()
computerSpecs["OS Version"] = platform.version().split()[3]+' '+platform.version().split()[4]
computerSpecs["Computer Name"] = platform.node()
computerSpecs["RAM"] = str((os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES'))/(1024.**3)) + "GB"

for specs in computerSpecs:
    print(specs,": ", computerSpecs[specs])