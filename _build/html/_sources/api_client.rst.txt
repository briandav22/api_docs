.. _api_client:

Scrutinizer API Client
======================


This class iniates an API Client that will be used for making requests to the Scrutinizer API. In order to get started you will need the hostname or IP address of your Scrutinizer appliance as well as an authentication token.

A sample api client might look like 

.. code-block:: python    

    scrut_client = scrut_api_client(hostname="some_hostname",
                                    authToken="some_authtoken")


    
Authentication Tokens can be generated from within the Scrutinizer user interface by going to the Admin Tab - > Security- > Authentication Tokens

.. image:: auth_token.png

