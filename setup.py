# setup.py
import io
import os

from setuptools import find_packages, setup

# -- 1) Locate this file's directory -------------------------------
here = os.path.abspath(os.path.dirname(__file__))

# -- 2) Utility to load README -------------------------------------
long_description = """
A lightweight Python client for connecting to the Dataverse (Dynamics 365) REST API 
with no-fuss browser based login.  

## Installation

```bash
pip install dataverse-rest-api
```

## Usage

```python
from dataverse_rest_api import DataverseClient

client = DataverseClient("https://yourorg.crm.dynamics.com")

client.authenticate()

# Query top 5 contacts
contacts = client.query("contacts", odata="$top=5")
print(contacts)

# Create a new contact
new_contact_id = client.create(
    "contacts", 
    {"firstname": "Sam", "lastname": "Smith"}
)
print(new_contact_id)

# Update that contact
client.patch_record(
    "contacts", 
    new_contact_id,
    {"jobtitle": "Software Engineer"}
)

# Delete the contact
client.delete_record("contacts", new_contact_id)

# Or send a fully custom request
resp = client.send_request(
    method="POST",
    endpoint="api/data/v9.2/tle_mycustomapi",
    data={}
)
print(resp.json())

# Reset the client and clear any cached access tokens 
client.reset() 
```
"""


# -- 3) Setup() -----------------------------------------------------
setup(
    name="dataverse_rest_api",
    version="0.4.3",
    description="Lightweight Python client for connecting to the Dataverse REST API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="tlenate",
    license="MIT",

    # GitHub project URLs
    url="https://github.com/tle-nate/dataverse-rest-api_python",
    project_urls={
        "Source": "https://github.com/tle-nate/dataverse-rest-api_python",
        "Issue Tracker": "https://github.com/tle-nate/dataverse-rest-api_python/issues",
    },

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],

    keywords="dataverse dynamics365 msal device-flow rest api client",

    # discover all packages (make sure __init__.py exists in each!)
    packages=find_packages(
        include=["dataverse_rest_api", "dataverse_rest_api.*"]),

    include_package_data=True,
    python_requires=">=3.7",
    install_requires=[
        "msal>=1.0.0",
        "requests>=2.20.0",
    ],
)
