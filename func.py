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
        if requestbody_str:
            body = json.loads(requestbody_str)
            print(body)
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
