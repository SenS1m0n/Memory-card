# 1) Link the necessary modules (QtCore and QtWidgets and their elements).
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('The state language of Brazil?', 'Portuguese', 'English', 'Spanish', 'Brazilian'))
question_list.append(Question('Which color does not appear on the American flag?', 'Green', 'Red', 'White', 'Blue'))
question_list.append(Question('A traditional residence of the Yakut people', 'Urasa', 'Yurt', 'Igloo', 'Hut'))
question_list.append(Question('Which football club is in england', 'Coventry', 'Rangers', 'Glamrock Rover', 'Swansea'))
question_list.append(Question('What is the least common color in a flag', 'Pink', 'Gray', 'Brown', 'Black'))
question_list.append(Question('What is the oldest football club in the world', 'Sheffield United', 'Tottenham Hotspurs', 'Coventry', 'QPR'))
question_list.append(Question('What is the biggest city in the world', 'Tokyo', 'London', 'New York', 'Shanghai'))
question_list.append(Question('What was the biggest recorded country in human history', 'The Mongol Empire', 'The Soviet union', 'Russia(2024)', 'The Roman empire'))
question_list.append(Question('How old is Vietnam according to available records', '4000y.o', '1000y.o', '3000y.o', '6000y.o'))
question_list.append(Question('What was the fastest goal scored in football', '1.8 seconds', '6.2 seconds', '3.5 seconds', '2.5 seconds'))
question_list.append(Question('What is the country with the most and best quality football making', 'Pakistan', 'England', 'China', 'Brazil'))
question_list.append(Question('When was the first ever World Cup held', '1930', '1926', '1966', '1827'))
question_list.append(Question('How old is the oldest still playing footballer', '57y.o', '41y.o', '45y.o', '54y.o'))
question_list.append(Question('Who has scored the most points in basketball', 'Lebron James', 'Kobe Bryant', 'Kareem Abdul Jabbar', 'Wilt CHamberlain'))
question_list.append(Question('Which athlete won the largest number of gold medals at the Olympic Games', 'Michael Phelps', 'Usain Bolt', 'Maria Sharapavo', 'Yusuf Bolt'))


app = QApplication([])
win = QWidget()
win.setWindowTitle('Memory Card')

# 2) Create an application object, windowed application. Set the heading and dimensions.
lb_Question = QLabel('The most diffcult question in the wolrd')
btn_OK = QPushButton('Answer')

RadioGroupBox = QGroupBox('Answer Options')

rbtn1 = QRadioButton('Option1')
rbtn2 = QRadioButton('Option2')
rbtn3 = QRadioButton('Option3')
rbtn4 = QRadioButton('Option4')

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox= QGroupBox('Test result')
lb_Result = QLabel('Are you correct or not?')
lb_Correct = QLabel('the answer will be here!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignmentFlag.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout() #question
layout_line2 = QHBoxLayout() #answer options
layout_line3 = QHBoxLayout() #button

layout_line1.addWidget(lb_Question, alignment=Qt.AlignmentFlag.AlignCenter)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_line3.addWidget(btn_OK)


layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

win.setLayout(layout_card)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next question')
    
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Answer')
    
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

def test():
    if btn_OK.text() == 'Answer':
        show_result()
    else:
        show_question()
        
answers = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q : Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()
  
def check_answer():
    if answers[0].isChecked():  
        show_correct('Correct!')
        win.score += 1
        print('Statistics\n -Total question:', win.total, '\n - Right answer:', win.score)
        print('Rating:', win.score/win.total*100,'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Incorrect!')
            print('Rating:', win.score/win.total*100,'%')

def next_question():
    win.total += 1
    if win.total - 1 < len(question_list):
        ask(question_list[win.total - 1])
    else:
        win.total -= 1
        RadioGroupBox.hide()
        AnsGroupBox.setTitle("Quiz has ended!")
        lb_Result.setText("You have answered " + str(win.score) + " out of " + str(win.total) + " questions correctly!")
        lb_Correct.setText("Your final grade is " + str(win.score/win.total * 100) + "%")
        lb_Question.hide()
        AnsGroupBox.show()
        
def click_OK():
    if btn_OK.text() == 'Answer':
        check_answer()
    else:
        next_question()
        
win.total = 0
win.score = 0
win.cur_question = 0
btn_OK.clicked.connect(click_OK)
next_question()
win.show()
app.exec()

