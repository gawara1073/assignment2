from setuptools import setup

package_name = 'my_package'

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
    description='My ROS2 package',
    license='BSD-3-Clause',
    entry_points={
        'console_scripts': [
            'battery_publisher = my_package.battery_publisher:main',
        ],
    },
)

