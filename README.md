#  Large Language Models and their role within Social Science: recreating the HEXACO Personality Inventory experiment with Generative Agents

Public repository for data and code associated with [Hexaco &amp; GenAgents Paper](pdf.pdf).

## Project Navigation:

### Results:

* [PopCensus 5-Factor Solution](popCensus_5Factor.ipynb)
* [PopCensus 6-Factor Solution](popCensus_6Factor.ipynb)
* [PopCensus 10-Factor Solution](popCensus_10Factor.ipynb)
* [PopProfessional 8-Factor Solution](popProfessional_8Factor.ipynb)

### Data Files:

* <b>data/pop_census.json</b> - contains all the character biographies for PopCensus.  Use data_support.fix_name() to translate 'Full Name' to index in results and ipsatised_results files.

* <b>data/popc_results.csv</b> - contains scores from hexaco lexical analysis survey.  Columns are adjectives, indexed by names (via fix_name()).

* <b>data/popc_ipsatised_results.csv</b> - contains ipsatised scores from survey.  Columns are adjectives, indexed by names (via fix_name()).

* <b>data/pop_population.json</b> - contains all the character biographies for PopPopulation.  Use data_support.fix_name() to translate 'Full Name' to index in results and ipsatised_results files.

* <b>data/popp_results.csv</b> - contains scores from hexaco lexical analysis survey, for PopProfessional.  Columns are adjectives, indexed by names (via fix_name()).

* <b>data/popp_ipsatised_results.csv</b> - contains ipsatised scores from survey, for PopProfessional.  Columns are adjectives, indexed by names (via fix_name()).

* <b>data/adjectives.json</b> - a list of all the adjectives from the survey.

* <b>data/hexaco-pi-r-responses-gpt4.csv</b> - responses from HEXACO-PI-R 100 survey (PopCensus), generated with GPT-4.

* <b>data/hexaco-pi-r-responses-llama.csv</b> - responses from HEXACO-PI-R 100 survey (PopCensus), generated with Llama-3.2. <br>
<i>Note: Llama refused to give a response for question 98 ('It wouldn't bother me to harm someone I didn't like.') 85 times (response=='[content-filtered]').  This question is part of the Altruism facet, which is not included in 6 main dimensions.</i>

## License

Data and Code released under MIT License.  Please cite our [research]() if you use either in your work.

## Contact

* [Sarah Mercer](https://github.com/drsezzer/)

---

Copyright (c) 2023-2025 The Alan Turing Institute.

