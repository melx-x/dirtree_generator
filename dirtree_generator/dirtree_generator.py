import pathlib 
import os


PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "

class DirectoryTree:
    def __init__(self, dir, dir_only=False):
        self._generator = _TreeGen(dir, dir_only)
    
    def generate(self):
        entries = self._generator.build_tree()
        for entry in entries:
            print(entry)

class _TreeGen:
    def __init__(self, dir, dir_only=False):
        self._dir  = pathlib.Path(dir)
        self._dir_only = dir_only
        self._tree = []

    def build_tree(self):
        self._tree_head()
        self._tree_body(self._dir)
        return self._tree

    def _tree_head(self):
        self._tree.append(f"{self._dir}{os.sep}")
        self._tree.append(PIPE)

    def _tree_body(self, directory, prefix=""):
        entries = self._prepare_entries(directory)
        entries_count = len(entries)
        for index, entry in enumerate(entries):
            connector = ELBOW if index == entries_count - 1 else TEE
            if entry.is_dir():
                self._add_directory(entry, connector, prefix, index, entries_count)
            else:
                self._add_file(entry, prefix, connector)

    def _prepare_entries(self, directory):
        entries = directory.iterdir()
        if self._dir_only:
            entries = [entry for entry in entries if entry.is_dir()]
            return entries
        entries = sorted(entries, key=lambda x: x.is_file())
        return entries
        
    def _add_directory(self, entry, connector, prefix, index, entries_count):
        self._tree.append(f"{prefix}{connector} {entry.name}{os.sep}")
        if index != entries_count - 1:
            prefix += PIPE_PREFIX
        else:
            prefix += SPACE_PREFIX
        self._tree_body(entry, prefix=prefix)
        self._tree.append(prefix.rstrip())

    def _add_file(self, file, prefix, connector):
        self._tree.append(f"{prefix}{connector} {file.name}")

# add 1 empty directory case