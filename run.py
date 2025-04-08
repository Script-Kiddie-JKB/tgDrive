# import os 
# import runpy
# import requests
# import time
# from dotenv import load_dotenv
# load_dotenv()

# def is_alive():
#   repl_slug = os.environ.get("REPL_SLUG")
#   repl_owner = os.environ.get("REPL_OWNER")
#   repl_url = f"https://{repl_slug}.{repl_owner}.repl.co"
#   repl_url_local = "http://0.0.0.0:8080"
#   try:
#     resp = requests.get(repl_url_local, timeout=60)
#   except Exception as e:
#     print("Server response wait timed out!")
#     return False
#   return resp.ok

# def run_safe():
#   "prevent session string from expiring due to two instances running"
#   try:
#     if not is_alive():
#       kill_server()
#       print("Starting a new instance...")
#       # runpy.run_module('app', run_name="tgindex")
#       os.system("python3 -m app")
#     else:
#       print("Server is already running...")
#   except Exception as e:
#     print(f"Your session String has been revoked due to {e}. \n\n Please generate New one.")
#     os.system("python app/generate_session_string.py") 
  
# def kill_server():
#   print("Killing server just incase it is not responding...")
#   kill_server_cmd = "pkill -9 -f 'python3 -m app'"
#   os.system(kill_server_cmd)
#   time.sleep(30)
    
# run_safe()

# import os 
# import runpy
# import requests
# import psutil

# from dotenv import load_dotenv
# load_dotenv()

# IP_FILE = "ip.txt"

# def get_ip():
#     import socket   
#     hostname = socket.gethostname()   
#     IPAddr = socket.gethostbyname(hostname)   
#     print("Your Current IP Address is:" + IPAddr)
#     process_name = os.path.basename(__file__)
#     print("Your current process name is: " + process_name)
#     return IPAddr

# def update_ip_file():
#     "save the current ip"
#     with open(IP_FILE, "w") as f:
#         f.write(get_ip())

# def load_ip():
#     with open(IP_FILE, "r") as f:
#         return f.read()

# current_ip = get_ip()
# last_ip = load_ip()

# def is_alive():
#     repl_slug = os.environ.get("REPL_SLUG")
#     repl_owner = os.environ.get("REPL_OWNER")
#     resp = requests.get(f"https://{repl_slug}.{repl_owner}.repl.co")
#     return resp.ok

# def run_safe():
#     if not is_alive():
#         runpy.run_module('app')
#     else:
#         print("Server is already running...")
    
# # prevent session string from expiring when ip gets changed
# # p = find_process("python3 run.py")
# if current_ip != last_ip:
#     print(f"IP has been changed from {last_ip} to {current_ip}")
#     update_ip_file()
#     # kill the server here
#     kill_server_cmd = "pkill -9 -f 'python3 run.py'"
#     os.system(kill_server_cmd)
#     kill_server_by_self()

# run_safe()

# def kill_server_by_self():
#     import os
#     process_name = os.path.basename(__file__)
#     for proc in psutil.process_iter():
#         if proc.name() == process_name:
#             proc.kill()
#             print(f"{process_name} server has been killed")
#             return
#     print(f"{process_name} server not found")

# import os 
# import runpy
# import requests
# import time
# from dotenv import load_dotenv
# load_dotenv()

# def is_alive():
#   repl_slug = os.environ.get("REPL_SLUG")
#   repl_owner = os.environ.get("REPL_OWNER")
#   repl_url = f"https://{repl_slug}.{repl_owner}.repl.co"
#   repl_url_local = "http://0.0.0.0:8080"
#   try:
#     resp = requests.get(repl_url_local, timeout=60)
#   except Exception as e:
#     print("Server response wait timed out!")
#     return False
#   return resp.ok

# def run_safe():
#   "prevent session string from expiring due to two instances running"
#   try:
#     if not is_alive():
#       kill_server()
#       print("Starting a new instance...")
#       # runpy.run_module('app', run_name="tgindex")
#       os.system("python3 -m app")
#     else:
#       print("Server is already running...")
#   except Exception as e:
#     print(f"Your session String has been revoked due to {e}. \n\n Please generate New one.")
#     os.system("python app/generate_session_string.py") 
  
# def kill_server():
#   print("Killing server just incase it is not responding...")
#   kill_server_cmd = "pkill -9 -f 'python3 -m app'"
#   os.system(kill_server_cmd)
#   time.sleep(30)
    
# run_safe()


import os 
import runpy
import requests
import time
import psutil    
from dotenv import load_dotenv

load_dotenv()

APP_CMD = "python3 -m app"

def find_process_cmd(cmdline):
  for proc in psutil.process_iter():
    is_running = cmdline in proc.cmdline() 
    if(is_running):
      return True

def is_alive():
  repl_slug = os.environ.get("REPL_SLUG")
  repl_owner = os.environ.get("REPL_OWNER")
  repl_url = f"https://{repl_slug}.{repl_owner}.repl.co"
  repl_url_local = "http://0.0.0.0:8080"
  try:
    resp = requests.get(repl_url_local, timeout=60)
  except Exception as e:
    print("Server response wait timed out!")
    return False
  return resp.ok

def run_safe():
  "prevent session string from expiring due to two instances running"
  try:
    if not is_alive():
      kill_server()
      # proc = runpy.run_module('app', alter_sys=True)
      if not find_process_cmd(APP_CMD):
        # prevent running app if it is already running  
        print("Starting a new instance...")
        os.system(APP_CMD)
    else:
      print("Server is already running...")
  except Exception as e:
    os.system("python app/generate_session_string.py") 
  
def kill_server():
  print("Killing server just incase it is not responding...")
  kill_server_cmd = f"pkill -9 -f '{APP_CMD}'"
  os.system(kill_server_cmd)
  time.sleep(30)
    
run_safe()


# import os
# import psutil
# import requests
# import time
# import subprocess
# from dotenv import load_dotenv

# load_dotenv()

# APP_CMD = "python3 -m app"

# def find_process_cmd(cmdline):
#     for proc in psutil.process_iter():
#         is_running = cmdline in proc.cmdline()
#         if is_running:
#             return True
#     return False

# def is_alive():
#     repl_slug = os.environ.get("REPL_SLUG")
#     repl_owner = os.environ.get("REPL_OWNER")
#     repl_url = f"https://{repl_slug}.{repl_owner}.repl.co"
#     repl_url_local = "http://0.0.0.0:8080"
#     try:
#         resp = requests.get(repl_url_local, timeout=60)
#     except Exception as e:
#         print("Server response wait timed out!")
#         return False
#     return resp.ok

# def run_safe():
#     try:
#         if not is_alive():
#             kill_server()
#             if not find_process_cmd(APP_CMD):
#                 print("Starting a new instance...")
#                 subprocess.run(APP_CMD.split())
#         else:
#             print("Server is already running...")
#     except Exception as e:
#         subprocess.run("python app/generate_session_string.py".split()) 

# def kill_server():
#     print("Killing server just incase it is not responding...")
#     subprocess.run(["pkill", "-9", "-f", APP_CMD])
#     time.sleep(30)
    
# run_safe()
