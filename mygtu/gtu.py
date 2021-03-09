import os
import pytz
import ujson
import itertools
from typing import Optional
from datetime import datetime
from .utils import ylist
from pathlib import Path

DIR = Path(__file__).parent.resolve()

class logic:

    def __init__(
        self,
        *,
        branch :str = "IC",
        year :str = "FIRST_YEAR",
        url :str = "https://www.gtu.ac.in/uploads/",
        path :str = (DIR / 'database/subject_code.json'),
        course :str = "BE",
    ) -> None:
        self._branch = branch
        self._year = year
        self._course = course
        self._uri = url
        self._path = path
        
    
    def database(self):
        with open(self._path, "r") as k:
            data = ujson.load(k)
        return data[f"{self._branch}"][f"{self._year}"]
     
    def fetch_uri(self):
        y = ylist.year()
        base = self._uri
        course = self._course
        a = y[0]
        b = y[1]
        c = y[2]
        fetch = [
            f"{base}S{a}/{course}",
            f"{base}S{b}/{course}", 
            f"{base}W{b}/{course}", 
            f"{base}W{c}/{course}"
        ]
        return fetch  
        

    def gather_url(
        self, 
        db: Optional[str] = None,
    ):
        op = [".pdf"]
        db = self.database()
        x = self.fetch_uri()
        z = list(itertools.product(x,db))
        p = list(["/".join(all) for all in z])
        q = list(itertools.product(p, op))
        return list(["".join(all) for all in q])
    
