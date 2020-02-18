---
layout: post
author:
  name: 'Paper ID: 94'
  email: bitsnnfl@gmail.com
share: true
title: "[ID_94] Brain Tumor Segmentation with Deep Neural Networks"
categories:
- CNN
- Segmentation
tags: []

---
**Abstract** - In this paper, we present a fully automatic brain tumor segmentation method based on Deep Neural Networks (DNNs). The proposed networks are tailored to glioblastomas (both low and high grade) pictured in MR images. By their very nature, these tumors can appear anywhere in the brain and have almost any kind of shape, size, and contrast. These reasons motivate our exploration of a machine learning solution that exploits a flexible, high capacity DNN while being extremely efficient. Here, we give a description of different model choices that we’ve found to be necessary for obtaining competitive performance. We explore in particular different architectures based on Convolutional Neural Networks (CNN), i.e. DNNs specifically adapted to image data. We present a novel CNN architecture which differs from those traditionally used in computer vision. Our CNN exploits both local features as well as more global contextual features simultaneously. Also, different from most traditional uses of CNNs, our networks use a final layer that is a convolutional implementation of a fully connected layer which allows a 40 fold speed up. We also describe a 2-phase training procedure that allows us to tackle difficulties related to the imbalance of tumor labels. Finally, we explore a cascade architecture in which the output of a basic CNN is treated as an additional source of information for a subsequent CNN. Results reported on the 2013 BRATS test dataset reveal that our architecture improves over the currently published state-of-the-art while being over 30 times faster.

**Paper** - [https://arxiv.org/pdf/1505.03540v3.pdf](https://arxiv.org/pdf/1505.03540v3.pdf "https://arxiv.org/pdf/1505.03540v3.pdf")

**Dataset** - [https://www.smir.ch/BRATS/Start2015](https://www.smir.ch/BRATS/Start2015 "https://www.smir.ch/BRATS/Start2015") (Request Dataset using University Email. It'll be accepted in about 2 working days)

**Problem Statement** -

1. The paper is implemented on BRATS 2013 dataset. Implement the paper using the BRATS 2015 dataset (as given above)
2. Implement the InputCascadeCNN architecture only, as described in the paper.
3. Show the segmented image for 10 images. Also report the precision, recall, and dice score for all three tumor categories.