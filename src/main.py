# ID: 011890402, Name: Preston Backhaus

from packagedata import create_packages
from hashtable import HashTable

# Create packages, add to hashtable
packages = create_packages()
hashtable = HashTable(40)
for package in packages:
    hashtable.hash_insert(package)


