from setuptools import setup, find_packages

setup(
    name='custom_payroll_ksa',
    version='1.0.0',
    description='Custom Payroll Logic for KSA (EOSB, GOSI, Debit Mapping)',
    author='Your Name',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=['frappe']
)
