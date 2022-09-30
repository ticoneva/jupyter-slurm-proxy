import os

def get_icon_path():
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icons', 'jupyter.svg'
    )


def setup_srun():

    cpu = 4
    mem = "24G"
    
    server_process = {
        'command': ["srun", 
                    f"-c {cpu}",
                    f"--mem={mem}",
                    "--tunnel {port}:{port}",
                    "jupyter lab",
                    "--no-browser",
                    "--port={port}"],
        'timeout': 20,
        'launcher_entry': {
            'title': 'Slurm (GPU)',
            'icon_path': get_icon_path()
        }
    }
    return server_process
