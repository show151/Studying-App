import PySide6.QtWidgets as Qw
import PySide6.QtCore as Qc
import os
import english_practice as ep
import json

DATA_FOLE = "words.json"

class EnglishWordDictionary(Qw.QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("English Practice")
    self.setGeometry(150, 150, 500, 300)
    layout = Qw.QVBoxLayout(self)

    #単語帳
    self.word_dict = self.load_words()

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

    self.update_word_list()

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
    self.save_words()
    self.update_word_list()
    self.word_input.clear()
    self.meaning_input.clear()
    Qw.QMessageBox.information(self, "Word Added", f"'{word}' has been added to the word list.", Qw.QMessageBox.StandardButton.Ok)

  def update_word_list(self):
    """単語帳を更新する"""
    self.word_list.clear()
    for word, meaning in self.word_dict.items():
      item = Qw.QListWidgetItem(f"{word}: {meaning}")
      item.setFlags(item.flags() | Qc.Qt.ItemFlag.ItemIsUserCheckable)
      item.setCheckState(Qc.Qt.CheckState.Unchecked)
      self.word_list.addItem(item)

  def remove_checked_words(self, item):
    """チェックされた単語を削除する"""
    new_dict = {word: meaning for word, meaning in self.word_dict.items() 
                if not any(f"{word}: {meaning}" == self.word_list.item(i).text()
                          and self.word_list.item(i).checkState() == Qc.Qt.CheckState.Checked
                          for i in range(self.word_list.count()))}

    if len(new_dict) != len(self.word_dict):
      self.word_dict = new_dict
      self.save_words()
      self.update_word_list()

  def save_words(self):
    """単語帳を保存する"""
    with open(DATA_FOLE, "w", encoding="utf-8") as file:
      json.dump(self.word_dict, file, ensure_ascii=False, indent=4)

  def load_words(self):
    """単語帳を読み込む"""
    if os.path.exists(DATA_FOLE):
      with open(DATA_FOLE, "r", encoding="utf-8") as file:
        return json.load(file)
    return {}

  def start_practice(self):
    """練習を開始する"""
    if not self.word_dict:
      Qw.QMessageBox.warning(self, "No Words", "Please add words to the list to start practicing.")
      return

    self.practice_window = ep.EnglishPractice(self.word_dict, self)
    self.practice_window.show()
    self.hide()