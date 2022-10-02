# Moonquake Emergency Warning System (MEWS)

![MEWS](https://github.com/calvpang/FMS_Moonquake/blob/main/Images/MEWS_logo/MEWS%20logo.png?raw=true)

This repository contains the Flat Moon Society's submission for the NASA Space Apps 2022 - "Make a Moonquake Map!" Challenge.

[MEWS Demo](https://calvpang.github.io/MEWS_Site/posts/2022-10-02-MEWS/)

[MEWS Video](https://youtu.be/ryLAF4xHzWs)

---
## High-Level Project Summary
When they explored the Moon, NASA’s Apollo astronauts left behind several instruments to collect geophysical data near each Apollo landing site. Your challenge is to develop an app that plots the seismic data these instruments transmitted back to Earth on an interactive 3-D globe.

Systems that can provide emergency alerts on Earth have been converging from regional detection sites, into larger systems that can be accessed on a country and global scale. However, this has been a slow process, as even within a country, the sensors used between regions and the way the data is collected varies. As humanity begins to create a base on the moon, which will then be used to expand to other planets, a single, consistent database for storing and using moon data will be essential for timely and safe building of structures and also for creating emergency warning systems for people working on the moon. Our project aims to develop this database and demonstrate its utility.

## Detailed Project Description
Our project consists of three main components:
Database for the storage and dissemination of moonquake data;
A [visualisation tool](https://calvpang.github.io/MEWS_Site/posts/2022-10-02-MEWS/) to demonstrate the utility of the data as it would be used in one of our apps; and
The [Moonquake Emergency Warning System](https://flatmoonsociety.my.canva.site/) (MEWS), a three tiered product that provides targeted information to educators, analysts, and remote operators.

The MEWS database is designed to be a single point of contact for all Moon related environmental data, starting with historical moonquakes as recorded by the NASA Apollo missions from 1969-1977, and with the capacity to ingest data from new sensors as they are deployed on the Moon. The MWAS database will be public for anyone that wants to contribute or download data. Additionally we will offer [three apps](https://flatmoonsociety.my.canva.site/) which are built on top of the database:
- MEWS Education Edition for Everyone (eMEWS) to learn more about the moon and explore in a free, open-source platform.
- MEWS Analytics Platform Edition (MEWS APES) for moon site planners, engineers, SMEs, consultants, space start-ups, risk assessors, and remote operators.
- MEWS Enterprise Edition (MEWSE) for real-time quake and environmental  monitoring on the Moon at an enterprise level.

We used python to load the data and translate the different formats into one common table. We use the plotly library to visualise a height map of the Moon and to overlay it with the different types of events.

During our hack event we made use the following tools:
- GitHub to host our software and serve the interactive Moon app;
- Canva to build and host our sales site, and to create all our animations;
- Final Cut Pro to record, combine, and edit our 30s pitch video;
- Google Docs for collaborative editing and planning;
- Python for the data processing and visualisation;
- OBS Studio to screen capture our interactive content;
- Slack for communication and planning;
- YouTube to host our pitch video.

## Space Agency Data
[NASA Scientific Visualisation Studio - CGI Moon Kit](https://svs.gsfc.nasa.gov/cgi-bin/details.cgi?aid=4720) - The dataset supplied Colour and Displacement Maps assembled from data captured from the Lunar Reconnaissance Orbiter which facilitated the overlaying and rendering of a 3D representation of the moon to which seismic events could be visualised in further detail.

[Apollo Passive Seismic Experiment Expanded Event Catalog](https://pds-geosciences.wustl.edu/missions/apollo/seismic_event_catalog.htm) - The catalogue supplied various datasets containing raw and analysed data regarding lunar seismic events captured from the four seismic stations deployed during the Apollo Passive Seismic Experiment. The datasets typically included event timing, amplitude, quality and classification of seismic sources for the years 1969 to 1977. However, the datasets across the catalogue also featured inconsistent data schemas and esoteric data dictionaries (even for the same authors) which necessitated significant data cleaning and wrangling to conduct scientific analysis, demonstrating a future requirement for the development of an international data standard. For the current project, the team focused on datasets within the catalogue which contained the following features: event timing, event location, event depth and event type.
- gagnepia_2006_catalog
- lognonne_2003_catalog
- nakamura_1979_sm_locations
- nakamura_1983_ai_locations
- nakamura_2005_dm_locations

Pipelines were developed to convert the event times into a consistent format and to reclassify the inconsistent event types into four categories (Deep Moonquakes, Shallow Moonquakes, Meteorite Impacts, Artificial Impacts). The data was suggestive of a cyclical nature of lunar seismic events corresponding to lunar day and night, resulting in an attempt to engineer new features to facilitate more detailed analyses and visualisations of lunar seismic events.

## Hackathon Journey
We started our journey with a solid brainstorming session where we shot for the stars, thinking as big as we could. From here we settled on a theme and scope of work and triaged our ideas based on this. Throughout the weekend we would meet to review progress and modify or remove project components based on the time and data available to us. Discussion with mentors, previous participants, and current teams was often a good way to get an external view on the work we were doing and helped to limit our scope creep.

Our team chose the moonquakes challenge as it allows us to address many of the problems that we commonly see with public data sources. Many people and organisations want to provide access to their data for a variety of reasons. However, there are some common problems that users will encounter when trying to work with these data:
Multiple data sources: There is no single place which hosts all the relevant data. People need to search multiple locations to download or upload data.
Heterogeneous data: Each data source hosts data in a different format, and has different methods for retrieving the data.
Accessibility: Though the data may be available, it can be hard to understand and work with due to lack of visualisation and exploration tools, and data documentation that is written for mission specialists rather than end users.
Lack of interoperability: Individuals looking to use the data will often re-invent solutions that are then not shared with others. When solutions are shared, they do not work with different data sources or with other solutions. 

Overcoming these challenges takes time and effort and will result in much lower engagement with the data. Our project aims to address these issues by providing a single point of engagement for multiple audiences both for the retrieval and exploration of the data, and for the storage of the data.

The duration of the space apps challenge was long enough for us to really sink our teeth into a problem and come up with some great ideas, but also short enough that we didn’t get burnt out or bogged down in small details.

## References
[Create Interactive Globe + Earthquake Plot in Python with Plotly, Ryota Kiuchi, 2020](https://towardsdatascience.com/create-interactive-globe-earthquake-plot-in-python-b0b52b646f27) 

[Apollo Passive Seismic Experiment Expanded Event Catalogue, Renee Weber, 2020](https://pds-geosciences.wustl.edu/missions/apollo/seismic_event_catalog.htm)

[CGI Moon Kit, Ernie Wright, 2019](https://svs.gsfc.nasa.gov/cgi-bin/details.cgi?aid=4720) 
