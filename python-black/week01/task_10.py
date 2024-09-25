#! /usr/bin/env python3
# Задача 10

from enum import Enum

class State(Enum):
    NOTHING = 1
    OPEN_DOUBLE_QUOTE = 2
    OPEN_SINGLE_QUOTE = 3

slash_state_enabled = False
current_state = State.NOTHING
buffer = ""
texts = []

string = input()

for char in string:

    if char == '"' and not slash_state_enabled:
        if current_state == State.OPEN_DOUBLE_QUOTE:
            current_state = State.NOTHING
            texts.append(buffer)
            buffer = ""
            continue
        elif current_state == State.NOTHING:
            current_state = State.OPEN_DOUBLE_QUOTE
            continue
    elif char == "'" and not slash_state_enabled:
        if current_state == State.OPEN_SINGLE_QUOTE:
            current_state = State.NOTHING
            texts.append(buffer)
            buffer = ""
            continue
        elif current_state == State.NOTHING:
            current_state = State.OPEN_SINGLE_QUOTE
            continue
    elif char == '\\' and not slash_state_enabled:
        slash_state_enabled = True
        continue

    if slash_state_enabled and char not in '"\'\\':
        slash_state_enabled = False
        buffer += '\\'

    if current_state != State.NOTHING:
        slash_state_enabled = False
        buffer += char

for text in texts:
    print(text)
