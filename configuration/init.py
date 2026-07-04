from configuration.models import SystemSetting
from configuration.manager import ConfigurationManager

from database.engine import SessionLocal

def initialize_settings():

    session=SessionLocal()
    manager=ConfigurationManager(session)

    defaults=[
        {
            "key":"AQI_STANDARD",
            "value":"CPCB",
            "datatype":"string",
            "description":"Current AQI Standard"
        },

        {
            "key":"CAMPUS_NAME",
            "value":"Kristu Jayanti University, Central Campus",
            "datatype":"string",
            "description":"Campus Name"
        },

        {
            "key":"REFRESH_INTERVAL",
            "value":"5",
            "datatype":"integer",
            "description":"Dashboard Refresh Interval"
        }
    ]

    for item in defaults:
        existing=manager.get_setting(item["key"])

        if existing is None:
            manager.save_setting(
                SystemSetting(**item)
            )

            session.close()
            print("Configuration initialized.")

if __name__=="__main__":
    initialize_settings()