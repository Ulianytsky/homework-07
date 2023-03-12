from setuptools import setup, find_namespace_packages


setup(
    name = "Clean_folder", 
    version= '0.1',
    license='MIT', 
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['cleanfolder = clean_folder.clean:main']}
)