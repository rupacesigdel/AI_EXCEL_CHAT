from setuptools import setup, find_packages

setup(
    name='aiexcel',  # Replace with your package name
    version='0.1.0',  # Replace with your version
    description='A brief description of your package',
    long_description=open('README.md').read(),  # Optional: long description from a README file
    long_description_content_type='text/markdown',  # Optional: content type of the long description
    author='rupacesigdel',  # Replace with your name
    author_email='rupeshcgdl2060@gmail.com',  # Replace with your email
    url='https://github.com/rupacesigdel/EXCEL_USING_AI',  # Replace with the URL of your package repository
    packages=find_packages(),  # Automatically find and include all packages in the directory
    include_package_data=True,  # Include package data specified in MANIFEST.in
    install_requires=[
        'numpy',  # List your dependencies here
        'pandas',
        'requests',
        # Add other dependencies as needed
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',  # Replace with appropriate status
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # Replace with your license
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        # Add other classifiers as needed
    ],
    python_requires='>=3.7',
)
