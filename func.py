import io
import json
import oci
import logging
from urllib.parse import urlparse, parse_qs
from fdk import response
import pandas as pd
import numpy

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
        if requestbody_str:
            body = json.loads(requestbody_str)
            print(body)
            timex = body['payload'][0]['time']
            z = body['payload'][0]['values']['z']
            y = body['payload'][0]['values']['y']
            x = body['payload'][0]['values']['x']

            df = pd.DataFrame([[timex, x, y, z]], columns=["timex", "x", "y", "z"])

            fullname = f"oci://test_sensor_logger@fro8fl9kuqli/output_{timex}.csv"
            df.to_csv(fullname, index = False)
        
        else:
            body = {}
    except Exception as ex:
        print('ERROR: The request body is not JSON', ex, flush=True)
        raise


    logging.getLogger().info("function handler end")
    
    return response.Response(
        ctx, 
        response_data=json.dumps(resp),
        headers={"Content-Type": "application/json"}
    )
