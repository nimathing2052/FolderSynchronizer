import argparse
import time
from folder_sync import FolderSynchronizer

def main():
    parser = argparse.ArgumentParser(description="Synchronize two folders.")
    parser.add_argument("source_folder", help="Path to the source folder")
    parser.add_argument("replica_folder", help="Path to the replica folder")
    parser.add_argument("sync_interval", type=int, help="Synchronization interval in seconds")
    parser.add_argument("log_file", help="Path to the log file")
    args = parser.parse_args()

    synchronizer = FolderSynchronizer(args.source_folder, args.replica_folder, args.sync_interval, args.log_file)
    synchronizer.run()

if __name__ == "__main__":
    main()
