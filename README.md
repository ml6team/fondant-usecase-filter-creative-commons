# Creative commons licensed data pipeline

<p align="center">
    <a href="https://github.com/ml6team/fondant">
        <img src="https://raw.githubusercontent.com/ml6team/fondant/main/docs/art/fondant_banner.svg" height="150px"/>
    </a>
</p>
<p align="center">
</p>

## Introduction

This repository contains a [Fondant](https://fondant.ai) pipeline to load and filter the 
[fondant-cc-25m](https://huggingface.co/datasets/fondant-ai/fondant-cc-25m) dataset. This 
dataset contains more than 25 million images with a creative commons license, extracted from 
CommonCrawl.

### Pipeline overview

The primary goal of this sample is to showcase how you can use a Fondant pipeline and reusable
components to load an image dataset from HuggingFace Hub and download all images.
Pipeline Steps:

- [Load from Huggingface Hub](https://github.com/ml6team/fondant/tree/main/components/load_from_hf_hub):
  The pipeline begins by loading the image dataset from Huggingface Hub.
- [Download Images](https://github.com/ml6team/fondant/tree/main/components/download_images):
  The download image component download images and stores them to parquet.
- [Filter Images](https://github.com/ml6team/fondant/tree/main/components/filter_image_resolution):
  The filter image component filters images based on their resolution.

## Running the sample pipeline and explore the data

Accordingly, the getting started documentation, you can go to the `src` folder and run the pipeline
by using the `LocalRunner` as follow:

```bash
fondant run local pipeline.py
```

> Note: The 'load_from_hub' component accepts an argument that defines the dataset size.
> You have the option to adjust it to load more images from HuggingFace.
> Therefore, you can modify this line:
> `"n_rows_to_load": 1000`


After the pipeline is succeeded you can explore the data by using the fondant data explorer:

```bash
fondant explore --base_path ./data-dir
```

