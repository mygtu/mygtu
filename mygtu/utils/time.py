from datetime import datetime 
import pytz

class time:
    @staticmethod 
    def current(zone='Asia/Kolkata', strf='%Y') -> int: 
        return datetime.now( 
            pytz.timezone( 
                zone 
                ) 
            ).strftime(
                strf
            )
