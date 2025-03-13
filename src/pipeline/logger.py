import logging
import os
from datetime import datetime

LOG_FİLE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FİLE)
os.makedirs(logs_path,exist_ok=True)

LOG_FİLE_PATH=os.path.join(logs_path,LOG_FİLE)

logging.basicConfig(
    filename=LOG_FİLE_PATH,
    format="[%(asctime)s]%(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)

if __name__=="__main__":
    logging.info("logging has started")