from setuptools import setup

package_name = 'my_package'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'psutil'],
    zip_safe=True,
    maintainer='Ryota Sugawara',
    maintainer_email='sugawararyota0813@icloud.com',
    description='A ROS 2 package for monitoring and publishing battery charge and consumption.',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'battery_publisher = my_package.battery_publisher:main',
            'battery_listener = my_package.battery_listener:main',
        ],
    },
)

