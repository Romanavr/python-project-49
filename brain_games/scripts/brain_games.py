#!/usr/bin/env python3

from brain_games import cli

def greetings():
    print('Welcome to the Brain Games!')

def main():
    greetings()
    cli.welcome_user()

if __name__ == '__main__':
    main()
