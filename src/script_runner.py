import logging
import platform
import subprocess
from paths import INSTALL_SCRIPT

def run_install_script():
    if platform.system() == "Windows":
        message = "This project cannot be run on native Windows. Please run from WSL/Linux/macOS."
        logging.error(message)
        raise RuntimeError(message)

    if not INSTALL_SCRIPT.exists():
        message = "Install script not found at: " + str(INSTALL_SCRIPT)
        logging.error(message)
        raise FileNotFoundError(message)
    
    logging.info("About to run: " + str(INSTALL_SCRIPT))
    try:
        result = subprocess.run(["bash", str(INSTALL_SCRIPT)], check=True, capture_output=True, text=True)
        if result.stdout:
            logging.info("Script stdout:\n" + result.stdout)
        message = "Install script completed successfully"
        logging.info(message)
        print(message)

    except subprocess.CalledProcessError as e:
        logging.exception("Install script failed with return code: " + str(e.returncode))
        if e.stderr: # Script error
            logging.error("Script stderr:\n" + e.stderr)
        raise