---
layout: post
author:
  name: Paper ID 1
  difficulty: Hard
share: true
title: 'Deep Sketch Hashing: Fast Free-hand Sketch-Based Image Retrieval'
categories:
- CNN
- IR
tags: []

---
**Abstract** - Free-hand sketch-based image retrieval (SBIR) is a specific cross-view retrieval task, in which queries are abstract and ambiguous sketches while the retrieval database is formed with natural images. Work in this area mainly focuses on extracting representative and shared features for sketches and natural images. However, these can neither cope well with the geometric distortion between sketches and images nor be feasible for large-scale SBIR due to the heavy continuous-valued distance computation. In this paper, we speed up SBIR by introducing a novel binary coding method, named Deep Sketch Hashing (DSH), where a semi-heterogeneous deep architecture is proposed and incorporated into an end-to-end binary coding framework. Specifically, three convolutional neural networks are utilized to encode free-hand sketches, natural images and, especially, the auxiliary sketch-tokens which are adopted as bridges to mitigate the sketch-image geometric distortion. The learned DSH codes can effectively capture the crossview similarities as well as the intrinsic semantic correlations between different categories. To the best of our knowledge, DSH is the first hashing work specifically designed for category-level SBIR with an end-to-end deep architecture. The proposed DSH is comprehensively evaluated on two large-scale datasets of TU-Berlin Extension and Sketchy, and the experiments consistently show DSH’s superior SBIR accuracies over several state-of-the-art methods, while achieving significantly reduced retrieval time and memory footprint. 

**Paper** - [https://openaccess.thecvf.com/content_cvpr_2017/papers/Liu_Deep_Sketch_Hashing_CVPR_2017_paper.pdf](https://openaccess.thecvf.com/content_cvpr_2017/papers/Liu_Deep_Sketch_Hashing_CVPR_2017_paper.pdf "https://openaccess.thecvf.com/content_cvpr_2017/papers/Liu_Deep_Sketch_Hashing_CVPR_2017_paper.pdf") 

**Dataset** - [http://cybertron.cg.tu-berlin.de/eitz/projects/sbsr/](http://cybertron.cg.tu-berlin.de/eitz/projects/sbsr/ "http://cybertron.cg.tu-berlin.de/eitz/projects/sbsr/")