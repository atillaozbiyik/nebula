import os, platform
if platform.python_version().startswith("2."):
    print ("Only Python 3.x is supported!")
    exit()

from clang.cindex import Index, Config, CursorKind, TranslationUnit, SourceLocation
from ctypes.util import find_library
from tools import debug
from PyQt5.QtGui import QStandardItem, QStandardItemModel

class QOutlineItem (QStandardItem):
    location = SourceLocation()

    def __init__(self, name):
        super(QStandardItem, self).__init__(name)


class AstParser:

    def __init__(self):
        # from ctypes.util import find_library
        # print(find_library("clang"))
        # if (os.path.exists("/usr/lib/llvm-3.9/lib/libclang-3.9.1.so")):
        #     Config.set_library_file("/usr/lib/llvm-3.9/lib/libclang-3.9.1.so")
        # if (os.path.exists("/usr/lib/x86_64-linux-gnu/libclang-3.9.so")):
        Config.set_library_file("/usr/lib/x86_64-linux-gnu/libclang-3.9.so")
        # Config.set_library_file(find_library('clang'))

        self.index = Index.create()

    def append(self, parent, node, kinds):

        for c in [c for c in node.get_children()]:
            if c.kind in kinds:

                if c.kind == CursorKind.STRUCT_DECL:
                    pass

                item = QOutlineItem(c.spelling)
                item.location = c.location
                item.setEditable(False)
                parent.appendRow(item)
                # Print out information about the node
                debug('Found %s, (%s)  [line=%s, col=%s]' % (c.displayname, str(c.kind), c.location.line, c.location.column))

                for gc in [c for c in c.get_children()]:
                    self.append(item, gc, kinds)

    def get_outline(self, file, kinds):
        opts = ['-x', 'c-header', '-std=c++11', '-D__CODE_GENERATOR__']
        tu = self.index.parse(file , opts)
        if not tu:
            debug("Unable to analyse file")
            return None

        root = QStandardItemModel()
        self.append (root, tu.cursor, kinds)
        return root

