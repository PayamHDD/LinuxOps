from ssh.executor import SSHExecutor

from logging.audit import audit_log


def register(mcp):

    @mcp.tool()
    def get_system_info() -> dict:

        """
        Get basic Linux system information.
        """

        audit_log(
            "get_system_info",
            "uname -a"
        )

        executor = SSHExecutor()

        return executor.execute(
            "uname",
            ["-a"]
        )


    @mcp.tool()
    def get_disk_usage() -> dict:

        """
        Get filesystem disk usage.
        """

        audit_log(
            "get_disk_usage",
            "df -h"
        )

        executor = SSHExecutor()

        return executor.execute(
            "df",
            ["-h"]
        )