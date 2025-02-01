import PySide6.QtWidgets as Qw
import PySide6.QtCore as Qc
import english_word_dictionary as ewd
import english_practice as ep
sp_exp = Qw.QSizePolicy.Policy.Expanding

class SubjectSelection(Qw.QWidget):
  def __init__(self):
    super().__init__()
    layout = Qw.QVBoxLayout(self)
    self.setWindowTitle("Subject Selection")
    self.setGeometry(150, 150, 300, 200)

    self.word_dict = []  # Initialize word_dict as an empty list
    layout.setSpacing(20)
    layout.setAlignment(Qc.Qt.AlignmentFlag.AlignCenter)

    button_style = """
            QPushButton {
                font-size: 18px;
                padding: 10px;
                border-radius: 8px;
                background-color: #a0a0a0;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }
            QPushButton:pressed {
                background-color: #a0a0a0;
            }
        """

    self.btn_eng = Qw.QPushButton("Dictionary")
    self.btn_eng.setStyleSheet(button_style)
    self.btn_eng.setSizePolicy(sp_exp, sp_exp)
    self.btn_eng.clicked.connect(self.open_english_word_dictionary)
    layout.addWidget(self.btn_eng)

    self.btn_practice = Qw.QPushButton("Practice")
    self.btn_practice.setStyleSheet(button_style)
    self.btn_practice.setSizePolicy(sp_exp, sp_exp)
    self.btn_practice.clicked.connect(self.open_english_practice)
    layout.addWidget(self.btn_practice)

    self.btn_back = Qw.QPushButton("Back")
    self.btn_back.setStyleSheet(button_style)
    self.btn_back.setSizePolicy(sp_exp, sp_exp)
    self.btn_back.clicked.connect(self.close)
    layout.addWidget(self.btn_back)

  def open_english_word_dictionary(self):
    self.english_practice = ewd.EnglishWordDictionary()
    self.english_practice.show()
    self.hide()

  def open_english_practice(self):
    if not self.word_dict:
      Qw.QMessageBox.warning(
          self, "No Words", "Please add words to the list to start practicing.")
      return

    self.practice_window = ep.EnglishPractice(self.word_dict, self)
    self.practice_window.show()
    self.hide()
