# Understanding the Influence of AI-Generated Content on Political Perspectives Among Young Voters

This project investigates how political content generated by large language models (LLMs) influences opinion formation among young voters in Germany, with a particular focus on the 2025 federal election. The study centers on two key policy areas: climate change and education.

The project folder includes all data, analysis scripts, and notebooks used in the study. Materials are organized by research phase and hypothesis, allowing full transparency and reproducibility of the methodology and results.

## Project Structure

### data/
Contains original survey exports and processed datasets:
- `cleaned_file.csv`: Final dataset used for analysis.
- `data_llmsandpoliticalopinion_2025-02-25_10-53.csv`: Raw SoSci Survey exports.
- `variables_llmsandpoliticalopinion_2025-02-25_10-11.csv` and `values_llmsandpoliticalopinion_2025-02-25_10-11.csv`: Codebooks documenting survey items and value labels.

### plots/
Stores all generated visualizations, organized thematically:
- `demographic_distributions/`: Plots showing the sample’s demographic characteristics.
- `hypothesis1/` to `hypothesis5/`: Visualizations of each hypothesis.

### Notebooks and Scripts
- `data_preprocessing.py`: Script for loading, cleaning, and transforming the dataset. 
- `data_demographic_overview.ipynb`: Descriptive overview of participant characteristics.
- `hypothesis1.ipynb` to `hypothesis5.ipynb`: Statistical testing and result interpretation, one notebook per hypothesis.
- `information_habits_analysis.ipynb`: Analysis of participants’ media usage and trust in political information sources.
- `open_ended_analysis.ipynb`: Keyword-based analysis of qualitative responses explaining credibility and trust evaluations.

## Tools and Environment
- Python 3.11
- Core libraries: pandas, numpy, matplotlib, seaborn, scipy, statsmodels, sklearn
- Jupyter Notebooks, developed in Visual Studio Code
- Survey platform: SoSci Survey

## Reproducibility
All analysis steps are scripted and reproducible. Preprocessing functions are modularized. Notebooks are annotated with explanations of each step, and all plots can be regenerated from the final dataset.

## License / Citation
If this project or its methodology is used in academic or applied research, please cite the original thesis and dataset accordingly.
