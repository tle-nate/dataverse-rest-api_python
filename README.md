# dataverse_rest_api

A lightweight Python client for the Dataverse (Dynamics 365) REST API
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
