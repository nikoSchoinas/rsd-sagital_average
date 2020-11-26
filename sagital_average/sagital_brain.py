from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

import numpy as np


def run_averages(file_input='brain_sample.csv', file_output='brain_average.csv'):
    """
    Calculates the average through the coronal planes
    The input file should has as many columns as coronal planes
    The rows are intersections of the sagital/horizontal planes

    The result is the average for each sagital/horizontal plane (rows)
    """
    # Open the file to analyse
    planes = np.loadtxt(file_input, dtype=int,  delimiter=',')

    planes = np.array(planes)
    # Calculates the averages through the sagital/horizontal planes
    # and makes it as a row vector
    averages = [np.mean(sagital_sect) for sagital_sect in planes]
    # write it out on my file
    np.savetxt(file_output, averages, fmt='%.1f', delimiter=',')
