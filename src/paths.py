from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = PROJECT_DIR / "logs" / "provisioning.log"
INSTALL_SCRIPT = PROJECT_DIR / "scripts" / "install.sh"
INSTANCES_FILE = PROJECT_DIR / "configs" / "instances.json"
ALLOWED_VALUES_FILE = PROJECT_DIR / "configs" / "allowed_values.json"