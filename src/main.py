import PyQt6.QtWidgets as Qw
import PyQt6.QtCore as Qc
import sys
import timer_widget as tw
import goals_widget as gw
import subject_selection as ss
import json

sp_exp = Qw.QSizePolicy.Policy.Expanding
DATA_FILE = "goals.json"

class MainWindow(Qw.QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Studying App")
    self.setGeometry(150, 150, 600, 300)

    central_widget = Qw.QWidget()
    self.setCentralWidget(central_widget)
    main_layout = Qw.QVBoxLayout(central_widget)

    button_layout = Qw.QHBoxLayout()
    button_layout.setSpacing(20)
    button_layout.setAlignment(Qc.Qt.AlignmentFlag.AlignLeft)
    main_layout.addLayout(button_layout)

    self.btn_timer = Qw.QPushButton("Timer")
    self.btn_timer.setMinimumSize(50, 20)
    self.btn_timer.setMaximumSize(100, 20)
    self.btn_timer.setSizePolicy(sp_exp, sp_exp)
    self.btn_timer.clicked.connect(self.show_timer)
    button_layout.addWidget(self.btn_timer)

    self.btn_Goals = Qw.QPushButton("Set Goals")
    self.btn_Goals.setMinimumSize(50, 20)
    self.btn_Goals.setMaximumSize(100, 20)
    self.btn_Goals.setSizePolicy(sp_exp, sp_exp)
    self.btn_Goals.clicked.connect(self.show_goals)
    button_layout.addWidget(self.btn_Goals)

    self.btn_prac = Qw.QPushButton("Practice")
    self.btn_prac.setMinimumSize(50, 20)
    self.btn_prac.setMaximumSize(100, 20)
    self.btn_prac.setSizePolicy(sp_exp, sp_exp)
    self.btn_prac.clicked.connect(self.open_subject_selection)
    button_layout.addWidget(self.btn_prac)

    self.btn_Quit = Qw.QPushButton("Quit")
    self.btn_Quit.clicked.connect(self.close)
    self.btn_Quit.setMinimumSize(50, 20)
    self.btn_Quit.setMaximumSize(100, 20)
    self.btn_Quit.setSizePolicy(sp_exp, sp_exp)
    button_layout.addWidget(self.btn_Quit)

    self.goals_list = Qw.QListWidget()
    self.goals_list.itemChanged.connect(self.check_goals)
    main_layout.addWidget(self.goals_list)

    self.sb_status = Qw.QStatusBar()
    self.setStatusBar(self.sb_status)
    self.sb_status.setSizeGripEnabled(False)
    self.sb_status.showMessage("Ready", 5000)

    self.load_goals()

  def show_timer(self):
    self.timer_window = tw.TimerWidget()
    self.timer_window.show()

  def show_goals(self):
    self.goals_window = gw.GoalsWidget()
    self.goals_window.goals_added.connect(self.add_goal)
    self.goals_window.show()

  def add_goal(self, goal_text, checked=False):
    item = Qw.QListWidgetItem(goal_text)
    item.setFlags(item.flags() | Qc.Qt.ItemFlag.ItemIsUserCheckable)
    item.setCheckState(
        Qc.Qt.CheckState.Checked if checked else Qc.Qt.CheckState.Unchecked)
    self.goals_list.addItem(item)
    self.save_goals()

  def check_goals(self, item):
    if item.checkState() == Qc.Qt.CheckState.Checked:
      self.goals_list.takeItem(self.goals_list.row(item))
      self.save_goals()

  def save_goals(self):
    goals = []
    for i in range(self.goals_list.count()):
      item = self.goals_list.item(i)
      if item is not None:
        goals.append(
            {"text": item.text(), "checked": item.checkState() == Qc.Qt.CheckState.Checked})
    with open(DATA_FILE, "w") as file:
      json.dump(goals, file)

  def load_goals(self):
    try:
      with open(DATA_FILE, "r") as file:
        goals = json.load(file)
        for goal in goals:
          self.add_goal(goal["text"], goal["checked"])
    except FileNotFoundError:
      pass

  def open_subject_selection(self):
    self.subject_window = ss.SubjectSelection()
    self.subject_window.show()

if __name__ == "__main__":
  app = Qw.QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec())
