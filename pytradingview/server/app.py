
import threading
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import logging
import sys
import time

MAX_RESTARTS = 3
http_server_active = False

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

http_port_nd = 6001
http_app = FastAPI()

http_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def start_server(nd_http_port, http_port_py):
    global http_port_nd
    http_port_nd = nd_http_port
    logger.info(f"start_server: {nd_http_port} {http_port_py}")
    
    # http_thread = threading.Thread(target=start_http_server, args=(http_port_py,), daemon=True)
    # http_thread.start()
    
    start_http_server(http_port_py)

def start_http_server(http_port_py):
    global http_server_active
    restart_count = 0
    while restart_count < MAX_RESTARTS:
        try:
            http_server_active = True
            logger.info(f"Starting HTTP server on 127.0.0.1:{http_port_py}")
            uvicorn.run(http_app, host="127.0.0.1", port=http_port_py)
        except Exception as e:
            logger.error(f"HTTP server crashed: {str(e)}")
            http_server_active = False
            restart_count += 1
            time.sleep(2)
        else:
            break
    
    if restart_count >= MAX_RESTARTS:
        logger.critical("Max restart attempts reached for HTTP server")
        http_server_active = False
