"""Contains the standard train/test splits for the cyclegan data."""

"""The size of each dataset. Usually it is the maximum number of images from
each domain."""
DATASET_TO_SIZES = {
    'real2naruto_train': 50,
    'real2naruto_test': 1,
    'real2naruto_anvil': 1,
}

"""The image types of each dataset. Currently only supports .jpg or .png"""
DATASET_TO_IMAGETYPE = {
    'real2naruto_train': '.jpg',
    'real2naruto_test': '.jpg',
    'real2naruto_anvil': '.jpg',
}

"""The path to the output csv file."""
PATH_TO_CSV = {
    'real2naruto_train': './input/real2naruto/real2naruto_train.csv',
    'real2naruto_test': './input/real2naruto/real2naruto_test.csv',
    'real2naruto_anvil': './input_anvil/real2naruto/real2naruto_test.csv',
}
