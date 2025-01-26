import PyQt6.QtWidgets as Qw
import PyQt6.QtCore as Qc

class GoalsWidget(Qw.QWidget):

  goals_added = Qc.pyqtSignal(str)

  def __init__(self):
    super().__init__()
    self.setWindowTitle("Goals")
    self.setGeometry(150, 150, 400, 300)
    layout = Qw.QVBoxLayout(self)

    self.input_field = Qw.QLineEdit(self)
    self.input_field.setPlaceholderText("Enter a goal")
    layout.addWidget(self.input_field)

    self.btn_add = Qw.QPushButton("Add Goal")
    self.btn_add.clicked.connect(self.add_goal)
    layout.addWidget(self.btn_add)

    self.goal_list = Qw.QListWidget(self)
    layout.addWidget(self.goal_list)

  def add_goal(self):
    goal_text = self.input_field.text()
    if goal_text:
      self.goals_added.emit(goal_text)
      self.input_field.clear()
      self.close()
