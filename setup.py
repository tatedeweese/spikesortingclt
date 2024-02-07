from setuptools import setup, find_packages

setup(
    name = 'spikesortingclt',
    version = '0.1.0',
    description = """Wrapper for Harris SpikeSorting pipeline""",
    author = "Tate DeWeese",
    author_email = "tdewees3@jhmi.edu",
    packages = find_packages(),
    include_package_data=True,
)
