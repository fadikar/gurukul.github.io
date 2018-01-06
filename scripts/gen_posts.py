## This script contains useful functions to generate a html page given a 
## blog post txt file. It also creates meta data for the blog posts to be 
## used to make summaries.
## Input should be a txt file of specific format 

def read_file(infile):

    metadata = []
    post = []

    with open(infile, 'r') as f:
        for line in f:
            if line[0] == '#':
                metadata.append(line.strip('\n'))
            else:
                post.append(line)

    return {'metadata':metadata, 'post':post}

def get_title(metadata):
    title = filter(lambda x: '##title' in x, metadata)
    title = title[0][8: len(title[0])]
    return title

def get_subtitle(metadata):
    subtitle = filter(lambda x: '##subtitle' in x, metadata)
    subtitle = subtitle[0][11: len(subtitle[0])]
    return subtitle

def get_author(metadata):
    author = filter(lambda x: '##author' in x, metadata)
    author = author[0][9: len(author[0])]
    return author

def get_date(metadata):
    date = filter(lambda x: '##date' in x, metadata)
    date = date[0][7: len(date[0])]
    return date

def get_topic(metadata):
    topic = filter(lambda x: '##topic' in x, metadata)
    topic = topic[0][8: len(topic[0])]
    return topic

def modify_template(file_to_modify, string2find, replace_value, outfile):
    
    # Read in the file
    with open(file_to_modify, 'r') as file:
        filedata = file.read()
        
    # Replace the target string
    for i in range(len(string2find)):
        filedata = filedata.replace(string2find[i], str(replace_value[i]))
        
    # Write the file out
    with open(outfile, 'w') as file:
        file.write(filedata)