import PySide6.QtWidgets as Qw

class SciencePractice(Qw.QWidget):
  def __init__(self):
    super().__init__()
    layout = Qw.QVBoxLayout(self)
    self.label = Qw.QLabel("Science Practice: Answer scientific questions!", self)
    layout.addWidget(self.label)
