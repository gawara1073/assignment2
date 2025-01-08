from setuptools import setup

package_name = 'my_package'

setup(
    name='my_package',
    version='0.0.1',
    packages=[my_package],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + my_packsge]),
        ('share/' + my_package, ['package.xml']),
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
        ],
    },
)

