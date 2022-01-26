import string
from tkinter import *
from tkinter.ttk import *
import datetime
import platform
try:
    import winsound
except:
    import os

#WINDOW_CREATE
window = Tk()
window.title("Clock")
window.geometry('500x250')

#STOPWATCH_VARIABLES
stopwatch_counter_num = 1
stopwatch_running = False

#TIMER_VARIABLES
timer_counter_num = 0
timer_running = False

#CLOCK_FUNCTION
def clock():
    date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
    date, time1 = date_time.split()
    time2, time3 = time1.split("/")
    hour, minute, second = time2.split(":")

    if int(hour) > 12 and int(hour) < 24:
        time = str(int(hour) - 12) + ':' + minute + ':' + second + ' ' + time3
    else:
        time = time2 + ' ' + time3
    
    time_label.config(text = time)
    date_label.config(text = date)
    time_label.after(1000, clock)

#ALARM_FUNCTION
def alarm():
    main_time = datetime.datetime.now().strftime("%H:%M %p")
    alarm_time = alarm_entry.get()
    alarm_time1, alarm_time2 = alarm_time.split(' ')
    alarm_hour, alarm_minutes = alarm_time1.split(':')
    main_time1, main_time2 = main_time.split(' ')
    main_hour1, main_minutes = main_time1.split(':')
    if int(main_hour1) > 12 and int(main_hour1) < 24:
        main_hour = str(int(main_hour1) - 12)
    else:
        main_hour = main_hour1
    if int(alarm_hour) == int(main_hour) and int(alarm_minutes) == int(main_minutes) and main_time2 == alarm_time2:
        for i in range(3):
            alarm_status.config(text = 'Time is up!')
            if platform.system() == 'Windows':
                winsound.Beep(5000, 1000)
            elif platform.system() == 'Darwin':
                os.system('say Time is Up')
            elif platform.system() == 'Linux':
                os.system('beep -f 5000')
        alarm_entry.config(state = 'enabled')
        alarm_button.config(state = 'enabled')
        alarm_entry.delete(0, END)
        alarm_status.config(text = '')
    else:
        alarm_status.config(text = 'Alarm has started')
        alarm_entry.config(state = 'disabled')
        alarm_button.config(state = 'disabled')
    alarm_status.after(1000, alarm)

#STOPWATCH_FUNCTIONS
def stopwatch_counter(label):
    def count():
        if stopwatch_running:
            global stopwatch_counter_num
            tt = datetime.datetime.fromtimestamp(stopwatch_counter_num)
            string = tt.strftime("%M:%S")
            display = string
            label.config(text = display)
            label.after(1000, count)
            stopwatch_counter_num += 1
    count()

def stopwatch(work):
    if work == 'start':
        global stopwatch_running
        stopwatch_running = True
        stopwatch_start.config(state = 'disabled')
        stopwatch_stop.config(state = 'enabled')
        stopwatch_reset.config(state = 'enabled')
        stopwatch_counter(stopwatch_label)
    elif work == 'stop':
        stopwatch_running = False
        stopwatch_start.config(state = 'enabled')
        stopwatch_stop.config(state = 'disabled')
        stopwatch_reset.config(state = 'enabled')
    elif work == 'reset':
        global stopwatch_counter_num
        stopwatch_running = False
        stopwatch_counter_num = 1
        stopwatch_label.config(text = 'Stopwatch')
        stopwatch_start.config(state = 'enabled')
        stopwatch_stop.config(state = 'disabled')
        stopwatch_reset.config(state = 'disabled')

#TIMER_FUNCTIONS
def timer_counter(label):
    def count():
        global timer_running
        if timer_running:
            global timer_counter_num
            if timer_counter_num == 0:
                for i in range(3):
                    display = "Time is up!"
                    if platform.system() == 'Windows':
                        winsound.Beep(5000, 1000)
                    elif platform.system() == 'Darwin':
                        os.system('say Time is Up')
                    elif platform.system() == 'Linux':
                        os.system('beep -f 5000')
            timer_running = False
            timer('reset')
        else:
            tt = datetime.datetime.fromtimestamp(timer_counter_num)
            string = tt.strftime('%H:%M:%S')
            display = string
            timer_counter_num -= 1
            label.config(text = display)
        label.after(1000, count)
    count()

def timer(work):
    if work == 'start':
        global timer_running, timer_counter_num
        timer_running = True
        if timer_counter_num == 0:
            timer_time_str = timer_entry.get()
            hours, minutes, seconds = timer_time_str.split(':')
            minutes = int(minutes) + (int(hours) * 60)
            seconds = int(seconds) + (int(minutes) * 60)
            timer_counter_num = timer_counter_num + seconds
        timer_counter(timer_label)
        timer_start.config(state = 'disabled')
        timer_stop.config(state = 'enabled')
        timer_reset.config(state = 'enabled')
        timer_entry.delete(0, END)
    elif work == 'stop':
        timer_running = False
        timer_start.config(state = 'enabled')
        timer_stop.config(state = 'disabled')
        timer_reset.config(state = 'enabled')
    elif work == 'reset':
        timer_running = False
        timer_counter_num = 0
        timer_start.config(state = 'enabled')
        timer_stop.config(state = 'disabled')
        timer_reset.config(state = 'disabled')
        timer_entry.config(state = 'enabled')
        timer_label.config(text = 'Timer')


#TAB_CONTROL
tabs_control = Notebook(window)
clock_tab = Frame(tabs_control)
alarm_tab = Frame(tabs_control)
stopwatch_tab = Frame(tabs_control)
timer_tab = Frame(tabs_control)
tabs_control.add(clock_tab, text = 'Clock')
tabs_control.add(alarm_tab, text = 'Alarm')
tabs_control.add(stopwatch_tab, text = 'Stopwatch')
tabs_control.add(timer_tab, text = 'Timer')
tabs_control.pack(expand = 1, fill = "both")

#CLOCK_CONTROL
time_label = Label(clock_tab, font = 'calibri 40 bold', foreground = 'black')
time_label.pack(anchor = 'center')
date_label = Label(clock_tab, font = 'calibri 40 bold', foreground = 'black')
date_label.pack(anchor = 's')

#ALARM_CONTROL
alarm_entry = Entry(alarm_tab, font = 'calibri 15 bold')
alarm_entry.pack(anchor = 'center')
alarm_instructions = Label(alarm_tab, font = 'calibri 10 bold', text = "Enter Alarm Time. Eg -> 01:30 PM, 01 -> Hour, 30 -> Minutes")
alarm_instruction = Label(anchor = 's')
alarm_button = Button(alarm_tab, text = "Set Alarm", command = alarm)
alarm_button.pack(anchor = 's')
alarm_status = Label(alarm_tab, font = 'calibri 15 bold')
alarm_status.pack(anchor = 's')

#STOPWATCH_CONTROL
stopwatch_label = Label(stopwatch_tab, font='calibri 40 bold', text='Stopwatch')
stopwatch_label.pack(anchor='center')
stopwatch_start = Button(stopwatch_tab, text='Start', command=lambda:stopwatch('start'))
stopwatch_start.pack(anchor='center')
stopwatch_stop = Button(stopwatch_tab, text='Stop', state='disabled',command=lambda:stopwatch('stop'))
stopwatch_stop.pack(anchor='center')
stopwatch_reset = Button(stopwatch_tab, text='Reset', state='disabled', command=lambda:stopwatch('reset'))
stopwatch_reset.pack(anchor='center')

#TIMER_CONTROL
timer_entry = Entry(timer_tab, font = 'calibri 15 bold')
timer_entry.pack(anchor = 'center')
timer_instructions = Label(timer_tab, font = 'calibri 10 bold', text = 'Enter Timer Time. Eg -> 01:30:30, 01 -> Hour, 30 -> Minutes, 30 -> Seconds')
timer_instructions.pack(anchor = 'center')
timer_label = Label(timer_tab, font = 'calibri 50 bold', text = 'Timer')
timer_label.pack(anchor = 'center')
timer_start = Button(timer_tab, text = 'Start', command=lambda:timer('start'))
timer_start.pack(anchor = 'center')
timer_stop = Button(timer_tab, text = 'Stop', state = 'disabled', command=lambda:timer('stop'))
timer_stop.pack(anchor = 'center')
timer_reset = Button(timer_tab, text = 'Reset', state = 'disabled', command=lambda:timer('reset'))
timer_reset.pack(anchor = 'center')

#FINALIZE
clock()
window.mainloop()