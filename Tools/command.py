import logging
from SSH.executor import SSHExecutor
from Security.validator import validate_command

# Logging
logger = logging.getLogger(__name__)


def register(mcp):

    @mcp.tool()
    def execute_command(
        command: str,
        args: list[str] = []
    ) -> dict:

        """
        Execute an approved Linux command.

        Only predefined commands and arguments
        are allowed.
        """

        validate_command(command, args)

        logger.info(
            "execute_command",
            f"{command} {args}"
        )

        executor = SSHExecutor()

        return executor.execute(
            command,
            args
        )