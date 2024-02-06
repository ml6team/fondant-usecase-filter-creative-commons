"""Pipeline to download and filter images from the Common Crawl dataset.""" ""
from pathlib import Path

import pandas as pd
import pyarrow as pa
from fondant.component import PandasTransformComponent
from fondant.pipeline import Pipeline, lightweight_component

PIPELINE_NAME = "cc-image-filter-pipeline"
PIPELINE_DESCRIPTION = "Load cc image dataset"
BASE_PATH = "./fondant-artifacts"

# Create data directory if it doesn't exist
Path(BASE_PATH).mkdir(parents=True, exist_ok=True)

pipeline = Pipeline(
    name=PIPELINE_NAME, description=PIPELINE_DESCRIPTION, base_path=BASE_PATH
)

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

images = raw_data.apply(
    "download_images",
    arguments={
        "input_partition_rows": 100,
        "resize_mode": "no",
    },
)


@lightweight_component(consumes={"image_width": pa.int32(), "image_height": pa.int32()})
class FilterImageResolution(PandasTransformComponent):
    """Component that filters images based on height and width."""

    def __init__(
        self,
        *,
        min_image_dim: int,
        max_aspect_ratio: float,
    ) -> None:
        """
        Args:
            min_image_dim: minimum image dimension.
            max_aspect_ratio: maximum aspect ratio.
        """
        self.min_image_dim = min_image_dim
        self.max_aspect_ratio = max_aspect_ratio

    def transform(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        import numpy as np

        width = dataframe["image_width"]
        height = dataframe["image_height"]
        min_image_dim = np.minimum(width, height)
        max_image_dim = np.maximum(width, height)
        aspect_ratio = max_image_dim / min_image_dim
        mask = (min_image_dim >= self.min_image_dim) & (
            aspect_ratio <= self.max_aspect_ratio
        )

        return dataframe[mask]


big_images = images.apply(
    FilterImageResolution,
    arguments={
        "min_image_dim": 512,
        "max_aspect_ratio": 2.5,
    },
)

big_images.write(
    "write_to_file",
    arguments={"path": "/fondant-artifacts/output"},
    consumes={"image": pa.binary()},
)
