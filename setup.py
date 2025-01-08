package_name = 'my_package'

from setuptools import setup

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ryota Sugawara',
    maintainer_email='sugawararyota0813@icloud.com',
    description='A ROS 2 package for monitoring and publishing',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'battery_publisher = my_package.battery_publisher:main',
        ],
    },
)

