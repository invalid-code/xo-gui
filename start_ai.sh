#!/bin/bash
tmux list-panes | grep "active" | cut -d':' -f1| xargs tmux clear-history -t 
clear
python test_ai.py
