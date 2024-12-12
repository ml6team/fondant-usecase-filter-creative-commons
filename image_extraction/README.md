# Common crawl image extraction pipeline

<p align="center">
    <a href="https://github.com/ml6team/fondant">
        <img src="https://raw.githubusercontent.com/ml6team/fondant/main/docs/art/fondant_banner.svg" height="150px"/>
    </a>
</p>
<p align="center">
</p>

# Image Extraction Pipeline Overview

This pipeline was used to create the 25-million creative commons image dataset. The pipeline consists of two steps:

- Read WARC Paths: This step takes as input the name of a CommonCrawl index and retrieves a list of warc files
- Extract Images from warc: In this step, the pipeline consumes the list of warc files, downloads each archive, and extracts the images based on their licence.

More info related to how we detect if an image on a webpage is creative common licenced, you can find in our [blogpost](https://www.ml6.eu/blogpost/ai-image-generation-without-copyright-infringement). You can find the main logic of this starting from [main.py](./components/extract_images_from_warc/src/main.py).

**Disclaimer**: This pipeline to extract the images is not 100% stable and should be used as an inspiration and not as a ready to use pipeline.