from setuptools import setup

package_name = 'v2x_servicedummy'

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
    maintainer='zdm',
    maintainer_email='notanemail@donotuse.home',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'servicedummynode = v2x_servicedummy.servicedummynode:main'
        ],
    },
)
