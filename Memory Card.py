#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets (QApplication, Qwidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox, QMessageBox, QRadioButton)
from random import randint

app = QApplication ([])
main_win = Qwidget()
main_win.setWindowTitle('Memory Card')

btn_OK = QPushButton ('Ответить')
lb_Question = QLabel ('В каком году родился А.С. Пушкин?')
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('1801')
rbtn_2 = QRadioButton('1799')
rbtn_3 = QRadioButton('1810')
rbtn_4 = QRadioButton('1765')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, aligment =(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBox
layout_card.setSpacing(5)





class Question():
    def (self, question, right_answer, wrong1, wrong2, wrong3)
    self.question = question
    self.right_answer = right_answer
    self.wrong1 = wrong1
    self.wrong2 = wrong2
    self.wrong3 = wrong3

questions_list = []
questions_list.append(Question ('Кто национальные жители Швеции?', 'Шведы', 'Англичане', 'Монголы', 'Африканцы'))
questions_list.append(Question('Какой цвет есть на флаге Бразилии?', 'Зелёный', 'Чёрный', 'Розовый', 'Фиолетовый'))
questions_list.append(Question('Кто был основателем Америки?', 'Христофор Колумб', 'Васко да Гама', 'Александр Македонский', 'Наполеон'))

def show_result():
    RadioGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Cтатистика\n-Всего вопросов: ', window.total,'\n-Правильныx ответов', window.total)
        print('Рейтинг: ', (window.score / window.total * 100), '%')
        else:
            if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked()
            show_correct('Неверно!')
            

def next_question():
    window.score += 1
    print('Cтатистика\n-Всего вопросов: ', window.total,'\n-Правильныx ответов', window.total)
    cur_question = randint(0, len(questions_list) -1)
    q = questions_list[cur_question]
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(questions_list):
        window.cur_question = 0
    q = questions_list[window.cur_question]
    ask (q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
        else:
        next_question()
window = Qwidget ()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')

btn_OK.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_question()
window.resize(400, 300)
window.show()
app.exec()


def ask(q: Question):
    shuffle (answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question ()