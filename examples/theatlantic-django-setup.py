
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='theatlantic-django',
    version="2.0.168",
    description="TheAtlantic.com's Django Frontend",
    author='The Atlantic',
    author_email='programmers@theatlantic.com',
    url='https://github.com/theatlantic/theatlantic-django',
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)
