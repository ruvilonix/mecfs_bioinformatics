"""
Apply standard MAGMA and S-LDSC analysis to Donertas et al.'s GWAS of anxiety
"""

from mecfs_bio.asset_generator.concrete_standard_analysis_task_generator import (
    concrete_standard_analysis_generator_assume_already_has_rsid,
)
from mecfs_bio.assets.gwas.anxiety.donertas_et_al_2021.processed.extracted_donertas_anxiety_data import (
    DONERTAS_ET_AL_ANXIETY_EXTRACTED,
)
from mecfs_bio.build_system.task.gwaslab.gwaslab_create_sumstats_task import (
    GWASLabColumnSpecifiers,
)
from mecfs_bio.build_system.task.magma.plot_magma_brain_atlas_result import PlotSettings
from mecfs_bio.build_system.task.pipes.drop_null_pipe import DropNullsPipe

DONERTAS_ANXIETY_STANDARD_ANALYSIS = (
    concrete_standard_analysis_generator_assume_already_has_rsid(
        base_name="donertas_et_al_anxiety_standard_analysis",
        raw_gwas_data_task=DONERTAS_ET_AL_ANXIETY_EXTRACTED,
        sample_size=484598,  # from gwas catalog
        include_hba_magma_tasks=True,
        fmt=GWASLabColumnSpecifiers(
            rsid="hm_rsid",
            snpid="hm_variant_id",
            chrom="hm_chrom",
            pos="hm_pos",
            ea="hm_effect_allele",
            nea="hm_other_allele",
            info=None,
            eaf="hm_effect_allele_frequency",
            beta="hm_beta",
            p="p_value",
            se="standard_error",
            OR=None,
        ),
        hba_plot_settings=PlotSettings("plotly_white"),
        include_independent_cluster_plot_in_hba=True,
    )
)
