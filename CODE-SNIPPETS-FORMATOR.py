#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃														   ┃
from multiprocessing.managers import BaseProxy
import sys
from PySide6.QtCore		import Qt, QTimer
from PySide6.QtGui 		import QIcon, QFont
from PySide6.QtWidgets 	import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel
#┃														   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃														   ┃
class FORMATOR(QWidget):
	#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
	#┃														   ┃
	def __init__(self):
		#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
		#┃														   ┃
		super().__init__()
		self.setWindowTitle("CODE-SNIPPETS-FORMATOR")
		self.resize(800, 800)
		self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
		#┃														   ┃
		#┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
		#┃														   ┃
		import sys
		import os
		#┃														   ┃
		#┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
		#┃														   ┃
		def PATH(REL_PATH):
			try:
				BASE_PATH = sys._MEIPASS
			except AttributeError:
				BASE_PATH = os.path.abspath(".")
			return os.path.join(BASE_PATH, REL_PATH)
		self.setWindowIcon(QIcon(PATH("ICO-128.ico")))
		#┃														   ┃
		#┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
		#┃														   ┃
		LAYOUT = QVBoxLayout()
		#┃														   ┃
		#┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
		#┃														   ┃
		self.LABEL = QLabel(">INPUT:")
		self.LABEL.setFont(QFont("Consolas", 12))
		LAYOUT.addWidget(self.LABEL)
		#┃														   ┃
		#┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
		#┃														   ┃
		self.TEXT_EDIT = QTextEdit()
		self.TEXT_EDIT.setFont(QFont("Consolas", 12))
		LAYOUT.addWidget(self.TEXT_EDIT)
		#┃														   ┃
		#┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
		#┃														   ┃
		#self.BUTTON = QPushButton(">FORMAT")
		#self.BUTTON.setFont(QFont("Consolas", 12))
		#self.BUTTON.clicked.connect(self.FORMAT_TEXT)
		#LAYOUT.addWidget(self.BUTTON)
		self.TEXT_EDIT.textChanged.connect(self.FORMAT_TEXT)
		#┃														   ┃
		#┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
		#┃														   ┃
		self.OUTPUT = QTextEdit()
		self.OUTPUT.setFont(QFont("Consolas", 12))
		self.OUTPUT.setReadOnly(True)
		LAYOUT.addWidget(self.OUTPUT)
		#┃														   ┃
		#┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
		#┃														   ┃
		self.COPY_BTN = QPushButton(">COPY")
		self.COPY_BTN.setFont(QFont("Consolas", 12))
		self.COPY_BTN.clicked.connect(self.COPY)
		LAYOUT.addWidget(self.COPY_BTN)
		#┃														   ┃
		#┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
		#┃														   ┃
		self.setLayout(LAYOUT)
		#┃														   ┃
		#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
	#┃														   ┃
	#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
	#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
	#┃														   ┃
	def FORMAT_TEXT(self):
		raw_text = self.TEXT_EDIT.toPlainText()
		lines = raw_text.splitlines()
		FORMATTED = []
		#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
		#┃														   ┃
		for i, line in enumerate(lines):
			#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
			#┃														   ┃
			NEW_LINE = ""
			COUNT = 0  # COUNT CONSECUTIVE SPACES
			for c in line:
				#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
				#┃														   ┃
				if c == " ":
					COUNT += 1 # *4 SPACES -> "\t"
				if COUNT == 4:
					NEW_LINE += "\\t"
					COUNT = 0
				#┃														   ┃
				#┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
				#┃														   ┃
				else:
					#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
					#┃														   ┃
					# If there were fewer than 4 loose spaces, we added them as is.
					if COUNT > 0:
						NEW_LINE += " " * COUNT
						COUNT = 0
					#┃														   ┃
					#┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
					#┃														   ┃
					# If character is an actual tab, convert to "\t"
					if c == "\t":
						NEW_LINE += "\\t"
					#┃														   ┃
					#┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
					#┃														   ┃
					else:
						NEW_LINE += c
     				#┃														   ┃
					#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
				#┃														   ┃
				#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
			#┃														   ┃
			#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
			#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
			#┃														   ┃
			# Add spaces (<4) to the end of the line if there are any
			if COUNT > 0:
				NEW_LINE += " " * COUNT
			#┃														   ┃
			#┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
			#┃														   ┃
			if i < len(lines) - 1:
				FORMATTED.append(f'"{NEW_LINE}",')
			#┃														   ┃
			#┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
			#┃														   ┃
			# Enclose in quotation marks and add a comma if it is not the last line
			else:
				FORMATTED.append(f'"{NEW_LINE}"')
			#┃														   ┃
			#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
		#┃														   ┃
		#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
		#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
		#┃														   ┃
		self.OUTPUT.setPlainText("\n".join(FORMATTED))
  		#┃														   ┃
		#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
	#┃														   ┃
	#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
	#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
	#┃														   ┃
	def COPY(self):
		#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
		#┃														   ┃
		CLIP = QApplication.clipboard()
		CLIP.setText(self.OUTPUT.toPlainText())
		self.COPY_BTN.setText("SUCCESS!")
		#┃														   ┃
		#┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
		#┃														   ┃
		from PySide6.QtCore import QTimer
		QTimer.singleShot(2000, lambda: self.COPY_BTN.setText(">COPY"))
		#┃														   ┃
		#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
	#┃														   ┃
	#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┃														   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃														   ┃
if __name__ == "__main__":
	APP = QApplication(sys.argv)
	HMI = FORMATOR()
	HMI.show()
	sys.exit(APP.exec())
#┃														   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛