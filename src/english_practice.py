import PySide6.QtWidgets as Qw
import PySide6.QtCore as Qc
import random

sp_exp = Qw.QSizePolicy.Policy.Expanding

class EnglishPractice(Qw.QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("English Practice")
    self.setGeometry(150, 150, 500, 300)
    layout = Qw.QVBoxLayout(self)

    #単語帳
    self.word_dict = {}

    #単語帳の登録
    self.add_word_label = Qw.QLabel("Add a New Word:", self)
    layout.addWidget(self.add_word_label)

    word_input_layout = Qw.QHBoxLayout()
    self.word_input = Qw.QLineEdit(self)
    self.word_input.setPlaceholderText("Enter English Word")
    word_input_layout.addWidget(self.word_input)

    self.meaning_input = Qw.QLineEdit(self)
    self.meaning_input.setPlaceholderText("Enter Meaning")
    word_input_layout.addWidget(self.meaning_input)

    self.add_word_button = Qw.QPushButton("Add Word", self)
    self.add_word_button.clicked.connect(self.add_word)
    word_input_layout.addWidget(self.add_word_button)

    layout.addLayout(word_input_layout)

    #単語帳の表示
    self.word_list_label = Qw.QLabel("Word List:", self)
    layout.addWidget(self.word_list_label)

    self.word_list = Qw.QListWidget(self)
    self.word_list.itemChanged.connect(self.remove_checked_words)
    layout.addWidget(self.word_list)

    #単語練習
    self.practice_label = Qw.QLabel("Practice Word:", self)
    layout.addWidget(self.practice_label)

    self.practice_word_label = Qw.QLabel("", self)
    self.practice_word_label.setStyleSheet("font-size: 18px; font-weight: bold;")
    layout.addWidget(self.practice_word_label)

    self.practice_input = Qw.QLineEdit(self)
    self.practice_input.setPlaceholderText("Enter the Meaning")
    layout.addWidget(self.practice_input)

    self.check_answer_button = Qw.QPushButton("Check Answer", self)
    self.check_answer_button.clicked.connect(self.check_answer)
    self.check_answer_button.setSizePolicy(sp_exp, sp_exp)
    layout.addWidget(self.check_answer_button)

    self.new_question_button = Qw.QPushButton("New Question", self)
    self.new_question_button.clicked.connect(self.new_question)
    self.new_question_button.setSizePolicy(sp_exp, sp_exp)
    layout.addWidget(self.new_question_button)

    self.result_label = Qw.QLabel("", self)
    layout.addWidget(self.result_label)

    self.btn_Quit = Qw.QPushButton("Quit")
    self.btn_Quit.clicked.connect(self.close)
    self.btn_Quit.setSizePolicy(sp_exp, sp_exp)
    layout.addWidget(self.btn_Quit)

  def add_word(self):
    """単語を追加する"""
    word = self.word_input.text().strip()
    meaning = self.meaning_input.text().strip()

    if not word or not meaning:
      Qw.QMessageBox.warning(self, "Input Error", "Please enter both word and meaning.")
      return

    if word in self.word_dict:
      Qw.QMessageBox.warning(self, "Duplicate Word", "This word is already in the list.")
      return

    self.word_dict[word] = meaning

    item = Qw.QListWidgetItem(f"{word} - {meaning}")
    item.setFlags(item.flags() | Qc.Qt.ItemFlag.ItemIsUserCheckable)
    item.setCheckState(Qc.Qt.CheckState.Unchecked)
    self.word_list.addItem(item)

    self.word_input.clear()
    self.meaning_input.clear()
    Qw.QMessageBox.information(self, "Word Added", f"'{word}' has been added to the word list.")

  def new_question(self):
    """ランダムな単語を出題する"""
    if not self.word_dict:  # 単語帳が空なら警告
      Qw.QMessageBox.warning(self, "No Words", "No words in the list. Add words first.")
      return

    try:
      self.current_word = random.choice(list(self.word_dict.keys()))
      self.practice_word_label.setText(self.current_word)
      self.practice_input.clear()
      self.result_label.clear()
    except IndexError:  # 念のためエラーハンドリング
      Qw.QMessageBox.warning(self, "Error", "Something went wrong. Please try again.")

  def check_answer(self):
    """回答をチェックする"""
    if not hasattr(self, "current_word") or not self.current_word:
      Qw.QMessageBox.warning(self, "No Question", "Please generate a question first.")
      return

    user_input = self.practice_input.text().strip()
    correct_answer = self.word_dict.get(self.current_word, "")

    if not correct_answer:
      Qw.QMessageBox.warning(self, "Error", "Something went wrong. Try again.")
      return

    if user_input.lower() == correct_answer.lower():
      self.result_label.setText("Correct!")
      self.result_label.setStyleSheet("color: green;")
    else:
      self.result_label.setText(f"Wrong! Correct answer is '{correct_answer}'.")
      self.result_label.setStyleSheet("color: red;")

  def remove_checked_words(self, item):
    """チェックされた単語を削除する"""
    if item.checkState() == Qc.Qt.CheckState.Checked:
      word = item.text()
      self.word_dict.pop(word, None)
      row = self.word_list.row(item)
      self.word_list.takeItem(row)