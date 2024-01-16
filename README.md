# GPT-Hackathon - Chess network analysis
My submission for a GPT themed hackathon in NYC.

This code was 100% written by ChatGPT and lots of prompting

# Overview
This repo contains a script that that uses chess.pgn, networkx, and matplotlib to connect chess games together from a very large pgn file. The script creates a directed graph with players as nodes and their game outcomes as edges. 

# Installation
To run this you just need to install pip install chess, networkx, and matplotlib

You will also need a large pgn file - get them courtesy of [the lichess database](https://database.lichess.org/)

I used 2014-02, and then trimmed it down to 10,000 games because the file sizes are _huge._

# Usage

Run the script and you should get something like this 
![image](https://github.com/IsaacGemal/GPT-Hackathon/assets/147355120/6f012262-d114-436f-921b-9c9f39eea3f9)

It takes about 12 seconds on my decently spec'd PC to comb through 10,000 games

# Bugs

I'm sure there's plenty of bugs - for instance it will crash if you make up a username. But that's within the margin of error for a hackathon.

# Closing notes

If you do anything cool with this please let me know!
