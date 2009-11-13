from setuptools import setup, find_packages

setup(name="django-paypal-api",
           version="0.1",
           description="Paypal API with django integration",
           author="Brian Guertin",
           author_email="dev@brianguertin.com",
           packages=find_packages(),
           include_package_data=True,
)

