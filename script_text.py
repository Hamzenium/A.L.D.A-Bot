from pptx import Presentation
import pprint
import os
import re
import os.path


def path_adder(dir_path):
    # list to store files
    res = []

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    return res


def extract_text_from_ppt(presentation):
    # Initialize an empty list to store the text
    slides_text = []

    # Loop through all slides in the presentation
    for slide in presentation.slides:
        # Loop through all shapes in the slide
        text_list = " "
        for shape in slide.shapes:
            # Check if the shape is a text box
            if shape.has_text_frame:
                # Extract the text from the text box and add it to the list
                text = shape.text
                # remove appendix because they will also have the keywords the algorithm will detect
                if 'appendix' in text.lower():
                    break
                elif 'sensitivity' not in text.lower():
                    text_list = text_list + str(text)
        slides_text.append(text_list)
    return slides_text


def filter_lesson_lists(slides_text, new_file, final_folder_directory):
    # new_slides_text slices the title page out
    new_slides_text = slides_text[1:]
    filtered_slides_text = []
    for text in new_slides_text:
        if 'lessons learned' in text.lower():
            key_word = re.search(r'lessons learned', text, re.IGNORECASE)
            filtered_slides_text.append(text)

    final_folder_file = os.path.join(final_folder_directory, new_file)

    newFile = open(final_folder_file, "w")
    for text in filtered_slides_text:
        newFile.write(text)
    newFile.close()


def batch_processor(array, folder_path, f_p):
    for file in array:
        if file != ".DS_Store":
            summary_file_name = file[:-5]
            summary_file_name += "_summary.txt"
            filename = folder_path + "//" + file
            presentation = Presentation(filename)
            filter_lesson_lists(extract_text_from_ppt(presentation), summary_file_name, f_p)
