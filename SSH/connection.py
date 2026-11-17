import paramiko

from config import Config


class SSHConnection:

    def __init__(self):

        self.client = None

    def connect(self):

        self.client = paramiko.SSHClient()

        self.client.load_system_host_keys()

        self.client.set_missing_host_key_policy(
            paramiko.RejectPolicy()
        )

        self.client.connect(
            hostname=Config.SSH_HOST,
            port=Config.SSH_PORT,
            username=Config.SSH_USERNAME,
            key_filename=Config.SSH_KEY,
            timeout=Config.SSH_TIMEOUT,
            banner_timeout=Config.SSH_TIMEOUT,
            auth_timeout=Config.SSH_TIMEOUT
        )

        return self.client

    def close(self):

        if self.client:

            self.client.close()
            self.client = None