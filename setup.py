# Copyright 2020 The MathWorks, Inc.

from setuptools import setup, find_packages

setuptools.setup(
    name="jupyter-matlab-vnc-proxy",
    packages=setuptools.find_packages(where='.'),
    version='0.1.2',
    description="Jupyter extension to provide MATLAB via VNC connection",
    keywords=["Jupyter"],
    entry_points={
        'jupyter_serverproxy_servers': [
            'MATLAB_VNC_DESKTOP = jupyter_matlab_vnc_proxy:setup_desktop',
        ]
    },
    install_requires=['jupyter-server-proxy>=1.4.0'],
    package_data={'jupyter_matlab_vnc_proxy': ['resources/*']},
    include_package_data=True,
    zip_safe=False
)
