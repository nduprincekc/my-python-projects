import platform

uname = platform.uname()
print(f'System:{uname.system}')
print(f'Node:{uname.node}')
print(f'Release:{uname.release}')
print(f'Version:{uname.version}')
print(f'Machine:{uname.machine}')
print(f'Processor:{uname.processor}')
