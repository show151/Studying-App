import PySide6.QtWidgets as Qw
import PySide6.QtCore as Qc

sp_exp = Qw.QSizePolicy.Policy.Expanding

class TimerWidget(Qw.QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Timer")
    self.setGeometry(150, 150, 300, 200)
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

    self.timer_display = Qw.QLabel("25:00", self)
    self.timer_display.setAlignment(Qc.Qt.AlignmentFlag.AlignCenter)
    self.timer_display.setStyleSheet("font-size: 40px;")
    layout.addWidget(self.timer_display)

    input_layout = Qw.QHBoxLayout()

    self.min_input = Qw.QLineEdit(self)
    self.min_input.setPlaceholderText("Minutes")
    self.min_input.setAlignment(Qc.Qt.AlignmentFlag.AlignCenter)
    self.min_input.setStyleSheet("font-size: 20px;")
    self.min_input.setMaximumWidth(100)
    input_layout.addWidget(self.min_input)

    self.sec_input = Qw.QLineEdit(self)
    self.sec_input.setPlaceholderText("Seconds")
    self.sec_input.setAlignment(Qc.Qt.AlignmentFlag.AlignCenter)
    self.sec_input.setStyleSheet("font-size: 20px;")
    self.sec_input.setMaximumWidth(100)
    input_layout.addWidget(self.sec_input)

    layout.addLayout(input_layout)

    button_layout = Qw.QVBoxLayout()
    layout.addLayout(button_layout)

    self.set_time_button = Qw.QPushButton("Set Time")
    self.set_time_button.setStyleSheet(button_style)
    self.set_time_button.setSizePolicy(sp_exp, sp_exp)
    self.set_time_button.clicked.connect(self.set_custom_time)
    button_layout.addWidget(self.set_time_button)

    self.start_button = Qw.QPushButton("Start")
    self.start_button.setStyleSheet(button_style)
    self.start_button.setSizePolicy(sp_exp, sp_exp)
    self.start_button.clicked.connect(self.start_timer)
    button_layout.addWidget(self.start_button)

    self.stop_button = Qw.QPushButton("Stop")
    self.stop_button.setStyleSheet(button_style)
    self.stop_button.setSizePolicy(sp_exp, sp_exp)
    self.stop_button.clicked.connect(self.stop_timer)
    button_layout.addWidget(self.stop_button)

    self.reset_button = Qw.QPushButton("Reset")
    self.reset_button.setStyleSheet(button_style)
    self.reset_button.setSizePolicy(sp_exp, sp_exp)
    self.reset_button.clicked.connect(self.reset_timer)
    button_layout.addWidget(self.reset_button)

    self.btn_Quit = Qw.QPushButton("Quit")
    self.btn_Quit.clicked.connect(self.close)
    self.btn_Quit.setStyleSheet(button_style)
    self.btn_Quit.setSizePolicy(sp_exp, sp_exp)
    button_layout.addWidget(self.btn_Quit)

    self.timer = Qc.QTimer(self)
    self.timer.timeout.connect(self.update_timer)

    self.default_time = 25 * 60
    self.remaining_time = self.default_time
    self.user_set_time = self.default_time

  def start_timer(self):
    self.timer.start(1000)

  def stop_timer(self):
    self.timer.stop()

  def reset_timer(self):
    self.timer.stop()
    self.remaining_time = self.user_set_time
    self.update_timer_display()

  def set_custom_time(self):
    try:
      minutes = int(self.min_input.text()) if self.min_input.text() else 0
      seconds = int(self.sec_input.text()) if self.sec_input.text() else 0
      if minutes >= 0 and 0 <= seconds < 60:
        self.user_set_time = minutes * 60 + seconds
        self.remaining_time = self.user_set_time
        self.update_timer_display()
        Qw.QMessageBox.information(
            self, "Timer", f"Time set to {minutes} minutes and {seconds} seconds.")
      else:
        Qw.QMessageBox.warning(
            self, "Invaild input", "Please enter valid minutes (>= 0) and seconds (0-59).")
    except ValueError:
      Qw.QMessageBox.warning(
          self, "Invalid input", "Please enter valid numbers for minutes and seconds.")
    self.min_input.clear()
    self.sec_input.clear()

  def update_timer(self):
    if self.remaining_time > 0:
      self.remaining_time -= 1
      self.update_timer_display()
    else:
      self.timer.stop()
      Qw.QMessageBox.information(self, "Timer", "Time's up!")

  def update_timer_display(self):
    minutes, seconds = divmod(self.remaining_time, 60)
    self.timer_display.setText(f"{minutes:02}:{seconds:02}")
