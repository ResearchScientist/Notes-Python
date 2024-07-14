# Descriptive

- confidence interval : uncertainty of an estimate
- stat significance : likeliness of not due to randomness

## Measures

Central Tendency
- mean : ave
- median : middle
- mode : most frequent

Dispersion
- range : diff between min and max
- std dev : diff from mean
- variance : ave squared diff from mean
- min
- max

Position
- percentile : 
- quartile : q1=25% , q2=50% , q3=75% of all data

# Inferential

sample predicts population

- parameter : population characteristic
- statistic : sample characteristic
- point estimate : using a statistic to estimate a parameter

- standard error : variability between multiple sample means, high SE indicates means are more spread out from each other
- standard error when only one sample is obtained : (population std dev) / (sqrt(sample size n))

- population proportion : % of members in a population that share a characteristic
- population proportion standard error : (sqrt(%(1-%)))/(sample size n)

- confidence interval : describes uncertainty of an estimate

## Confidence Interval

- identify a sample statistic
    - sample mean
    - % of users
    - margin of error : max expected difference between population parameter and sample statistic
- choose a confidence level
    - likeliness that the true population parameter is within the calculated confidence interval
    - 90% , 95% , 99%
- find the margin of error
    - for 90% , the z score is 1.645
    - for 95% , the z score is 1.96
    - for 99% , the z score is 2.58
    - SE for a mean = (population std dev) / (sqrt(sample size n))
    - SE for a proportion = (sqrt(sample proportion * (1 - sample proportion)))/(sample size n)
    - MoE = (z score) * (SE)
- calculate the interval
    - upper limit = sample mean + margin of error
    - lower limit = sample mean - margin of error
    - upper limit = sample proportion + margin of error
    - lower limit = sample proportion - margin of error
- interpret the interval
    - 95% CI does not mean that 95% of data is within the interval
    - 95% CI does not mean that 95% of all possible sample means are within the interval
    - 95% CI means a 95% likeliness that the true population parameter is within the calculated confidence interval

# Probability

classical = (desired outcome)/(total outcomes)
empirical = (event occurrences)/(total events)

P(A) = event A
P(A') = not event A

complement
P(A') = 1 - P(A)

mutually exclusive events
P(A|B) = P(A) + P(B)

independent events
P(A&B) = P(A) * P(B)

dependent events
P(A&B) = P(A) * P(B given A)
P(B given A) = P(A&B) / P(A)

## Bayes

P(A given B) = (P(B given A) * P(A)) / (P(B))

# Distributions

## Binomial

for discrete data

- n repeated trials
- each trial only has 2 possible outcomes
- each trial hss same probability of success
- each trial is independent

Given
An exact probability of an event happening

Answers
The probability of an event happening n times during a repeated experiment

Examples
coin tosses
customers arriving at a store to either make a purchase or not make a purchase

## Poisson

for discrete data along some duration

- events can be counted
- the mean number of events for a given duration is known
- events are independent

Given 
The average probability of an event happening for a given duration

Answers
The probability that n events can happen during the given period.

Examples
number of orders placed at a restaurant
number of calls to expect during a certain time period

## Gaussian (normal)

for continuous data

- mean at center
- symmetrical around mean
- bell shaped
- total area under curve equals 1

- 68% of data within 1 std dev
- 95% of data within 2 std dev
- 99.7% of data within 3 std dev

- z score , data point's # of std deviations from the population mean
    - 0 : equal to mean
    - pos : above mean
    - neg : below mean

z score = (score-mean)/(std dev)

As sample size n increases , the sample distribution approaches a normal distribution

## Standard Normal

- 1 std dev = 1
- 2 std dev = 2
- 3 std dev = 3

# Sampling

Answers
- how many products do we need to test to determine that they all work
- how to select users for an A/B test
- how to select sample of viewers

## Process

- identify target population
- select sampling frame
- choose sampling method
- determine sample size
- collect sample data

Random Sampling Method

- simple : every population member has an equal chance of being selected
- stratified : divide population into groups and randomly select members from each group
    - allows for ensuring each group is represented
- cluster : divide population into clusters and randomly select some clusters, include all members from those clusters
    - for large and diverse populations with clearly defined subgroups
    - may be difficult to generalize to whole population
- systematic : put all population members in order, choose a random starting point, select members at regular intervals

Non Probability Sampling
not as representative but requires less resources

- convenience : members chosen on ease of availability
    - undercoverage bias , certain groups do not frequent that location
- voluntary response : members volunteer
    - non response bias , certain groups are less likely to respond
    - strong opinions more like to respond
- snowball : participants recruit other participants
    - over representation bias , participants recruit only similar participants
- purposive : participants selected based on purpose of study
    - researcher bias , groups excluded and sample not representative

# Hypothesis Testing

- define null H0 and alternate Ha
    - H0 : assumed to be true , observed data occurs by chance
    - Ha : accepted to be true only with evidence , observed data does not occur by chance
- choose significance level
    - 10%,5%,1% chance of rejecting H0 when it is true
- find p-value
    - probability of finding data equal to or more extreme than observed data when H0 is true
    - choosing a significance level of 3% sets 3% as the threshold for accepting H0 as true , < 3% indicates evidence towards Ha
- reject H0 or fail to reject H0
    - if p < significance level , reject H0
    - if p > significance level , fail to reject H0
    - type 1 error : false pos , reject H0 when H0 true
    - type 2 error : false neg , fail to reject H0 when H0 false

## One Sample Test

Tests if a population parameter (mean,%) is equal to some value.

Example
Average click through rate equal to 1000.

### Z Test (one sample)

Requirements

- random sample from a normal distribution population
- std dev of population is known

Steps

- define H0
- define Ha
    - mean,% != some value
    - mean,% < some value
    - mean,% > some value
- set significance level
- calculate p value
    - z score = (sample mean - population mean)/(population std dev / (sqrt(sample size)))
    - p value is the area under the curve to the left of the z score for left tail test or to the right of the z score for a right tail test
- conclude H0
    - if p value < significance level , reject H0 , there is a statistically significant difference between mean and value
    - if p value > significance level , fail to reject H0 , there is no difference between mean and value

Example

- H0 : ave delivery time is 40 min
- Ha : ave delivery time is < 40 min
- significance level : 5%
- p value : 
    - z score : -2.82 , this is almost 3 std dev below the normal mean
    - p value : 0.23% , this is less than 5%
- H0 : reject H0 and conclude that delivery time < 40 is true

## Two Sample Test

Tests if two population parameters (means,%) are equal to each other.

Requirements

- samples are independent of each other
- each sample's data is randomly drawn from a normal distribution population
- std dev of population is not known
- aim for n > 30

### T Test (two samples)

Compares means between two groups.

Steps

- define H0
- define Ha
    - mean,% != some value
    - mean,% < some value
    - mean,% > some value
- set significance level
- calculate p value
    - t score = (sample mean A - sample mean B)/(sqrt(((std dev sample A)^2/sample size A)+((std dev sample B)^2/sample size B)))
    - p value is the area under the curve both to the left of the z score on the left tail end and to the right of the z score on the right tail end
- conclude H0
    - if p value < significance level , reject H0 , there is a statistically significant difference between both means
    - if p value > significance level , fail to reject H0 , there is no difference between both means

Example

A/B testing
Do users spend more time on new website version or the other.

|sample|Group A|Group B|
|--|--|--|
|n|40|38|
|mean|300s|305s|
|std dev|18.5s|16.7s|

- H0 : users spend same amount of mean time on site A and site B
- Ha : users spend different amounts of mean time on site A and site B
- significance level : 5%
- p value : 
    - t score : -1.25
    - p value : 21.48% , this is > 5%
- H0 : fail to reject H0 and conclude that there is no statistical difference in means between both groups

### Z Test (two samples)

Compares proportions between two populations.

Steps

- define H0
- define Ha
- set significance level
- calculate p value
    - z score = ((sample proportion A) - (sample proportion B))/(sqrt(pooled proportion * (1 - pooled proportion) * ((1/sample size A)+(1/sample size B))))
    - p value is the area under the curve both to the left of the z score on the left tail end and to the right of the z score on the right tail end
- conclude H0
    - if p value < significance level , reject H0 , there is a statistically significant difference between group proportions
    - if p value > significance level , fail to reject H0 , there is no difference between group proportions

Example

User satisfaction.

|sample|Group A|Group B|
|--|--|--|
|n|50|50|
|proportion|67%|57%|

- H0 : there is no difference in the proportion of satisfied users in each group
- Ha : there is a difference in the proportion of satisfied users in each group
- significance level : 5%
- p value : 
    - z score : 1.03
    - p value : 30.3% , this is > 5%
- H0 : fail to reject H0 and conclude that there is no statistical difference in proportions between each group
