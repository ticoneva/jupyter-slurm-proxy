import setuptools

setuptools.setup(
    name="jupyter-slurm-proxy",
    version='0.0.1',
    url="https://github.com/scrp-cuhk/jupyter-slurm-proxy",
    author="Vinci Chow",
    description="Jupyter extension to launch Jupyter on Slurm nodes",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy>=3.2.2'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'rstudio = jupyter_slurm_proxy:setup_ssh'
        ]
    },
    package_data={
        'jupyter_slurm_proxy': ['icons/jupyter.svg'],
    },
)
