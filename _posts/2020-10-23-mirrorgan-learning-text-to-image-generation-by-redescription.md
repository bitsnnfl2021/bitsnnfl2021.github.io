---
layout: post
author:
  name: Paper ID 96
  difficulty: Medium
share: true
title: 'MirrorGAN: Learning Text-to-image Generation by Redescription'
categories:
- GAN
- Text-to-Image
tags: []

---
**Abstract** - Generating an image from a given text description has two goals: visual realism and semantic consistency. Although significant progress has been made in generating high-quality and visually realistic images using generative adversarial networks, guaranteeing semantic consistency between the text description and visual content remains very challenging. In this paper, we address this problem by proposing a novel global-local attentive and semantic-preserving text-to-image-to-text framework called MirrorGAN. MirrorGAN exploits the idea of learning textto-image generation by redescription and consists of three modules: a semantic text embedding module (STEM), a global-local collaborative attentive module for cascaded image generation (GLAM), and a semantic text regeneration and alignment module (STREAM). STEM generates word- and sentence-level embeddings. GLAM has a cascaded architecture for generating target images from coarse to fine scales, leveraging both local word attention and global sentence attention to progressively enhance the diversity and semantic consistency of the generated images. STREAM seeks to regenerate the text description from the generated image, which semantically aligns with the given text description. Thorough experiments on two public benchmark datasets demonstrate the superiority of MirrorGAN over other representative state-of-the-art methods.

**Paper** - [https://openaccess.thecvf.com/content_CVPR_2019/papers/Qiao_MirrorGAN_Learning_Text-To-Image_Generation_by_Redescription_CVPR_2019_paper.pdf](https://openaccess.thecvf.com/content_CVPR_2019/papers/Qiao_MirrorGAN_Learning_Text-To-Image_Generation_by_Redescription_CVPR_2019_paper.pdf "https://openaccess.thecvf.com/content_CVPR_2019/papers/Qiao_MirrorGAN_Learning_Text-To-Image_Generation_by_Redescription_CVPR_2019_paper.pdf")

**Dataset** - [https://github.com/qiaott/MirrorGAN](https://github.com/qiaott/MirrorGAN "https://github.com/qiaott/MirrorGAN")