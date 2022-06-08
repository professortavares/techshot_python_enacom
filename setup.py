from setuptools import setup, find_packages

setup(
    author="Leonardo D Tavares",
    author_email='leonardo.tavares@enacom.com.br',
    description=".",
    include_package_data=True,
    keywords='.',
    name='enafood',
    packages=find_packages(include=['enafood', 'enafood.*']),
    url='https://github.com/professortavares/techshot_python_enacom',
    version='0.1.1',
)