---
layout: post
title: Clay 3D Printing
---

## The Intersection of Computer Science and Pottery

I have recently been interested in finding projects that link pottery and computer science together. My mother is a visual artist who has spent a large portion of her life working with clay, and I have spent a large part of my life playing with and working on computers, currently working as a software developer.

I feel that we both exsert a lot of creativity in our respective fields, but it is quite hard to bridge the two in a common language.

Mum recently started working with clay 3D printers as part of personal career growth in her capacity as a lab technician at [AUT](https://www.aut.ac.nz/), and had the opportunity to lend my flatmate and I a [Cerambot](https://www.cerambot.com/) 3D printer for a few weeks to play around with. This blog post outlines the process of using the 3D printer to turn a design in Blender into a piece of pottery, and all the little issues along the way. But it also signifies the start of an interest in finding ways to combine the field of ceramics with computer science (tentative name for the project "Throwing Exceptions").

All of the technical work with the 3D printer was done in collaboration with my friend [Kieran](https://www.linkedin.com/in/kieran-hitchcock/), and all the glazing and firing was done in collaboration with my mother, in her pottery studio. A lot of inspiration and guidance was taken from [Jonathan Keep's blog](http://www.keep-art.co.uk/journal_1.html).

## Overview

I'll give an overview of the making process from design in blender to firing the finished product in a kiln, and then I'll give a summary of all the interesting hiccups, happy accidents, and learnings we had along the way.

Note that Kieran has done an awesome [write up](https://github.com/jerome3o/clay_3d_printing) on the specific setup for our [Cerambot](https://www.cerambot.com/) printer. However I will provide a general overview here for broader context and brevity.

## Process

### Design and rendering

- Design in Blender
  - We used the awesome open-source 3D design tool [Blender](https://www.blender.org/) to make our designs
  - Finished designs were exported as `.stl` files.
- Render in Cura
  - Import the `.stl` files into the open source 3D printing software [UltiMaker Cura](https://ultimaker.com/software/ultimaker-cura)
  - This program allows you to render your design to `.gcode` that will instruct the printer how to print the design
  - You'll need to get a good configuration for your printer setup - ours are defined [here](https://github.com/jerome3o/clay_3d_printing/tree/main/cura)
- We then put the `.gcode` files onto a MicroSD and take it to the printer

#### A note on design limitations

- Can't have any over-hanging parts or the clay will slump
- The larger designs can get quite unstable as the clay is very soft, so making sure the design is well stacked vertically is a must

### Printer setup

- Clay preparation
  - We used [Mac's Mud: Classic White](https://www.macsmud.co.nz/shop/product/299873/macs-mud-classic-white/) as a starting point
  - We mixed in water till the clay had a consistency of mud, allowing for better extrusion
- Filling the ram extruder
  - Getting the clay into the ram extruder without any air bubbles was a tricky task to get right, but we devised a repeatable method
  - The goal is to minimise air pockets, to avoid popping at the final extrusion
  - Method:
    - Compactly fill a tall container with the slushy clay
    - Push the ram extruder upside down into the clay, filling it up to the small outlet
    - This prevents most air bubbles and take the least amount of time
- Platform for the work to be printed on
  - We used bits of cardboard to print on, with a thin layer of clay on the top
  - This was in the hope that as the work dried and shrunk, the cardboard and clay layer would provide slack, preventing the work from cracking
  - This remained an issue, causing quite a few failures
- Make sure the printer is aligned with the ground plate
  - This is outlined in Kieran's write-up - it's a bit finicky, and can involve adding a custom gcode prefix to the generated code.
- Monitor printing
  - Turn on the printer, select the design and start printing!
  - Stand by incase of a failure, to reset and start again avoiding wasted time and clays
- Removing workings
  - Very carefully remove the work from the printer
  - Put it somewhere with relatively stagnant airflow
    - this allows it to dry slowly and evenly, reducing non-uniform shrinkage related cracks
- Cleaning up the printer
  - Once you've finished your printing session make sure to wash clay off all components
  - Letting clay dry on important mechanical components can be a pain to clean up later

### Pottery

- Bisque fire
- Glaze
- Fire

## Happy Accidents and Learnings

## Next steps

- Streamline the process
- Expertiment with glazes
- Try and get the outputs water tight
