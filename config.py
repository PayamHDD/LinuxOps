import os


class Config:

    SSH_HOST = os.getenv("SSH_HOST", "192.168.1.100")
    SSH_PORT = int(os.getenv("SSH_PORT", "22"))

    SSH_USERNAME = os.getenv("SSH_USERNAME", "mcpuser")

    SSH_KEY = os.getenv(
        "SSH_KEY",
        os.path.expanduser("~/.ssh/id_ed25519")
    )

    SSH_TIMEOUT = 10
    COMMAND_TIMEOUT = 30

    MAX_OUTPUT_SIZE = 100_000

    AUDIT_LOG = "logs/audit.log"

    ALLOWED_PATHS = [
        "/etc",
        "/var/log",
        "/proc",
        "/sys"
    ]

    ALLOWED_SERVICES = [
        "sshd",
        "rsyslog",
        "auditd",
        "firewalld",
        "chronyd"
    ]