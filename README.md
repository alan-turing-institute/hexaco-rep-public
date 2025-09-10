#  Applying Psychometrics to Large Language Model Simulated Populations: Recreating the HEXACO Personality Inventory Experiment with Generative Agents


## Abstract: 

Generative agents powered by Large Language Models demonstrate human-like characteristics through sophisticated natural language interactions. Their ability to assume roles and personalities based on predefined character biographies has positioned them as cost-effective substitutes for human participants in social science research. This paper explores the validity of such persona-based agents in representing human populations; we recreate the HEXACO personality inventory experiment by surveying 310 GPT-4 powered agents, conducting factor analysis on their responses, and comparing these results to the original findings presented by Ashton, Lee, & Goldberg in 2004. Our results found 1) a coherent and reliable personality structure was recoverable from the agents' responses demonstrating partial alignment to the HEXACO framework. 2) the derived personality dimensions were consistent and reliable within GPT-4, when coupled with a sufficiently curated population, and 3) cross-model analysis revealed variability in personality profiling, suggesting model-specific biases and limitations. We discuss the practical considerations and challenges encountered during the experiment. This study contributes to the ongoing discourse on the potential benefits and limitations of using generative agents in social science research and provides useful guidance on designing consistent and representative agent personas to maximise coverage and representation of human personality traits.

Public repository for data and code associated with our paper: [arXiv](https://arxiv.org/abs/2508.00742), by [Sarah Mercer](drsezzer.github.io).

## Project Navigation:

### Results:

Lexical Analysis:

The following notebooks contain code to perform PCA and present the resulting factors.  Additionally, cronbach alpha's, jaccard coefficients (with original hexaco findings) are presented.  Alongside, semantic similiarity score for the terms within in factor, and the factors against hexaco dimensions.
* [PopCensus 5-Factor Solution](PopCensus-5Factor-Results.ipynb)
* [PopCensus 6-Factor Solution](PopCensus-6Factor-Results.ipynb)
* [PopCensus 10-Factor Solution](PopCensus-10Factor-Results.ipynb) (including Fig. 4 and Fig. 5).
* [PopProfessional 8-Factor Solution](PopProfessional-8Factor-Results.ipynb) (including Fig. 12).

HEXACO-PI-R 100:
* [Survey results using GPT-4, Llama-3.2, Sonnet 3.7 and Phi-4](hexaco_pi_r.ipynb)

### Data Files:

PopCensus:

* [data/pop_census.json](data/pop_census.json) - contains all the character biographies for PopCensus.  Use data_support.fix_name() to translate 'Full Name' to index in results and ipsatised_results files.

* <b>data/popc_responses_file*.csv</b> - batches of agent responses (under 50MB each).

* <b>data/popc_results.csv</b> - contains scores from hexaco lexical analysis survey.  Columns are adjectives, indexed by names (via fix_name()). *

* <b>data/popc_ipsatised_results.csv</b> - contains ipsatised scores from survey.  Columns are adjectives, indexed by names (via fix_name()). *

PopProfessional:

* [data/pop_professional.json](data/pop_professional.json) - contains all the character biographies for PopProfessional.  Use data_support.fix_name() to translate 'Full Name' to index in results and ipsatised_results files.

* <b>data/popp_results.csv</b> - contains scores from hexaco lexical analysis survey, for PopProfessional.  Columns are adjectives, indexed by names (via fix_name()). *

* <b>data/popp_ipsatised_results.csv</b> - contains ipsatised scores from survey, for PopProfessional.  Columns are adjectives, indexed by names (via fix_name()). *

(*) can be generated from agent responses, using data/data_prep.ipynb.

Lexical Analysis Support:

* [data/adjectives.json](data/adjectives.json) - a list of all the adjectives from the survey.

HEXACO-PI-R 100:

* <b>data/hexaco-pi-r-responses-gpt4.csv</b> - responses from HEXACO-PI-R 100 survey (PopCensus), generated with GPT-4.

* <b>data/hexaco-pi-r-responses-llama.csv</b> - responses from HEXACO-PI-R 100 survey (PopCensus), generated with Llama-3.2 (3Bn, via Ollama). <br>
<i>Note: Llama refused to give a response for question 98 ('It wouldn't bother me to harm someone I didn't like.') 85 times (response=='[content-filtered]').  This question is part of the Altruism facet, which is not included in 6 main dimensions.</i>

* <b>data/hexaco-pi-r-responses-sonnet.csv</b> - responses from HEXACO-PI-R 100 survey (PopCensus), generated with Claude Sonnet 3.7. <br>

* <b>data/hexaco-pi-r-responses-phi4.csv</b> - responses from HEXACO-PI-R 100 survey (PopCensus), generated with Microsoft's Phi4 (14Bn, via Ollama). <br>

---

### Supporting code

* [Figure 1, Figure 11](Fig1-Occupations.ipynb) - population broken down by OSC2020 Occupation codes, and plotted against census data (England & Wales 2020).

* [Figure 2](Fig2-ScreePlot.ipynb) - Scree plot of unrotated eigenvalues (pop census).

* [Figure 3](Fig3-SolutionCronbachs.ipynb) - Heatmap of Cronbach's alphas for each factor in all solutions.

* [Figure 6](Fig6-ConvergentValidity.ipynb) - Heatmap of correlation between agents' survey responses and their PIR-100 results.

* [Figure 13](Fig13-SolutionSimilarity.ipynb) - Heatmap of correlation between PopCensus' 10 factors and PopProfessional's 8 factors.

* [Figure 14](Fig14-BiographyLengths.ipynb) - plot of agent consistency vs biography length (for PopCensus).

## Installation Notes

Python packages pandas and gensim are required to run these notebooks.  

PCA is conducted using 'R', create a _private.py file in the support subdirectory that contains the following definition:

> r_binary_folder = '[your path to]/bin/Rscript'

Ensure 'psych' and 'readr' are installed in your R environment:

``` 
install.packages("tidyverse")
install.packages("psych")
```

This project expects to find the [FastText](https://fasttext.cc/docs/en/crawl-vectors.html) model (cc.en.300.vec) in a subfolder called 'model_data'.

## License

Data and Code released under MIT License.  Please cite our [research](http://arxiv.org/) if you use either in your work.

## Notes

Copyright (c) 2023-2025 The Alan Turing Institute.

