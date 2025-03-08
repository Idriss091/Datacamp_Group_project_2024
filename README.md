# Solar Energy Forecasting RAMP Challenge

**Authors:** Idriss Lakas, Anis Dounia

## Introduction

Accurate forecasting of solar power output is essential for efficient energy management, optimal integration of renewable energy sources, and maintaining grid stability. Predicting solar power categories accurately can help energy providers plan better, minimize energy losses, and optimize resource allocation.

The goal of this RAMP challenge is to develop a robust algorithm that accurately classifies solar energy output into distinct power generation categories based on historical sensor and inverter-level data from solar plants.

## Data Description

The provided dataset consists of time-series measurements collected from two solar power plants in India over a 34-day period. Key features include:

- **Hour, Day, Month**: Temporal features extracted from timestamps.
- **SOURCE_KEY**: Encoded identifiers representing individual inverters.
- **DC_POWER**: Direct current power output used to define power categories for classification.
- **AC_POWER, TOTAL_YIELD**: Additional metrics related to overall energy production.

## Getting started

### Install

To run a submission and the notebook you will need the dependencies listed
in `requirements.txt`. You can install install the dependencies with the
following command-line:

```bash
pip install -U -r requirements.txt
```


### Download data

You need to run the following script to download the data from Kaggle:

```bash
python prepare_data.py
```

### Challenge description

Get started on this RAMP with the
[dedicated notebook](template_starting_kit.ipynb).

### Test a submission

The submissions need to be located in the `submissions` folder. For instance
for `my_submission`, it should be located in `submissions/my_submission`.

To run a specific submission, you can use the `ramp-test` command line:

```bash
ramp-test --submission my_submission
```

You can get more information regarding this command line:

```bash
ramp-test --help
```

### To go further

You can find more information regarding `ramp-workflow` in the
[dedicated documentation](https://paris-saclay-cds.github.io/ramp-docs/ramp-workflow/stable/using_kits.html)
