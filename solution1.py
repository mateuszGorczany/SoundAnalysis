#!/usr/bin/env python3

import glob
import speech_recognition as sr
import argparse 
from tqdm import tqdm
from typing import List, Dict

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory", help="Directory of the input files *.wav", default="test_wavs")

args = parser.parse_args()

recognizer = sr.Recognizer()

def get_files(directory: str) -> List[str]:
    return glob.glob(directory + "/*.wav")

def recognize(file: str) -> str:
    audio = sr.AudioFile(file)
    with audio as source:
        audio = recognizer.record(source)
    
    return recognizer.recognize_google(audio)

def save_results(results: Dict[str, str]) -> None:
    with open("results.csv", "w") as file:
        file.write("filename;result\n")
        for key, value in results.items():
            file.write(f"{key};{value}\n")

if __name__ == "__main__":
    results = {}
    for file in tqdm(get_files(args.directory)):
        fname = file.split("/")[-1]
        results[fname] = recognize(file)
    
    save_results(results)

