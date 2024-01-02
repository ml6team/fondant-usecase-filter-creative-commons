"""Pipeline to download and filter images from the Common Crawl dataset.""" ""
from pathlib import Path

import pyarrow as pa
from fondant.pipeline import Pipeline

PIPELINE_NAME = "cc-image-filter-pipeline"
PIPELINE_DESCRIPTION = "Load cc image dataset"
BASE_PATH = "./data-dir"

# Create data directory if it doesn't exist
Path(BASE_PATH).mkdir(parents=True, exist_ok=True)

# Define pipeline
pipeline = Pipeline(
    name=PIPELINE_NAME, description=PIPELINE_DESCRIPTION, base_path=BASE_PATH
)

# Load from hub component
raw_data = pipeline.read(
    "load_from_hf_hub",
    arguments={
        "dataset_name": "fondant-ai/fondant-cc-25m",
        "n_rows_to_load": 100,  # Modify the number of images you want to download.
    },
    produces={
        "alt_text": pa.string(),
        "image_url": pa.string(),
        "license_location": pa.string(),
        "license_type": pa.string(),
        "webpage_url": pa.string(),
        "surt_url": pa.string(),
        "top_level_domain": pa.string(),
    },
)

# Download images component
images = raw_data.apply(
    "download_images",
    arguments={
        "input_partition_rows": 100,
        "resize_mode": "no",
    },
)

# Filter images component
big_images = images.apply(
    "filter_image_resolution",
    arguments={
        "min_image_dim": 512,
        "max_aspect_ratio": 2.5,
    },
)
