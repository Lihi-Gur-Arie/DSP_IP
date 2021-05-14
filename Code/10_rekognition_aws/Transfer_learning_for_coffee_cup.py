
import os, json


def get_photos_names_from_dir(dir_path, my_class, confidence_treshold):
    # Get the names of all json files in the directory:

    json_files = [pos_json for pos_json in os.listdir(dir_path) if pos_json.endswith('.json')]
    print(json_files)

    photos_list = []

    # Itterate over each json file
    for curr_json in json_files:
        with open(dir_path + curr_json) as f:
            data = json.load(f)
            confidence = itterate_labels(data, my_class)
            photos_list.append ([curr_json, confidence])

    # return the photos above threshold
    return [x[0] for x in photos_list if x[1] > confidence_treshold]

def itterate_labels (data, my_class):

    # Itterate over each label in the JSON file, and return the confidence_treshold for my_class
    for curr_label in data['Labels']:
        # When the class is the desiered class, return it's confidence
        if curr_label.get('Name') == my_class:
            return curr_label.get('Confidence')

#################################################################################################################

if __name__ == "__main__":

    dir_path = 'json/coffee_cup/'
    my_class = 'Coffee Cup'
    confidence = 99

    photos_list = get_photos_names_from_dir(dir_path = dir_path, my_class = my_class, confidence_treshold= confidence)







