from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['sim_input_ctrl_move'],
    package_dir={'': 'src'}
)

setup(**d)
