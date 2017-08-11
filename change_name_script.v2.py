import os


dir = '/Users/username/documents/images'

for filename in os.listdir(dir):
    shirt_code, fabric_code = filename[6:11], filename[0:5]
    new_name = "{0}-{1}.jpg".format(shirt_code, fabric_code)

    print(new_name)

    absolute_path = os.path.join(dir, filename)
    new_path = os.path.join(dir, new_name)

    os.rename(absolute_path, new_name)
