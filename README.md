<h1> Case Study: How Does a Bike-Share Navigate Speedy Success? </h1>

## Table of Contents
<!-- AUTO-GENERATED-CONTENT:START (TOC:collapse=true&collapseText="Click to expand") -->
<details>
<summary>"Click to expand"</summary>

- [Introduction](#Introduction)
- [Scenario](#Scenario)
- [Characters and teams](#Characters)
- [About the company](#AboutCompany)
- [QUESTION](#AnaliseQuestions)
- [Deliverables](#Deliverables)
  - [A clear statement of the business task](#ClearStatement)
  - [A description of all data sources used](#Sources)
  - [Documentation of any cleaning or manipulation of data](#Manipulation)
  - [A summary of my analysis](#Summary)
  - [Supporting visualizations and key findings](#KeyFindings)
  - [My top three recommendations based on my analysis](#Recommendations)

</details>
<!-- AUTO-GENERATED-CONTENT:END -->


<h2 id="Introduction"> Introduction </h2>
&nbsp; &nbsp; &nbsp; In this case study, I'll work for a fictional company, Cyclistic, and meet different characters and team members. In order to
answer the key business questions, following the steps of the data analysis process: 

* Ask
* Prepare
* Process 
* Analyze
* Share
* Act 

<h2 id="Scenario"> Scenario </h2>
  
&nbsp; &nbsp; &nbsp; As a data analyst working in the marketing analyst team at Cyclistic, a bike-share company in Chicago. The director
of marketing believes the company’s future success depends on maximizing the number of annual memberships. Therefore,
our team wants to understand how casual riders and annual members use Cyclistic bikes differently. From these insights,
our team will design a new marketing strategy to convert casual riders into annual members. But first, Cyclistic executives
must approve mine recommendations, so they must be backed up with compelling data insights and professional data
visualizations.

<h2 id="Characters"> Characters and teams </h2>

* Cyclistic: A bike-share program that features more than 5,800 bicycles and 600 docking stations. Cyclistic sets itself
apart by also offering reclining bikes, hand tricycles, and cargo bikes, making bike-share more inclusive to people with
disabilities and riders who can’t use a standard two-wheeled bike. The majority of riders opt for traditional bikes; about
8% of riders use the assistive options. Cyclistic users are more likely to ride for leisure, but about 30% use them to
commute to work each day.
* Lily Moreno: The director of marketing and your manager. Moreno is responsible for the development of campaigns
and initiatives to promote the bike-share program. These may include email, social media, and other channels.
* Cyclistic marketing analytics team: A team of data analysts who are responsible for collecting, analyzing, and
reporting data that helps guide Cyclistic marketing strategy. You joined this team six months ago and have been busy
learning about Cyclistic’s mission and business goals — as well as how you, as a junior data analyst, can help Cyclistic
achieve them.
* Cyclistic executive team: The notoriously detail-oriented executive team will decide whether to approve the
recommended marketing program.

<h2 id="AboutCompany"> About the company </h2>

&nbsp; &nbsp; &nbsp; In 2016, Cyclistic launched a successful bike-share offering. Since then, the program has grown to a fleet of 5,824 bicycles that
are geotracked and locked into a network of 692 stations across Chicago. The bikes can be unlocked from one station and
returned to any other station in the system anytime.<br>

&nbsp; &nbsp; &nbsp; Until now, Cyclistic’s marketing strategy relied on building general awareness and appealing to broad consumer segments.
One approach that helped make these things possible was the flexibility of its pricing plans: single-ride passes, full-day passes,
and annual memberships. Customers who purchase single-ride or full-day passes are referred to as casual riders. Customers
who purchase annual memberships are Cyclistic members.<br>

&nbsp; &nbsp; &nbsp; Cyclistic’s finance analysts have concluded that annual members are much more profitable than casual riders. Although the
pricing flexibility helps Cyclistic attract more customers, Moreno believes that maximizing the number of annual members will
be key to future growth. Rather than creating a marketing campaign that targets all-new customers, Moreno believes there is a
very good chance to convert casual riders into members. She notes that casual riders are already aware of the Cyclistic
program and have chosen Cyclistic for their mobility needs.<br>

&nbsp; &nbsp; &nbsp; Moreno has set a clear goal: Design marketing strategies aimed at converting casual riders into annual members. In order to
do that, however, the marketing analyst team needs to better understand how annual members and casual riders differ, why
casual riders would buy a membership, and how digital media could affect their marketing tactics. Moreno and her team are
interested in analyzing the Cyclistic historical bike trip data to identify trends.

<h2 id="AnaliseQuestions"> QUESTION </h2>

### How do annual members and casual riders use Cyclistic bikes differently?

<h2 id="Deliverables"> Deliverables </h2>

1. [A clear statement of the business task](#ClearStatement) 
2. [A description of all data sources used](#Sources)
3. [Documentation of any cleaning or manipulation of data](#Manipulation)
4. [A summary of my analysis](#Summary)
5. [Supporting visualizations and key findings](#KeyFindings)
6. [My top three recommendations based on my analysis](#Recommendations)

<h2 id="ClearStatement"> A clear statement of the business task </h2>

<h3> Questions </h3>

* What is the problem i'm are trying to solve?
  * A: Cyclistic’s finance analysts have concluded that annual members are much more profitable than casual riders. Although the pricing flexibility helps Cyclistic attract more customers. I'm helping the Marketing team, getting insights analyzing the Cyclistic historical bike trip data to identify trends and responding the question: How do annual members and casual riders use Cyclistic bikes differently? So they can use data to make Data-Driven decisions. 
  
* How can my insights drive business decisions?
  * A: 


<h2 id="Sources"> A description of all data sources used </h2>

<h3> Questions </h3>

* Where i get this data?
  * I get this data from https://divvy-tripdata.s3.amazonaws.com/index.html . Cyclistic is a fictional company, downloaded last 12 months of data.

* How is the data organized?
  * A: The excel files are divided by months each one contains columns for ride_id, rideable_type, started_at, ended_at, start_station_name, start_station_id, end_station_name, end_station_id, start_lat, start_lng, end_lat, end_lng and member_casual.
  

<h2 id="Manipulation"> Documentation of any cleaning or manipulation of data </h2>

<h3> Questions </h3>

* What tools I choose and why?
  * A:I choose python to use Pandas.
  
* What steps I did to ensure that my data is clean?
   * A: First I import all the files into a DF:
   
   ``` 
   
   df = pd.concat([pd.read_csv(one_filename, 
                            usecols=['ride_id', 
                                     'rideable_type', 
                                     'started_at', 
                                     'ended_at', 
                                     'start_station_name', 
                                     'start_station_id', 
                                     'end_station_name', 
                                     'end_station_id', 
                                     'member_casual'])
    for one_filename in glob.glob('cases/divvy-tripdata*.csv')]) 
    
    ```
   Then I use a function to drop all the null values:
   
   ```
      
      df = df.dropna()
   
   ```
   
<h2 id="Summary"> A summary of this analysis </h2> 

<h3> Questions </h3>

* How I organize my data to perform analysis on it?
* Has my data been properly formatted?
* What surprises did I discover in the data?
* What trends or relationships did I find in the data?
* How will these insights help answer the business questions?

<h3> Key tasks </h3>

1. Aggregate my data so it’s useful and accessible.
2. Organize and format the data.
3. Perform calculations.
4. Identify trends and relationships.


<h2 id="KeyFindings"> Supporting visualizations and key findings </h2>

<h3> Questions </h3>

* Was this analise able to answer the question of how annual members and casual riders use Cyclistic bikes differently?
* What story does this data tell?
* How do my findings relate to the original question?
* Who is my audience? What is the best way to communicate with them?
* Can data visualization help me share my findings?
* Is my presentation accessible to my audience?

<h3> Key tasks </h3>

1. Determine the best way to share your findings.
2. Create effective data visualizations.
3. Present your findings.
4. Ensure your work is accessible

<h2 id="Recommendations"> My top three recommendations based on this analysis </h2>

<h3> Questions </h3>

* Final conclusion based on this analysis?
* How could my team and business apply those insights?
* What next steps me or my stakeholders should take based on my findings?
