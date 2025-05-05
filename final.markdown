---
layout: page
title: A Collision Course: Investigating Traffic Safety in New York City
permalink: /FinalAssignment/
---

## Introduction
In a dense, ever-changing city like New York, traffic is not just a logistical challenge—it reflects the complex interplay of infrastructure, public policy, individual behavior, and unpredictable events. This project analyzes more than a decade of NYPD collision records, offering a window into how traffic safety has changed over time. From the effects of Vision Zero (NYC DOT, 2014) to the dramatic disruptions of the COVID-19 pandemic, we examine how, when, and where accidents happen—and what that reveals about the city in motion.

## Long-Term Trends in Traffic Collisions
An analysis of NYPD data from 2013 to 2024 reveals a steady increase in reported traffic collisions, peaking in 2015 with over 85,000 incidents. Post-2015, collision numbers stabilized until a significant drop in 2020, coinciding with pandemic-induced lockdowns and reduced traffic volumes. Although there has been a gradual uptick since 2021, collision rates remain below pre-pandemic levels.

![Crashes pr. year](motor_vehicle_collisions_by_year.png)

Between 2013 and 2019, traffic collisions in NYC rose steadily, peaking in 2015 with over 85,000 recorded incidents (NYPD, 2024). The trend plateaued thereafter—until 2020, when the pandemic triggered a sharp decline. That year saw an abrupt drop in overall traffic volume as lockdowns and remote work transformed mobility patterns 

Interestingly, collision rates did not fully rebound after restrictions lifted. Instead, post-2020 figures suggest a subtle but lasting reduction in total crashes, raising questions about whether urban travel has permanently changed.


## Tracking Injuries and Fatalities Over Time

![Injuries and fatalities](traffic_incidents_overview.png)

Injury trends followed a similar trajectory to total collisions, with rising numbers through 2018, followed by a drop in 2020. At their peak, over 22,000 people were injured annually in NYC traffic crashes. This began to fall after 2019, consistent with citywide reductions in vehicle use and pedestrian activity (NYC DOT, 2021). However interestingly, even though the yearly number of collisions stayed down after 2020, the number of injuries quickly increased after 2020.  

Fatalities, however, did not follow suit. Despite fewer collisions, deaths remained high through the pandemic years. According to the NHTSA (2021), similar trends were observed nationwide: lower traffic volumes led to more speeding and higher-severity crashes. In NYC, traffic deaths held steady between 67 and 123 annually—challenging the assumption that fewer crashes always mean safer roads.

## When Collisions Happen: Patterns by Weekday and Hour
Traffic collisions are deeply influenced by daily rhythms. In 2019, weekday mornings (7–8 AM) and afternoons (3–6 PM) saw the highest concentration of crashes, matching traditional commuting times. These patterns reflect a city moving to a shared beat.

![Collision density](collision_density_2019_2020.png)

In 2020, although the structure of these patterns persisted, the intensity collapsed, which is especially clear in the morning rush hour. Collision density dropped especially in the morning rush hour — visual proof of the pandemic’s impact on urban life. Still, the presence of rush-hour in the afternoon peaks even during lockdowns speaks to the inertia of human routine.

## Behavioral Contributors to Crashes
Every crash has a cause, and in NYC, the leading one is consistently the same: driver inattention or distraction. According to Vision Zero progress reports, this factor accounts for the largest portion of crashes annually (Vision Zero, 2023). Other behaviors—such as failure to yield, tailgating, and illegal turning—persist as secondary causes.

<iframe src="{{ site.baseurl }}/Interactive_Crashes_by_Contributing_Factor.html" width = "100%" height="500" frameborder="0"></iframe>

Despite the pandemic, the distribution of contributing factors changed very little. The data suggests that while volume dropped, the risk landscape stayed largely intact. The challenge of inattentive driving remains unsolved—even when the streets are half-empty.

## Geographic Variation: Borough-Level Collisions
Spatial differences within the city also matter. The following map visualizes total crashes by borough for 2019 and 2020.
<iframe src="{{ site.baseurl }}/crashes_by_borough.html" width = "100%" height="500" frameborder="0"></iframe>
In Queens and Brooklyn consistently report the highest number of traffic collisions, followed closely by Manhattan. This pattern partly reflects population density and vehicle usage, but geographic size is also a key factor. Queens and Brooklyn are the two of the largest boroughs by area, with extensive road networks, higher car ownership rates, and a significant share of interborough traffic. These structural factors increase exposure and likelihood of vehicle crashes (New York City Department of Transportation, 2020).

In contrast, Staten Island — the smallest in terms of population and among the least connected by mass transit — records the fewest collisions. The maps also reveal a marked decrease in crashes in 2020 across all boroughs, aligning with pandemic-related reductions in travel. Yet the spatial distribution of risk remained largely intact, suggesting persistent geographic patterns in traffic behavior.

## Rush Hour Severity: Injuries and Fatalities

A more focused lens on evening rush hours (3 PM to 6 PM) reveals where and when severe outcomes like injuries and fatalities occur. In 2019, intense hotspots are visible throughout Manhattan and Brooklyn during evening peaks, reflecting high congestion and pedestrian activity. In 2020, while overall counts dropped, critical zones remained — notably around transit hubs and major intersections. These maps highlight the disproportionate severity of certain locations, even during periods of reduced traffic, reinforcing the case for spatially targeted safety interventions.

<iframe src="{{ site.baseurl }}/heatmap.html" width = "100%" height="800" frameborder="0"></iframe>

## References 
City of New York (2014). Vision Zero Action Plan. Retrieved from https://www.nyc.gov/html/visionzero/pages/home/home.html
New York City Department of Transportation. (2020). New York City Mobility Report. https://portal.311.nyc.gov/kacategory/?id=311-88
