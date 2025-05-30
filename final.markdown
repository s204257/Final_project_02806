---
layout: page
title: A Collision Course Investigating Traffic Safety in New York City
permalink: /FinalAssignment/
---

## Introduction
In a dense, ever-changing city like New York, traffic is not just a logistical challenge, it reflects the complex interplay of infrastructure, public policy, individual behavior, and unpredictable events. This project analyzes more than a decade of NYPD collision records, offering a window into how traffic safety has changed over time. From the effects of Vision Zero (NYC DOT, 2014) to the dramatic disruptions of the COVID-19 pandemic, we examine how, when, and where accidents happen, and what that reveals about the city in motion.

## Long-Term Trends in Traffic Collisions
An analysis of NYPD data from 2013 to 2024 reveals a steady increase in reported traffic collisions, peaking in 2015 with over 85,000 incidents. Post-2015, collision numbers stabilized until a significant drop in 2020, coinciding with pandemic-induced lockdowns and reduced traffic volumes. Although there has been a gradual uptick since 2021, collision rates remain below pre-pandemic levels.

![Crashes pr. year](motor_vehicle_collisions_by_year.png)

Between 2013 and 2019, traffic collisions in NYC rose steadily, peaking in 2015 with over 85,000 recorded incidents (NYPD, 2024). The trend plateaued thereafter, until 2020, when the pandemic triggered a sharp decline. That year saw an abrupt drop in overall traffic volume as lockdowns and remote work transformed mobility patterns.

Interestingly, collision rates did not fully rebound after restrictions lifted. Instead, post-2020 figures suggest a subtle but lasting reduction in total crashes, raising questions about whether urban travel has permanently changed.


## Tracking Injuries and Fatalities Over Time

![Injuries and fatalities](traffic_incidents_overview.png)

Injury trends followed a similar trajectory to total collisions, with rising numbers through 2018, followed by a drop in 2020. At their peak, over 22,000 people were injured annually in NYC traffic crashes. This began to fall after 2019, consistent with citywide reductions in vehicle use and pedestrian activity (NYC DOT, 2021). However interestingly, even though the yearly number of collisions stayed down after 2020, the number of injuries quickly increased after 2020.  

Fatalities, however, did not follow suit. Despite fewer collisions, deaths remained high through the pandemic years. According to the NHTSA (2021), similar trends were observed nationwide: lower traffic volumes led to more speeding and higher-severity crashes. In NYC, traffic deaths held steady between 67 and 123 annually, which challenges the assumption that fewer crashes always mean safer roads.

## When Collisions Happen: Patterns by Weekday and Hour
Traffic collisions are deeply influenced by daily rhythms. In 2019, weekday mornings (7–8 AM) and afternoons (3–6 PM) saw the highest concentration of crashes, matching traditional commuting times. These patterns reflect a city moving to a shared beat.

![Collision density](collision_density_2019_2020.png)

In 2020, although the structure of these patterns persisted, the intensity collapsed, which is especially clear in the morning rush hour. Collision density dropped especially in the morning rush hour, which could be visual proof of the pandemic’s impact on urban life. Still, the presence of rush-hour in the afternoon peaks even during lockdowns speaks to the inertia of human routine.


## Geographic Variation: Borough-Level Collisions
Spatial differences within the city also matter. The following map visualizes total crashes by borough for 2019 and 2020.
<iframe src="{{ site.baseurl }}/crashes_by_borough.html" width = "100%" height="500" frameborder="0"></iframe>
Queens and Brooklyn consistently report the highest number of traffic collisions, followed closely by Manhattan. This pattern partly reflects population density and vehicle usage, but geographic size is also a key factor. Queens and Brooklyn are the two of the largest boroughs by area, with extensive road networks, higher car ownership rates, and a significant share of interborough traffic. These structural factors increase exposure and likelihood of vehicle crashes (New York City Department of Transportation, 2020).

In contrast, Staten Island, which is the smallest in terms of population and among the least connected by mass transit, records the fewest collisions. The maps also reveal a marked decrease in crashes in 2020 across all boroughs, aligning with pandemic-related reductions in travel. Yet the spatial distribution of risk remained largely intact, suggesting persistent geographic patterns in traffic behavior.

## Rush Hour Severity: Injuries and Fatalities

A more focused lens on evening rush hours (3 PM to 6 PM) reveals where and when severe outcomes like injuries and fatalities occur. In 2019, intense hotspots are visible throughout Manhattan and Brooklyn during evening peaks, reflecting high congestion and pedestrian activity. In 2020, while overall counts dropped, critical zones remained stable, but mostly around transit hubs and major intersections. These maps highlight the disproportionate severity of certain locations, even during periods of reduced traffic, reinforcing the case for spatially targeted safety interventions.

<iframe src="{{ site.baseurl }}/heatmap.html" width = "100%" height="800" frameborder="0"></iframe>

## Behavioral Contributors to Crashes
Every crash has a cause, and in NYC, the leading one is consistently the same: driver inattention or distraction. According to Vision Zero progress reports, this factor accounts for the largest portion of crashes annually (Vision Zero, 2023). Other behaviors, such as failure to yield, tailgating, and illegal turning, persist as secondary causes.

<iframe src="{{ site.baseurl }}/Interactive_Crashes_by_Contributing_Factor.html" width = "125%" height="600" frameborder="0"></iframe>

Despite the pandemic, the distribution of contributing factors changed very little. The data suggests that while volume dropped, the risk landscape stayed largely intact. The challenge of inattentive driving remains almost unsolved, even when the streets are half-empty.

From the initial plots we also saw, that the number of fatalies increased in 2020 compared to 2019, despite there being half as many crashes. This indicates, that the crashes in 2020 were more serious than the ones in 2019. Given that the streets were half-empty, the opportunity to drive too fast were greater, which is represented in the fact, that the amount of crashes due to "Unsafe Speed" remained roughly the same for 2019 and 2020. 

When looking at the proportion of crashes and their contributing factors, we can see some interesting trends. "Following Too Closely" decreases after 2019, which can be explained by the fewer cars on the streets. The opposite trend is seen both for "Traffic Control Disregarded" and "Unsafe Speed" where the proportion increases after 2019. Again, these type of crashes may be more likely to occur when there are less cars on the streets and thereby less traffic.

<iframe src="{{ site.baseurl }}/Interactive_Crashes_by_Contributing_Factor_Normalized.html" width = "125%" height="600" frameborder="0"></iframe>

Furthermore, it is clear from the number of summons made through the years, that in general, speeding is becoming more frequent. When looking at the amount of summons in total for the years 2019 and 2020 and how many of them are from speeding, the suggested trend is confirmed. This means that even though the total amount of crashes has become smaller, the amount of speeding has become larger, which means the risk of fatalities has also become larger. 

![Summons](summons_analysis_subplots.png)


## A City Still in Motion, but Moving Differently

Over the past decade, traffic in New York City has shifted in unexpected ways. While collisions rose through the mid-2010s, they dropped sharply in 2020, and unlike many other pandemic trends, they haven’t bounced back. As of 2024, crash numbers remain well below pre-pandemic levels, likely due to lasting changes in how people work, commute, and move through the city.

Yet fewer crashes haven’t made streets entirely safer. Fatalities stayed high during the pandemic, and speeding became more common, even with less traffic. Risk didn’t disappear—it changed shape.

Patterns by borough and rush hour remained surprisingly stable, showing that location and timing still play a major role in crash outcomes. And core problems like distracted driving and unsafe speed continue to drive incidents year after year.

New York’s streets have changed, but the need for safety hasn’t. As the city continues to adapt, so must its approach to traffic: with smarter design, focused enforcement, and policies that meet today’s reality, not yesterday’s traffic.

## References 
* City of New York (2014). [Vision Zero Action Plan](https://www.nyc.gov/html/visionzero/pages/home/home.html)
* New York City Department of Transportation. (2020). [New York City Mobility Report](https://portal.311.nyc.gov/kacategory/?id=311-88)
* New York City Police Department [Collisions & Summonses Traffic Data Archive](https://www.nyc.gov/site/nypd/stats/traffic-data/traffic-data-archive.page)
* New York City OpenData. [Motor Vehicle Collisions - Crashes](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/about_data)

## Explainer notebook 

When previewing the notebook on GitHub it is not possible to view the heatmaps, but the rest should be fine. 

* [Explainer notebook on Github](https://github.com/s204257/Final_project_02806/blob/main/Explainer.ipynb)
