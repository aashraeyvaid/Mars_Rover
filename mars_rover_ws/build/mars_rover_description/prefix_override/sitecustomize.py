import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/aashraey-vaid/mars_rover_ws/install/mars_rover_description'
