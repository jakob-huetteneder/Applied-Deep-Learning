# Style Transfer - Transformation of images of real people into anime-styled images
## Type of Project
Bring your own method
## Project Idea and Approach
The idea of this project is to transform an input image of a real person's face to an image in Naruto-style that resembles the face. The approach for this is to use an existing Generative Adversarial Network (GAN) to be able to make a model out of two unpaired domains (real people's faces and faces of Naruto characters).
## Datasets
Naruto faces:
- https://www.kaggle.com/datasets/neetuk/naruto-face-dataset this dataset contains only images of faces of Naruto characters.
- (https://huggingface.co/datasets/lambdalabs/naruto-blip-captions) this dataset contains images of faces of Naruto characters paired with a description, only the images would be used.

Real faces:

There are more datasets for this, on possibility is the [Labeled Faces in the Wild dataset](http://vis-www.cs.umass.edu/lfw/#download)
## Work Breakdown Structure
### Dataset collection & Project setup (ca. 8h)
Dataset collection & preprocessing, literature review on existing architectures that can be used.

### Designing and Building the Network (ca. 20h)
Initial network design and implementation.

### Training and Fine-tuning the Network (ca. 15h)
Initial training, evaluating results & fine-tuning.

### Building an Application (ca. 8h)
Desinging an intuitive user interface that lets you input an image and presents you the output.

### Writing the final Report (ca. 10h)
Documenting methodologies, results & discussion, conclusions & future recommendations.

### Preparing the Presentation (ca. 4h)

## References
- Zhu, J. Y., Park, T., Isola, P., & Efros, A. A. (2017). Unpaired image-to-image translation using cycle-consistent adversarial networks.
This paper introduces the CycleGAN, a method for unpaired image-to-image translation.
(https://openaccess.thecvf.com/content_ICCV_2017/papers/Zhu_Unpaired_Image-To-Image_Translation_ICCV_2017_paper.pdf)
- Lee, H., Tseng, H., Huang, J. B., Singh, M. K., & Yang, M. H. (2018). Diverse image-to-image translation via disentangled representations.
The paper presents an approach to produce diverse outputs from a single input, which could be useful to generate multiple Naruto-style versions of the same real person's image.
(https://link.springer.com/content/pdf/10.1007/s11263-019-01284-z.pdf?pdf=button)
