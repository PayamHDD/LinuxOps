from SSH.executor import SSHExecutor
from Security.validator import validate_service
from Logging.logger import audit_log


def register(mcp):

    @mcp.tool()
    def get_service_status(
        service: str
    ) -> dict:

        """
        Get systemd service status.
        """

        validate_service(service)

        audit_log(
            "get_service_status",
            service
        )

        executor = SSHExecutor()

        return executor.execute(
            "systemctl",
            ["status", service]
        )