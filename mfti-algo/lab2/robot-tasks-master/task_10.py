#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_3():
    if not chek_wall_up_and_down():
        fill_cell()
    while not wall_is_on_the_right():
        move_right()
        if not chek_wall_up_and_down():
            fill_cell()

def chek_wall_up_and_down():
    return not wall_is_above() and not wall_is_beneath()

if __name__ == '__main__':
    run_tasks()
