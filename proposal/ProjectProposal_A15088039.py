#!/usr/bin/env python
# coding: utf-8

# # COGS 108 - Project Proposal

# # Names & PID
# 
# - Name: Odalys Juarez
# - PID: A15088039

# # Research Question

# Is there a relationship between Compton restaurant's Health Inspection Score and their proximity to high transit areas?

# ## Background and Prior Work

# Research regarding the specific relationship between an establishment's Health Inspection Score and its location near highly transited areas has not been conducted as of yet. Looking into data that may aid into helping find correlations between these two variables will include understanding the rating system used in the Los Angeles County. Information to this can be viewed in the public County of Los Angeles Public Health website that details the grading and requirements for retail food facilities. Health Inspections conducted by Inspectors run on a one hundred point system. At the beginning of the inspection, the restaurant starts with one hundred points. If violations are found, points will be subtracted from the one hundred score. A letter grade is assigned from the total score. Letter ranges are:
# - A (100 - 90)
# - B (89 - 80)
# - C (79 - 70)
# - Given Score (69 and below)
# 
# Scores lower than 69 will simply be assigned their score. 
# 
# The only relevant source found was one regarding research conducted by to understand the relationship between the frequency of health inspections and restaurant sociodemographic characteristics to the food safety inspection outcomes in both chain and non-chain establishments. Variable that were used were restaurant type, inspection frequency, and violation type. Results from the study concluded that chain establishments had fewer violations during inspections. They wanted to understand whether one could predict a restaurants inspection score based on whether it was related to a chain or not. Their results are interesting in regard to my research question since I want to find associations between an establishments Health Inspection score and location. I believe that location is a factor on an establishments score being that most chain establishments would push to find locations near more regularly populated areas. Being part of a chain will also require maintenance to conserve brand image and popularity. This represents a difference between locally inclined restaurants and restaurants meant for mainly any form of customer.
# 
# References (include links):
# - 1)http://www.publichealth.lacounty.gov/eh/dse/RetailFoodInsection/desfood.htm#resp
# - 2)http://publichealth.lacounty.gov/eh/misc/ehpost.htm
# - 3)https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5349477/
# - 4)https://www.chinahighlights.com/travelguide/article-local-restaurants.htm

# # Hypothesis
# 

# A restaurant’s Health Inspection score would be higher based on its proximity near high transit areas due to a favor for outsider versus local clientele. Locally favored services that are not part of chains are based on a different model of service than those that are part of chains, causing different demand for an upkeep brand image and identity.

# # Data

# The variables of interest would be placed in a tabular format where the variables of interest would be placed in columns. Each available food facility found in the city of Compton would constitute a single observation. Variables I would need in order to view possible correlations would be Inspection scores and a food services' distance from highways and freeways. This distance would be calculated through the Google Map tool that measures the distance between points. The city of Compton has two major highways that act as the city’s border. Distances from the establishment in relation to these two landmarks would be represented in as two different variables in their independent column. Additional variables of interest I would look into would include public ratings of an establishment through Yelp as a way of comparing the official Inspection score to general public opinion. This to understand whether populace opinion affects an establishment need to keep up with sanitation. The number of reviews an establishment has collected would be looked into in order to gather information on the popularity of the service. Yelp gives a user the ability to state their city and country of origin. Using this data will give me a comprehensive understanding whether consumers were local or not.
# 
# Variables:
# - Inspection Score
# - Distance from highway A
# - Distance from highway B
# - Yelp Review
# - Yelp Review local demographic
# - Yelp Review outsider demographic
# 

# # Ethics & Privacy

# Data found on the County of Los Angeles Public Health website is open source information available to the public. In order to gather information from Yelp I would need to request to use this information through the Yelp Fusion API or by contacting online customer support on Yelp Fusion. Data used for academic use is Yelp API is acceptable as long as it follows terms and conditions. 
# Usage of reviewer’s location of origin and name will be subject to concerns of privacy. In order to fix those concerns, dataset will not include the reviewer's name. The reviewer's name will be replaced by an assignation number that will represent a separate individual and an independent observation. Location associated with reviewer will be conserved for experiment being as it is the focus of interest. Age and sex for a reviewer will not be considered in dataset due to it including components not deemed important in restaurant’s overall evaluation. This is also done with the interest of save guarding an individual’s identity. No other information regarding the individual will be collected unless they become prevalent. Further concerns for privacy will be evaluated and considered for omission in dataset.
# 

# In[ ]:




