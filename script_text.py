import collections
import collections.abc
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


# def extract_text_from_ppt(presentation):
#     # Initialize an empty list to store the text
#     slides_text = []
#
#     # Loop through all slides in the presentation
#     for slide in presentation.slides:
#         # Loop through all shapes in the slide
#         text_list = " "
#         for shape in slide.shapes:
#             # Check if the shape is a text box
#             if shape.has_text_frame:
#                 # Extract the text from the text box and add it to the list
#                 text = shape.text
#                 # remove appendix because they will also have the keywords the algorithm will detect
#                 if 'appendix' in text.lower():
#                     break
#                 elif 'sensitivity' not in text.lower():
#                     text_list = text_list + str(text)
#         slides_text.append(text_list)
#     return slides_text

def extract_text_from_ppt(presentation):
    prs = presentation
    # list_of slides will have all the text extracted from slides
    list_of_slides = []
    for slide in prs.slides:
        # list_of_elements stores all the sentences of one shape in slide
        list_of_elements = []
        # Go through all the shapes in the slides
        for shape in slide.shapes:
            # Check if the shape is in table form
            if shape.has_table:
                line = ''
                for cell in shape.table.iter_cells():
                    line += cell.text+'\n'
                list_of_elements.append(line)
            # Check if Shape is in textframe
            elif shape.has_text_frame:
                for paragraph in shape.text_frame.paragraphs:
                    line = ''
                    for run in paragraph.runs:
                        if "sensitivity" not in run.text.lower():
                            line += run.text
                    list_of_elements.append(line)

        # remove all the extra characters ' ' and ''
        new_list = [x for x in list_of_elements if x != '' and x != ' ']
        list_of_slides.append(new_list)
    return list_of_slides

#
# def filter_lesson_lists(slides_text, new_file, final_folder_directory):
#     # new_slides_text slices the title page out
#     new_slides_text = slides_text[1:]
#     filtered_slides_text = []
#     for text in new_slides_text:
#         if 'lessons learned' in text.lower():
#             key_word = re.search(r'lessons learned', text, re.IGNORECASE)
#             filtered_slides_text.append(text)
#
#     final_folder_file = os.path.join(final_folder_directory, new_file)
#
#     newFile = open(final_folder_file, "w")
#     for text in filtered_slides_text:
#         newFile.write(text)
#     newFile.close()


# Takes Action Items and lessons learned from the read slides text and appends them onto a new list
def filter_slide_lists(slides_text, key_word):
    # new_slides_text slices the title page out
    new_slide_list = slides_text[1:]
    filtered_slides_text = []
    for slide in new_slide_list:
        for element in slide:
            if key_word in element.lower() and not any("appendix" in word.lower() for word in slide):
                if key_word == "decision criteria":
                    filtered_slides_text.append(slide[slide.index(element):])
                else:
                    filtered_slides_text.append(slide)
                break

    return filtered_slides_text

def create_new_files(slides_text, new_file, final_folder_directory):
    lessons_learned_data = filter_slide_lists(slides_text, "lessons learned")
    decision_criteria_data = filter_slide_lists(slides_text, "decision criteria")
    action_items_data = filter_slide_lists(slides_text, "action item")
    extracted_data = decision_criteria_data + lessons_learned_data + action_items_data

    final_folder_file = os.path.join(final_folder_directory, new_file)

    fo = open(final_folder_file, "w", encoding='utf-8')
    for slide in extracted_data:
        for list_of_elements in slide:
            for elements in list_of_elements:
                fo.write(elements)
            fo.write('\n')
        fo.write('\n\n')
    fo.close()

#
# def batch_processor(array, folder_path, f_p):
#     for file in array:
#         summary_file_name = file[:-5]
#         summary_file_name += "_summary.txt"
#         filename = folder_path + "//" + file
#         presentation = Presentation(filename)
#         filter_lesson_lists(extract_text_from_ppt(presentation), summary_file_name, f_p)

def batch_processor(array, folder_path, f_p):
    for file in array:
        summary_file_name = file[:-5]
        summary_file_name += "_summary.txt"
        filename = folder_path + "//" + file
        presentation = Presentation(filename)
        create_new_files(extract_text_from_ppt(presentation), summary_file_name, f_p)
