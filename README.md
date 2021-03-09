# mygtu

download old gtu papers 
with async downloader.


# Installation Guide.
(recommanded.)
```text
pip install mygtu
```
```text
pip3 install --no-cache git+https://github.com/batatavadaX/testgtu.git
```

# Basic Example.

```py
# default values are set to BE IC.

from mygtu import dl, gf
import asyncio

async def main():
    urls = gf.gather_url()
    await dl.download(urls)

asyncio.run(main())


# will download all the old papers of ic branch.
```



# Another Example.
```py
# you can pass your own values as json.

from mygtu import dl, logic
import asyncio

async def main():
    gf = logic(
    path="path/to_json.json", 
    branch="IC", 
    year="FIRST_YEAR",
    course="BE"
    )
    db = gf.database()
    urls = gf.gather_url(db)
    await dl.download(urls)

asyncio.run(main())
```

# Json Example.

```json
{
    "IC":{
        "FIRST_YEAR":[
            "3110006",
            "3110003",
            "3110005",
            "3110007",
            "3110014"
        ]
    }
}
```

```py
# pass json file path
from mygtu import logic
gf = logic(path="path/to_json.json")
```

# Note.

=>i was writing this and same day gtu declared
exam time-table so i am publishing half work,
it may be unstable because its not tested.

=>this software is not developed by gtu.
