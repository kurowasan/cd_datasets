import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn3


def plot_distribution_type_dataset(df: pd.DataFrame, output_path: str, verbose: bool = True):
    """
    Get the distribution of the type of dataset (synth, pseudo-real, real).
    Plot a Venn diagram similar to Fig.2.
    Args:
        df: dataframe containing the curated papers
        output_path: the path to save the plot
        verbose: whether to print the distribution
    """
    print("=" * 100)
    print("Percentage of papers using each type of dataset:\n")
    only_synth = len(df[(df['synthetic'] == 1) & (df['pseudo_real'] == 0) & (df['real'] == 0)]) / len(df) * 100
    only_pseudo_real = len(df[(df['synthetic'] == 0) & (df['pseudo_real'] == 1) & (df['real'] == 0)]) / len(df) * 100
    only_real = len(df[(df['synthetic'] == 0) & (df['pseudo_real'] == 0) & (df['real'] == 1)]) / len(df) * 100
    synth_pseudo_real = len(df[(df['synthetic'] == 1) & (df['pseudo_real'] == 1) & (df['real'] == 0)]) / len(df) * 100
    synth_real = len(df[(df['synthetic'] == 1) & (df['pseudo_real'] == 0) & (df['real'] == 1)]) / len(df) * 100
    pseudo_real_real = len(df[(df['synthetic'] == 0) & (df['pseudo_real'] == 1) & (df['real'] == 1)]) / len(df) * 100
    all_types = len(df[(df['synthetic'] == 1) & (df['pseudo_real'] == 1) & (df['real'] == 1)]) / len(df) * 100

    # Plot a Venn diagram
    # the order is (100, 010, 110, 001, 101, 011, 111)
    data = (only_synth, only_pseudo_real, synth_pseudo_real, only_real, synth_real, pseudo_real_real, all_types)
    total = sum(data)
    format1 = lambda x: f"{(x/total):1.0%}"
    out = venn3(subsets=data, set_labels=('Synthetic', 'Pseudo-real', 'Real-world'), subset_label_formatter=format1)

    # increase the font size
    for text in out.set_labels:
        text.set_fontsize(20)
    for x in range(len(out.subset_labels)):
        if out.subset_labels[x] is not None:
            out.subset_labels[x].set_fontsize(20)

    plt.savefig(os.path.join(output_path, 'venn_diagram.png'))
    plt.close()

    if verbose:
        print(f"Only synthetic datasets:                 {only_synth:.1f}%")
        print(f"Only pseudo-real datasets:               {only_pseudo_real:.1f}%")
        print(f"Only real datasets:                      {only_real:.1f}%")
        print(f"Synthetic & pseudo-real datasets:        {synth_pseudo_real:.1f}%")
        print(f"Synthetic & real datasets:               {synth_real:.1f}%")
        print(f"Pseudo-real & real datasets:             {pseudo_real_real:.1f}%")
        print(f"Synthetic & pseudo-real & real datasets: {all_types:.1f}%")

        print(f"Contains real datasets: {len(df[df['real'] == 1]) / len(df) * 100:.1f}%")


def plot_distribution_fields(df: pd.DataFrame, output_path: str, verbose: bool = True):
    """
    Plot the distribution of the fields of datasets similar to Fig.3.
    Args:
        df: dataframe containing the curated papers
        output_path: the path to save the plot
        verbose: whether to print the distribution
    """
    fields_series = df['field'].str.split(',').explode()
    fields_series = fields_series.dropna()
    fields_count = fields_series.value_counts() / len(fields_series) * 100

    plt.bar(fields_count.index, fields_count.values)
    plt.xlabel('Field')
    plt.ylabel('Count')
    plt.title('Distribution of fields of pseudo-real & real-world datasets')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'field_distribution.png'))
    plt.close()

    if verbose:
        pd.options.display.float_format = "{:,.1f}".format
        print("=" * 100)
        print('Distribution of fields of pseudo-real & real-world datasets\n')
        print(fields_count)

        len_real = len(df[df['real'] == 1])
        df_sachs = df[((df['real'] == 1) & (df['real_datasets'].str.contains('Sachs')))]
        print(f"Percentage of papers containing Sachs: {len(df_sachs) / len_real * 100:.1f}%")
        df_only_sachs = df[((df['real'] == 1) & (df['real_datasets'] == 'Sachs'))]
        print(f"Percentage of papers having only Sachs as real-world data: {len(df_only_sachs) / len_real * 100:.1f}%")


def plot_distribution_datasets(df: pd.DataFrame, verbose: bool = True):
    """
    Plot the distribution of the specific datasets (e.g., Sachs, bnlearn) used in the papers.
    Args:
        df: dataframe containing the curated papers
        verbose: whether to print the distribution
    """
    print("=" * 100)
    print("Distribution of real-world datasets used in the papers:")
    datasets_series = df['real_datasets'].str.split(',').explode()
    datasets_series = datasets_series.dropna()
    datasets_count = datasets_series.value_counts() / len(datasets_series) * 100
    print(datasets_count)

    print("\nDistribution of pseudo-real datasets used in the papers:")
    datasets_series = df['pseudo_datasets'].str.split(',').explode()
    datasets_series = datasets_series.dropna()
    datasets_count = datasets_series.value_counts() / len(datasets_series) * 100
    print(datasets_count)


def plot_distribution_metrics(df: pd.DataFrame, output_path: str, verbose: bool = True):
    """
    Plot the distribution of the type of metrics used in the papers similar to Table 1.
    Args:
        df: dataframe containing the curated papers
        output_path: the path to save the plot
        verbose: whether to print the distribution
    """
    df_synth = df[((df['synthetic'] == 1) | (df['pseudo_real'] == 1))]
    synth_struct = df_synth['synth_structural'].sum() / len(df_synth) * 100
    synth_obs = df_synth['synth_observational'].sum() / len(df_synth) * 100
    synth_int = df_synth['synth_interventional'].sum() / len(df_synth) * 100
    synth_vis = df_synth['synth_qualitative'].sum() / len(df_synth) * 100

    df_real = df[df['real'] == 1]
    real_struct = df_real['real_structural'].sum() / len(df_real) * 100
    real_obs = df_real['real_observational'].sum() / len(df_real) * 100
    real_int = df_real['real_interventional'].sum() / len(df_real) * 100
    real_vis = df_real['real_qualitative'].sum() / len(df_real) * 100

    # save the results as a table in a csv file
    result = pd.DataFrame({
        'Synth and pseudo': [synth_struct, synth_vis, synth_obs, synth_int],
        'Real-world': [real_struct, real_vis, real_obs, real_int]
    }, index=['Structural', 'Observational', 'Interventional', 'Qualitative'])
    result.to_csv(os.path.join(output_path, 'table_metrics.csv'))

    if verbose:
        print("=" * 100)
        print(f"Percentage of papers using each type of metric:")
        print("\nSynthetic and pseudo-real datasets:")
        print(f"structural:     {synth_struct:.1f}%")
        print(f"qualitative:    {synth_vis:.1f}%")
        print(f"observational:  {synth_obs:.1f}%")
        print(f"interventional: {synth_int:.1f}%")
        print("\nReal-world datasets:")
        print(f"structural:     {real_struct:.1f}%")
        print(f"qualitative:    {real_vis:.1f}%")
        print(f"observational:  {real_obs:.1f}%")
        print(f"interventional: {real_int:.1f}%")
        real_w_interv = len(df[((df['real'] == 1) & (df['interventions'] == 1))])
        could_use_interv = len(df[((df['real'] == 1) & (df['interventions'] == 1) & (df['real_interventional'] == 0))]) / real_w_interv * 100
        print(f"Percentage of papers using real-world data that could have used interventional metrics: {could_use_interv:.1f}%")


def print_other_stats(df: pd.DataFrame):
    """
    Print interesting miscellaneous statistics.
    Args:
        df: dataframe containing the curated papers
    """
    print("=" * 100)
    print("Miscellaneous statistics. Percentage of ...\n")

    nb_real = len(df[df['real'] == 1])
    print(f"Papers using real-world data with small graphs (<= 20 nodes): {len(df[df['small'] == 1]) / nb_real * 100:.1f}%")
    print(f"Papers proposing methods that deals with interventional data: {len(df[df['interv_setting'] == 1]) / len(df) * 100:.1f}%")
    print(f"Papers using real-world data with interventions: {len(df[df['interventions'] == 1]) / nb_real * 100:.1f}%")
    print(f"Papers using only non-time series data: {len(df[df['time_series'] == 0]) / len(df) * 100:.1f}%")


def main(output_path: str, include_sachs: bool, verbose: bool):
    """
    Main function to analyze the curated papers.
    Args:
        output_path: the path to save the plots and tables
        include_sachs: whether to include the papers that contain only Sachs as their real-world dataset
        verbose: whether to print the distribution
    """
    plt.style.use('ggplot')

    # load curated data
    df = pd.read_csv('curated_papers.csv')
    print("Total number of papers: ", len(df))
    df = df[df['included'] == 1]
    print("Total number of included papers: ", len(df))


    if not include_sachs:
        # remove the papers that contain only Sachs as their real-world dataset
        len_before = len(df)
        df = df[~((df['real'] == 1) & (df['real_datasets'] == 'Sachs'))]
        print(f"Number of papers removed (have only Sachs as a real-world dataset): {len_before - len(df)}")

    # Produce Fig.2: Distribution of the type of dataset as a Venn diagram
    plot_distribution_type_dataset(df, output_path, verbose)

    # Produce Fig.3: Distribution of the field of study as a bar plot
    plot_distribution_fields(df, output_path, verbose)

    # Produce Table 1: Distribution of the type of metrics used in the papers
    plot_distribution_metrics(df, output_path, verbose)

    print_other_stats(df)
    plot_distribution_datasets(df)


if __name__ == "__main__":
    main(output_path='results/', include_sachs=False, verbose=True)
