# Creative common license dataset

## Overview

We present a sample pipeline that demonstrates how to effectively utilize a creative
commons image dataset within a fondant pipeline. This dataset comprises images from diverse sources
and is available in various data formats.

### Pipeline overview

The primary goal of this sample is to showcase how you can use a Fondant pipeline and reusable
components to load an image dataset from HuggingFace Hub and download all images.
Pipeline Steps:

- [Load from Huggingface Hub](https://github.com/ml6team/fondant/tree/main/components/load_from_hf_hub):
  The pipeline begins by loading the image dataset from Huggingface Hub.
- [Download Images](https://github.com/ml6team/fondant/tree/main/components/download_images): 
  The download image component download images and stores them to parquet.

## Running the sample pipeline and explore the data

Accordingly, the getting started documentation, we can run the pipeline by using the `LocalRunner`
as follow:

```bash
fondant run local pipeline.py
```

> Note: The 'load_from_hub' component accepts an argument that defines the dataset size.
> You have the option to adjust it to load more images from HuggingFace.
> Therefore, you can modify this line:
> `"n_rows_to_load": 1000`

If you wish to run the entire pipeline, including the filtering step, use the following command:

```bash
fondant run local filter_pipeline
```

After the pipeline is succeeded you can explore the data by using the fondant data explorer:

```bash
fondant explore --base_path ./data
```

