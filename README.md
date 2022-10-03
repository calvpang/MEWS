# Moonquake Emergency Warning System (MEWS)

![MEWS](https://github.com/calvpang/FMS_Moonquake/blob/main/Images/MEWS_logo/MEWS%20logo.png?raw=true)

This repository contains the Flat Moon Society's [submission](https://2022.spaceappschallenge.org/challenges/2022-challenges/moonquake-map/teams/flat-moon-society-aus/project) for the NASA Space Apps 2022 - "Make a Moonquake Map!" Challenge.

[MEWS Demo](https://calvpang.github.io/MEWS_Site/posts/2022-10-02-MEWS/)

[MEWS Video](https://youtu.be/DOFP5LiE0fs)

---
## High-Level Project Summary
Earth has created systems for earthquake emergency alerts but is limited by the varying data formats and lack of a central database. As humanity begins to create a base on the Moon, which will then be used to expand to other planets, a single, consistent database for storing and using moonquake data will be essential for the timely and safe building of structures, and for creating emergency warning systems for people and assets on the Moon. Our project aims to develop this centralized database to effectively and correctly map moonquake data, and demonstrate how the data can be visualised for outreach and advanced analysis to support our exploration and establishment on the Moon.

## Detailed Project Description
### WHAT DOES OUR PROJECT DO?

Our [project](https://github.com/calvpang/MEWS) consists of three main components:

1. A centralized and standardized database for the storage and dissemination of moonquake data;
2. A [visualisation tool](https://calvpang.github.io/MEWS_Site/posts/2022-10-02-MEWS/) of the 3D moonquake map that we developed to demonstrate the utility of the data as it would be used in one of our apps; and
3. The [Moonquake Emergency Warning System (MEWS)](https://flatmoonsociety.my.canva.site/), the application of our3D moonquake mapping solution in the form of a three-tiered product that provides targeted information to educators, analysts, and remote operators.

**MEWS Database**: The MEWS database is designed to be a single point of contact for all moonquake-related data. Historical moonquakes as recorded by the NASA Apollo missions from 1969-1977 has already been integrated into the MEWS database, and the framework is now set to ingest data from new sensors as they are deployed on the Moon. The MEWS database will be public and open-source for anyone that wants to contribute or download moonquake data.

**3D Moonquake Map**: Moonquake locations are plotted onto a 3D moon surface, and we incorporated elevation mapping of the moon so users can visualize terrain height alongside quake occurrences. We added filters to the visualization to allow users to cycle through the different types of events (deep moonquakes, shallow moonquakes, meteorites, artificial impacts such as the impact from the crafts during moon landings).

**MEWS Apps**: As part of our 3D moonquake mapping solution, we will offer [three apps](https://flatmoonsociety.my.canva.site/) which are built on top of the MEWS database:

- MEWS Education Edition for Everyone (eMEWS) to learn more about the Moon and explore in a free, open-source platform;
- MEWS Analytics Platform Edition (MEWS APE) for moon site planners, engineers, SMEs, consultants, space start-ups, risk assessors, and remote operators; and
- MEWS Enterprise Edition (MEWSE) for real-time quake and environmental monitoring on the Moon at an enterprise level.

To learn more about the MEWS mapping and app solutions, view our website [here](https://flatmoonsociety.my.canva.site/)

### SOLUTION PROCESS, CODING LANGUAGES, TOOLS AND RESOURCES FOR OUR PROJECT

**Data preparation**: We used python to load the data and translate the different formats into one common table. The process of data engineering, consolidating disparate sources of data with inconsistent formats and missing values, data wrangling to clean and transform the data was a challenge and consumed a hefty portion of our allocated time. 

**3D moonquake map build**: We use the plotly library to visualise a height map of the Moon and to overlay it with the moonquake locations as well as the different types of events.

**MEWS app designs**: We created design mock-ups of our three MEWS apps that will appeal to the three distinct target audience groups (education, analysts and remote monitoring), and created a marketing website to showcase these solutions.

**Resources and tools**: During the hackathon, we made use the following tools:
- GitHub to host our software and serve the interactive Moon app;
- Quarto to publish our interactive Moon app;
- Canva to build and host our marketing website, and to create all our design collateral and animations;
- Google Docs for project management, content development, collaborative editing and planning;
- Python for the data processing and visualisation;
- Slack for communication and planning;
- OBS Studio to screen capture our interactive content;
- Final Cut Pro to record, combine, and edit our 30s pitch video;
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
We started our journey with a solid brainstorming session where we shot for the stars, thinking as big as we could. From here we settled on a theme and scope of work and triaged our ideas based on this. 

To get our creative juices flowing, we spent some time deciding on a team name. We settled on ‘Flat Moon Society (AUS)’ for its juxtaposition with the science team behind it! With the tagline of “We've forgotten the crackers!” in reference to Wallace and Gromit discovering that the moon is in fact made of cheese, we designed our team logo with a flat moon made out of cheese. Our moon design was generated by DALLE 2, the artificial intelligence design engine and we designed team t-shirts to wear during the hackathon. Our intention was to generate interest, conversation and amusement, an ice breaker with the wider cohort and opportunity to show a lighter side to our team while we worked on a very serious and real-world challenge.

Throughout the weekend we would meet to review progress and modify or remove project components based on the time and data available to us. Discussion with mentors, previous participants, and other current teams was often a good way to get an external view on the work we were doing and helped to limit our scope creep.

Our team chose the **moonquakes challenge** as it allows us to address many of the problems that we commonly see with public data sources. Many people and organisations want to provide access to their data for a variety of reasons. However, there are some common problems that users will encounter when trying to work with these data:
- Multiple data sources: There is no single place which hosts all the relevant data. People need to search multiple locations to download or upload data.
- Heterogeneous data: Each data source hosts data in a different format, and has different methods for retrieving the data.
- Accessibility: Though the data may be available, it can be hard to understand and work with due to lack of visualisation and exploration tools, and data documentation that is written for mission specialists rather than end users.
- Lack of interoperability: Individuals looking to use the data will often re-invent solutions that are then not shared with others. When solutions are shared, they do not work with different data sources or with other solutions.

Overcoming these challenges takes time and effort and will result in a much lower engagement with the data. Our project aims to address these issues by providing a single point of engagement for multiple audiences both for the retrieval and exploration of the data, and for the storage of the data.

Choosing a Moon challenge also allowed us to explore the opportunities in supporting remote sensing and operations initiatives that are so close to home. With Western Australia being one of the world's leading regions for remote operations capability and experience, we thought it would make an interesting and relevant challenge for us to undertake.

The duration of the space apps challenge was long enough for us to really sink our teeth into a problem and come up with some great ideas, but also short enough that we didn’t get burnt out or bogged down in small details. The hackathon was a terrific opportunity to work together as a team, meet other space enthusiasts and expand our network locally.

We would like to take this opportunity to thank the organisers of this year's NASA International Space Apps Challenge, the mentors, and participants - it really was a great experience for us and our first hackathon experience.

## References
[Create Interactive Globe + Earthquake Plot in Python with Plotly, Ryota Kiuchi, 2020](https://towardsdatascience.com/create-interactive-globe-earthquake-plot-in-python-b0b52b646f27) 

[Apollo Passive Seismic Experiment Expanded Event Catalogue, Renee Weber, 2020](https://pds-geosciences.wustl.edu/missions/apollo/seismic_event_catalog.htm)

[CGI Moon Kit, Ernie Wright, 2019](https://svs.gsfc.nasa.gov/cgi-bin/details.cgi?aid=4720)
