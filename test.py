#Authentication to GitHub Enterprise instance
#
# Usage: python test.py
#

import requests
import pandas as pd
import json
import os
import sys
import time
import datetime
import csv
import re
import getpass
import urllib3
import argparse
import logging
import logging.handlers
import logging.config
import yaml
import pprint
import base64

from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
from requests.auth import HTTPProxyAuth


