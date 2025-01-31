import PySide6.QtWidgets as Qw

class MathPractice(Qw.QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Math Practice")
    self.label = Qw.QLabel("Math Practice: Solve basic math problems!", self)
    layout = Qw.QVBoxLayout(self)
    layout.addWidget(self.label)

    