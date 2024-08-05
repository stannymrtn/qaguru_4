from pathlib import Path


def get_resource_path(filename):
    return str(Path(__file__).parent.joinpath('resources', filename))
