import logging
from Logging.logger import setup_logging
import Tools.command as commander

from mcp.server.fastmcp import FastMCP

from Tools import command
from Tools import filesystem
from Tools import services
from Tools import system

# Setup logging
logger = logging.getLogger(__name__)
setup_logging()

mcp = FastMCP("Linux-MCP")


# Register MCP Tools

command.register(mcp)
filesystem.register(mcp)
services.register(mcp)
system.register(mcp)


if __name__ == "__main__":

    mcp.run(
        transport="stdio"
    )
