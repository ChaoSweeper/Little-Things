"""
locate dictionary with multiple csv files
and combine them into one csv file
"""
import os
import glob
import pandas as pd


def locate_csv_files(path):
    """
    locate all csv files in the directory
    """
    csv_files = glob.glob(os.path.join(path, "*.csv"))
    return csv_files


def merge_csv_files(csv_files):
    """
    combine all csv files in the directory
    """
    combined_csv = pd.concat([pd.read_csv(f) for f in csv_files])
    return combined_csv


def save_combined_csv(combined_csv, path):
    """
    save combined csv file
    """
    combined_csv.to_csv(path, index=False)
    combined_csv.to_csv(os.path.join(path, "combined.csv"), index=False)
