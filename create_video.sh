#!/bin/bash
mencoder mf://\*.png -mf w=800:h=600:fps=10:type=png -ovc lavc -lavcopts vcodec=mpeg4 -oac copy -o output.avi
