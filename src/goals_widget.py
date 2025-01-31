import PySide6.QtWidgets as Qw
import PySide6.QtCore as Qc

sp_exp = Qw.QSizePolicy.Policy.Expanding
class GoalsWidget(Qw.QWidget):

  goals_added = Qc.Signal(str)

  def __init__(self):
    super().__init__()
    self.setWindowTitle("Goals")
    self.setGeometry(150, 150, 400, 300)
    layout = Qw.QVBoxLayout(self)

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

    self.input_field = Qw.QLineEdit(self)
    self.input_field.setPlaceholderText("Enter a goal")
    layout.addWidget(self.input_field)

    self.btn_add = Qw.QPushButton("Add Goal")
    self.btn_add.setStyleSheet(button_style)
    self.btn_add.setSizePolicy(sp_exp, sp_exp)
    self.btn_add.clicked.connect(self.add_goal)
    layout.addWidget(self.btn_add)

    self.btn_Quit = Qw.QPushButton("Quit")
    self.btn_Quit.clicked.connect(self.close)
    self.btn_Quit.setStyleSheet(button_style)
    self.btn_Quit.setSizePolicy(sp_exp, sp_exp)
    layout.addWidget(self.btn_Quit)

    self.goal_list = Qw.QListWidget(self)
    layout.addWidget(self.goal_list)

  def add_goal(self):
    goal_text = self.input_field.text()
    if goal_text:
      self.goals_added.emit(goal_text)
      self.input_field.clear()
      self.close()
    else:
      Qw.QMessageBox.warning(self, "Warning", "Please enter a goal")
      return
