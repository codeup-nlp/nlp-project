<center><h1>Natural Language Processing - Github Programming Language Prediction</center>
    
> - Google Slides: https://docs.google.com/presentation/d/1uqp20l36bEUZK94Rtpab25Aq80QhSghQ1nXXIlHlKcU/edit#slide=id.g12c040e4cd4_2_0

<a name ='toc'></a>
# Table of Contents 
1. [Project Planning](#project_planning)
    1. [Project Objectives](#project_objectives)
    2. [Business Goals](#business_goals)
    3. [Audience](#audience)
    4. [Deliverables](#deliverables)
2. [Executive Summary](#exe_sum)
    1. [Goals](#goals)
    2. [Findings](#findings)
3. [Acquire Data](#acquire)
    1. [Data Dictonary](#data_dict)
    2. [Acquire Takeaways](#acquire_takeaways)
4. [Prepare Data](#prep_data)
    1. [Distributions](#distributions)
    2. [Prepare Takeaways](#prepare_takeaways)
5. [Data Exploration](#explore)
    1. [Explore Takeaways](#explore_takeaways)
    2. [Hypothesis](#hypothesis)
6. [Modeling & Evaluation](#modeling)
    1. [Modeling Takeaways](#model_takeaways)
6. [Project Delivery](#delivery)
    1. [Conclusions & Next Steps](#conclusions_next_steps)
    2. [Project Replication](#replication)

<hr style="border-top: 10px groove tan; margin-top: 5px; margin-bottom: 5px"></hr>

<a name='project_planning'></a>
## Project Planning
✓ 🟢 **Plan** ➜ ☐ _Acquire_ ➜ ☐ _Prepare_ ➜ ☐ _Explore_ ➜ ☐ _Model_ ➜ ☐ _Deliver_

<a name='project_objectives'></a>
### Project Objectives 
> - For this project our team is to build a model that can predict what programming language a repository will be, given the text of a README file.
> - In addition to this, we are to build a well-documented jupyter notebook that contains the analysis of this prediction.
> - Any abstracted modules that are created to make the presentation more clean, during the acquistion and preparation of data.
> - Finally, we are to build a few Google slides to present toward a general audience that summarizes the findings within the project, with visualizations.

<a name='business_goals'></a>
### Business Goals 
> - Build a model that will scrape the README file from a Github repository.
> - Prepare, explore and clean the data so that it can be input into modeling.
> - Utilizie Term Frequence Inverse Document Frequency (TFIDF) and a combination of the two features to assist with the modeling.
> - Document all these steps thoroughly.

<a name='audience'></a>
### Audience 
> - General population and individuals without specific knowledge or understanding of the topic or subject.

<a name='deliverables'></a>
### Deliverables
> - A clearly named final notebook. This notebook will contain more detailed processes other than noted within the README and have abstracted scripts to assist on readability.
> - A README that explains what the project is, how to reproduce the project, and notes about the project.
> - A Python module or modules that automate the data acquisition and preparation process. These modules should be imported and used in your final notebook.

<div style="text-align: right"><a href='#toc'>Table of Contents</a></div>
<hr style="border-top: 10px groove tan; margin-top: 1px; margin-bottom: 1px"></hr>

<a name='exe_sum'></a>
## Executive Summary
> - 125 repository README files were scraped from Github.
> - Javascript files were analyzed and compared against all other README files.
> - Our model performed well, identifying Javascript, HTML, C++, Python, and Jupyter Notebook repositories with an accuracy of over 46%.

<a name='goals'></a>
### Goals
> - Build a model that can predict what programming language a repository will be, given the text of a README file.

<a name='findings'></a>
### Findings
> - Findings here.git 

<div style="text-align: right"><a href='#toc'>Table of Contents</a></div>
<hr style="border-top: 10px groove tan; margin-top: 1px; margin-bottom: 1px"></hr>

<a name='acquire'></a>
## Acquire Data
✓ _Plan_ ➜ 🟢 **Acquire** ➜ ☐ _Prepare_ ➜ ☐ _Explore_ ➜ ☐ _Model_ ➜ ☐ _Deliver_
> - We divided our four man team up to look for 25 repositories each. We also added other repositories based of found programming language. 
> - Once we had our destinations, we scraped the README text and all the programming languages.
> - We began exploration once data was ready

<a name='data_dict'></a>
### DataFrame Dict

| Feature           | Datatype                         | Definition                                                 |
|:------------------|:---------------------------------|:-----------------------------------------------------------|
| prog_lang         | 5728 non-null: object           | The predominant programming language used in the repository|
| original          | 5728 non-null: object           | Original readme content of the scraped repository          |
| cleaned           | 5728 non-null: object           | The cleaned version of the readme                          |
| label             | 5728 non-null: object           | The programming language label; the target variable
| stemmed           | 5728 non-null: object           | The cleaned, stemmed version of the readme                 |
| lemmatized        | 5728 non-null: object           | The cleaned, lemmatized version of the readme              |

<a name='acquire_takeaways'></a>
### Takeaways from Acquire:
> - Target Variable: label
> - This dataframe currently has 100+ rows and 6 columns.
> - There are 0 missing values.
> - All columns are string object types.

<div style="text-align: right"><a href='#toc'>Table of Contents</a></div>
<hr style="border-top: 10px groove tan; margin-top: 1px; margin-bottom: 1px"></hr>

<a name='prep_data'></a>
## Prepare Data
✓ _Plan_ ➜ ✓ _Acquire_ ➜ 🟢 **Prepare** ➜ ☐ _Explore_ ➜ ☐ _Model_ ➜ ☐ _Deliver_

> - Converted all characters to lowercase, 
> - Normalized unicode characters, 
> - Encoded into ascii byte strings and ignored unknown characters,
> - Decoded into usable UTF-8 strings,
> - Removed anything that was not either a letter, number, or whitespace,
> - tokenized the data.
> - Then we created both stemmed and lemmatized versions of the cleaned data.
> - Finally, we split the data into train and test sets.

<a name='prepare_takeaways'></a>
### Prepare Takeaways

> - The data was cleaned and is ready for exploration on the train data set.
                     
<div style="text-align: right"><a href='#toc'>Table of Contents</a></div>
<hr style="border-top: 10px groove tan; margin-top: 1px; margin-bottom: 1px"></hr>


<a name='explore'></a>
## Explore Data
✓ _Plan_ ➜ ✓ _Acquire_ ➜ ✓ _Prepare_ ➜ 🟢 **Explore** ➜ ☐ _Model_ ➜ ☐ _Deliver_

> - Utilizing a class, we explored the data and tested several hypotheses.
> - We compared word, and bigram counts and created visualizations.
> - We created word clouds for quick visualization of the most common words.

<a name='explore_takeaways'></a>
### Explore Takeaways

> - The top 5 most common words in Javascript readme files occur in Javascript files much more frequently than all other readme files.
> - Javascript sentiment analysis compound scores tend to be more positive than all Non-Javascript, while all Non-Javascript tend to be more neutral than Javascript.

<div style="text-align: right"><a href='#toc'>Table of Contents</a></div>
<hr style="border-top: 10px groove tan; margin-top: 1px; margin-bottom: 1px"></hr>


<a name='modeling'></a>
## Modeling & Evaluation
✓ _Plan_ ➜ ✓ _Acquire_ ➜ ✓ _Prepare_ ➜ ✓ _Explore_ ➜ 🟢 **Model** ➜ ☐ _Deliver_

> - Created a class to vectorize and create, fit, and evaluate models on in and out-of-sample datasets.
> - Utilized a class method using cross-validate to fit and evaluate models on a specified number of K-Folded splits, garnering an average validate accuracy score for each classifier type.
> - Chose the best model from cross-validation and evaluated the accuracy on out-of-sample test data.

#### K-Fold and Cross-validation References:
> - For more information on the sklean dummy classifier, visit https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html
> - For information on Decision Tree model, visit https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html

<a name='model_takeaways'></a>
### Modeling Takeaways

> - Baseline accuracy of 29.0% based on sklearn dummy classifer.
> - Got best performance from not 'top five classifier'.
> - The best performing model was the Desicion Tree with a accuracy of 46.0%.
> - Using that model, we achived a 17.0% increae over baseline.

<div style="text-align: right"><a href='#toc'>Table of Contents</a></div>
<hr style="border-top: 10px groove tan; margin-top: 1px; margin-bottom: 1px"></hr>

<a name='delivery'></a>
## Project Delivery
✓ _Plan_ ➜ ✓ _Acquire_ ➜ ✓ _Prepare_ ➜ ✓ _Explore_ ➜ ✓ _Model_ ➜ 🟢 **Deliver**



<a name='conclusions_next_steps'></a>
### Conclusion and Next Steps
> - Acquire a larger random sample of github repositories for increased accuracy on model
> - Identify different features to further access README file
    - graphic or visualization in the README
    - Coding example in the README

<a name='replication'></a>
### Project Replication
> - Download the `acquire.py`, `prepare.py`, and `model.py` modules to your working directory.
> - Download the all files from dataset which can be found in the base_acquire.py
> - Run the `final_report.ipynb` Juypter Notebook.


<div style="text-align: right"><a href='#toc'>Table of Contents</a></div>
<hr style="border-top: 10px groove tan; margin-top: 1px; margin-bottom: 1px"></hr>
