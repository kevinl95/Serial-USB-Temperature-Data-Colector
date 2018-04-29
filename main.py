#!/usr/bin/env python

import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import os
import serial
import serial.tools.list_ports
import tkinter as tk
import time
from time import sleep
from tkinter import filedialog as fd
from tkinter import ttk


running = True
f = ""


def collect(strPort, interval):
    global f
    # Ask for a location to save the CSV file
    f = fd.asksaveasfile(mode='w', defaultextension=".csv")
    print(f)
    if f is None:  # User canceled save dialog
        return
    # Overwrite existing file
    try:
        os.remove(f)
    except:
        # File does not exist yet
        pass
    sp = serial.Serial(strPort, 9600)
    while running:
        # Wait one minute
        sleep(interval)
        line = sp.readline().decode("utf-8")
        data = [float(val) for val in line.split(' ')]
        t = time.strftime("%Y-%m-%d %H:%M:%S")
        newRow = "\n%s,%s,%s\n" % (t, data[0], data[1])
        with open(f.name, "a") as datafile:
            datafile.write(newRow)


def plot():
    global f
    try:
        # Plot Celcius
        t, c = np.genfromtxt(f, usecols=(0, 1), unpack=True, delimiter=',')
        plt.plot(t, c, '.r-')
        plt.xlabel('Time')
        plt.ylabel('Temperature (Celcius)')
        plt.grid(True)
        plt.show()
        # Plot Fahrenheit
        t, f = np.genfromtxt(f, usecols=(0, 2), unpack=True, delimiter=',')
        plt.plot(t, f, '.r-')
        plt.xlabel('Time')
        plt.ylabel('Temperature (F)')
        plt.grid(True)
        plt.show()
    except:
        pass


def onIncrement(counter):
    counter.set(counter.get() + 1)


def main():
    root = tk.Tk()
    root.title("Serial USB Temperature Plotter")
    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(tk.N,tk.W,tk.E,tk.S))
    mainframe.pack()
    serial_label = ttk.Label(mainframe, text="Sensor Serial Port:")
    serial_label.grid(row=0, column=0)
    serial_var = tk.StringVar(root)
    raw_ports = list(serial.tools.list_ports.comports())
    ports = []
    for p in raw_ports:
        if p.description == "USB Serial":
            ports.append(p.device)
    serial_menu = ttk.OptionMenu(mainframe, serial_var, *ports)
    serial_menu.grid(row=0, column=1)
    counter = tk.IntVar()
    counter.set(1)
    duration_label = ttk.Label(mainframe, textvariable=counter)
    duration_label.grid(row=1, column=1)
    duration_increment = ttk.Button(mainframe,
                                    text="Increase Collection Interval (sec)",
                                    command=lambda: onIncrement(counter))
    duration_increment.grid(row=1, column=0)
    collect_button = ttk.Button(mainframe, text="Begin Data Collection",
                                command=lambda: collect(serial_var.get(),
                                                        counter.get()))
    collect_button.grid(row=2, column=0, sticky=(tk.E, tk.W))
    end_button = ttk.Button(mainframe, text="End Data Collection",
                            command=lambda: plot())
    end_button.grid(row=2, column=1, sticky=(tk.E, tk.W))
    root.mainloop()


if __name__ == '__main__':
   main()
