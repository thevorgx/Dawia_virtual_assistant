"""Organize files in a directory by type."""


import os
import shutil
from pathlib import Path
import wx

AUDIO_EXTENSIONS = ['.mp3', '.wav', '.aac', '.flac', '.m4a', '.ogg', '.wma']
IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg']
VIDEO_EXTENSIONS = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv']
DOCUMENT_EXTENSIONS = ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.odt']
ARCHIVE_EXTENSIONS = ['.zip', '.rar', '.tar', '.gz', '.7z']
OTHER_EXTENSIONS = ['.exe', '.iso', '.bat', '.sh', '.bin']

def select_directory():
    """Select a directory using a dialog box."""
    app = wx.App(False)
    dialog = wx.DirDialog(None, "Choose a directory:", style=wx.DD_DEFAULT_STYLE)

    if dialog.ShowModal() == wx.ID_OK:
        folder_selected = dialog.GetPath()
    else:
        folder_selected = None

    dialog.Destroy()
    app.MainLoop()

    return folder_selected

def organize_files_by_type(directory_path):
    """Organize files in a directory by type."""
    file_types = {
        'Audio': AUDIO_EXTENSIONS,
        'Images': IMAGE_EXTENSIONS,
        'Videos': VIDEO_EXTENSIONS,
        'Documents': DOCUMENT_EXTENSIONS,
        'Archives': ARCHIVE_EXTENSIONS,
        'Others': OTHER_EXTENSIONS
    }

    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isfile(item_path):
            file_extension = Path(item).suffix.lower()
            moved = False
            for category, extensions in file_types.items():
                if file_extension in extensions:
                    target_folder = os.path.join(directory_path, category)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(item_path, target_folder)
                    print(f'Moved {item} to {category} folder')
                    moved = True
                    break

            if not moved:
                unknown_folder = os.path.join(directory_path, 'unknown_format_files')
                os.makedirs(unknown_folder, exist_ok=True)
                shutil.move(item_path, unknown_folder)
                print(f'Moved {item} to unknown_format_files folder')

def organize_directory():
    """Select a directory and organize files by type."""
    directory = select_directory()

    if directory:
        organize_files_by_type(directory)
