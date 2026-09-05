# EQ-Graph

A research knowledge graph of EuroQol-funded projects and their publications, connecting projects and people to studies, instruments, methods, findings, limitations, and research products. This repository contains two parts: a research workflow that builds a knowledge graph and a website that presents the results.

## Graph creation

The workflow includes code, AI prompts, and development records for these steps:

1. **Ontology creation:** Define and test the record types and relationships used in the graph.
2. **Publication search:** Find papers using project records, researcher profiles, and funding information.
3. **Screening:** Use AI to screen abstracts and assess full texts for EuroQol support or project links.
4. **Extraction:** Use AI to record study details, methods, findings, and limitations.
5. **Graph construction:** Combine records in a database and check structure and links against research questions.

The [method](docs/METHOD.md) explains the workflow, inclusion criteria, and known limits. The [results](docs/RESULTS.md) report the counts and checks at each stage.

The main files are:

| Location | Contents |
|---|---|
| [Ontology development](pilot/ontology-development-v4/README.md) | Data definitions, vocabulary, and tests |
| [Development records](archive/README.md) | Earlier designs, review rounds, and trials |
| [Input](input/README.md) | EuroQol project records |
| [Pipeline](pipeline/README.md) | Publication search, screening, full-text retrieval, and extraction code |
| [Scripts](scripts/README.md) | Database construction, checks, data export, and analysis code |

## Website

The [website](https://eq-graph.abundanceds.com) presents the graph through charts, interactive connections, and an AI chat that answers questions using the database. Code and setup instructions are in [web/](web/README.md).

## Data

The beta release dated 29 August 2026 contains 1,024 projects, 797 publications, and 642 confirmed links between projects and publications.

The [download page](https://eq-graph.abundanceds.com/data) provides CSV files and a SQLite database for analysis outside the website.

## Funding

This project was supported by the EuroQol Research Foundation (seed grant **2582-SG**).

## Contact

Paul Schneider, Anuja Kulkarni, and Kazik Pogoda <br>
[Abundance Decision Systems](https://abundanceds.com) <br>
[contact@abundanceds.com](mailto:contact@abundanceds.com)
