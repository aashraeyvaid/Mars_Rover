from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'mars_rover_description'


# Collect all model files while preserving directory structure
model_files = []

for root, dirs, files in os.walk('models'):
    if files:
        model_files.append(
            (
                os.path.join('share', package_name, root),
                [os.path.join(root, f) for f in files]
            )
        )


setup(
    name=package_name,
    version='0.0.0',

    packages=find_packages(exclude=['test']),

    data_files=[
        # Register package with ROS 2
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),

        # Install package.xml
        (
            'share/' + package_name,
            ['package.xml']
        ),

        # Install launch files
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')
        ),

        # Install config files
        (
            os.path.join('share', package_name, 'config'),
            glob('config/*.yaml')
        ),

        # Install all model files
        *model_files,
    ],

    install_requires=['setuptools'],

    zip_safe=True,

    maintainer='aashraey-vaid',
    maintainer_email='aashraeyvaid3@gmail.com',

    description='Mars rover robot description package',

    license='Apache-2.0',

    extras_require={
        'test': [
            'pytest',
        ],
    },

    entry_points={
        'console_scripts': [],
    },
)