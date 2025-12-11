import os
from dotenv import load_dotenv


load_dotenv()

token = os.getenv("TOKEN")
admin_ids = {7075258047, 2022851663}
my_db = "my_database.db"
