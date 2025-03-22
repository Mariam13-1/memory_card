from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QPushButton,QRadioButton,QHBoxLayout,QMessageBox,QGroupBox,QButtonGroup
from random import shuffle 
from random import randint

class Question():
    def __init__(self,question,right_answer,wrong_answer1,wrong_answer2,wrong_answer3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

question_list = []
question_list.append(Question("What color doesn't exist in the American Flag?", "Green", "Red", "Blue", "White"))
question_list.append(Question("What is spoken languge in Egypt?", "Arabic", "French", "English", "Italian"))
question_list.append(Question("The national language of Brazil","Portogueze" ,"French" ,"English" ,"Spanish"))


app = QApplication([])    
main_win = QWidget ()
main_win.setWindowTitle ('Memory card project')

question_lb = QLabel("What nationality doesn't exist")

RadioGroupBox = QGroupBox("Answer options")
answer1 = QRadioButton('Enets')
answer2 = QRadioButton('smurfs')
answer3 = QRadioButton('Chulyms')
answer4 = QRadioButton('Aleuts')

RadioGroup = QButtonGroup()
RadioGroup.addButton(answer1)
RadioGroup.addButton(answer2)
RadioGroup.addButton(answer3)
RadioGroup.addButton(answer4)

answer_btn =  QPushButton('answer')

hlayout = QHBoxLayout()
vlayout1 = QVBoxLayout()
vlayout2 = QVBoxLayout()

vlayout1.addWidget(answer1, alignment= Qt.AlignCenter)
vlayout1.addWidget(answer2, alignment= Qt.AlignCenter)
vlayout2.addWidget(answer3, alignment= Qt.AlignCenter)
vlayout2.addWidget(answer4, alignment= Qt.AlignCenter)
hlayout.addLayout(vlayout1)
hlayout.addLayout(vlayout2)
RadioGroupBox.setLayout(hlayout)

ansGroupBox = QGroupBox("Test Results")
lb_result = QLabel("Correct\Incorrect")
lb_correct = QLabel ('The answer will be here')

lb_layout = QVBoxLayout ()
lb_layout.addWidget(lb_result, alignment= (Qt.AlignTop| Qt.AlignLeft))
lb_layout.addWidget(lb_correct, alignment= (Qt.AlignTop| Qt.AlignLeft))
ansGroupBox.setLayout(lb_layout)
ansGroupBox.hide()

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()



main_layout = QVBoxLayout()
layout_line1.addWidget(question_lb, alignment= Qt.AlignCenter, stretch = 2)
layout_line2.addWidget(RadioGroupBox , alignment= Qt.AlignCenter, stretch = 3)
layout_line2.addWidget(ansGroupBox , alignment= Qt.AlignCenter, stretch = 3)
layout_line3.addWidget(answer_btn, alignment= Qt.AlignCenter, stretch = 2)


main_layout.addLayout(layout_line1, stretch = 3)
main_layout.addLayout(layout_line2, stretch = 3)
main_layout.addStretch(3)
main_layout.addLayout(layout_line3, stretch = 3)

def show_ans():
    RadioGroupBox.hide()
    ansGroupBox.show()
    answer_btn.setText("Next Question")

def show_question():
    ansGroupBox.hide()
    RadioGroupBox.show()
    RadioGroup.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    RadioGroup.setExclusive(True)
    answer_btn.setText('answer')

answers = [answer1, answer2, answer3, answer4]
def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_answer1)
    answers[2].setText(q.wrong_answer2)
    answers[3].setText(q.wrong_answer3)
    lb_correct.setText(q.right_answer)
    question_lb.setText(q.question) 
    show_question()

def check_answers():
    if answers[0].isChecked():
        main_win.correct +=1
        show_correct('Correct')
        print("Total Questions",main_win.total)
        print("Correct Questions",main_win.correct)
        print("Rate",(main_win.correct/main_win.total)*100, "%")

    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Incorrect')

def show_correct(res):
    lb_result.setText(res)
    show_ans()

def next_question():
    main_win.total+=1
    cur_question = randint(0,len(question_list)-1)
    ask(question_list[cur_question])

def check_btn():
    if answer_btn.text () == "answer":
        check_answers()
    elif answer_btn.text () == "Next Question":
        next_question()


main_win.total = 0
main_win.correct = 0
next_question()
answer_btn.clicked.connect(check_btn)
main_win.setLayout(main_layout)
main_win.show()
app.exec_()





