#!/bin/bash
pip install --no-cache-dir gunicorn
gunicorn app:ap
