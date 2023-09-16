"""
Author: Nima Thing
Date: September 16, 2023
Description: This is a folder synchronization program prepared as an assignment Task for Veeeam Software Application
"""

import os
import shutil
import logging
import time

class FolderSynchronizer:
    def __init__(self, source_folder, replica_folder, sync_interval, log_file):

        # Inside the __init__ method of FolderSynchronizer in folder_sync.py
        if not os.path.exists(source_folder):
            raise ValueError(f"Source folder '{source_folder}' does not exist.")
        if not os.path.exists(replica_folder):
            raise ValueError(f"Replica folder '{replica_folder}' does not exist.")

        """
        Initializes the FolderSynchronizer.

        Args:
            source_folder (str): Path to the source folder.
            replica_folder (str): Path to the replica folder.
            sync_interval (int): Synchronization interval in seconds.
            log_file (str): Path to the log file.
        """
        self.source_folder = source_folder
        self.replica_folder = replica_folder
        self.sync_interval = sync_interval
        self.log_file = log_file

        self.setup_logging()

    def setup_logging(self):
        """
        Sets up logging to both a file and the console.
        """
        logging.basicConfig(filename=self.log_file, level=logging.INFO,
                            format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        console_handler.setFormatter(formatter)
        logging.getLogger().addHandler(console_handler)

    def synchronize_folders(self):
        """
        Synchronizes the source folder with the replica folder.
        """
        if not os.path.exists(self.source_folder):
            logging.error(f"Source folder '{self.source_folder}' does not exist.")
            return

        if not os.path.exists(self.replica_folder):
            os.makedirs(self.replica_folder)
            logging.info(f"Replica folder '{self.replica_folder}' created.")

        for item in os.listdir(self.source_folder):
            source_item = os.path.join(self.source_folder, item)
            replica_item = os.path.join(self.replica_folder, item)

            if os.path.isdir(source_item):
                self.synchronize_folders_recursive(source_item, replica_item)
            else:
                self.synchronize_file(source_item, replica_item)

    def synchronize_folders_recursive(self, source_folder, replica_folder):
        """
        Recursively synchronizes subfolders.

        Args:
            source_folder (str): Path to the source folder.
            replica_folder (str): Path to the replica folder.
        """
        if not os.path.exists(replica_folder):
            os.makedirs(replica_folder)
            logging.info(f"Replica folder '{replica_folder}' created.")

        for item in os.listdir(source_folder):
            source_item = os.path.join(source_folder, item)
            replica_item = os.path.join(replica_folder, item)

            if os.path.isdir(source_item):
                self.synchronize_folders_recursive(source_item, replica_item)
            else:
                self.synchronize_file(source_item, replica_item)

    def synchronize_file(self, source_file, replica_file):
        """
        Synchronizes an individual file.

        Args:
            source_file (str): Path to the source file.
            replica_file (str): Path to the replica file.
        """
        try:
            if not os.path.exists(replica_file) or os.path.getmtime(source_file) > os.path.getmtime(replica_file):
                shutil.copy2(source_file, replica_file)
                logging.info(f"File copied: '{source_file}' -> '{replica_file}'")
            elif os.path.getmtime(source_file) < os.path.getmtime(replica_file):
                os.remove(replica_file)
                logging.info(f"File removed: '{replica_file}'")
        except Exception as e:
            logging.error(f"Error synchronizing file '{source_file}': {str(e)}")

    def run(self):
        """
        Runs the synchronization process in a loop with the specified interval.
        """
        try:
            while True:
                self.synchronize_folders()
                logging.info("Synchronization complete.")
                time.sleep(self.sync_interval)
        except KeyboardInterrupt:
            logging.info("Synchronization process terminated.")