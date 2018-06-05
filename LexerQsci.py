from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qsci import QsciScintilla, QsciLexerPython, QsciLexerCPP


class Editor(QsciScintilla):

    filename = ""

    def __init__(self, parent=None):
        super(Editor, self).__init__(parent)
        font = QtGui.QFont()
        font.setFamily('Courier')
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.setFont(font)
        self.setMarginsFont(font)


        # self.setBackgroundColor

        # Margin 0 is used for line numbers
        fontmetrics = QtGui.QFontMetrics(font)
        self.setMarginsFont(font)
        self.setMarginWidth(0, fontmetrics.width("00000") + 6)
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(QtGui.QColor("#cccccc"))

        # Brace matching: enable for a brace immediately before or after
        # the current position
        #
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        # Set the autocompletions to case INsensitive
        self.setAutoCompletionCaseSensitivity(False)
        # Set the autocompletion to not replace the word to the right of the cursor
        self.setAutoCompletionReplaceWord(False)
        # Set the autocompletion source to be the words not only in document but all
        self.setAutoCompletionSource(QsciScintilla.AcsAll)
        # Set the autocompletion dialog to appear as soon as 1 character is typed
        self.setAutoCompletionThreshold(3)


        # Current line visible with special background color
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QtGui.QColor("#ffe4e4"))

        # Set Python lexer
        # Set style for Python comments (style number 1) to a fixed-width
        # courier.
        #
        lexer = QsciLexerCPP()
        lexer.setDefaultFont(font)
        self.setLexer(lexer)
        # self.SendScintilla(QsciScintilla.SCI_STYLESETFONT, 1, 'Courier')
        self.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR,0)
