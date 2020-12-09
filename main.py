from dotenv import DotEnv

dotenv = DotEnv()
NUTRIONIX_APP_ID = dotenv.get('NUTRI_APP_ID')
NUTRIONIX_API_KEY = dotenv.get('NUTRI_API_KEY')
