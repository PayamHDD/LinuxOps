from ssh.executor import SSHExecutor

from security.validator import validate_path

from logging.audit import audit_log


def register(mcp):

    @mcp.tool()
    def read_file(path: str) -> dict:

        """
        Read a Linux file.
        """

        path = validate_path(path)

        audit_log(
            "read_file",
            path
        )

        executor = SSHExecutor()

        return executor.execute(
            "cat",
            [path]
        )


    @mcp.tool()
    def list_directory(path: str) -> dict:

        """
        List directory contents.
        """

        path = validate_path(path)

        audit_log(
            "list_directory",
            path
        )

        executor = SSHExecutor()

        return executor.execute(
            "ls",
            ["-la", path]
        )