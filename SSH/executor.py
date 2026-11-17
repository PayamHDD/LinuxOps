import shlex

from config import Config
from SSH.connection import SSHConnection


class SSHExecutor:

    def execute(self, command, args=None):

        connection = SSHConnection()

        try:

            client = connection.connect()

            args = args or []

            remote_command = shlex.join(
                [command, *args]
            )

            stdin, stdout, stderr = client.exec_command(
                remote_command,
                timeout=Config.COMMAND_TIMEOUT
            )

            channel = stdout.channel

            exit_code = channel.recv_exit_status()

            output = stdout.read(
                Config.MAX_OUTPUT_SIZE
            ).decode(errors="replace")

            error = stderr.read(
                Config.MAX_OUTPUT_SIZE
            ).decode(errors="replace")

            return {
                "exit_code": exit_code,
                "stdout": output,
                "stderr": error
            }

        finally:

            connection.close()