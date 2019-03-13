.. _api_request:

Requesting Data
=================

The ``scrut_request()`` class takes in a single argument, this argument is going to be whatever variable you iniatiated the :ref:`api_params` class with. 


.. code-block:: python

    response = scrut_request(params) #take in params as an argument
        
    scrut_print(response.data) #json is stored in data property
    scrut_print(response.resp) #request object is stored in resp property.  


In the above code block we have iniated this class with the response variable. One the JSON data is returned fromt he Scrutinizer API it is stored into two properties. 

``resp`` : This class uses the request library under the hood. We store the request object the ``resp`` property. 
``data`` : More commonly you would want to access the ``data`` property. This property is already converted into JSON data which makes it easier to loop over, and modify as needed. 

Here is a simple example of looping over the data property to filter on all source IP addresses returned. 

.. code-block:: python

    for ip_address in response.data['report']['table']['inbound']['rows']:
        print('Source IP Address: ' + ip_address[1]['label'])

Taking a look at the :ref:`api_json_example` will help you understand what key / value pairs you will need to filter on different elements. 





