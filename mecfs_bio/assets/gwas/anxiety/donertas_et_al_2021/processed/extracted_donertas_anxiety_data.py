from mecfs_bio.assets.gwas.anxiety.donertas_et_al_2021.raw.raw_donertas_data import (
    DONERTAS_ET_AL_ANXIETY_RAW,
)
from mecfs_bio.build_system.task.extract_gzip_task import ExtractGzipTextFileTask

DONERTAS_ET_AL_ANXIETY_EXTRACTED = ExtractGzipTextFileTask.create_for_gwas_file(
    source_file_task=DONERTAS_ET_AL_ANXIETY_RAW,
    asset_id="donertas_et_al_anxiety_extracted",
)
