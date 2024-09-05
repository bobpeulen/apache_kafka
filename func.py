#
# oci-apigw-display-httprequest-info-python version 1.0.
#
# Copyright (c) 2020 Oracle, Inc.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
#

import io
import json
import oci
import logging
from urllib.parse import urlparse, parse_qs

from fdk import response


def handler(ctx, data: io.BytesIO=None):
    logging.getLogger().info("function handler start")
    
    resp = {}

    # retrieving the request headers
    headers = ctx.Headers()
    logging.getLogger().info("Headers: " + json.dumps(headers))
    resp["Headers"] = headers

    # retrieving the function configuration
    resp["Configuration"] = dict(ctx.Config())
    logging.getLogger().info("Configuration: " + json.dumps(resp["Configuration"]))

    try:
      requestbody_str = data.getvalue().decode('UTF-8')
      print(requestbody_str)
      
      if requestbody_str:
        resp["Request body"] = json.loads(requestbody_str)
      
      else:
        resp["Request body"] = {}
    

    except Exception as ex:
      print('ERROR: The request body is not JSON', ex, flush=True)
      raise

    return headers
