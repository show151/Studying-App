import PySide6.QtWidgets as Qw
import PySide6.QtCore as Qc
import random

class EnglishPractice(Qw.QWidget):
  """練習用ウィンドウ"""
  def __init__(self, word_dict, parent):
    """初期化"""
    super().__init__()
    self.setWindowTitle("English Practice")
    self.setGeometry(150, 150, 500, 300)
    self.word_dict = word_dict
    self.parent = parent

    layout = Qw.QVBoxLayout(self)

    self.question_label = Qw.QLabel("", self)
    self.question_label.setStyleSheet("font-size: 18px; font-weight: bold;")
    layout.addWidget(self.question_label)

    self.button_group = Qw.QButtonGroup(self)
    self.button_group.setExclusive(True)

    self.option_buttons = []
    for i in range(4):
      btn =  Qw.QRadioButton("", self)
      self.option_buttons.append(btn)
      self.button_group.addButton(btn)
      layout.addWidget(btn)

    self.check_button = Qw.QPushButton("Check Answer", self)
    self.check_button.clicked.connect(self.check_answer)
    layout.addWidget(self.check_button)

    self.show_answer_button = Qw.QPushButton("Show Answer", self)
    self.show_answer_button.clicked.connect(self.show_answer)
    layout.addWidget(self.show_answer_button)

    self.result_label = Qw.QLabel("", self)
    layout.addWidget(self.result_label)

    self.next_button = Qw.QPushButton("Next Question", self)
    self.next_button.clicked.connect(self.new_question)
    layout.addWidget(self.next_button)

    self.btn_Quit = Qw.QPushButton("Quit")
    self.btn_Quit.clicked.connect(self.close)
    layout.addWidget(self.btn_Quit)

    self.new_question()

  def new_question(self):
    """ランダムな問題作成、4択表示"""
    if not self.word_dict:
      Qw.QMessageBox.warning(self, "Error", "No words in the dictionary.")
      return

    self.current_word = random.choice(list(self.word_dict.keys()))
    self.question_label.setText(self.current_word)

    correct_answer = self.word_dict[self.current_word]
    all_answers = list(self.word_dict.values())

    choices = random.sample(all_answers, min(len(all_answers), 4))
    if correct_answer not in choices:
      choices[random.randint(0, 3)] = correct_answer

    random.shuffle(choices)

    self.button_group.setExclusive(False)
    for btn in self.option_buttons:
      btn.setText("")
      btn.setChecked(False)
    self.button_group.setExclusive(True)

    for i, btn in enumerate(self.option_buttons):
      btn.setText(choices[i])

    self.result_label.clear()

  def check_answer(self):
    """回答チェック"""
    selected_button = self.button_group.checkedButton()
    if not selected_button:
      Qw.QMessageBox.warning(self, "Error", "Please select an answer.")
      return

    selected_text = selected_button.text()
    correct_answer = self.word_dict[self.current_word]

    if not correct_answer:
      Qw.QMessageBox.warning(self, "Error", "No correct answer found.")
      return

    if selected_text == correct_answer:
      self.result_label.setText("Correct!")
      self.result_label.setStyleSheet("color: green;")
    else:
      self.result_label.setText(
          f"Incorrect! Correct answer: {correct_answer}")
      self.result_label.setStyleSheet("color: red;")

  def show_answer(self):
    """正解を表示"""
    if not hasattr(self, "current_word") or self.current_word not in self.word_dict:
      Qw.QMessageBox.warning(self, "Error", "No question available. Please start a new question.")
      return

    correct_answer = self.word_dict[self.current_word]
    self.result_label.setText(f"Correct answer: {correct_answer}")
    self.result_label.setStyleSheet("color: lightblue;")

  def close(self):
    """ウィンドウを閉じる"""
    self.parent.show()
    super().close()