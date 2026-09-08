from fastmcp import FastMCP
import os

mcp = FastMCP("commandmcp")

@mcp.tool()
def create_directory(path: str):
    os.makedirs(path, exist_ok=True)
    return f"Directory {path} created successfully"

@mcp.tool()
def list_directory(path: str):
    if not os.path.exists(path):
        return f"Directory {path} does not exist"
    return os.listdir(path)

@mcp.tool()
def read_file(path: str):
    if not os.path.exists(path):
        return f"File {path} does not exist"

    with open(path, "r") as file:
        return file.read()


if __name__ == "__main__":
    mcp.run(transport="stdio")

