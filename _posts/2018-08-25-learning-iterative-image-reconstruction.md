---
layout: post
share: true
title: Learning Iterative Image Reconstruction
date: 2018-08-25 23:18:08 +0530
author:
  name: Aditya Rana
  email: f2016182@pilani.bits-pilani.ac.in
categories:
- Image Reconstruction
tags:
- Easy

---
Successful image reconstruction requires the recognition of a scene and the generation of a clean image of that scene. The papers propose to use recurrent neural networks for both analysis and synthesis. The networks have a hierarchical architecture that represents images in multiple scales with different degrees of abstraction. The mapping between these representations is mediated by a local connection structure.  The networks are supplied with degraded images and then trained to reconstruct the originals iteratively. This iterative reconstruction makes it possible to use partial results as context information to resolve ambiguities. It demonstrate the power of the approach using three examples: superresolution, filling in of occluded parts, and noise removal / contrast enhancement.  