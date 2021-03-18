import csv

clean = lambda s: s.rstrip().lstrip().replace('\n','').replace('\r\n','')

def get_post(title, id, difficulty, tags, abstract, paper, datasets):
    dataset_str = '\n\n'.join([f'[{d.lower()}]({d.lower()})' for d in datasets])
    tag_str = '\n'.join(['- ' + clean(tag.lower()) for tag in tags])
    return f'''\
---
layout: post
author:
  name: Paper ID {id}
  difficulty: {difficulty}
share: true
title: {title}
categories:
{tag_str}
tags: []

---
**Abstract** - {abstract}

**Paper** - [{paper}]({paper})

**Dataset -** {dataset_str}
    '''

with open('NNFL-papers.csv') as f:
    reader = csv.reader(f)
    next(reader)
    id = 0
    for row in reader:
        title, paper, datasets, abstract, ta, difficulty, tags, _, _ = row
        if title:
            title = title.rstrip().lstrip().replace(' ', '-')
            datasets = datasets.split(',')
            tags = tags.split(',')
            id += 1
            with open(f'_posts/2021-01-01-{title}.md','w') as pf:
                pf.write(get_post(title, id, difficulty, tags, abstract, paper, datasets))
            #break
