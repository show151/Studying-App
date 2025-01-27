import PyQt6.QtWidgets as Qw
import PyQt6.QtCore as Qc

sp_exp = Qw.QSizePolicy.Policy.Expanding

class EnglishPractice(Qw.QWidget):
  def __init__(self):
    super().__init__()
    layout = Qw.QVBoxLayout(self)
    self.setWindowTitle("English Practice")
    self.setGeometry(150, 150, 600, 400)

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

    self.word_label = Qw.QLabel("Word: Apple", self)
    layout.addWidget(self.word_label)

    self.input_field = Qw.QLineEdit(self)
    layout.addWidget(self.input_field)

    self.btn_check = Qw.QPushButton("Check", self)
    self.btn_check.setStyleSheet(button_style)
    self.btn_check.setSizePolicy(sp_exp, sp_exp)
    self.btn_check.clicked.connect(self.check_answer)
    layout.addWidget(self.btn_check)

    self.btn_quit = Qw.QPushButton("Quit")
    self.btn_quit.setStyleSheet(button_style)
    self.btn_quit.setSizePolicy(sp_exp, sp_exp)
    self.btn_quit.clicked.connect(self.close)
    layout.addWidget(self.btn_quit)

    self.result_label = Qw.QLabel("", self)
    layout.addWidget(self.result_label)

  def check_answer(self):
    answer = self.input_field.text().strip().lower()
    if answer == "りんご":
      self.result_label.setText("Correct!")
    else:
      self.result_label.setText("Incorrect!")
