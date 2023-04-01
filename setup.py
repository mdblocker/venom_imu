from setuptools import setup

package_name = 'venom_imu'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mdblocker',
    maintainer_email='mdaltonblocker@gmail.com',
    description='Publisher for H1 Venom IMU data',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'talker = venom_imu.publisher_member_function:main',
        ],
    },
)
