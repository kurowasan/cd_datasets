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
| Cheng et al., 2023               | CausalTime                       | [https://www.causaltime.cc/](https://www.causaltime.cc/)                                    |
| Göbler et al., 2023              | CausalAssembly                   | [https://github.com/boschresearch/causalAssembly](https://github.com/boschresearch/causalAssembly) |
| Lawrence et al., 2021            | -                                | [https://github.com/causalens/cdml-neurips2020](https://github.com/causalens/cdml-neurips2020) |
| Pratapa et al., 2020             | BEELINE                          | [https://github.com/murali-group/BEELINE](https://github.com/murali-group/BEELINE)          |
| Dibaeinia and Sinha, 2020        | SERGIO                           | [https://github.com/PayamDiba/SERGIO](https://github.com/PayamDiba/SERGIO)                  |
| Runge et al., 2019               | CauseMe                          | [https://causeme.uv.es/](https://causeme.uv.es/)                                            |
| Sanchez-Romero et al., 2019      | -                                | [https://github.com/cabal-cmu/Feedback-Discovery](https://github.com/cabal-cmu/Feedback-Discovery) |
| Tu et al., 2019                  | Neuropathic Pain Diagnosis Simulator | [https://github.com/TURuibo/Neuropathic-Pain-Diagnosis-Simulator](https://github.com/TURuibo/Neuropathic-Pain-Diagnosis-Simulator) |
| Schaffter et al., 2011           | GeneNetWeaver                    | [https://gnw.sourceforge.net/genenetweaver.html](https://gnw.sourceforge.net/genenetweaver.html) |
| Smith et al., 2011               | NetSim                           | [https://www.fmrib.ox.ac.uk/datasets/netsim/](https://www.fmrib.ox.ac.uk/datasets/netsim/)  |
| Hyvarinen et al., 2010       | .    | .                                                           | .                                                                                                   |
| Marbach et al., 2010             | DREAM4                           | [https://www.synapse.org/Synapse:syn3049712/wiki/74630](https://www.synapse.org/Synapse:syn3049712/wiki/74630)                                                                                           |
| Van den Bulcke et al., 2006      | SynTReN                          | [https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1...](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-7-43) |

### Gene regulatory network datasets
| Article                | Name                                                    | Link                                                                                                                 |
|------------------------|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Replogle et al., 2022  | Perturb-seq (cell line K562)                            | [https://github.com/causalbench/causalbench](https://github.com/causalbench/causalbench)                             |
| Replogle et al., 2022  | Perturb-seq (cell line RPE1)                            | [https://github.com/causalbench/causalbench](https://github.com/causalbench/causalbench)                             |
| Frangieh et al., 2021  | Perturb-CITE-seq data from melanoma cells               | [https://singlecell.broadinstitute.org/single_cell/study/SCP...](https://singlecell.broadinstitute.org/single_cell/study/SCP1064/multi-modal-pooled-perturb-cite-seq-screens-in-patient-models-define-novel-mechanisms-of-cancer-immune-evasion) |
| Frot et al., 2019      | RNA-seq of ovarian cancer                               | .                                                                                                                    |
| Dixit et al., 2016     | Perturb-Seq of bone marrow-derived dendritic cells      | [https://www.cell.com/cell/fulltext/S0092-8674(16)31610-5](https://www.cell.com/cell/fulltext/S0092-8674(16)31610-5)                                                                                                                    |
| Singer et al., 2016    | Naive and activated T cells (Drop-seq)                  | [https://www.cell.com/cell/fulltext/S0092-8674(16)31149-7](https://www.cell.com/cell/fulltext/S0092-8674(16)31149-7)(https://www.cell.com/cell/fulltext/S0092-8674(16)31149-7)                                                                                                                    |
| Klein et al., 2015     | scRNAseq data of mouse embryonic stem cells             | .                                                                                                                    |
| Sachs et al., 2005     | Flow cytometry dataset of immune cells                  | [https://www.bnlearn.com/research/sachs05/](https://www.bnlearn.com/research/sachs05/)                                                                                                                    |
| [Wille et al., 2004](https://link.springer.com/content/pdf/10.1186/gb-2004-5-11-r92.pdf)     | Microarray of *A. thaliana* gene expression             | [link](https://link.springer.com/article/10.1186/gb-2004-5-11-r92#MOESM1)                                                                                                                     |

### Brain imaging datasets
| Dataset                      | Link raw data                                               | Link preprocessed                                                                                   |
|------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Shah et al., 2018            | [https://github.com/shahpreya/MTLnet](https://github.com/shahpreya/MTLnet) | -                                                                                                   |
| Poldrack et al., 2015        | [https://openneuro.org/datasets/ds000031/](https://openneuro.org/datasets/ds000031/) | .                                                                                                   |
| Di Martino et al., 2014      | [https://fcon_1000.projects.nitrc.org/indi/abide/](https://fcon_1000.projects.nitrc.org/indi/abide/) | [http://preprocessed-connectomes-project.org/abide/download.html](http://preprocessed-connectomes-project.org/abide/download.html) |
| Van Essen et al., 2013       | [https://db.humanconnectome.org.](https://db.humanconnectome.org.)                                                           | .                                                                                                   |
| Ramsey et al., 2010          | [https://openneuro.org/datasets/ds000003/versions/00001](https://openneuro.org/datasets/ds000003/versions/00001) | [https://github.com/cabal-cmu/Feedback-Discovery](https://github.com/cabal-cmu/Feedback-Discovery) |
| Wang et al., 2003            | .    | .                                                           | .                                                                                                   |

