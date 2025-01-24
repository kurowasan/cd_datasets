# The Landscape of Causal Discovery Data: Grounding Causal Discovery in Real-World Applications
In this repository, we make accessible the list of curated papers used in the systematic review presented in Section 4 and the code used to analyze it. We also give a list of pseudo-real and real-world datasets with their links and references.

## 📝 Systematic Review
The file `retrieve_papers.py` contains the code used to retrieve causal discovery papers using the Semantic Scholar API. To use it, you may need to get an [API key](https://www.semanticscholar.org/product/api#api-key-form) and add your API key by replacing `XXX` at the line `headers = {'x-api-key': 'XXX'}`.

The CSV file `curated_papers.csv` contains the paper found with several annotations that were made manually. The annotations indicate if the paper was included, what type of dataset and metrics was used, etc. See Appendix A.1 for a complete presentation of the different fields.

Finally, the Python code `analyze.py` can be used to analyze the `curated_papers.csv` file. It generates the graph and the data presented in Section 4.


## 📖 Causal Discovery Datasets
Here is a list of datasets that were discussed in our paper with links to download them.

### Pseudo-real datasets

| Article                          | Name                             | Link                                                                                        |
|----------------------------------|----------------------------------|---------------------------------------------------------------------------------------------|
| [Cheng et al., 2023](https://arxiv.org/abs/2310.01753)               | CausalTime                       | [https://www.causaltime.cc/](https://www.causaltime.cc/)                                    |
| [Göbler et al., 2023](https://proceedings.mlr.press/v236/gobler24a.html)              | CausalAssembly                   | [https://github.com/boschresearch/causalAssembly](https://github.com/boschresearch/causalAssembly) |
| [Lawrence et al., 2021](https://arxiv.org/abs/2104.08043)            | -                                | [https://github.com/causalens/cdml-neurips2020](https://github.com/causalens/cdml-neurips2020) |
| [Pratapa et al., 2020](https://www.nature.com/articles/s41592-019-0690-6)             | BEELINE                          | [https://github.com/murali-group/BEELINE](https://github.com/murali-group/BEELINE)          |
| [Dibaeinia and Sinha, 2020](https://www.cell.com/cell-systems/fulltext/S2405-4712(20)30287-8)        | SERGIO                           | [https://github.com/PayamDiba/SERGIO](https://github.com/PayamDiba/SERGIO)                  |
| [Runge et al., 2019](https://www.nature.com/articles/s41467-019-10105-3)               | CauseMe                          | [https://causeme.uv.es/](https://causeme.uv.es/)                                            |
| [Sanchez-Romero et al., 2019](https://direct.mit.edu/netn/article/3/2/274/2211/Estimating-feedforward-and-feedback-effective)      | -                                | [https://github.com/cabal-cmu/Feedback-Discovery](https://github.com/cabal-cmu/Feedback-Discovery) |
| [Tu et al., 2019](https://proceedings.neurips.cc/paper/2019/hash/4fdaa19b1f22a4d926fce9bfc7c61fa5-Abstract.html)                  | Neuropathic Pain Diagnosis Simulator | [https://github.com/TURuibo/Neuropathic-Pain-Diagnosis-Simulator](https://github.com/TURuibo/Neuropathic-Pain-Diagnosis-Simulator) |
| [Schaffter et al., 2011](https://academic.oup.com/bioinformatics/article/27/16/2263/254752?login=false)           | GeneNetWeaver                    | [https://gnw.sourceforge.net/genenetweaver.html](https://gnw.sourceforge.net/genenetweaver.html) |
| [Smith et al., 2011](https://www.sciencedirect.com/science/article/pii/S1053811910011602?casa_token=dK1tI3DXJ1oAAAAA:L9Pck_SbAMzS7fI8JtpPVxB12oQL4jdF3_FUfTjuNPCYUYwSZsPrzhY6DbN6NoNMrfi7t-V2SZV_)               | NetSim                           | [https://www.fmrib.ox.ac.uk/datasets/netsim/](https://www.fmrib.ox.ac.uk/datasets/netsim/)  |
| Marbach et al., 2010             | DREAM4                           | [https://www.synapse.org/Synapse:syn3049712/wiki/74630](https://www.synapse.org/Synapse:syn3049712/wiki/74630)                                                                                           |
| [Van den Bulcke et al., 2006](https://link.springer.com/article/10.1186/1471-2105-7-43)      | SynTReN                          | [https://bmcbioinformatics.biomedcentral.com/artic...](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-7-43) |

### Biology datasets
| Article                | Name                                                    | Link                                                                                                                 |
|------------------------|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [Replogle et al., 2022](https://www.cell.com/cell/fulltext/S0092-8674(22)00597-9?dgcid=raven_jbs_aip_email)  | Perturb-seq (cell line K562)                            | [https://github.com/causalbench/causalbench](https://github.com/causalbench/causalbench)                             |
| [Replogle et al., 2022](https://www.cell.com/cell/fulltext/S0092-8674(22)00597-9?dgcid=raven_jbs_aip_email)  | Perturb-seq (cell line RPE1)                            | [https://github.com/causalbench/causalbench](https://github.com/causalbench/causalbench)                             |
| [Frangieh et al., 2021](https://www.nature.com/articles/s41588-021-00779-1)  | Perturb-CITE-seq data from melanoma cells               | [https://singlecell.broadinstitute.org/single_cell...](https://singlecell.broadinstitute.org/single_cell/study/SCP1064/multi-modal-pooled-perturb-cite-seq-screens-in-patient-models-define-novel-mechanisms-of-cancer-immune-evasion) |
| [Frot et al., 2019](https://academic.oup.com/jrsssb/article/81/3/459/7048382?login=false)     | RNA-seq of ovarian cancer                               | [portal.gdc.cancer.gov](portal.gdc.cancer.gov)                                                                                                                    |
| [Dixit et al., 2016](https://www.cell.com/cell/fulltext/S0092-8674(16)31610-5)     | Perturb-Seq of bone marrow-derived dendritic cells      | [https://www.cell.com/cell/fulltext/S0092-8674...](https://www.cell.com/cell/fulltext/S0092-8674(16)31610-5)                                                                                                                    |
| [Singer et al., 2016](https://www.cell.com/cell/fulltext/S0092-8674(16)31149-7)    | Naive and activated T cells (Drop-seq)                  | [https://www.cell.com/cell/fulltext/S0092-8674...](https://www.cell.com/cell/fulltext/S0092-8674(16)31149-7)                                                                                                                    |
| [Sachs et al., 2005](https://www.science.org/doi/abs/10.1126/science.1105809)     | Flow cytometry dataset of immune cells                  | [https://www.bnlearn.com/research/sachs05/](https://www.bnlearn.com/research/sachs05/)                                                                                                                    |
| [Wille et al., 2004](https://link.springer.com/content/pdf/10.1186/gb-2004-5-11-r92.pdf)     | Microarray of *A. thaliana* gene expression             | [https://link.springer.com/article/10.1186...](https://link.springer.com/article/10.1186/gb-2004-5-11-r92#MOESM1)                                                                                                                     |

### Brain imaging datasets
| Dataset                      | Link raw data                                               | Link preprocessed                                                                                   |
|------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [Randi et al., 2023](https://www.nature.com/articles/s41586-023-06683-4)      |   [https://osf.io/e2syt/](https://osf.io/e2syt/)  |  [https://huggingface.co/datasets/qsimeon/celeg...](https://huggingface.co/datasets/qsimeon/celegans_connectome_data)  |
| [Thompson et al., 2020](https://www.nature.com/articles/s41597-020-00595-y)        | [https://openneuro.org/datasets/ds002799...](https://openneuro.org/datasets/ds002799/versions/1.0.4) | same |
| [Shah et al., 2018](https://onlinelibrary.wiley.com/doi/abs/10.1002/hbm.23887?casa_token=ehocP69XtfwAAAAA:IzGAy-q-iubWXGaSlY_cH2fsRNl7Od8LJfHEIPKQniOerrp8SzyOVotr_2unB_muVAYy0vkUFBMN4w)            | [https://github.com/shahpreya/MTLnet](https://github.com/shahpreya/MTLnet) | -                                                                                                   |
| [Poldrack et al., 2015](https://www.nature.com/articles/ncomms9885)        | [https://openneuro.org/datasets/ds000031/](https://openneuro.org/datasets/ds000031/) | .                                                                                                   |
| [Di Martino et al., 2014](https://www.nature.com/articles/mp201378)      | [https://fcon_1000.projects.nitrc.org/indi/abide/](https://fcon_1000.projects.nitrc.org/indi/abide/) | [http://preprocessed-connectomes-project.org...](http://preprocessed-connectomes-project.org/abide/download.html) |
| [Van Essen et al., 2013](https://www.sciencedirect.com/science/article/abs/pii/S1053811913005351?casa_token=vLWNXEDAk9MAAAAA:R9p1NoVlrKXWDBmM6yK9ZXaXXWw8MIiId_uz5ZKeGysUTvBQ6xI46lEhvO617maVSG678w3_)       | [https://db.humanconnectome.org.](https://db.humanconnectome.org.)                                                           | .                                                                                                   |
| [Ramsey et al., 2010](https://www.sciencedirect.com/science/article/pii/S105381190900977X?casa_token=ZEz6i96-VesAAAAA:4PvOwVle6XeO4iAEr4EWESUP77L73FdzF49pU59IqrTAuRp_tPFNIKMyD0Pr1n1HnHpISvZD1w6J)          | [https://openneuro.org/datasets/ds000003...](https://openneuro.org/datasets/ds000003/versions/00001) | [https://github.com/cabal-cmu/Feedback-Discovery](https://github.com/cabal-cmu/Feedback-Discovery) |
| Wang et al., 2003            | .    | .                                                           | .                                                                                                   |


### Earth Sciences
| Article                                                                 | Name                                            | Link                                                                               |
|------------------------------------------------------------------------|-------------------------------------------------|------------------------------------------------------------------------------------|
| [Kaltenborn et al., 2024](https://arxiv.org/abs/2311.03721)              | ClimateSet                                      | [link to dataset](https://climateset.github.io/)                                   |
| [Nguyen et al., 2024](https://arxiv.org/abs/2307.01909)                  | ClimateLearn                                    | contained in ClimateSet                                                            |
| [Yu et al., 2024](https://proceedings.neurips.cc/paper_files/paper/2023/file/45fbcc01349292f5e059a0b8b02c8c3f-Paper-Datasets_and_Benchmarks.pdf)                  | ClimSim                                         | contained in ClimateSet                                                            |
| [Watson-Parris et al., 2022](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2021MS002954)                       | ClimateBench                                    | contained in ClimateSet                                                            |
| [Rasp et al., 2020](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020MS002203)                         | WeatherBench                                    | contained in ClimateSet                                                            |
| [de Witt et al., 2021](https://ojs.aaai.org/index.php/AAAI/article/view/17749)                           | RainBench                                       | contained in ClimateSet                                                            |
| -                                                                    | KNMI Climate Explorer                           | [link to database](https://climexp.knmi.nl/)                                       |
| -                                                                    | NCEP/NCAR 40-year reanalysis project            | [link to database](https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html)    |
| [Hersbach et al., 2020](https://rmets.onlinelibrary.wiley.com/doi/full/10.1002/qj.3803)                     | ERA reanalysis project                          | [link to database](https://cds.climate.copernicus.eu)                              |
| --                                                                      | Climate Prediction Center (CPC) global rainfall dataset | [link to dataset](https://psl.noaa.gov/data/gridded/tables/precipitation.html) |
| [Pastorello et al., 2020](https://www.nature.com/articles/s41597-020-0534-3)                   | FLUXNET                                         | [link to database](https://fluxnet.org)                                            |
| -                                                                     | Tropospheric Ozone Assessment Report (TOAR)     | [link to database](https://toar-data.org) |
| -                                                                     | CDC Influenza report                            | [link to dataset](https://www.cdc.gov/fluview/overview/fluview-interactive.html?CDC_AAref_Val=https://www.cdc.gov/flu/weekly/fluviewinteractive.htm)                        |
| [Eyring et al., 2016](https://gmd.copernicus.org/articles/9/1937/2016/)                       | Climate Model Intercomparison Project (CMIP)    | [link to database](https://wcrp-cmip.org)                                          |


### Miscellaneous real-world datasets
| Article                                                                 | Name                                            | Link                                                                               |
|------------------------------------------------------------------------|-------------------------------------------------|------------------------------------------------------------------------------------|
| [Gamella et al., 2024](https://arxiv.org/pdf/2404.11341)  | Causal Chambers                            | [link to simulator](https://github.com/juangamella/causal-chamber) |
| [Wang et al., 2023](https://openreview.net/pdf?id=JFaZ94tT8M) | MOS 6502 microprocessor | [link to dataset](https://github.com/KordingLab/LearningCausalDiscovery) |
| [Gentzel et al., 2019](https://arxiv.org/abs/1910.05387) | Software Systems (PostgreSQL, JDK, Networking) | [link to datasets](https://groups.cs.umass.edu/kdl/causal-eval-data/) |
| [Mooij et al., 2016](https://jmlr.org/papers/v17/14-518.html) | Cause-effect pairs (Tübingen pairs) | [link to dataset](https://webdav.tuebingen.mpg.de/cause-effect/) |
