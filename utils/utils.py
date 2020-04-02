from time import sleep


def slow_input(search_input, phrase):
    for c in phrase:
        sleep(0.1)
        search_input.send_keys(c)
