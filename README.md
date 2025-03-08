# Solar Energy Forecasting RAMP Challenge


## Introduction

This challenge aims to classify the solar energy output into different power categories.

## Data Description
The dataset contains time-series power generation data from solar plants. It has features such as:
- **hour, day, month**: Extracted from timestamps.
- **SOURCE_KEY**: Encoded identifier of the source.
- **DC_POWER**: Direct Current power output (used for classification).
- **AC_POWER, TOTAL_YIELD**: Additional power-related features .

  Authors: [Idriss Lakas], [Anis Dounia]

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
