import shutil
from datetime import datetime

class BackupManager:
    def create_backup(self):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        source = "data/notes.json"
        backup_file = f"data/backups/notes_backup_{timestamp}.json"

        shutil.copy(source, backup_file)

        print(f"Backup created successfully: {backup_file}")