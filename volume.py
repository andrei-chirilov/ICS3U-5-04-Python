#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: November 2019
# This program calcultes the volume of a cylinder

import math


def volume_calculator(radius, height):
    # This'll determine the volume

    # process
    volume = math.pi * radius * radius * height
    return round(volume, 2)


def main():
    # This asks for user input and runs volume_calculator()

    while True:
        try:
            # input
            radius = float(input("What is the radius: "))
            height = float(input("What is the height: "))
            # runs volume_calculator()
            volume = volume_calculator(height=height, radius=radius)
            # output
            print("The volume is " + str(volume) + " units cubed.")
            break
        except ValueError:
            print("Invalid input.")


if __name__ == "__main__":
    main()
