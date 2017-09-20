from clang.cindex import Index, Config, CursorKind, TranslationUnit
from tools import debug

class AstParser:

    def __init__(self):
        # from ctypes.util import find_library
        # print(find_library("clang"))
        Config.set_library_file("/usr/lib/llvm-3.9/lib/libclang-3.9.1.so")

        # For Ubuntu 14.04:
            # sudo ln -s /usr/lib/llvm-3.9/lib/libclang-3.9.1.so /usr/lib/x86_64-linux-gnu/libclang.so.1

        self.index = Index.create()
        # self.outline = []

    # def __append_outline__(self, parent, ch):
    #     print("Adding " + str(ch.spelling))
    #     item = OutlineItem()
    #
    #     self.outline.append( (str(ch.spelling) , ch.get_children())  )
    #
    #     if ch.get_children() is not None:
    #         for c in ch.get_children():
    #             self.__append_outline__(ch, c)

    def get_outline(self, file):
        tu = self.index.parse(None, [file])
        if not tu:
            debug("Unable to analyse file")
            return None

        # children = [c for c in tu.cursor.get_children()]
        #
        # for c in children:
        #     self.__append_outline__(children, c)

        return tu