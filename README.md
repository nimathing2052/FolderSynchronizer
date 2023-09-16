# Folder Synchronization Program

This Python program is designed to synchronize two folders, a source folder, and a replica folder, maintaining an identical copy of the source folder in the replica folder. The synchronization process is one-way, and changes made in the source folder are propagated to the replica folder. The program also logs file creation, copying, and removal operations to a log file and console output.

## Challenges Addressed

- **Synchronization**: The program ensures a full, identical copy of the source folder is maintained in the replica folder.

- **Periodic Synchronization**: Synchronization is performed periodically at a user-defined interval.

- **Logging**: File operations (creation, copying, removal) are logged to both a log file and the console output.

- **Command Line Arguments**: Folder paths, synchronization interval, and log file path are provided as command-line arguments.

- **Modular and Object-Oriented**: The program is structured using Object-Oriented Programming (OOP) principles for modularity and good code organization.

## Usage

1. Clone this repository or download the code.

2. Create a virtual environment (optional but recommended) to manage dependencies:
   ```bash
   python -m venv env
   source env/bin/activate  # On macOS/Linux
   .\env\Scripts\activate  # On Windows

## Install dependencies (if any) or run the program directly:

bash
Copy code
python folder_synchronizer.py source_folder replica_folder sync_interval_in_seconds log_file.log
source_folder: Path to the source folder.
replica_folder: Path to the replica folder.
sync_interval_in_seconds: Synchronization interval in seconds.
log_file: Path to the log file.
Follow the prompts to perform folder synchronization.

## Requirements
This program is written in Python and does not have any external dependencies beyond the Python standard library.

## Contributing
Feel free to contribute to this project by opening issues or creating pull requests. Your feedback and contributions are highly appreciated!

-Nima Thing
