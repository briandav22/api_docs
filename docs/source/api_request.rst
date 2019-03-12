.. _api_request:

Requesting Data
=================

The scrut_request() class takes in a single argument that is built from settings up the parameters. This class leverages the python requests library. 

This is typically the final part of any script. You will now have the JSON data return to you to do whatever you want with. 

The response that comes back from the request is stored in two properties. 

More often then not you will be looking for the JSON data, which is stored in the ``data``. 

Since this class is using the requests library under the hood, we also make the raw request object available to you in the ``resp`` property. 

.. code-block:: python

    response = scrut_request(params) #take in params as an argument
        
    scrut_print(response.data) #json is stored in data property
    scrut_print(response.resp) #request object is stored in resp property.  

