import re

from config import Config
from security.permissions import ALLOWED_COMMANDS


def validate_command(command, args):

    if command not in ALLOWED_COMMANDS:

        raise ValueError(
            f"Command not allowed: {command}"
        )

    if command != "systemctl":

        if args != ALLOWED_COMMANDS[command]:

            raise ValueError(
                "Invalid command arguments"
            )

    else:

        if not args:

            raise ValueError(
                "Missing systemctl arguments"
            )

        if args[0] not in ALLOWED_COMMANDS["systemctl"]:

            raise ValueError(
                "Invalid systemctl operation"
            )

        if len(args) != 2:

            raise ValueError(
                "Invalid systemctl arguments"
            )

        validate_service(args[1])


def validate_service(service):

    if service not in Config.ALLOWED_SERVICES:

        raise ValueError(
            f"Service not allowed: {service}"
        )


def validate_path(path):

    import os

    path = os.path.realpath(path)

    for allowed in Config.ALLOWED_PATHS:

        allowed = os.path.realpath(allowed)

        if os.path.commonpath(
            [allowed, path]
        ) == allowed:

            return path

    raise ValueError(
        "Access to this path is not allowed"
    )