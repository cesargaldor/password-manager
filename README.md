[![Python 3.7](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/)

# Password manager

This is a password manager made with Python and MongoDB.

## Installation

Before starting to use this script, you must install PyMongo.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install it.

```bash
pip install pymongo
```

Also, you have to set up your MongoDB database and collection. I recommend you to follow the first 5 minutes of [this video.](https://www.youtube.com/watch?v=rE_bJl2GAY8)

## Usage

1. When you download this repository, you must create 2 new files.
2. First file ```masterpw.py``` where you must declare ```MASTERPW = "yourMasterPasswordHere"```.
3. Second file ```mongodb.py``` with the following code. You have to replace 
```yourMongoDBuser``` , ```yourMongoDBpassword```, ```NameOfYourDatabase``` and ```NameOfYourCollection```  with the actual values.

```python
import pymongo
from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://yourMongoDBuser:yourMongoDBpassword@db-oaqga.mongodb.net/test?retryWrites=true&w=majority"
)

db = cluster["NameOfYourDatabase"]
collection = db["NameOfYourCollection"]
```
4. Run ```main.py``` and enjoy.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
