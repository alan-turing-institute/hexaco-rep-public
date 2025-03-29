# hexaco-rep-public
Public repository for data and code associated with Hexaco &amp; GenAgents Paper.

Project Navigation:

* <b>data/pop_census.json</b> - contains all the character biographies for PopCensus.  Use data_support.fix_name() to translate 'Full Name' to index in results and ipsatised_results files.

* <b>data/popc_results.csv</b> - contains scores from hexaco lexical analysis survey.  Columns are adjectives, indexed by names (via fix_name()).

* <b>data/popc_ipsatised_results.csv</b> - contains ipsatised scores from survey.  Columns are adjectives, indexed by names (via fix_name()).

* <b>data/adjectives.json</b> - a list of all the adjectives from the survey.

* <b>data/popp_results.csv</b> - contains scores from hexaco lexical analysis survey, for PopProfessional.  Columns are adjectives, indexed by names (via fix_name()).

* <b>data/popp_ipsatised_results.csv</b> - contains ipsatised scores from survey, for PopProfessional.  Columns are adjectives, indexed by names (via fix_name()).


* <b>data/hexaco-pi-r-responses-gpt4.csv</b> - responses from HEXACO-PI-R 100 survey (PopCensus), generated with GPT-4.

* <b>data/hexaco-pi-r-responses-llama.csv</b> - responses from HEXACO-PI-R 100 survey (PopCensus), generated with Llama-3.2. <br>
<i>Note: Llama refused to give a response for question 98 ('It wouldn't bother me to harm someone I didn't like.') 85 times (response=='[content-filtered]').  This question is part of the Altruism facet, which is not included in 6 main dimensions.</i>
