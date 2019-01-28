import os


# Each website you crawl is a separate directory
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('CREATING DIRECTORY: ' + directory)
        os.makedirs(directory)

# Create queue and crawled files (like vis[] in DFS)
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# Create a new file
def write_file(path, data):
    fstream = open(path, 'w')
    fstream.write(data)
    fstream.close()

# Add data into an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# Delete contents of a file
def delete_file_content(path):
    with open(path, 'w'):
        pass

# Read a file and convert each line to set item
def file_to_set(file_name):
    entities = set()
    with open(file_name, 'rt') as file:
        for line in file:
            entities.add(line.replace('\n', ''))
    return entities

# Iterate through a set, convert items to lines in file
def set_to_file(entities, file):
    delete_file_content(file)
    for link in sorted(entities):
        append_to_file(file, link + '\n')