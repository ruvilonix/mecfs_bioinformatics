"""
Task to download GWAS summary statistics from Donertas et al's Anxiety GWAS

see:
https://www.ebi.ac.uk/gwas/studies/GCST90038651

Citation:
Dönertaş, Handan Melike et al. “Common genetic associations between age-related diseases.” Nature aging vol. 1,4 (2021): 400-412. doi:10.1038/s43587-021-00051-5
"""

from pathlib import PurePath

from mecfs_bio.build_system.meta.asset_id import AssetId
from mecfs_bio.build_system.meta.gwas_summary_file_meta import GWASSummaryDataFileMeta
from mecfs_bio.build_system.meta.read_spec.dataframe_read_spec import (
    DataFrameReadSpec,
    DataFrameTextFormat,
)
from mecfs_bio.build_system.task.download_file_task import DownloadFileTask

DONERTAS_ET_AL_ANXIETY_RAW = DownloadFileTask(
    meta=GWASSummaryDataFileMeta(
        id=AssetId("donertas_et_al_anxiety_raw"),
        trait="anxiety",
        project="donertas_et_al",
        sub_dir="raw",
        project_path=PurePath("33959723-GCST90038651-EFO_0004262.h.tsv.gz"),
        read_spec=DataFrameReadSpec(
            format=DataFrameTextFormat(separator="\t", null_values=["NaN", "NA"]),
        ),
    ),
    url="https://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90038001-GCST90039000/GCST90038651/harmonised/33959723-GCST90038651-EFO_0004262.h.tsv.gz",
    md5_hash="1cba3d8eaeecceab7b851cd4414cfb60",
)
