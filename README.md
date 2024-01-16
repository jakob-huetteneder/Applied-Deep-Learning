## Introduction

I got the CycleGAN implementation from here [cyglegan-1](https://github.com/leehomyc/cyclegan-1)

As error metric, the least square loss is used. How that works for GANs is further specified here: https://arxiv.org/pdf/1611.04076.pdf


## Getting Started
### Prepare dataset
In your project you should have a folder structure like this:

- input
	- dataset_name
		- dataset_name_train
			- folder_a
			- folder_b
		- dataset_name_test
			- folder_a
			- folder_b

* Create the csv file as input to the data loader. 
	* Edit the cyclegan_datasets.py file. For example, if your dataset contains 1000 images in folder_a and 800 images in folder_b both in PNG format, you can just edit the cyclegan_datasets.py as following:
	```python
	DATASET_TO_SIZES = {
    'dataset_name_train': 1000
	}

	PATH_TO_CSV = {
    'dataset_name_train': './input/dataset_name/dataset_name_train.csv'
	}

	DATASET_TO_IMAGETYPE = {
    'dataset_name_train': '.png'
	}

	``` 
	* Run create_cyclegan_dataset.py:
	```bash
	python create_cyclegan_dataset.py --image_path_a=./input/dataset_name/dataset_name_train/folder_a --image_path_b=./input/dataset_name/dataset_name_train/folder_b --dataset_name="dataset_name_train" --do_shuffle=0
	```

### Training
* Create the configuration file. The configuration file contains basic information for training/testing. An example of the configuration file could be fond at configs/exp_01.json. 

* Start training:
```bash
python main.py --to_train=1 --log_dir=output/cyclegan/exp_01 --config_filename=configs/exp_01.json
```
* Check the intermediate results.
	* Tensorboard
	```bash
	tensorboard --port=6006 --logdir=./output/cyclegan/exp_01/#timestamp# 
	```
	* Check the html visualization at ./output/cyclegan/exp_01/#timestamp#/epoch_#id#.html.  

### Restoring from the previous checkpoint.
```bash
python main.py \
    --to_train=2 \
    --log_dir=./output/cyclegan/exp_01 \
    --config_filename=./configs/exp_01.json \
    --checkpoint_dir=./output/cyclegan/exp_01/#timestamp#
```
### Testing
* Create the testing dataset.
	* Edit the cyclegan_datasets.py file the same way as training.
	* Create the csv file as the input to the data loader. 
	```bash
 	python create_cyclegan_dataset.py --image_path_a=./input/dataset_name/dataset_name_test/folder_a --image_path_b=./input/dataset_name/dataset_name_test/folder_b --dataset_name="dataset_name_test" --do_shuffle=0
	```
* Run testing.
```bash
python main.py \
    --to_train=0 \
    --log_dir=./output/cyclegan/exp_01 \
    --config_filename=./configs/exp_01_test.json \
    --checkpoint_dir=./output/cyclegan/exp_01/#old_timestamp# 
```
The result is saved in CycleGAN_TensorFlow/output/cyclegan/exp_01/#new_timestamp#.




