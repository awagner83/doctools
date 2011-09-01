#!/bin/bash

py.test \
    --cov=doctools \
    --cov-report=term-missing \
    tests.py

