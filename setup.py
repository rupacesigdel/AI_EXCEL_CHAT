from setuptools import setup, find_packages

setup(
    name='aiexcel',  
    version='0.1.0',  
    description='A brief description of your package',
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown', 
    author='rupacesigdel', 
    author_email='rupeshcgdl2060@gmail.com',  
    url='https://github.com/rupacesigdel/EXCEL_USING_AI',  
    packages=find_packages(), 
    include_package_data=True, 
    install_requires=[
        'numpy', 
        'pandas',
        'requests',

    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.7',
)