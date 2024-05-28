#создай приложение для запоминания информаци
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel, QButtonGroup)
from random import shuffle
from random import randint


app = QApplication([])

class Question():
        def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
            self.question = question 
            self.right_answer = right_answer
            self.wrong1 = wrong1
            self.wrong2 = wrong2
            self.wrong3 = wrong3

list_question = []
list_question.append(Question('Перевод слова Hello:', 'Привет', 'Амогус', 'пока', 'я голодный'))
list_question.append(Question('Столица России', "Москва", "камчатка", 'Ленск', 'Лондон'))
list_question.append(Question('Кто написал Гарри Поттера', 'Джоанн Роулинг', "Гарри Поттер", 'Месси', 'Бузова'))
list_question.append(Question('Какой мой любимый цвет', 'бирюзовый', 'голубой', 'Синий', 'Хелп они же одинаковы'))
list_question.append(Question('кто из них зеленый', 'куроппи', 'куроми', 'пумпурин', 'синаморол'))
list_question.append(Question('кто получил премию на лучшую песню', "newjeans", "itzy", 'gidle', 'twice'))

# Создаем панель вопроса
btn_OK = QPushButton('Начать тест')
lb_Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox("Варианты ответов")


rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox.setLayout(layout_ans1)


# Создаем панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


# Размещаем все виджеты в окне:
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# Размещаем в одной строке обе панели, одна из них будет скрываться, другая показываться:
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
RadioGroupBox.hide() # эту панель мы уже видели, скроем, посмотрим, как получилась панель с ответом


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)


# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым

def show_question():
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn_OK.setText('Ответить')
        RadioGroup.setExclusive(False)
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def show_result():
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('Следующий вопрос')



def show_correct(res):
        lb_Result.setText(res)
        show_result()

def next_question():
        window.total+= 1
        cur_question = randint(0, len(list_question) - 1)
        q = list_question[cur_question]
        ask(q)
        
def click_OK():
        if btn_OK.text() == 'Ответить':
                check_answer()
        else:
            next_question()


def ask(q: Question):
        shuffle(answers)
        answers[0].setText(q.right_answer)
        answers[1].setText(q.wrong1)
        answers[2].setText(q.wrong2)
        answers[3].setText(q.wrong3)
        lb_Question.setText(q.question)
        lb_Correct.setText(q.right_answer)
        show_question()

def check_answer():
        if answers[0].isChecked():
                show_correct('Правильно!')
                window.score += 1
                print('Статистика')
                print('Всего вопросов:', window.total)
                print('Правильных ответов:', window.score)
                print('Рейтинг:', (window.score/window.total)*100)
        else:
            if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
                show_correct('Неправильно')
                print('Статистика')
                print('Всего вопросов:', window.total)
                print('Правильных ответов:', window.score)
                print('Рейтинг:', (window.score/window.total)*100)
      
window = QWidget()
window.setLayout(layout_card)
btn_OK.clicked.connect(click_OK)   
window.score = 0
window.total = 0
next_question() 
window.cur_question = -1
window.setWindowTitle('Memory Card')


window.resize(400,300)
window.show()
app.exec()



#window.cur_question += 1
        #if window.cur_question >= len(list_question):
            #    window.cur_question = 0
       # q = list_question[window.cur_question]
        #ask(q)