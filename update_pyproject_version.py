import toml


def update_version():
    # Read version from version.txt
    with open("version.txt", "r") as file:
        version = file.read().strip()

    # Load the pyproject.toml file
    with open("pyproject.toml", "r") as file:
        data = toml.load(file)

    # Assuming you are managing the version under a tool section,
    # for example, [tool.my_package] or similar
    data["tool"]["my_package"]["version"] = version  # Adjust the path as necessary

    # Save the updated pyproject.toml
    with open("pyproject.toml", "w") as file:
        toml.dump(data, file)


if __name__ == "__main__":
    update_version()
