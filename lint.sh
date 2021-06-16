#! /usr/bin/env bash
isort . && black . && flake8 . && mypy .
