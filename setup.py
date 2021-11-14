import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
   name='reassessing_the_ins_and_outs_of_unemployment',
   version='0.1',
   description='A package that replicates and extends Shimer (2012) "Reassessing the ins and outs of unemployment"',
   author='Ye Sun',
   author_email='ye.sun1@sciencespo.fr',
   packages=['reassessing_the_ins_and_outs_of_unemployment'],  #same as name
   long_description=long_description,
   long_description_content_type="text/markdown",
   url='https://github.com/caibengbu/ecma33330_proj',
   project_urls={
        "Bug Tracker": "https://github.com/caibengbu/ecma33330_proj/issues",
   },
   classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
   ],
   package_dir={"": "src"},
   packages=setuptools.find_packages(where="src"),
   install_requires=['requests', 'pandas', 'numpy', 'matplotlib', 'wheel', 'setup'], #external packages as dependencies
   python_requires=">=3.6"
)