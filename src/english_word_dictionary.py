import PySide6.QtWidgets as Qw
import PySide6.QtCore as Qc
import random
import english_practice as ep

class EnglishWordDictionary(Qw.QWidget):
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

    self.practice_button = Qw.QPushButton("Practice", self)
    self.practice_button.clicked.connect(self.start_practice)
    layout.addWidget(self.practice_button)

    self.btn_Quit = Qw.QPushButton("Quit")
    self.btn_Quit.clicked.connect(self.close)
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

  def remove_checked_words(self, item):
    """チェックされた単語を削除する"""
    if item.checkState() == Qc.Qt.CheckState.Checked:
      word = item.text()
      self.word_dict.pop(word, None)
      row = self.word_list.row(item)
      self.word_list.takeItem(row)

  def start_practice(self):
    """練習を開始する"""
    if not self.word_dict:
      Qw.QMessageBox.warning(self, "No Words", "Please add words to the list to start practicing.")
      return

    self.practice_window = ep.EnglishPractice(self.word_dict, self)
    self.practice_window.show()
    self.hide()