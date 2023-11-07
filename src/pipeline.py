# Pipeline code goes here
import logging
import sys

from fondant.pipeline import ComponentOp, Pipeline


logger = logging.getLogger(__name__)
sys.path.append("../")

PIPELINE_NAME = "cc-image-filter-pipeline"
PIPELINE_DESCRIPTION = "Load cc image dataset"
BASE_PATH = "./data-dir"

# Define pipeline
pipeline = Pipeline(pipeline_name=PIPELINE_NAME, base_path=BASE_PATH)

# Load from hub component
load_component_column_mapping = {
    "alt_text": "images_alt+text",
    "image_url": "images_url",
    "license_location": "images_license+location",
    "license_type": "images_license+type",
    "webpage_url": "images_webpage+url",
    "surt_url": "images_surt+url",
    "top_level_domain": "images_top+level+domain",
}

load_from_hf_hub = ComponentOp(
    component_dir="components/load_from_hf_hub",
    arguments={
        "dataset_name": "fondant-ai/fondant-cc-25m",
        "column_name_mapping": load_component_column_mapping,
        "n_rows_to_load": 100,  # Modify the number of images you want to download.
    },
)

# Download images component
download_images = ComponentOp.from_registry(
    name="download_images",
    arguments={"input_partition_rows": 100, "resize_mode": "no"},
)

# Add components to the pipeline
pipeline.add_op(load_from_hf_hub)
pipeline.add_op(download_images, dependencies=[load_from_hf_hub])
