import anvil.media
import anvil.server

import os
import shutil
import subprocess
from PIL import Image, ImageOps

anvil.server.connect("server_5K3UNMHRYLT5M4MM2KLYVUSV-GK5CWC6EWGPRA5C4")


@anvil.server.callable
def naruto_image(anvil_image):
    # Path to your folder
    input_folder_path = './input_anvil/real2naruto/real2naruto_test/folder_a'
    output_folder_path = './output/cyclegan/anvil_app'

    delete_folder_content(input_folder_path)
    delete_folder_content(output_folder_path)

    with anvil.media.TempFile(anvil_image) as filename:
        image = Image.open(filename)
        image.save(os.path.join(input_folder_path, 'saved_image.jpg'))

    input_image_path = os.path.join(input_folder_path, 'saved_image.jpg')

    resize_and_pad_image(input_image_path)

    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Change the current working directory
    os.chdir(script_directory)

    cmd = [
        'python', 'main.py',
        '--to_train=3',
        '--log_dir=./output/cyclegan/exp_01',
        '--config_filename=./configs/anvil_config.json',
        '--checkpoint_dir=./output/cyclegan/exp_01/20240116-071058'
    ]

    subprocess.run(cmd, check=True)

    file_path = os.path.join(output_folder_path, 'generated_image.jpg')

    with open(file_path, 'rb') as file:
        # Read the file as binary
        image_data = file.read()

    return anvil.BlobMedia('image/jpeg', image_data, name='image.jpg')


def delete_folder_content(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')


def resize_and_pad_image(input_path, size=(256, 256)):
    with Image.open(input_path) as img:
        img.thumbnail(size, Image.Resampling.LANCZOS)
        padded_img = ImageOps.expand(img, border=(max((size[0] - img.size[0]) // 2, 0),
                                                  max((size[1] - img.size[1]) // 2, 0)),
                                     fill='black')
        padded_img.save(input_path)


anvil.server.wait_forever()
