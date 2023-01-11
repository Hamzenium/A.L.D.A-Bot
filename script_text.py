from pptx import Presentation
import pprint
import os

file_path = r"/Users/muhammadhamzasohail/Desktop/Tester_ALDA"


def path_adder(dir_path):
    # list to store files
    res = []

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    return res


print(path_adder(file_path))


def extract_text_from_ppt(presentation):

    # Initialize an empty list to store the text
    slides_text = []

    # Loop through all slides in the presentation
    for slide in presentation.slides:
        # Loop through all shapes in the slide
        text_list = []
        for shape in slide.shapes:
            # Check if the shape is a text box
            if shape.has_text_frame:
                # Extract the text from the text box and add it to the list
                text = shape.text
                text_list.append(text)
        slides_text.append(text_list)
    return slides_text


def filter_lesson_lists(slides_text):
    filtered_slides_text = []
    for slide_text in slides_text:
        for text in slide_text:
            if 'lesson' in text.lower():
                filtered_slides_text.append(slide_text)
                break
    return filtered_slides_text


def batch_processor(array,folder_path):
    for file in array:
        print("Pointer for each file")
        filename = folder_path + "//" + file
        presentation = Presentation(filename)
        data = filter_lesson_lists(extract_text_from_ppt(presentation))
        pprint.pprint(data)


result = path_adder(file_path)
batch_processor(result,file_path)
