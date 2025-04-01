#  Large Language Models and their role within Social Science: recreating the HEXACO Personality Inventory experiment with Generative Agents

[![DOI](pdf.pdf)](pdf.pdf)

Public repository for data and code associated with [Hexaco &amp; GenAgents Paper](pdf.pdf).

by [Sarah Mercer](drsezzer.github.io).

## Project Navigation:

### Results:

Lexical Analysis:

The following notebooks contain code to perform PCA and present the resulting factors.  Additionally, cronbach alpha's, jaccard coefficients (with original hexaco findings) are presented.  Alongside, semantic similiarity score for the terms within in factor, and the factors against hexaco dimensions.
* [PopCensus 5-Factor Solution](popCensus_5Factor.ipynb)
* [PopCensus 6-Factor Solution](popCensus_6Factor.ipynb)
* [PopCensus 10-Factor Solution](popCensus_10Factor.ipynb)
* [PopProfessional 8-Factor Solution](popProfessional_8Factor.ipynb)

HEXACO-PI-R 100:
* [Survey results using GPT-4 & Llama-3.2](hexaco_pir_results.ipynb)

### Data Files:

PopCensus:

* [data/pop_census.json](data/pop_census.json) - contains all the character biographies for PopCensus.  Use data_support.fix_name() to translate 'Full Name' to index in results and ipsatised_results files.

* <b>data/popc_results.csv</b> - contains scores from hexaco lexical analysis survey.  Columns are adjectives, indexed by names (via fix_name()).

* <b>data/popc_ipsatised_results.csv</b> - contains ipsatised scores from survey.  Columns are adjectives, indexed by names (via fix_name()).  

PopProfessional:

* [data/pop_professional.json](data/pop_professional.json) - contains all the character biographies for PopProfessional.  Use data_support.fix_name() to translate 'Full Name' to index in results and ipsatised_results files.

* <b>data/popp_results.csv</b> - contains scores from hexaco lexical analysis survey, for PopProfessional.  Columns are adjectives, indexed by names (via fix_name()).

* <b>data/popp_ipsatised_results.csv</b> - contains ipsatised scores from survey, for PopProfessional.  Columns are adjectives, indexed by names (via fix_name()).

Lexical Analysis Support:

* [data/adjectives.json](data/adjectives.json) - a list of all the adjectives from the survey.

HEXACO-PI-R 100:

* <b>data/hexaco-pi-r-responses-gpt4.csv</b> - responses from HEXACO-PI-R 100 survey (PopCensus), generated with GPT-4.

* <b>data/hexaco-pi-r-responses-llama.csv</b> - responses from HEXACO-PI-R 100 survey (PopCensus), generated with Llama-3.2. <br>
<i>Note: Llama refused to give a response for question 98 ('It wouldn't bother me to harm someone I didn't like.') 85 times (response=='[content-filtered]').  This question is part of the Altruism facet, which is not included in 6 main dimensions.</i>

## License

Data and Code released under MIT License.  Please cite our [research]() if you use either in your work.

## Notes

Copyright (c) 2023-2025 The Alan Turing Institute.

