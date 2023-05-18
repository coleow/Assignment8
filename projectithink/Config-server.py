import zmq
import time

# Citation: ZeroMQ beginner tutorial

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


def choose_sort_option(enter_a_digit):
    
    sort_options = {"1": "alphabetically", "2": "most-recent", "3": "phrase", "4": "username"}
    return sort_options.get(enter_a_digit, "wrong digit")


while True:
    
    enter_a_digit = socket.recv().decode()

    time.sleep(1)

    sort_order = choose_sort_option(enter_a_digit)

    socket.send(sort_order.encode())