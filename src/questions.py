## FORMAT OF QUESTIONS FILE
##
##   The questions file is a python file with a QUESTIONS variable.
##   This QUESTIONS variable must be a list, of tuples with two
##   elements.  Each tuple defines an individual question.
##
##   The first element in the question tuple must be a string and is
##   the text for the actual question.  The second element in the
##   tuple specifies the answer type and its initial value: if it is a
##   string then the answer is a text box; if it is a tuple of strings
##   then it is a group of radio buttons.

QUESTIONS =[
CheckQuestion('If there is RNA expression, what patterns does the RNA make?',('Evenly distributed', 'Single transcripts', 'Nuclear', 'Cell type specific', 'More in some cells than others', 'Other')),
CheckQuestion('If there is protein expression, what patterns does the protein make?',('Punctate', 'Nuclear', 'Cell edges', 'Diffuse', 'Large aggregations', 'Cytoplasmic', 'Cell type specific', 'Other')),
RadioQuestion('Is RNA present in NBs?',('No', 'Yes')),
RadioQuestion('Is protein present in NBs?',('No', 'Yes')),
RadioQuestion('Is RNA present in other cells?',('No', 'Yes')),
RadioQuestion('Is protein present in other cells?',('No', 'Yes')),
TextQuestion('General comments', ''),]
