from image_processor import *
from text_processor import *
from random import random

def handle_error(file_path, error):
    fh = open("errors.txt", "a")
    fh.write("FILE: " + file_path + "\n\n" + str(error) + "\n\n------------------------------------------\n\n")
    fh.close()
    print(str(error))

def generate_ics_list(file_paths):

    returned_files = []

    for f in file_paths:
        text, link = retrieve_text(f)
        print(text)
        response = text_to_json(text)
        returned_files.append(create_ics(response, int(10000 * random()), link))

    return returned_files