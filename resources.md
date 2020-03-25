---
layout: home
title: Resources
permalink: "/resources/"
excerpt: Project Portal
show_excerpts: true
paginate: true
entries_layout: list

---
Hello Everyone!

This post is to give you some helpful resources to get going with your NNFL project no matter what your experience level is at this point. We’ll start from zero and go all the way to being an expert.

Note that you do not need to (and shouldn’t) learn everything beforehand to start practicing deep learning. It is strongly advised to learn the tools you need only _when_ you need them. The reasoning here is that the amount of topics/tools that comprise effective practice of deep learning is very high and is ever growing, and trying to learn everything beforehand will only slow you down before you do any actual significant work.

We have tried and kept resources for each tool/topic limited and high quality so that you do not need to spend time choosing the best tutorial. Most of these tutorials are code-first and practical introductions designed to get you up and running quickly and at the same time not sacrificing on depth and quality.

We hope this is helpful for everyone!

—————————————————

**Deep Learning Overview and Libraries:**

[http://introtodeeplearning.com](http://introtodeeplearning.com "http://introtodeeplearning.com") - MIT Intro to Deep Learning

We highly recommend all of you to go through this course. The course gives a fast paced, yet very comprehensive coverage of the most important and practical aspects of deep learning. The lectures cover a huge amount of content within a single hour.

For example, by the end of the 4th lecture, you’ll already have properly understood neural networks, activation functions, loss functions, backward propagation, regularization, adaptive learning rates, weight initialization, RNNs, LSTMs, gated LSTMs, BPTT, CNNs, image captioning, segmentation, autoencoders, VAEs, GANs, CycleGANs, etc.

_Also, the lab exercises of the above course serve as a good introduction to **Tensorflow 2.0**_

**For PyTorch:**

1\. An all-in-one beginner friendly introduction by Jeremy Howard (FastAI Co-founder): [https://pytorch.org/tutorials/beginner/nn_tutorial.html](https://pytorch.org/tutorials/beginner/nn_tutorial.html "https://pytorch.org/tutorials/beginner/nn_tutorial.html")

2\. A more detailed tutorial covering every doubt you could ever have about PyTorch. Do not waste your time by watching the videos. Each video has a detailed transcript attached in the form of a blog. Just read the blog. 

[https://deeplizard.com/learn/playlist/PLZbbT5o_s2xrfNyHZsM6ufI0iZENK9xgG](https://deeplizard.com/learn/playlist/PLZbbT5o_s2xrfNyHZsM6ufI0iZENK9xgG "https://deeplizard.com/learn/playlist/PLZbbT5o_s2xrfNyHZsM6ufI0iZENK9xgG")

3\. Another good course from Toronto in the form of jupyter notebooks: [https://www.cs.toronto.edu/\~lczhang/360/](https://www.cs.toronto.edu/\~lczhang/360/ "https://www.cs.toronto.edu/~lczhang/360/")

————————————————— 

**The Math you need for reading and understanding Deep Learning research papers:**

Matrix Calculus Refresher: [https://explained.ai/matrix-calculus/index.html](https://explained.ai/matrix-calculus/index.html "https://explained.ai/matrix-calculus/index.html")

And a full book to help you review all of the math geared towards machine/deep learning: [https://mml-book.com](https://mml-book.com "https://mml-book.com")

————————————————— 

**For refreshing your basics: Python, Jupyter, NumPy, Pandas, etc.**

1\. If you need to brush up your python skills, or have never coded before, this course will get you up to speed very quickly while still covering all the important parts of the language with respect to data science (exercises included): [https://www.kaggle.com/learn/python](https://www.kaggle.com/learn/python "https://www.kaggle.com/learn/python")

**2.** Introduction to Jupyter Notebooks: [https://realpython.com/jupyter-notebook-introduction/#getting-up-and-running-with-jupyter-notebook](https://realpython.com/jupyter-notebook-introduction/#getting-up-and-running-with-jupyter-notebook "https://realpython.com/jupyter-notebook-introduction/#getting-up-and-running-with-jupyter-notebook")

3\. NumPy refresher:

Introductory: [http://cs231n.github.io/python-numpy-tutorial/#numpy](http://cs231n.github.io/python-numpy-tutorial/#numpy "http://cs231n.github.io/python-numpy-tutorial/#numpy")

Comprehensive (recommended): [https://nbviewer.jupyter.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-2-Numpy.ipynb](https://nbviewer.jupyter.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-2-Numpy.ipynb "https://nbviewer.jupyter.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-2-Numpy.ipynb")

**4.** Pandas, Matplotlib, Seaborn:

This is a great series of notebooks to get an ML-focused practical introduction to pandas and data vizualization:

* [https://mlcourse.ai/articles/topic1-exploratory-data-analysis-with-pandas/](https://mlcourse.ai/articles/topic1-exploratory-data-analysis-with-pandas/ "https://mlcourse.ai/articles/topic1-exploratory-data-analysis-with-pandas/")
* [https://mlcourse.ai/articles/topic2-visual-data-analysis-in-python/](https://mlcourse.ai/articles/topic2-visual-data-analysis-in-python/ "https://mlcourse.ai/articles/topic2-visual-data-analysis-in-python/")
* [https://mlcourse.ai/articles/topic2-part2-seaborn-plotly/](https://mlcourse.ai/articles/topic2-part2-seaborn-plotly/ "https://mlcourse.ai/articles/topic2-part2-seaborn-plotly/")

5\. Alternatives (in depth)**:**

* Pandas: [https://www.kaggle.com/learn/pandas](https://www.kaggle.com/learn/pandas "https://www.kaggle.com/learn/pandas")
* Vizualization: [https://www.kaggle.com/learn/data-visualization](https://www.kaggle.com/learn/data-visualization "https://www.kaggle.com/learn/data-visualization")
* Matplotlib fundamentals in depth: [https://matplotlib.org/matplotblog/posts/an-inquiry-into-matplotlib-figures/](https://matplotlib.org/matplotblog/posts/an-inquiry-into-matplotlib-figures/ "https://matplotlib.org/matplotblog/posts/an-inquiry-into-matplotlib-figures/")
* 

_A single resource to cover most of what you need for scientific programming in python:_ [_http://scipy-lectures.org_](http://scipy-lectures.org "http://scipy-lectures.org")

_This series covers Python, NumPy, Matplotlib and SciPy both at introductory and advanced levels._

—————————————————

**Setting up a deep learning computer/server/VM:**

You can go to [https://course.fast.ai](https://course.fast.ai "https://course.fast.ai") and check the “Server Setup” tab on the left.

It includes detailed instructions to setup your VM on most common services. Note that it is geared towards setting up your server to be able to do the [fast.ai](http://fast.ai/) course. In practice though, the setup described here is exactly what you need for any other sort of deep learning work too.

**Recommendations**:

1. Google Colab: free, but comes with some hassle when saving data/files.
2. Google Cloud: comes with $300 free credits. A bit of a hassle to setup, but smooth sailing afterwards. Needs credit card/debit card with auto-charge feature (won’t be charged unless you run out of $300)
3. Easiest setup + Comfortable Working: [https://gradient.paperspace.com/pricing](https://gradient.paperspace.com/pricing "https://gradient.paperspace.com/pricing")
   1. Paperspace has a free option that is underpowered as compared to Colab, but is more convenient
   2. The $8/mo option in Paperspace is great for individuals.

—————————————————

**Extras:**

A Neural Network Playground to experiment and build intuition with different datasets, architectures, activation functions, and regularization: [https://playground.tensorflow.org](https://playground.tensorflow.org "https://playground.tensorflow.org")

[1. Interactive tutorial on weight initialization:](https://www.deeplearning.ai/ai-notes/initialization/)

[2. Interactive tutorial on different optimizers:](https://www.deeplearning.ai/ai-notes/optimization/)

3\. Articles on advanced deep learning topics: [https://distill.pub](https://distill.pub "https://distill.pub") (not necessarily beginner friendly)

4\. Small, practical courses on several data science tools: [https://www.kaggle.com/learn/overview](https://www.kaggle.com/learn/overview "https://www.kaggle.com/learn/overview")

All the Best,

Team NNFL