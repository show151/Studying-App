import PyQt6.QtWidgets as Qw
import PyQt6.QtCore as Qc
import english_practice as ep
import math_practice as mp
import science_practice as sp

sp_exp = Qw.QSizePolicy.Policy.Expanding

class SubjectSelection(Qw.QWidget):
  def __init__(self):
    super().__init__()
    layout = Qw.QVBoxLayout(self)
    self.setWindowTitle("Subject Selection")
    self.setGeometry(150, 150, 300, 200)

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

    self.btn_math = Qw.QPushButton("Math")
    self.btn_math.setStyleSheet(button_style)
    self.btn_math.setSizePolicy(sp_exp, sp_exp)
    self.btn_math.clicked.connect(self.open_math_practice)
    layout.addWidget(self.btn_math)

    self.btn_sci = Qw.QPushButton("Science")
    self.btn_sci.setStyleSheet(button_style)
    self.btn_sci.setSizePolicy(sp_exp, sp_exp)
    self.btn_sci.clicked.connect(self.open_science_practice)
    layout.addWidget(self.btn_sci)

    self.btn_eng = Qw.QPushButton("English")
    self.btn_eng.setStyleSheet(button_style)
    self.btn_eng.setSizePolicy(sp_exp, sp_exp)
    self.btn_eng.clicked.connect(self.open_english_practice)
    layout.addWidget(self.btn_eng)

    self.btn_back = Qw.QPushButton("Back")
    self.btn_back.setStyleSheet(button_style)
    self.btn_back.setSizePolicy(sp_exp, sp_exp)
    self.btn_back.clicked.connect(self.close)
    layout.addWidget(self.btn_back)

  def open_math_practice(self):
    self.math_practice = mp.MathPractice()
    self.math_practice.show()
    self.close()

  def open_science_practice(self):
    self.science_practice = sp.SciencePractice()
    self.science_practice.show()
    self.close()

  def open_english_practice(self):
    self.english_practice = ep.EnglishPractice()
    self.english_practice.show()
    self.close()