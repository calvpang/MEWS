# Moonquake Emergency Warning System (MEWS)

![MEWS](https://github.com/calvpang/FMS_Moonquake/blob/main/Images/MEWS_logo/MEWS%20logo.png?raw=true)

This repository contains the Flat Moon Society's submission for the NASA Space Apps 2022 - "Make a Moonquake Map!" Challenge.

[MEWS Demo](https://calvpang.github.io/MEWS_Site/posts/2022-10-02-MEWS/)

[MEWS Video](https://youtu.be/wsJTLDNWOQ8)

---
## High-Level Project Summary

## Detailed Project Description

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

## References
