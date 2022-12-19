import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout,\
    QVBoxLayout, QPushButton,QGridLayout,QLabel


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.count = 0
        self.move(700, 200)
        self.resize(500, 450)
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_label = QHBoxLayout()

        self.hbox_result = QHBoxLayout()
        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)


        self.vbox.addLayout(self.hbox_result)


        self.a = QLabel(self)
        self.a.setGeometry(5, 5, 490, 70)


        self.input = QLineEdit(self)
        self.input.setGeometry(5, 5, 490, 70)
        self.b_1 = QPushButton("1", self)
        self.b_1.setGeometry(5, 150, 90, 40)
        self.b_2 = QPushButton("2", self)
        self.b_2.setGeometry(95, 150, 90, 40)
        self.b_3 = QPushButton("3", self)
        self.b_3.setGeometry(185, 150, 90, 40)
        self.b_4 = QPushButton("4", self)
        self.b_4.setGeometry(5, 200, 90, 40)
        self.b_5 = QPushButton("5", self)
        self.b_5.setGeometry(95, 200, 90, 40)
        self.b_6 = QPushButton("6", self)
        self.b_6.setGeometry(185, 200, 90, 40)
        self.b_7 = QPushButton("7", self)
        self.b_7.setGeometry(5, 250, 90, 40)
        self.b_8 = QPushButton("8", self)
        self.b_8.setGeometry(95, 250, 90, 40)
        self.b_9 = QPushButton("9", self)
        self.b_9.setGeometry(185, 250, 90, 40)
        self.b_0= QPushButton("0", self)
        self.b_0.setGeometry(95, 300, 90, 40)


        self.b_plus = QPushButton("+", self)
        self.b_plus.setGeometry(275, 150, 90, 40)

        self.b_minus = QPushButton("-", self)
        self.b_minus.setGeometry(275, 200, 90, 40)

        self.b_mul = QPushButton("*", self)
        self.b_mul.setGeometry(275, 250, 90, 40)

        self.b_div = QPushButton("/", self)
        self.b_div.setGeometry(365, 150, 90, 40)

        self.b_clear = QPushButton("Clear",self)
        self.b_clear.setGeometry(365, 200, 90, 40)

        self.b_10 = QPushButton(".", self)
        self.b_10.setGeometry(365, 300, 90, 40)

        self.b_result = QPushButton("=", self)
        self.b_result.setGeometry(365, 250, 90, 40)


        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_mul.clicked.connect(lambda: self._operation("*"))
        self.b_div.clicked.connect(lambda: self._operation("/"))


        self.b_clear.clicked.connect(lambda: self.action_clear())


        self.b_result.clicked.connect(self._result)
        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))
        self.b_10.clicked.connect(lambda: self._button("."))


    def action_clear(self):

        self.input.setText("")


    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)


    def _operation(self, op):
        try:
            self.num_1 = float(self.input.text())
            self.op = op
            self.input.setText("")
            self.a.setText(self.a.text()+op)
            self.count +=1
            if self.count >=2:
                self.a.setText("0")
        except:
            self.a.setText("0")
    def _result(self):
        try:

            self.num_2 = int(self.input.text())

            if self.op == "+":
                self.input.setText(str(self.num_1 + self.num_2))
            if self.op == "-":
                self.input.setText(str(self.num_1 - self.num_2))
            if self.op == "*":
                self.input.setText(str(self.num_1 * self.num_2))
            if self.op == "/":
                try:
                    self.input.setText(str(self.num_1 / self.num_2))
                except:
                    self.input.setText("Error")

        except:
            self.a.setText("0")

if __name__ == '__main__':

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

    ///////
    
    import telebot
import psycopg2
from telebot import types
from datetime import datetime

conn = psycopg2.connect(database="bot",
                        user="postgres",
                        password="1106",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()

token = '5866865230:AAF0VDLnMpyDLvGI5HeJkM8F7_jc7IJWy9Q'
bot = telebot.TeleBot(token)
ping_counter = 0

days_list = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота"]
week_number = datetime.today().isocalendar()[1] % 2


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    butn1 = types.KeyboardButton("Расписание на текущую неделю")
    butn2 = types.KeyboardButton("Расписание на следующую неделю")
    butn3 = types.KeyboardButton("Понедельник")
    butn4 = types.KeyboardButton("Вторник")
    butn5 = types.KeyboardButton("Среда")
    butn6 = types.KeyboardButton("Четверг")
    butn7 = types.KeyboardButton("Пятница")
    butn8 = types.KeyboardButton("Суббота")


    bot.send_message(message.chat.id, "Привет ,{first},Данный бот был создан для того,чтобы показать расписание МТУСИ."
                                      "\nВы можете ознакомится с возможностями данного бота, используя команду /help".format(first=message.from_user.first_name, reply_markup=keyboard))


@bot.message_handler(commands=['week'])
def weekNumber(message):
    if week_number == 1:
        bot.send_message(message.chat.id, "Сейчас  нечетная неделя")
    else:
        bot.send_message(message.chat.id, "Сейчас  четная неделя")





@bot.message_handler(commands=['help'])
def weekNumber(message):
    bot.send_message(message.chat.id, "Описание доступных команд:\n"
                                      "/help - Узнать команды бота\n"
                                      "/week - Узнать какая сейчас неделя (четная/нечетная) "
                                      "\n /cat - Выводит смешного кота "
                                      "\n /date - Узнать какая сейчас дата "
                                      "\n <Расписание на текущую неделю> -Узнать расписание на эту неделю "
                                      "\n <Расписание на следующую неделю> - Узнать расписание на будущую неделю"
                                      "\n <Понедельник - Суббота>  - Узнать расписание на определенный день")


@bot.message_handler(commands=['date'])
def date(message):
    bot.send_message(message.chat.id,"Дата    " + datetime.now().strftime("%y.%m.%d %H:%M:%S"))


@bot.message_handler(commands=['cat'])
def cat(message):
    bot.send_video(message.chat.id, 'https://tenor.com/ru/view/cat-the-cat-he-dance-he-dance-gif-24077288')
@bot.message_handler(content_types='text')
def reply(message):
    if message.text.lower() in days_list:
        if week_number == 1:
            cursor.execute(f"SELECT * FROM timetable where day = '{message.text.lower()} 1' or day = '{message.text.lower()} 0' order by start_time")
        else:
            cursor.execute(f"SELECT * FROM timetable where day = '{message.text.lower()} 2' or day = '{message.text.lower()} 0' order by start_time")
        records = list(cursor.fetchall())
        text = f"{message.text}:\n"
        text += '____________________________________________________________\n'
        for i in records:
            text += f"Предмет: {i[2]}; Кабинет: {i[3]}; Время: {i[4]} Преподаватель: {i[5]}\n"
        text += "____________________________________________________________"
        bot.send_message(message.chat.id, text)
    elif 'текущую' in message.text.lower():
        text = ""
        for i in days_list:
            if week_number == 1:
                cursor.execute(f"SELECT * FROM timetable where day = '{i} 1' or day = '{i} 0' order by start_time")
            else:
                cursor.execute(f"SELECT * FROM timetable where day = '{i} 2' or day = '{i} 0' order by start_time")
            records = list(cursor.fetchall())
            text += f'{i.title()}:\n'
            text += '____________________________________________________________\n'
            if not records:
                text += "Выходной\n"
            for j in records:
                text += f"Предмет: {j[2]} Кабинет: {j[3]} Время: {j[4]} Преподаватель: {j[5]} \n"
            text += "____________________________________________________________"
            text += '\n\n'
        bot.send_message(message.chat.id, text)
    elif 'следующую' in message.text.lower():
        text = ""
        for i in days_list:
            if week_number + 1 == 1:
                cursor.execute(f"SELECT * FROM timetable where day = '{i} 1' or day = '{i} 0' order by start_time")
            else:
                cursor.execute(f"SELECT * FROM timetable where day = '{i} 2' or day = '{i} 0' order by start_time")
            records = list(cursor.fetchall())
            text += f'{i.title()}:\n'
            text += '____________________________________________________________\n'
            if not records:
                text += "Выходной\n"
            for j in records:
                text += f"Предмет: {j[2]} Кабинет: {j[3]} Время: {j[4]} Преподаватель: {j[5]} \n"
            text += "____________________________________________________________"
            text += '\n\n'
        bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, "Извините, я Вас не понял")


bot.infinity_polling()
