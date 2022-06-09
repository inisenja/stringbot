import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 10382237
    API_HASH = "6e4642268034e926c875725182a1e32d"
    BOT_TOKEN = "5577052679:AAHlZDwGiBAGi4lNCGJpgkSVFuO1towCE4s-UiDw44-QeR9DHk0S8"
    DATABASE_URL = "postgres://alnydrxa:wYmtQZ-1U9K4D6IlIBJDry4WydD3Iydn@tyke.db.elephantsql.com/alnydrxa"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "@iamsenja"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
